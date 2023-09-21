from typing import Tuple

from docutils import nodes
from docutils.nodes import Node


def section_id_and_anchor_from(section: Node) -> Tuple[str, str]:
    """
    Get the section id and anchor from the current section node, assuming
    it is a section and has an ID.
    """

    # try to find the `hash_` id from the section.
    if "names" in section:
        try:
            section_id = [
                name for name in section["names"] if name.startswith("hash_")
            ][0]
        except IndexError:
            raise NoSectionIdError()
    else:
        raise NoSectionIdError()

    # we don't need to create the anchor if the parent item  of the section is the document.
    if section.parent is not None and isinstance(section.parent, nodes.document):
        section_anchor = ""
    else:
        section_anchor = "#" + section["ids"][0]

    return section_id, section_anchor


class NoSectionIdError(Exception):
    """
    Thrown when a section or passed node doesn't have an ID.
    """

    pass
