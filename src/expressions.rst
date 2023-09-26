.. default-domain:: spec

.. _hash_Kpvc7lmibdbv:

Expressions
===========

.. rubric:: Syntax

.. syntax::
    Expression ::=
        Declaration
        | MergeDeclaration
        | NonDeclarativeExpression
    
    NonDeclarativeExpression ::= 
        SingleExpression
        | DefinitionExpression
        | UnaryExpression
        | BinaryExpression
        | ExpressionWithBlock
        
    ExpressionWithBlock ::=
        BlockExpression
        | ModuleDefinition
        | ImplDefinition
        | TraitDefinition

    DefinitionExpression ::=
        FunctionDefinition
        | StructDefinition
        | EnumDefinition
        | TypeFunctionDefinition


    SingleExpression ::=
        VariableExpression
        | AccessExpression
        | IndexExpression
        | AssignExpression
        | Import
        | LiteralExpression
        | ArrayExpression
        | TupleExpression
        | CallExpression
        | ContinueExpression
        | BreakExpression
        | ReturnExpression
        | RangeExpression
        | TypeExpression
        | ExpressionMacroInvocation
        | TokenMacroInvocation

    ExpressionList ::=
        NonDeclarativeExpression ($$,$$ NonDeclarativeExpression)* $$,$$?

    ExpressionArgument ::=
        Name ($$=$$ NonDeclarativeExpression)?
        | NonDeclarativeExpression


.. _hash_Sd2lh8RXfbAa:

Declaration
-----------

.. rubric:: Syntax

.. syntax::

    Declaration ::=
        SingularPattern $$:$$ Type? $$=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    mut k := 0
    foo := 1
    bar: f32 = 1.0
    pub baz := 1
    (a, b) := (1, 2)
    User(mut name, ...) := user


.. _hash_8MQGSyTVdPXx:

Literal Expressions
-------------------
.. rubric:: Syntax

.. syntax::
    LiteralExpression ::=
        Literal

.. rubric:: Examples

.. code-block:: rust

    "a"
    3.2
    'ø'
    7

.. _hash_qAHgsRCWiPk6:

Array Expressions
-------------------

.. rubric:: Syntax

.. syntax::
    ArrayExpression ::=
        $$[$$ ArrayElementExpression? $$]$$

    ArrayElementExpression ::=
        ArrayElementConstructor
        | ArrayRepetitionConstructor

    ArrayElementConstructor ::=
        ExpressionList

    ArrayRepetitionConstructor ::=
        NonDeclarativeExpression $$;$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    [1, 2, 3, 4]

:dp:`hash_qjAN2J9UmK7E`
Two dimensional arrays:

.. code-block:: rust

    [[1, 2, 3], [4, 5, 6]]


:dp:`hash_qjAN2J8UmK7E`
An array of four hundred and twenty 69s:

.. code-block:: rust

    [69; 420]

.. _hash_br5j9dey5jJ6:

Variable Expressions
--------------------

.. rubric:: Syntax

.. syntax::
    
        VariableExpression ::=
            Name

.. rubric:: Examples

.. code-block:: rust

    var
    foo

.. _hash_zq8Zc7e5k4Af:

Unary Expressions
-----------------

.. rubric:: Syntax

.. syntax::

    UnaryExpression ::=
        DerefExpression
        RefExpression
        NotExpression
        BitNotExpression
        NegationExpression

.. _hash_oYffwqHwmVwz:

Dereferencing Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    DerefExpression ::=
        $$*$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    foo := (value: &i32) => {
        deref_value := *value
    }

.. _hash_1iQlXSvyYYXR:

Reference Expressions
~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    RefExpression ::=
        $$&$$ ReferenceModifier? $$mut$$? NonDeclarativeExpression


.. rubric:: Examples

.. code-block:: rust

    bar := (value: &mut i32) => {
    }

    foo := () => {
        mut value := 7
        bar(&mut value)
    }

.. _hash_LhnJiydVfYul:

Not Expressions
~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    NotExpression ::=
        $$!$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    has_errors: bool := check_errors()

    if !has_errors {
        ...
    }

