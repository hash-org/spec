from dataclasses import dataclass
from typing import Tuple, Dict, List, NewType, Callable, Generator, Any, Optional

import sphinx.util.nodes
from docutils import nodes
from docutils.nodes import Node, Element
from sphinx.application import Sphinx
from sphinx.domains import ObjType
from sphinx.environment import BuildEnvironment
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.transforms import SphinxTransform

from . import paragraphs, syntax, terms, code_terms
from .base import Def, DefId, DefIdRole, DefRef, DefRefRole

Collector = NewType(
    "Collector", Callable[[Sphinx, List[DefId]], Generator[Node, None, None]]
)
Replacer = NewType("Replacer", Callable[[Sphinx, DefId, Def], None])
Creator = NewType("Creator", Callable[[BuildEnvironment, str, Optional[Def]], Node])


@dataclass
class RoleInfo:
    name: str
    pretty_name: str
    role: str
    collect_items_in_document: Collector
    create_ref_node: Creator
    replace_id_node: Replacer

    def __init__(
        self,
        name: str,
        role: str,
        pretty_name: str,
        collect_items_in_document: Collector,
        create_ref_node: Creator,
        replace_id_node: Replacer,
    ):
        self.name = name
        self.pretty_name = pretty_name
        self.role = role
        self.collect_items_in_document = collect_items_in_document
        self.replace_id_node = replace_id_node
        self.create_ref_node = create_ref_node


ROLES: List[RoleInfo] = [
    RoleInfo(
        "term",
        "term",
        "term",
        terms.collect_items_in_document,
        terms.create_ref_node,
        terms.replace_id_node,
    ),
    RoleInfo(
        "syntaxes",
        "syntax",
        "syntactic category",
        syntax.collect_items_in_document,
        syntax.create_ref_node,
        syntax.replace_id_node,
    ),
    RoleInfo(
        "paragraph",
        "p",
        "paragraph",
        paragraphs.collect_items_in_document,
        paragraphs.create_ref_node,
        paragraphs.replace_id_node,
    ),
    RoleInfo(
        "code_terms",
        "codeterm",
        "programmatic construct",
        code_terms.collect_items_in_document,
        code_terms.create_ref_node,
        code_terms.replace_id_node,
    ),
]


def get_roles() -> Dict[str, Element]:
    """
    Get all the additional roles that we add for the enrichment of the specification.
    """
    result = {}

    for role in ROLES:
        result["d" + role.name[0]] = DefIdRole(role.name)
        result[role.name[0]] = DefRefRole(role.name)

    return result


def get_object_types() -> Dict[str, ObjType]:
    """
    Get all the types of the objects that are defined in the domain.
    """
    result = {}

    for role in ROLES:
        result[role.name] = ObjType(role.pretty_name, role.name)

    return result


SphinxObject = NewType("SphinxObject", Tuple[str, str, str, str, str, int])


def get_objects(env: BuildEnvironment) -> List[SphinxObject]:
    """
    Get all the currently defined "objects" within the current domain. Objects
    refers to items that the user annotated with the special nodes that we introduce
    like `p`, `dp`, `t`, etc.

    This data is used to populate the documentation search system. The function will
    return a collection of [SphinxObject]s which is just a wrapper around a tuple type.
    The data is of the following shape:
    * Full name
    * Display name in the search
    * Object type
    * Document name (where it was located)
    * Anchor
    * Search priority (1: default, 0: important, 2: not important, -1: ignore)

    """
    result = []

    for kind in ROLES:
        storage = get_storage(env, kind)

        for item in storage.values():
            result.append(
                SphinxObject(
                    (
                        item.name,
                        item.display_name(env),
                        kind.name,
                        item.document,
                        item.anchor(),
                        1 if item.include_in_search() is not None else -1,
                    )
                )
            )

    return result


def get_storage(env: BuildEnvironment, kind: RoleInfo) -> Dict[str, Def]:
    """
    Get the storage for a particular kind of role. This will return a dictionary
    of all the known `defs` of a particular kind with the key being the name of
    the definition.

    This is across the entire environment, not a single document.
    """

    key = f"spec_items_{kind.name}"
    if not hasattr(env, key):
        setattr(env, key, {})

    return getattr(env, key)


