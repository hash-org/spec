from typing import List, Dict, Any

import sphinx
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from . import require_paragraph_ids
from .error import raise_error


def run_lints(app: Sphinx, env: BuildEnvironment):
    """
    Apply all lints to the current build.
    """
    require_paragraph_ids.check(app, raise_error)


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """
    Register the `lints` pass with Sphinx.
    """

    app.connect("env-check-consistency", run_lints)

    # register the lints
    app.add_config_value("lint_no_paragraph_ids", [], "", List[str])

    return {
        "version": "0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