.. _hash_aNHCHTzBbeSs:

Bit Not Expressions
~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    BitNotExpression ::=
        $$~$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    ~0b1010

.. _hash_jRX7F5gNpCFc:

Negation Expressions
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    NegationExpression ::=
        $$-$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    -42

.. _hash_xerbcwK8VIBz:

Binary Expressions
------------------

.. rubric:: Syntax

.. syntax::
    BinaryExpression ::=
        ArithmeticExpression
        | BitExpression
        | ComparisonExpression
        | LazyBooleanExpression


.. _hash_tuqDlmmo6jdF:

Arithmetic Expressions
~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    ArithmeticExpression ::=
        AddExpression
        | SubtractionExpression
        | MultiplicationExpression
        | DivisionExpression
        | ModuloExpression
        | ExponentiationExpression

    AddExpression ::=
        NonDeclarativeExpression $$+$$ NonDeclarativeExpression

    SubtractionExpression ::=
        NonDeclarativeExpression $$-$$ NonDeclarativeExpression

    MultiplicationExpression ::=
        NonDeclarativeExpression $$*$$ NonDeclarativeExpression

    DivisionExpression ::=
        NonDeclarativeExpression $$/$$ NonDeclarativeExpression

    ModuloExpression ::=
        NonDeclarativeExpression $$%$$ NonDeclarativeExpression

    ExponentiationExpression ::=
        NonDeclarativeExpression $$^^$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    1 + 2
    4.0 / 3.29
    8.4 * 5.3
    10 % 4
    3 - 2
    4 ^^ 2


.. _hash_QLArFzMsp9kG:

Bit Expressions
~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
        BitExpression ::=
            BitAndExpression
            | BitOrExpression
            | BitXorExpression
            | BitShiftLeftExpression
            | BitShiftRightExpression
    
        BitAndExpression ::=
            NonDeclarativeExpression $$&$$ NonDeclarativeExpression
    
        BitOrExpression ::=
            NonDeclarativeExpression $$|$$ NonDeclarativeExpression
    
        BitXorExpression ::=
            NonDeclarativeExpression $$^$$ NonDeclarativeExpression
    
        BitShiftLeftExpression ::=
            NonDeclarativeExpression $$<<$$ NonDeclarativeExpression
    
        BitShiftRightExpression ::=
            NonDeclarativeExpression $$>>$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    0b1010 & 0b1100
    0b1010 | 0b0011
    0b1010 ^ 0b1001
    13 << 3
    -10 >> 2

.. _hash_V4AOaHcg4Jd8:

Comparison Expressions
~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    ComparisonExpression ::=
        LessThanExpression
        | LessThanOrEqualExpression
        | GreaterThanExpression
        | GreaterThanOrEqualExpression
        | EqualExpression
        | NotEqualExpression

    LessThanExpression ::=
        NonDeclarativeExpression $$<$$ NonDeclarativeExpression

    LessThanOrEqualExpression ::=
        NonDeclarativeExpression $$<=$$ NonDeclarativeExpression

    GreaterThanExpression ::=
        NonDeclarativeExpression $$>$$ NonDeclarativeExpression

    GreaterThanOrEqualExpression ::=
        NonDeclarativeExpression $$>=$$ NonDeclarativeExpression

    EqualExpression ::=
        NonDeclarativeExpression $$==$$ NonDeclarativeExpression

    NotEqualExpression ::=
        NonDeclarativeExpression $$!=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    12 == 12
    42 > 12
    42 >= 35
    42 < 109
    42 <= 42
    12 != 42

.. _hash_WPlesql70uwO:

Lazy Boolean Expressions
~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    LazyBooleanExpression ::=
        LazyAndExpression
        | LazyOrExpression

    LazyAndExpression ::=
        NonDeclarativeExpression $$&&$$ NonDeclarativeExpression

    LazyOrExpression ::=
        NonDeclarativeExpression $$||$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    true && abort()
    false || true

.. _hash_e5M9hRfsFIE8:

Assignment Expressions
----------------------

.. rubric:: Syntax

