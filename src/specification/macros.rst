.. default-domain:: spec

.. warning::
    This section is not complete, and the specification has not been finalised.

.. _hash_1uuKov7eVd37:

Macros
======

.. _hash_ps3mJaxHGwrT:

Macro Invocation
----------------

.. rubric:: syntax

.. syntax::
    MacroInvocation ::=
        $$#$$ MacroInvocationHeader MacroSubject

    MacroInvocationHeader ::=
        MacroName
        | $$[$$ MacroInvocations $$]$$

    MacroInvocations ::=
        MacroInvocationHeaderWithArgs ($$,$$ MacroInvocationHeaderWithArgs)* $$,$$?    

    MacroInvocationHeaderWithArgs ::=
        MacroName MacroInvocationArguments?

    MacroName ::= Name

    MacroInvocationArguments ::=
        $$($$ ParameterList $$)$$

.. rubric:: Examples

.. code-block:: rust

    #[
      foreign_library("libfoo"),
      link_name("foo_create"), 
      link_section(section="__text", segment="__text")
    ]
    foo_create := () -> &raw Foo;

.. _hash_11DLTcqPgJRl:

Macro Subjects
~~~~~~~~~~~~~~

.. rubric:: syntax

.. syntax::
    MacroSubject ::=
        Expression
        | Pattern
        | Type
        | EnumVariant
        | StructField
        | MatchArm
        | Parameter
        | TypeParameter


.. _hash_MaenJcPL7dV4:

Token Macro Invocation
----------------------

.. rubric:: syntax

.. syntax::
    TokenMacroInvocation ::=
        $$@$$ TokenMacroInvocationHeader DelimitedTokenTree

    TokenMacroInvocationHeader ::=
        TokenMacroName
        | $$[$$ TokenMacroName TokenMacroInvocationArguments? $$]$$

    TokenMacroName ::=
        Name

    TokenMacroInvocationArguments ::=
        $$($$ ParameterList $$)$$

    DelimitedTokenTree ::=
        $$($$ TokenTree* $$)$$
        | $$[$$ TokenTree* $$]$$
        | $${$$ TokenTree* $$}$$

    TokenTree ::=
        DelimitedTokenTree
        | NonDelimitedToken


:dp:`hash_I2ViG44UZXTL`
A :ds:`NonDelimitedToken` is any :t:`lexical element` in category :s:`LexicalElement`, except 
the the category :s:`Delimiter`.


.. rubric:: Examples

.. code-block:: rust
    
    sums := () => {
        min := @min {1 + 2, 3 * 4, 7 - 6 + 1 };
        max := @max {1 + 2, 3 * 4, 7 - 6 + 1 };

        if max - min == 0 {
            println("min and max are equal")
        } else {
            println("min and max are not equal")
        }
    }



    welcome := () => {
        @[xml(variant=html)] {
            <html>
                <head>
                    <title>My page</title>
                </head>
                <body>
                    <h1>Hello, world!</h1>
                </body>
            </html>
        }
    }
