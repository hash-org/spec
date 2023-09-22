from typing import Protocol, Optional

import sphinx.util.logging
from docutils.nodes import Node


class EmitError(Protocol):
    def __call__(self, message: str, *args, location: Optional[Node]) -> None:
        pass


def raise_error(msg: str, *, location: Optional[Node] = None):
    """
    Emit an error to sphinx if one of the lints failed to pass.
    """
    logger = sphinx.util.logging.getLogger(__name__)
    logger.warning(msg, location=location)
