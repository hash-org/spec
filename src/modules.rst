.. default-domain:: spec

.. _hash_tDIrc0uhClZ6:

Modules
=======

.. rubric:: Syntax

.. syntax::

    SourceFile ::=
        ZeroWidthNoBreakingSpace?
        Shebang?
        Module

    ZeroWidthNoBreakingSpace ::=
        $$\u{FEFF}$$

    Shebang ::=
        $$#!$$ ~[$$\n$$]*

    Module ::=
        Item*

    Item ::=
        MacroItem
        | Statement

    MacroItem ::=
        $$#!$$ MacroInvocations

.. rubric:: Examples

.. code-block:: rust
    
    #!/usr/bin/env hashc
    #![feature(quantum_closures)]

    Foo := struct(
        x: i32,
        y: i32 = 0,
    )

    FooKind := enum(
        Bar,
        Baz,
    )

    main := () => {
        println("hello world")
    }

.. _hash_LHUnvR6tUOgT:

Statements
----------

.. rubric:: Syntax

.. syntax::
    Statement ::=
        Expression
        | $$;$$

    StatementList ::=
        Statement*