.. syntax::

    AssignExpression ::=
        Assignment
        | CompoundAssignment

    Assignment ::=
        NonDeclarativeExpression $$=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    b = 2
    (four, two) = (4, 2)

.. _hash_iFQ7NRzLVKRp:

Compound Assignment
~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    CompoundAssignment ::=
        ArithmeticCompoundAssignment
        | BitCompoundAssignment
        | LazyCompoundAssignment
        | MergeDeclaration


.. _hash_Y4o1cYOg6BwR:

Arithmetic Compound Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::
    ArithmeticCompoundAssignment ::=
        AddCompoundAssignment
        | SubtractionCompoundAssignment
        | MultiplicationCompoundAssignment
        | DivisionCompoundAssignment
        | ModuloCompoundAssignment
        | ExponentiationCompoundAssignment

    AddCompoundAssignment ::=
        NonDeclarativeExpression $$+=$$ NonDeclarativeExpression

    SubtractionCompoundAssignment ::=
        NonDeclarativeExpression $$-=$$ NonDeclarativeExpression
    
    MultiplicationCompoundAssignment ::=
        NonDeclarativeExpression $$*=$$ NonDeclarativeExpression
    
    DivisionCompoundAssignment ::=
        NonDeclarativeExpression $$/=$$ NonDeclarativeExpression

    ModuloCompoundAssignment ::=
        NonDeclarativeExpression $$%=$$ NonDeclarativeExpression
    
    ExponentiationCompoundAssignment ::=
        NonDeclarativeExpression $$^^=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust
    
    mut result := 0
    result += 1
    result /= 3
    result ^= 2
    result *= 81
    result %= 7
    result -= 0
    result ^^= 6

.. _hash_W2JfEPpxYlBR:

Bit Compound Assignments
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

    BitCompoundAssignment ::=
        BitAndCompoundAssignment
        | BitOrCompoundAssignment
        | BitXorCompoundAssignment
        | BitShiftLeftCompoundAssignment
        | BitShiftRightCompoundAssignment

    BitAndCompoundAssignment ::=
        NonDeclarativeExpression $$&=$$ NonDeclarativeExpression

    BitOrCompoundAssignment ::=
        NonDeclarativeExpression $$|=$$ NonDeclarativeExpression

    BitXorCompoundAssignment ::=
        NonDeclarativeExpression $$^=$$ NonDeclarativeExpression
    

    BitShiftLeftCompoundAssignment ::=
        NonDeclarativeExpression $$<<=$$ NonDeclarativeExpression
    
    BitShiftRightCompoundAssignment ::=
        NonDeclarativeExpression $$>>=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    mut result := 0
    result |= 9402
    result &= 59
    result <<= 2
    result >>= 3

.. _hash_67QA35Mu7Pa2:

Lazy Compound Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::
    LazyCompoundAssignment ::=
        LazyCompoundAndAssignment
        | LazyCompoundOrAssignment

    LazyCompoundAndAssignment ::=
        NonDeclarativeExpression $$&&=$$ NonDeclarativeExpression

    LazyCompoundOrAssignment ::=
        NonDeclarativeExpression $$||=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    value &&= true
    value ||= false

.. _hash_cfCQhWZGWi6K:

Merge Declarations
^^^^^^^^^^^^^^^^^^

.. warning:: 
    This is work in progress and not yet implemented.

.. rubric:: Syntax

.. syntax::
    MergeDeclaration ::=
        NonDeclarativeExpression $$~=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    Foo := struct(
        bar: i32,
        frobulatation_enabled := false,
    )


    Frobulate := trait {
        frob := (self) -> bool
    }

    Foo ~= impl Frobulate {
        frob := (self) => {
            self.frobulatation_enabled
        }
    }

.. _hash_DfmsxKNSiaha:

Index Expressions
-----------------


.. rubric:: Syntax

.. syntax::

    IndexExpression ::=
        NonDeclarativeExpression $$[$$ NonDeclarativeExpression $$]$$

.. rubric:: Examples

