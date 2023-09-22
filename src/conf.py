# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Extension setups -------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath("../extensions"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Hash Language Specification"
copyright = "2023, Hash Org"
author = "Hash Org"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["spec", "lints", "toctree"]

templates_path = []
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "hash"
html_theme_path = ["../themes"]

html_title = "Hash Language Specification"
html_short_title = "Language Specification"

html_theme_options = {
    "license": "MIT",
}

# -- Options for Linting -----------------------------------------------------
lint_no_paragraph_ids = ["index"]
