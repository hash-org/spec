.. default-domain:: spec

.. _hash_8m692UBlh0hv:

Patterns
========

.. rubric:: Syntax

.. syntax::
    Pattern ::= 
        PatternWithoutAlternation ($$|$$ PatternWithoutAlternation)*

    PatternList ::=
        Pattern ($$,$$ Pattern)* $$,$$?

    PatternWithoutAlternation ::=
        SingularPatternOrSpread ($$if$$ Expression)?

    SingularPatternOrSpread ::=
        SingularPattern 
        | SpreadPattern

    PatternArgumentList ::=
        MacroInvocationHeader PatternArgument ($$,$$ PatternArgument)* $$,$$?

    PatternArgument ::=
        Name ($$=$$ SingularPattern)?
        | SpreadPattern

    SingularPattern ::=
        BindPattern
        | IgnorePattern
        | LiteralPattern
        | TuplePattern
        | AccessPattern
        | ArrayPattern
        | ParenthesisedPattern
        | ConstructorPattern
        | RangePattern
        | ModulePattern
        | TokenMacroInvocation
        | PatternMacroInvocation


.. _hash_kIdKMlaLLkrR:

Bind Patterns
-------------

.. rubric:: syntax

.. syntax::
    BindPattern ::= 
        Visibility? $$mut$$? Name


.. _hash_XbDlpGyVglmF:

Ignore Patterns
-------------------

.. rubric:: syntax

.. syntax::
    IgnorePattern ::= 
        $$_$$

.. _hash_uWUZbwYO0w9y:

Literal Patterns
----------------

.. rubric:: syntax

.. syntax::
    LiteralPattern ::=
        BooleanLiteral
        | CharacterLiteral
        | StringLiteral
        | NumericLiteral

.. _hash_kIFPeSpA9JPJ:

Tuple Pattern
---------------
    
.. rubric:: syntax

.. syntax::
    TuplePattern ::= 
        $$($$ PatternArgumentList? $$)$$

.. _hash_KBmDjC2cq4PO:

Access Patterns
---------------

.. rubric:: syntax

.. syntax::
    AccessPattern ::= 
        SingularPattern $$::$$ Name

.. _hash_zKgZyFUxFQhq:

Array Patterns
--------------

.. rubric:: syntax

.. syntax::
    ArrayPattern ::= 
        $$[$$ PatternList? $$]$$

.. _hash_H49z9ojYyO5R:

Parenthesised Patterns
----------------------

.. rubric:: syntax

.. syntax::
    ParenthesisedPattern ::= 
        $$($$ Pattern $$)$$

.. _hash_GJUHZYKm3XJP:

Constructor Patterns
--------------------

.. rubric:: syntax

.. syntax::
    ConstructorPattern ::= 
        SingularPattern $$($$ PatternArgumentList? $$)$$

.. _hash_sOuR1ifqsxsG:

Range Patterns
--------------

.. rubric:: syntax

.. syntax::
    RangePattern ::= 
          InclusiveRangePattern
        | ExclusiveRangePattern

    InclusiveRangePattern ::=
        RangePatternBound? $$..$$ RangePatternBound?

    ExclusiveRangePattern ::=
        RangePatternBound? $$..<$$ RangePatternBound?
    
    RangePatternBound ::=
        CharacterLiteral
        | NumericLiteral
        

.. _hash_sfhFygZBKt9K:

Module Patterns
---------------

.. warning::
    This is a work in progress.

.. rubric:: syntax

.. syntax::
    ModulePattern ::= 
        $${$$ ModulePatternList? $$}$$

    ModulePatternList ::= 
        ModulePatternArgument ($$,$$ ModulePatternArgument)* $$,$$?

    ModulePatternArgument ::= 
        Name ($$as$$ Pattern)?


.. _hash_ox7EQ5KV71ju:

Spread Patterns
---------------

.. rubric:: syntax

.. syntax::
    SpreadPattern ::= $$...$$ BindPattern?

.. _hash_xDvkSOyx68Eo:

Macro Invocations as Patterns
-----------------------------

.. rubric:: syntax

.. syntax::
    PatternMacroInvocation ::= 
        MacroInvocationHeader SingularPattern

