"""
Defines the :c:`...` and :dc:`...` roles; code term definitions and  references.
"""

from typing import List, Generator, Optional

from docutils import nodes
from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from .base import Def, DefId


def collect_items_in_document(
    app: Sphinx, nodes: List[DefId]
) -> Generator[Node, None, None]:
    """
    Convert all the given `DefId`s into code terms
    """
    for node in nodes:
        yield CodeTerm(node["def_id"], app.env.docname)


class CodeTerm(Def):
    def __init__(self, name: str, document: str):
        self.name = name
        self.document = document

    def anchor(self) -> str:
        return f"codeterm_{self.name}"


def replace_id_node(app: Sphinx, node: DefId, syntax: Def):
    """
    Method that is called when the node is now rendered into
    actual text within the source.

    The transformation just replaces the node with an emphasis node
    and the literal text. This is equivalent of writing ``text``.
    """
    new = nodes.emphasis("", "")
    new["ids"].append(syntax.anchor())
    new += nodes.literal("", node["def_text"])
    node.replace_self(new)


def create_ref_node(env: BuildEnvironment, text: str, item: Optional[Def]) -> Node:
    """
    Method that is called when a code term reference :c:`...` is transformed into
    actual text within the source. This just creates a literal node with the text
    that was given.
    """
    return nodes.literal("", text)