class DefCollector(EnvironmentCollector):
    def clear_doc(self, app: Sphinx, env: BuildEnvironment, docname: str):
        """
        Remove all definitions and references contained into a document.

        This is called by Sphinx during incremental build, either when a document
        was removed or when the document has been changed. In the latter case,
        `process_doc` is called after this method.
        """

        for role in ROLES:
            storage = get_storage(app.env, role)
            for item in list(storage.values()):
                if item.document == docname:
                    del storage[item.name]

    def merge_other(
        self,
        app: Sphinx,
        env: BuildEnvironment,
        docnames: set[str],
        other: BuildEnvironment,
    ):
        """
        Merge the collected information from two environments into one.

        Sphinx supports parallel builds, with each process having its own
        environment instance, but once each document is processed, those
        parallel environments need to be merged together, this is the method
        that performs the merge.
        """
        for role in ROLES:
            storage = get_storage(app.env, role)
            other_storage = get_storage(other, role)

            for item in other_storage.values():
                if item.document in docnames:
                    storage[item.name] = item

    def process_doc(self, app: Sphinx, doctree: nodes.document):
        """
        Collect all the definitions and references present in the document.

        The method can expect no existing information about the same document
        being stored in the environment, as during incremental rebuilds, the `clear_doc`
        method is called ahead of this one.
        """
        for role in ROLES:
            storage = get_storage(app.env, role)
            defs = filter(
                lambda node: node["def_kind"] == role.name, doctree.findall(DefId)
            )

            for item in role.collect_items_in_document(app, list(defs)):
                storage[item.name] = item


class DefTransformer(SphinxTransform):
    """
    This pass converts all the special directives that were specified into already existing
    RST nodes, so that the rest of the sphinx pipeline can process them as normal.
    """

    default_priority = 500

    def apply(self, **kwargs: Any):
        """
        This method will finally convert all the specified definitions into their final
        rendered versions. This will replace all the `DefId` and `DefRef` nodes with
        the appropriate rendered selves. The table for the transformations can be found bellow:
        ```
        +----------------+----------------+----------------+-----------------+
        | Namesppace     | DefId          | DefRef         | Rendered        |
        +================+================+================+=================+
        | term           | dt             | t              | emphasised link |
        +----------------+----------------+----------------+-----------------+
        | paragraph      | dp             | p              | emphasised link |
        +----------------+----------------+----------------+-----------------+
        | syntax         | ds             | s              | monospaced link |
        +----------------+----------------+----------------+-----------------+
        | code           | dc             | c              | monospaced link |
        +----------------+----------------+----------------+-----------------+
        ```
        """

        for role in ROLES:
            storage = get_storage(self.env, role)

            for node in self.document.findall(DefId):
                if node["def_kind"] != role.name:
                    continue

                item = storage[node["def_id"]]
                role.replace_id_node(self.app, node, item)

            for node in self.document.findall(DefRef):
                if node["ref_kind"] != role.name:
                    continue

                if node["ref_target"] in storage:
                    item = storage[node["ref_target"]]
                    node.replace_self(
                        sphinx.util.nodes.make_refnode(
                            self.app.builder,
                            node["ref_source_doc"],
                            item.document,
                            item.anchor(),
                            role.create_ref_node(self.env, node["ref_text"], item),
                        )
                    )
                else:
                    # Hmm, something went wrong with linking, so we label this as a missing item. See the
                    # styling in `themes/hash/static/hash.css` for `spec-missing-ref`.
                    new = nodes.inline(
                        "", "", role.create_ref_node(self.env, node["ref_text"], None)
                    )
                    new["classes"].append("spec-missing-ref")
                    node.replace_self(new)


def setup(app: Sphinx):
    """
    Initialise the `definitions` plugin into the sphinx session.
    """
    app.add_node(DefId)
    app.add_env_collector(DefCollector)
    app.add_post_transform(DefTransformer)
