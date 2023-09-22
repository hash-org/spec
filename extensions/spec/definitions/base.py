from typing import Tuple

from docutils import nodes
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import SphinxRole


def parse_target_and_text_from_item(text: str) -> Tuple[str, str]:
    """
    We split the given input text into the "text" and the "target" which
    is essentially the ID that was given to the text. The text can come
    in a number of forms, either as a tag like this (located at the end
    of the sequence):
    ```
    text-blah-blah <...target...>
    ```
    or in brackets (the last most complete bracket sequence) like this:

    ```
    text-blah-blah [...target...] more-text
    ```

    If it is neither of those, we assume that the text and the target must be
    the same.
    """

    if "<" in text and text.endswith(">"):
        start = text.rfind("<")
        target = text[start + 1 : len(text) - 1]
        text = text[:start].rstrip()
    elif "[" in text and "]" in text:
        target = text[text.find("[") + 1 : text.rfind("]")]
        text = text.replace("[", "").replace("]", "")
    else:
        target = text

    return text, target


def id_from_text(text: str) -> str:
    """
    Convert a text chunk into an id-like format, we filter for any non-alpha numeric
    characters, and convert them into `_`.
    """
    return "".join(c if c.isalnum() else "_" for c in text.lower())


class Def:
    """
    This is a base class used for the various additional roles that we add, the
    `syntax`, `terms`, `codeterms`, and `paragraphs` should all inherit from this
    base class.
    """

    document: str
    name: str

    def anchor(self) -> str:
        """
        Get the anchor name for the item, this is the text that is rendered when the link
        is built.
        """
        pass

    def include_in_search(self) -> bool:
        """
        Whether the definition should be included in the search index.
        """
        return True

    def display_name(self, env: BuildEnvironment) -> str:
        """
        Get the display name for the item.
        """
        return self.name


class DefId(nodes.Element):
    def_text: str = ""
    def_id: str = ""

    def __init__(self, kind: str, text: str):
        text, target = parse_target_and_text_from_item(text)
        super().__init__(
            text, def_id=id_from_text(target), def_kind=kind, def_text=text
        )

    def astext(self) -> str:
        """
        Return the raw text of the node.
        """
        return self["def_text"]


class DefRef(nodes.Element):
    """
    A reference to a definition item, this isn't the actual definition item, but
    rather a reference to it.
    """

    def __init__(self, kind: str, source_doc: str, text: str):
        text, target = parse_target_and_text_from_item(text)

        super().__init__(
            ref_kind=kind,
            ref_source_doc=source_doc,
            ref_text=text,
            ref_target=id_from_text(target),
        )

    def astext(self) -> str:
        """
        Return the raw text of the node.
        """
        return self["ref_text"]


class DefIdRole(SphinxRole):
    """
    A role wrapper around a definition.
    """

    def __init__(self, kind):
        self.kind = kind

    def run(self):
        return [DefId(self.kind, self.text)], []


class DefRefRole(SphinxRole):
    """
    A role wrapper around a definition reference.
    """

    def __init__(self, kind):
        self.kind = kind

    def run(self):
        return [DefRef(self.kind, self.env.docname, self.text)], []
