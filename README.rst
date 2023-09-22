===========================
Hash Language Specification
===========================

The Hash Language Specification is a document describing the Hash 
programming language.


The specification is intended as a guide for implementers of the Hash 
language and to coordinate design decisions between them. It is intended 
that the official Hash compiler ``hashc`` will be the reference implementation 
for this specification, and in the future the two should be kept in sync.


The Hash Language Specification text is licenced under the ``MIT`` licence agreement
(as the rest of the compiler).

Installation
============

The Hash Language Specification uses ``pip-tools`` to manage its dependencies, which
can be installed with

.. code-block::

        pip install pip-tools

Once it is installed, the list of desired dependencies which is specified in
``requirements.in`` can be installed with:

.. code-block::

    pip-compile --require-hashes

Once that is done, you're good to go!

Building the specification
==========================

This specification uses Sphinx to build a rendered version of the specification.
The build script ``make.py`` is provided to build the specification, and can 
simply be involved by running::
    
    ./make.py

This will invoke Sphinx to build the specification in the ``build`` directory. By default,
Sphinx uses an incremental build system, to build a fresh copy of the specification, use::

    ./make.py -c


Development
===========

During development, it is useful to have Sphinx automatically rebuild the specification
when changes are made. This can be done by running::

    ./make.py -s

This will set the Sphinx to watch the specification sources and the extension sources, re-building
when a change is detected. Additionally, ``-s`` mode launches a simple HTTP server on port 8000
to serve the built specification. This can be accessed by pointing a web browser at ``http://localhost:8000``.

If you are changing the extensions, or an exception is thrown from the extension code, the
server will not automatically rebuild.

To debug an issue, use ``--debug`` mode which will build the specification in a single job,
it won't serve the contents, and it enables exceptions to be fully printed to the console.

++++++++++++
Contributing
++++++++++++

If you are modifying the sources of the extensions, make sure to run the standard
CI checks before submitting a pull request. This can be done by running:

.. code-block::
    black . && flake8 . --exclude .venv

`black <https://pypi.org/project/black/>`_ is a code formatter, and `flake8 <https://pypi.org/project/flake8/>`_ is a linter.
They can both be installed via ``pip``.

Writing the specification
=========================

To enhance the specification, this repository defines several Sphinx extensions to make
writing the specification easier. These extensions are defined in the ``extensions`` directory.
There are three main "extensions":

* ``spec`` - Defines additional directives that can be used throughout the specification.

* ``lints`` - Defines a lint pass which ensures that the contents of the specification match
  the expected specification style.

* ``toctree`` - Expands the standard Sphinx ``toctree`` directive to allow for an `Appendices`
  section to be included.

This section of the document describes how to use these extensions.

++++
Spec
++++

The ``spec`` extension adds a couple of directives to the specification. All of the directives
are only meant to be a wrapper around already existing functionality in ``Sphinx``. The ``definitions``
directives are intended to be used to define various "terms" in the specification that can be
referenced in other parts of the specification and can be searched through the ``Sphinx``
searching functionality.

+++++++++++
Definitions
+++++++++++

The ``spec`` extension adds a couple of ways to specify "definitions" in the specification. These
definitions come in three categories: terms, programmatic constructs, and syntactic categories.

.. list-table::
   :header-rows: 1

   * - Namespace
     - Link role
     - Definition role
     - Styling

   * - Terms
     - ``:t:`foo```
     - ``:dt:`foo```
     - Normal text

   * - Programmatic constructs
     - ``:c:`foo```
     - ``:dc:`foo```
     - Monospace text

   * - Syntactic categories
     - ``:s:`Foo```
     - ``:ds:`Foo```
     - Monospace text

The ``d{c|t|s}`` directives are used to define the originating part of the definition, and the
corresponding ``{c|t|s}`` directives can later be used to link back to the definition. An
example of this is shown below:

.. code-block:: rst

    A :dt`match` block is composed of a subject :t`expression` and a series of :t`match arms`.

Prefixes and suffixes
~~~~~~~~~~~~~~~~~~~~~


