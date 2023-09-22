from collections import defaultdict
from typing import Any, Dict, Set, NewType, Literal

from docutils import nodes
from docutils.nodes import Node
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import SphinxDirective

from .error import raise_error
from .definitions import utils

Storage = NewType("Storage", Dict[str, Set[str]])


def get_storage(env: BuildEnvironment) -> Storage:
    """
    Get the storage for all the information nodes in the current environment.
    """
    key = "spec_informational"

    if not hasattr(env, key):
        setattr(env, key, defaultdict(set))
    return getattr(env, key)


class InformationMarkerNode(nodes.Element):
    def __init__(self, kind: Literal["page", "section"]):
        super().__init__()
        self["kind"] = kind


def build_information_directive(kind: Literal["page", "section"]):
    class InformationalDirective(SphinxDirective):
        """
        A directive that indicates that the contents of the page or section are informational.

        It is simply intended to be used as:
        ```
        .. informational-page::
        ```
        or
        ```
        .. informational-section::
        ```
        """

        has_content = False

        def run(self):
            paragraph = nodes.paragraph()
            paragraph += nodes.Text(f"The contents of this {kind} are informational.")

            note = nodes.note()
            note += paragraph

            return [note, InformationMarkerNode(kind)]

    return InformationalDirective


class InformationPagesCollector(EnvironmentCollector):
    def clear_doc(self, app: Sphinx, env: BuildEnvironment, docname: str):
        """
        Clear the information nodes for the document.
        """
        storage = get_storage(env)

        if docname in storage:
            del storage[docname]

    def merge_other(
        self,
        app: Sphinx,
        env: BuildEnvironment,
        docnames: set[str],
        other: BuildEnvironment,
    ):
        """
        Merge the information nodes from the other environment into the current one.

        This is used when the environment is being rebuilt.
        """
        storage = get_storage(env)
        for document, contents in get_storage(other).items():
            storage[document] = storage[document].union(contents)

    def process_doc(self, app: Sphinx, document: nodes.document):
        """
        Process the document and check that all the information nodes are in the correct
        location.
        """
        storage = get_storage(app.env)

        for node in document.findall(InformationMarkerNode):
            if node["kind"] == "page":
                self.process_page(app, storage, node)
            elif node["kind"] == "section":
                self.process_section(app, storage, node)
            else:
                raise RuntimeError(f"unknown kind {node['kind']}")

    def process_section(self, app: Sphinx, storage: Storage, node: Node):
        """
        Check that the information node is at the top of a section node.
        """

        if type(node.parent) is not nodes.section:
            raise_error("information section must be inside a section", location=node)

        try:
            _id, anchor = utils.section_id_and_anchor_from(node.parent)
        except utils.NoSectionIdError:
            raise_error(
                "informational-section must be inside a section with an ID which starts with `hash_`",
                location=node,
            )
            return

        storage[app.env.docname].add(anchor)

    @staticmethod
    def process_page(app: Sphinx, storage: Storage, node: Node):
        """
        Check that the node is at the top of the document.
        """
        if type(node.parent) is not addnodes.document:
            raise_error(
                "information pages must be at the top of the document", location=node
            )
            return

        storage[app.env.docname].add("{{{whole-page}}}")


class InformationPagesTransformer(SphinxTransform):
    default_priority = 500

    def apply(self, **kwargs: Any):
        """
        Remove all the informational nodes from the document.
        """
        for node in self.document.findall(InformationMarkerNode):
            node.parent.remove(node)


def setup(app: Sphinx):
    """
    Entry point of the pages pass.
    """
    app.add_node(InformationMarkerNode)
    app.add_env_collector(InformationPagesCollector)
    app.add_post_transform(InformationPagesTransformer)