.. code-block:: rust

     a := [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a[1][2]

.. _hash_rJHNqIdEx0Nr:

Access Expressions
------------------

.. rubric:: Syntax

.. syntax::

    AccessExpression ::=
        FieldAccessExpression
        | NamespaceAccessExpression

    FieldAccessExpression ::=
        NonDeclarativeExpression $$.$$ FieldSelector

    FieldSelector ::=
        IndexedFieldSelector
        | NamedFieldSelector

    IndexedFieldSelector ::=
        DecimalLiteral

    NamedFieldSelector ::=
        Name

    NamespaceAccessExpression ::=
        NonDeclarativeExpression $$::$$ Name

.. rubric:: Examples

.. code-block:: rust

    foo.bar.1
    foo::bar

.. _hash_gqH9Bg8P1ey2:

Call Expressions
----------------

.. rubric:: Syntax

.. syntax::

    CallExpression ::=
        NonDeclarativeExpression $$($$ ParameterList? $$)$$


    ParameterList ::=
        Parameter ($$,$$ Parameter)* $$,$$?


    Parameter ::=
        Name
        | Name = NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    bar := foo(1, 2, 3, should_cache=true, should_log=false)

.. _hash_O6mTULDLSCjD:

Tuple Expressions
-----------------

.. rubric:: Syntax

.. syntax::

    TupleExpression ::=
        $$($$ ParameterList? $$)$$

.. rubric:: Examples

.. code-block:: rust
    
    (1, 'c', [1, 2])
    (i = 1, am = 'c', named = [1, 2])

.. _hash_fghbL291ks0P:

Control Flow Expressions
------------------------

.. _hash_qq4W0XDKhH3Z:

Return Expressions
~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    ReturnExpression ::=
        $$return$$ NonDeclarativeExpression?

.. rubric:: Examples

.. code-block:: rust

    return
    return 52

.. _hash_SHh7tcsCxGWd:

Break Expressions
~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    BreakExpression ::=
        $$break$$

.. rubric:: Examples

.. code-block:: rust

    loop {
        x := get_number()

        if x > 2 {
            break
        }
    }

.. _hash_0OlkIHYvhUlH:

Continue Expressions
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    ContinueExpression ::=
        $$continue$$

.. rubric:: Examples

.. code-block:: rust

    loop {
        x := get_number()

        if x > 2 {
            continue
        }
    }

.. _hash_3g4fwzJmMRuw:

Block Expressions
-----------------

.. rubric:: Syntax

.. syntax::
    BlockExpression ::=
        | BodyBlockExpression
        | LoopExpression
        | IfExpression
        | MatchExpression
        | UnsafeBlockExpression

.. _hash_MjcXZSIDcdso:

Body Blocks
~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    BodyBlockExpression ::=
        $${$$ Statement* Expression? $$}$$

.. rubric:: Examples

.. code-block:: rust

    foo := () => {
        mut t := {
            x := 1
            y := 2
            x + y
        }

        {
            t = do(t)
            t = something(t)
            t = crazy(t)
            t = with(t)
            t
        }
    }

.. _hash_eDqHfinZl9sD:

Unsafe Blocks
~~~~~~~~~~~~~

.. warning:: 
    This specification is not finalised.

.. rubric:: Syntax

.. syntax::
    
    UnsafeBlockExpression ::=
        $$unsafe$$ BlockExpression

.. rubric:: Examples

.. code-block:: rust

    #unsafe launch_rocket := () => {
        Intrinsics::write(0x1234, 0x5678)
        ...
    }


    main := () => {
        unsafe {
            launch_rocket()
        }
    }

.. _hash_gtSzBArdeSGx:

Loop Expressions
----------------

.. rubric:: Syntax

.. syntax::

    LoopExpression ::=
        WhileLoopExpression
        | ForLoopExpression
        | InfiniteLoopExpression

    LoopBody ::=
        BlockExpression

.. _hash_3P8J0iIodozl:

While Loops
~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    WhileLoopExpression ::=
        $$while$$ NonDeclarativeExpression LoopBody

.. rubric:: Examples