Sometimes writing ``:t:\`term\``` requires a prefix or a suffix with the term. For example,
pluralising the above example by adding ``s`` to the ``match-term`` can be done in the
the clunky way (just like in :math:`\\LaTeX`):

.. code-block:: rst

   The :t:`match` block can specify multiple :t:`match arm`\ s in the inner block.

However, this is too clunky, therefore the directives support specifying a prefix and a
suffix with the following way:

.. code-block:: rst

    The :t:`match` block can specify multiple :t:`[match arm]s` in the inner block.

Now, anything within the ``[]`` is now treated as the actual term, and the prefix and
suffix are just for display purposes.

Arbitrary labels
~~~~~~~~~~~~~~~~

Furthermore, if you need to link to some definition with an entirely different label,
you can do so with the following syntax:

.. code-block:: rst

    The :t:`match` block can specify multiple :t:`match cases <match arm>` in the inner block.

Now, the second definition link will link to ``match arm``, but it will be rendered in text
as ``match cases``. This is the markdown equivalent of ``[match cases](match arm)`` syntax.

+++++++++++++
Syntax blocks
+++++++++++++

It is intended that the specification describes the Hash language with reference to
the syntax, and in fact formally state the accept grammar of the language. To make
this easier, the ``spec`` extension adds a ``syntax`` directive which can be used
to specify a syntax block. A syntax block has several nice features:

* Syntax definitions become their own "Syntax definitions", and can be referenced
  with the ``:s:`` throughout the specification.

* Any references within the syntax block to other rules also become links to the
  definition of the rule.

An example of a syntax block is shown below:

.. code-block:: rst

    .. syntax::

        Match ::=
            $$match$$ Expression $${$$ MatchArmList $$}$$

        MatchArmList ::=
            MatchArm ($$,$$ MatchArm)* ($$,$$)?

        MatchArm ::=
            Pattern $$=>$$ Expression

        Pattern ::=
                  | LitPat
                  | BindPat
                  ...

Literal values in the syntax block are written between ``$$``. The ``$$`` are
not part of the literal value, and are only used to distinguish between the
literal value and the rest of the syntax. The ``$$`` are not rendered in the
final specification.

Definitions, which start with an identifier and followed by a `::=` with
the definition, are treated as syntax definitions. These definitions become
declarations of the syntax definition, and can be referenced with the ``:s:``
role. For example, the ``Match`` syntax definition can be referenced with
``:s:`Match```.

The right hand side of the syntax definition is parsed as a series of tokens,
identifiers are treated as references to other syntax definitions, and are
rendered as links to the definition. For example, the ``MatchArmList`` syntax
definition references the ``MatchArm`` syntax definition, and it is rendered
as a link to the definition.

++++++++++
Paragraphs
++++++++++

Each paragraph in the specification is required to have an ``id`` attribute. This
is used to link to the paragraph from other parts of the specification. The
``spec`` extension adds a ``dp`` and ``p`` directives. ``dp`` is used to
define the start of a paragraph, and ``p`` is used to reference a paragraph
by its ``id``. For example:

.. code-block:: rst

    :dp:`hash_foo` This is a paragraph.

    :dp:`hash_bar` Later in the file, we can reference :p:`hash_foo`.

The ``dp`` directive id must be specified with an id which begins with ``hash_``, and
with some random string after it. This is to ensure that the ``id`` is unique, and
that it doesn't conflict with any other ``id``\ s in the specification. It is intended that
IDs remain stable across specification versions to ensure that links to the specification
don't break.

Random IDs can be generated with the provided tool ``tools/generate_ids.py``. This tool
will generate a random ID, and print it to the console. This ID can then be used in
the specification.


+++++
Lints
+++++

Currently, the lints are very basic. The main pass is ``require_paragraph_ids`` which
will verify that all of the items in a document contain the `id` attribute, and that
the `id` attribute is a valid identifier. If a page shouldn't specify ids, i.e. the
``index`` page, then it can be configured to be ignored by adding the name of
the page to the ``lint_no_paragraph_ids`` option:

.. code-block:: diff

    -lint_no_paragraph_ids = ["index"]
    +lint_no_paragraph_ids = ["index", "my_page_name"]

If the item is added to the option, then the linter will check that the page doesn't
specify any IDs on sections, and paragraphs.

+++++++
Toctree
+++++++

This extension performs a single function, it introduces an ``appendices`` directive, which
can be specified after a ``toctree``, and it will include all of pages under it as the standard
appendices section (like in :math:`\\LaTeX`).

To use it, simply write the ``appendices`` after ``toctree``:

.. code-block:: rst

    .. toctree::
        :maxdepth: 2

        foo
        bar

    .. appendices::

        baz
        qux
