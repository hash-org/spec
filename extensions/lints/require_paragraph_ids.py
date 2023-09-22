from docutils import nodes
from sphinx.application import Sphinx

from spec.definitions.base import DefId  # type: ignore
from .error import EmitError


def check(app: Sphinx, raise_error: EmitError):
    """
    Apply the paragraph id lint check.
    """
    for document in app.env.found_docs:
        doctree = app.env.get_doctree(document)

        # If the document is specified in the paragraph id requirements, then
        # check it, otherwise check it doesn't have any ids.
        if document in app.config.lint_no_paragraph_ids:
            check_node_does_not_have_ids(doctree, raise_error)
        else:
            check_node_has_ids(doctree, raise_error)


def check_node_has_ids(node: nodes.Node, raise_error: EmitError):
    """
    Check that all nodes have an ID.
    """
    is_paragraph = type(node) is nodes.paragraph

    if is_paragraph and type(node.parent) is nodes.section:
        # If this is a paragraph, and it is in a section, this should item
        # should have an id.
        node_should_have_id(node, "paragraph", raise_error)
    elif is_paragraph and type(node.parent) is nodes.list_item:
        # If this is a paragraph in a list, then it should have an id.
        node_should_have_id(node, "list item", raise_error)
    elif is_paragraph and type(node.parent) is nodes.entry:
        if node.parent.parent.index(node.parent) == 0:
            node_should_have_id(node, "first cell of a table row", raise_error)
        else:
            node_should_not_have_id(
                node,
                "second or later cell of a table row",
                raise_error,
            )

    elif type(node) is nodes.section:
        # Check that a section has an associated id.
        if not any(name.startswith("hash_") for name in node["names"]):
            raise_error("section should have an id", location=node)

    else:
        node_should_not_have_id(node, type(node).__name__, raise_error)

    # Now recursively walk all the children and perform the same check
    for child in node.children:
        check_node_has_ids(child, raise_error)


def check_node_does_not_have_ids(node: nodes.Node, raise_error: EmitError):
    """
    This function checks that a given tree does not have ids, this is useful
    to invoke for modules that shouldn't feature any IDs.
    """

    if type(node) is nodes.section:
        # Check that a section has an associated id.
        if any(name.startswith("hash_") for name in node["names"]):
            raise_error("section should not have an id", location=node)
    else:
        node_should_not_have_id(node, type(node).__name__, raise_error)

    # Now recursively walk all the children and perform the same check
    for child in node.children:
        check_node_does_not_have_ids(child, raise_error)


def node_should_have_id(node: nodes.Node, name: str, raise_error: EmitError):
    """
    This function checks that a given node follows the following rules:

    - Any other element but the first is not an 'id' like element.

    - The first child node in the element is [DefItem].

    """
    if any(is_node_def(child) for child in node.children[1:]):
        raise_error(f"id in {name} is not the first element", location=node)
    elif not len(node.children) or not is_node_def(node.children[0]):
        raise_error(f"{name} should have an id on it", location=node)


def node_should_not_have_id(node: nodes.Node, name: str, raise_error: EmitError):
    """
    Ensure that a node does not have a defined id on it.
    """
    if any(is_node_def(child) for child in node.children):
        raise_error(f"`{name}` should not have an id on it", location=node)


def is_node_def(node: nodes.Node) -> bool:
    """
    Check if a node is a definition.
    """
    return (
        type(node) is DefId
        and node["def_kind"] == "paragraph"
        and node["def_id"].startswith("hash_")
    )