.. code-block:: rust

    mut x := initial_x()
    mut y := initial_y()


    while x < 2 && y > 3 {
        x = next_x_step(x)

        if x < 0 || y < 0 {
            break
        }

        if x > 2 {
            y = next_y_step(y)
        } else {
            y = previous_y_step(y)
        }
    }

.. _hash_DDXFlQeXdlTb:

For Loops
~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    ForLoopExpression ::=
        $$for$$ Pattern $$in$$ NonDeclarativeExpression LoopBody

.. rubric:: Examples

.. code-block:: rust

    ChessBoard := type [[Cell; 8]; 8]

    initialise_chess_board := () -> ChessBoard => {
        mut chess_board := [[Cell::Empty; 8]; 8]

        for row in 0..8 {
            for cell in 0..8 {
                chess_board[row][cell] = match (row, cell) {
                    ...
                }
            }
        }

        chess_board
    }


.. _hash_NEKqZT5DIyV7:

Infinite Loops
~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    InfiniteLoopExpression ::=
        $$loop$$ LoopBody

.. rubric:: Examples

.. code-block:: rust

    loop {
        print("zoom!")
    }

.. _hash_3u0oeQnFVsDL:

If Expressions
--------------

.. rubric:: Syntax

.. syntax::
    
    IfExpression ::=
        $$if$$ NonDeclarativeExpression BlockExpression ElseExpression?

    ElseExpression ::=
        $$else$$ (IfExpression | BodyBlockExpression)

.. rubric:: Examples

.. code-block:: rust

    if b == 2 {
        print("b is 2")
    } else if b == 3 {
        print("b is 3")
    } else {
        print("b isn't 2 or 3 ")
    }

.. _hash_YvISKrJpR43b:

Match Expressions
-----------------

.. rubric:: Syntax

.. syntax::
    MatchExpression ::=
        $$match$$ NonDeclarativeExpression $${$$ MatchArmList? $$}$$

    MatchArmList ::=
        MatchArm ($$,$$ MatchArm)* $$,$$?

    MatchArm ::=
        MacroInvocationHeader?
        Pattern $$=>$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    match foo() {
        0 | 1 => print("Got zero or one"),
        2 => print("Got two"),
        3 => print("Got three"),
        4 if the_sun_is_right() => print("Got 4 when the sun is right!"),
        4..10 => print("Got 4 to 10"),
        _ => print("Got something else")
    }

.. _hash_tTS2rltCjlbT:

Imports
-------

.. rubric:: Syntax

.. syntax::
    Import ::=
        $$import$$ $$($$ StringLiteral $$)$$

.. rubric:: Examples

.. code-block:: rust

    a := import("lib/a");
    b := import("lib/b");
    c := import("lib/sub/c");

.. _hash_Ruv4cVY02iVs:

Range Expressions
-----------------

.. rubric:: Syntax

.. syntax::
    RangeExpression ::=
        InclusiveRangeExpression
        | ExclusiveRangeExpression

    InclusiveRangeExpression ::=
        $$..$$ NonDeclarativeExpression
        | NonDeclarativeExpression $$..$$

    ExclusiveRangeExpression ::=
        $$..<$$ NonDeclarativeExpression
        | NonDeclarativeExpression $$..<$$

.. rubric:: Examples

.. code-block:: rust

    1..
    42..<86
    dawn..dusk
    ..< 5

.. _hash_CAfcmZP6nqhj:


Types in Expressions
--------------------

.. rubric:: Syntax

.. syntax::

    TypeExpression ::=
        $$type$$ Type

.. rubric:: Examples

.. code-block:: rust

    ChessBoard := type [[Cell; 8]; 8]
    NumberTypeAlias := type i32

.. _hash_udHYbgicfx0C:

Macro Invocations as Expressions
--------------------------------

.. rubric:: syntax

.. syntax::
    ExpressionMacroInvocation ::= 
        MacroInvocationHeader NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    #dump_ast
    foo := () => {
        ...
    }

    #non_exhaustive
    Bar := enum(
        Foo,
        Bar,
        Baz,
    )

    #[repr("C")]
    SizedPointer := struct(&raw u8, usize)
