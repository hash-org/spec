"""
Defines the :t:`...` and :dt:`...` roles; term definitions and references.
"""

from typing import Generator, List

from docutils import nodes
from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from .base import Def, DefId


def collect_items_in_document(
    app: Sphinx, nodes: List[DefId]
) -> Generator[Node, None, None]:
    """
    Convert all the given `DefId`s into term definitions.
    """
    for node in nodes:
        yield Term(node["def_id"], app.env.docname)


class Term(Def):
    def __init__(self, name: str, document: str):
        self.name = name
        self.document = document

    def anchor(self) -> str:
        return f"syntax_{self.name}"


def replace_id_node(app: Sphinx, node: Node, item: Def):
    """
    Method that is called when a term definition :dt:`...` is transformed into
    actual text within the source. This just creates an emphasis node with the text
    that was given.
    """
    new = nodes.emphasis("", node["def_text"])
    new["ids"].append(item.anchor())
    node.replace_self(new)


def create_ref_node(env: BuildEnvironment, text: str, item: Def) -> Node:
    """
    Method that is called when a syntax reference :t:`...` is transformed into
    actual text within the source. This just gets the text that was given.
    """
    return nodes.Text(text)
