.. default-domain:: spec

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
