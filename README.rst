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

`black <https://pypi.org/project/black/>` is a code formatter, and `flake8 <https://pypi.org/project/flake8/>` is a linter.
They can both be installed via ``pip``.
