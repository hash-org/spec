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

.. rubric:: Examples

.. code-block:: rust

.. _hash_XbDlpGyVglmF:

Ignore Patterns
-------------------

.. rubric:: syntax

.. syntax::
    IgnorePattern ::= 
        $$_$$

.. rubric:: Examples

.. code-block:: rust

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

.. rubric:: Examples

.. code-block:: rust

.. _hash_kIFPeSpA9JPJ:

Tuple Pattern
---------------
    
.. rubric:: syntax

.. syntax::
    TuplePattern ::= 
        $$($$ PatternArgumentList? $$)$$

.. rubric:: Examples

.. code-block:: rust

.. _hash_KBmDjC2cq4PO:

Access Patterns
---------------

.. rubric:: syntax

.. syntax::
    AccessPattern ::= 
        SingularPattern $$::$$ Name

.. rubric:: Examples

.. code-block:: rust

.. _hash_zKgZyFUxFQhq:

Array Patterns
--------------

.. rubric:: syntax

.. syntax::
    ArrayPattern ::= 
        $$[$$ PatternList? $$]$$

.. rubric:: Examples

.. code-block:: rust

.. _hash_H49z9ojYyO5R:

Parenthesised Patterns
----------------------

.. rubric:: syntax

.. syntax::
    ParenthesisedPattern ::= 
        $$($$ Pattern $$)$$

.. rubric:: Examples

.. code-block:: rust

.. _hash_GJUHZYKm3XJP:

Constructor Patterns
--------------------

.. rubric:: syntax

.. syntax::
    ConstructorPattern ::= 
        SingularPattern $$($$ PatternArgumentList? $$)$$

.. rubric:: Examples

.. code-block:: rust

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
        
.. rubric:: Examples

.. code-block:: rust

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

.. rubric:: Examples

.. code-block:: rust

.. _hash_ox7EQ5KV71ju:

Spread Patterns
---------------

.. rubric:: syntax

.. syntax::
    SpreadPattern ::= $$...$$ BindPattern?

.. rubric:: Examples

.. code-block:: rust

.. _hash_xDvkSOyx68Eo:

Macro Invocations as Patterns
-----------------------------

.. rubric:: syntax

.. syntax::
    PatternMacroInvocation ::= 
        MacroInvocationHeader SingularPattern

.. rubric:: Examples

.. code-block:: rust
