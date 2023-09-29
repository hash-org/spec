.. default-domain:: spec

.. _hash_8m692UBlh0hv:

Patterns
========

.. rubric:: Syntax

.. syntax::
    Pattern ::= 
        PatternWithoutAlternation ($$|$$ PatternWithoutAlternation)*

    PatternWithoutAlternation ::=
        SingularPattern 
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
        | GuardedPattern
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
    
    pub mut foo := 1;
    mut foo
    foo


.. _hash_XbDlpGyVglmF:

Ignore Patterns
-------------------

.. rubric:: syntax

.. syntax::
    IgnorePattern ::= 
        $$_$$

.. rubric:: Examples

.. code-block:: rust

    match t {
        Some(_) => {}
        None => {}
    }

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
    
    false := false
    'a' := 'a'
    "foo" := "foo"
    1 := 1

.. _hash_kIFPeSpA9JPJ:

Tuple Pattern
---------------
    
.. rubric:: syntax

.. syntax::
    TuplePattern ::= 
        $$($$ PatternArgumentList? $$)$$

    PatternArgumentList ::=
        MacroInvocationHeader PatternArgument ($$,$$ PatternArgument)* $$,$$?

    PatternArgument ::=
        Name ($$=$$ SingularPattern)?
        | SpreadPattern

.. rubric:: Examples

.. code-block:: rust

    match (a, b) {
     (1, 2) => {
        print("basic") 
     }
     (2..<10, y) => {
        print("y is {y}")
     }
     _ => {
        print("unclear")
     }
    }

.. _hash_KBmDjC2cq4PO:

Access Patterns
---------------

.. rubric:: syntax

.. syntax::
    AccessPattern ::= 
        SingularPattern $$::$$ Name

.. rubric:: Examples

.. code-block:: rust

    Direction := enum(
        North,
        South,
        East,
        West
    )

    compute_index := (direction: Direction, other: Direction) => {
        match (direction, other) {
            (Direction::South, Direction::North) => 0,
            (Direction::North, Direction::South) => 1,
            (Direction::East, Direction::West) => 2,
            (Direction::West, Direction::East) => 3,
            _ => panic("invalid direction")
        }
    }

.. _hash_zKgZyFUxFQhq:

Array Patterns
--------------

.. rubric:: syntax

.. syntax::
    ArrayPattern ::= 
        $$[$$ PatternList? $$]$$

    PatternList ::=
        Pattern ($$,$$ Pattern)* $$,$$?

.. rubric:: Examples

.. code-block:: rust

    [1, 2, 3]
    [1, 2, 3, ...rest]
    [1, 2, ...middle, 9, 10]

.. _hash_H49z9ojYyO5R:

Parenthesised Patterns
----------------------

.. rubric:: syntax

.. syntax::
    ParenthesisedPattern ::= 
        $$($$ Pattern $$)$$

.. rubric:: Examples

.. code-block:: rust
    
    (1 | 2 | 3 | 4)

.. _hash_GJUHZYKm3XJP:

Constructor Patterns
--------------------

.. rubric:: syntax

.. syntax::
    ConstructorPattern ::= 
        SingularPattern $$($$ PatternArgumentList? $$)$$

.. rubric:: Examples

.. code-block:: rust

    Dog(breed = dog_breed, name = dog_name) := Dog(
        name = "Bob",
        breed = "Husky"
    )

    viktor := Dog(name = "Viktor", breed = "Husky") 

    match viktor {
        Dog(breed = "Husky", ...) => {
            print("viktor is a husky")
        }
        _ => {
            print("viktor is not a husky")
        }
    }
    

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

    main := (k: i32) => {
        2..6 := k
        'c'..'z' := cast<_, char>(k)

        match k {
            -3..56 => print("it's negative three!"),
            57..<59 => print("between 57 and 59"),
            _ => print("not negative three"),
        };
    }

.. _hash_lGRG2mVPj8q8:

Guarded Patterns
----------------

.. warning::
    This is a work in progress.

.. rubric:: syntax

.. syntax::

    GuardedPattern ::=
        SingularPattern $$if$$ Expression

.. rubric:: Examples

.. code-block:: rust

    t := 4
    k := 1

    // Parsed as `Or(1, 4) if k`
    match t {
        (1 | 4) if k == 1 => {},
        _ => {}
    }

    // Parsed as `Or(1, 4 if k )`
    match t {
        1 | 4 if k == 1 => {},
        _ => {}
    }

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

    {
      Colour as MyColour,
      Shape as MyShape,
    } := import("drawing")

.. _hash_ox7EQ5KV71ju:

Spread Patterns
---------------

.. rubric:: syntax

.. syntax::
    SpreadPattern ::= $$...$$ BindPattern?

.. rubric:: Examples

.. code-block:: rust

    (first, ...) := (1, 2, 3, 4, 5)
    Dog(name, ...rest) := Dog(name = "Bob", breed = "Husky")
    [a, b, c, ...] := [1, 2, 3, 4, 5]

.. _hash_xDvkSOyx68Eo:

Macro Invocations as Patterns
-----------------------------

.. rubric:: syntax

.. syntax::
    PatternMacroInvocation ::= 
        MacroInvocationHeader SingularPattern

.. rubric:: Examples

.. code-block:: rust
