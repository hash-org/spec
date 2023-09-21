"""
Defines the :s:`...` and :ds:`...` roles; syntactic term definitions and references.
"""

from typing import Generator, List, Optional

from docutils import nodes
from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from .base import Def, DefId


class Syntax(Def):
    def __init__(self, name: str, document: str):
        self.name = name
        self.document = document

    def anchor(self) -> str:
        return f"syntax_{self.name}"

    def include_in_search(self) -> bool:
        return True

    def display_name(self, env: BuildEnvironment) -> str:
        return self.name


def collect_items_in_document(
    app: Sphinx, nodes: List[DefId]
) -> Generator[Node, None, None]:
    """
    Convert all the given `DefId`s into syntax definitions.
    """
    for node in nodes:
        yield Syntax(node["def_id"], app.env.docname)


def replace_id_node(app: Sphinx, node: DefId, syntax: Def):
    """
    Method that is called when a syntax definition :ds:`...` is transformed into
    actual text within the source. This just creates a literal node with the text
    that was given.
    """
    new = nodes.literal("", node["def_text"])
    new["ids"].append(syntax.anchor())
    node.replace_self(new)


def create_ref_node(env: BuildEnvironment, text: str, item: Optional[Def]) -> Node:
    """
    Method that is called when a syntax reference :s:`...` is transformed into
    actual text within the source. This just creates a literal node with the text
    that was given.
    """
    return nodes.literal("", text)
