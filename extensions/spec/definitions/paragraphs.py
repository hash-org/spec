"""
Defines the :p:`...` and :dp:`...` roles; paragraph definitions and references.
"""

import hashlib
from collections import defaultdict
from typing import Generator, List, Optional, cast

from docutils import nodes
from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from . import utils
from .base import Def, DefId
from ..error import raise_error


def find_parent_of_type(node: Node, ty) -> Optional[Node]:
    """
    Walk up the node tree and find the first parent of the given type `ty`.
    """
    cursor = node
    while cursor is not None:
        if isinstance(cursor, ty):
            return cursor
        cursor = cursor.parent
    return None


def plaintext_paragraph(node: Node) -> str:
    """
    Get the paragraph or the parent paragraph as text.
    """
    paragraph = find_parent_of_type(node, nodes.paragraph)
    if paragraph is None:
        paragraph = node

    return paragraph.astext().replace("\n", " ")


def collect_items_in_document(
    app: Sphinx, nodes_to_collect: List[DefId]
) -> Generator[Node, None, None]:
    """
    Convert all the given definitions into paragraphs.

    This method requires that the paragraphs have associated section ids (item with `hash_`)
    """
    ids = defaultdict(lambda: 1)
    for node in nodes_to_collect:
        section_node = find_parent_of_type(node, nodes.section)

        if section_node is None:
            raise RuntimeError(f"could not fund section for {node!r}")

        try:
            section_id, section_anchor = utils.section_id_and_anchor_from(section_node)
        except utils.NoSectionIdError:
            raise_error(
                "paragraph inside a section that doesn't have an id starting with `hash_`",
                location=section_node,
            )
            return

        yield Paragraph(
            name=node["def_id"],
            document=app.env.docname,
            section_id=section_id,
            section_anchor=section_anchor,
            plaintext=plaintext_paragraph(node),
            sequential=ids[section_id],
        )

        # Increment the current section count for the paragraph so we can have the specific
        # `sequential` number for the paragraph.
        ids[section_id] += 1


class Paragraph(Def):
    """
    The anchor used for the paragraph, which is the name of the paragraph.
    """

    section_anchor: str

    """
    The section id of the paragraph, which is the id of the section that the paragraph is in.
    """
    section_id: str

    """
    The plaintext of the paragraph, which is the text of the paragraph without any
    """
    plaintext: str

    """
    The discriminant of a paragraph in a list of paragraphs, which means that every paragraph
    regardless of section or position will have a unique section number.
    """
    sequential: int

    def __init__(
        self,
        name: str,
        document: str,
        section_anchor: str,
        section_id: str,
        plaintext: str,
        sequential: int,
    ):
        self.name = name
        self.document = document
        self.section_anchor = section_anchor
        self.section_id = section_id
        self.sequential = sequential
        self.plaintext = plaintext

    def number(self, env: BuildEnvironment) -> str:
        section = ".".join(
            str(n) for n in env.toc_secnumbers[self.document][self.section_anchor]
        )

        return f"{section}:{self.sequential}"

    def anchor(self) -> str:
        return self.name

    def include_in_search(self) -> bool:
        return False

    def display_name(self, env: BuildEnvironment) -> str:
        return f"{self.number(env)} {self.content_checksum()}"

    def content_checksum(self) -> str:
        sha256 = hashlib.sha256()
        sha256.update(self.plaintext.encode("utf-8"))
        return sha256.hexdigest()


def replace_id_node(app: Sphinx, node: DefId, item: Def):
    """
    Method that is called when the paragraph node is rendered into
    actual text within the source.

    The transformation adds a new node that is the left hand-side section
    number of the paragraph, and then followed by the paragraph text.
    """
    paragraph = cast(Paragraph, item)

    new = nodes.inline()
    new["ids"].append(paragraph.anchor())
    new["classes"].append("spec-paragraph-id")
    new += nodes.Text(paragraph.number(app.env))
    node.replace_self(new)


def create_ref_node(env: BuildEnvironment, text: str, item: Optional[Def]) -> Node:
    """
    This method is invoked when a reference to a paragraph (:p:`...`) is transformed
    into a link. This method is responsible for creating the actual link.
    """
    if item is not None:
        paragraph = cast(Paragraph, item)
        return nodes.emphasis("", paragraph.number(env))
    else:
        return nodes.emphasis("", "Paragraph " + text)
