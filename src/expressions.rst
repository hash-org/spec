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

.. _hash_8MQGSyTVdPXx:

Literal Expressions
-------------------
.. rubric:: Syntax

.. syntax::
    LiteralExpression ::=
        Literal


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

.. _hash_br5j9dey5jJ6:

Variable Expressions
--------------------

.. rubric:: Syntax

.. syntax::
    
        VariableExpression ::=
            Name


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

Dereference Expressions
~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    DerefExpression ::=
        $$*$$ NonDeclarativeExpression


.. _hash_1iQlXSvyYYXR:

Reference Expressions
~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    RefExpression ::=
        $$&$$ ReferenceModifier? $$mut$$? NonDeclarativeExpression


.. _hash_LhnJiydVfYul:

Not Expressions
~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    NotExpression ::=
        $$!$$ NonDeclarativeExpression

.. _hash_aNHCHTzBbeSs:

Bit Not Expressions
~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    BitNotExpression ::=
        $$~$$ NonDeclarativeExpression

.. _hash_jRX7F5gNpCFc:

Negation Expressions
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    NegationExpression ::=
        $$-$$ NonDeclarativeExpression

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

.. _hash_e5M9hRfsFIE8:

Assignment Expressions
----------------------

.. rubric:: Syntax

.. syntax::

    AssignExpression ::=
        Assignment
        | CompoundAssignment

    Assignment ::=

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

.. _hash_cfCQhWZGWi6K:

Merge Declarations
^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::
    MergeDeclaration ::=
        NonDeclarativeExpression $$~=$$ NonDeclarativeExpression

.. _hash_DfmsxKNSiaha:

Index Expressions
-----------------


.. rubric:: Syntax

.. syntax::

    IndexExpression ::=
        NonDeclarativeExpression $$[$$ NonDeclarativeExpression $$]$$

.. _hash_rJHNqIdEx0Nr:

Access Expressions
------------------

.. rubric:: Syntax

.. syntax::

    AccessExpression ::=
        FieldAccessExpression
        | NamespaceAccessExpression

    FieldAccessExpression ::=
        NonDeclarativeExpression $$.$$ Name

    NamespaceAccessExpression ::=
        NonDeclarativeExpression $$::$$ Name


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

.. _hash_O6mTULDLSCjD:

Tuple Expressions
-----------------

.. rubric:: Syntax

.. syntax::

    TupleExpression ::=
        $$($$ ParameterList? $$)$$


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

.. _hash_SHh7tcsCxGWd:

Break Expressions
~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    BreakExpression ::=
        $$break$$

.. _hash_0OlkIHYvhUlH:

Continue Expressions
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    ContinueExpression ::=
        $$continue$$

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

.. _hash_eDqHfinZl9sD:

Unsafe Blocks
~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    
    UnsafeBlockExpression ::=
        $$unsafe$$ BlockExpression

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

.. _hash_DDXFlQeXdlTb:

For Loops
~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    ForLoopExpression ::=
        $$for$$ Pattern $$in$$ NonDeclarativeExpression LoopBody

.. _hash_NEKqZT5DIyV7:

Infinite Loops
~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
    InfiniteLoopExpression ::=
        $$loop$$ LoopBody

.. _hash_3u0oeQnFVsDL:

If Expressions
--------------

.. rubric:: Syntax

.. syntax::
    
    IfExpression ::=
        $$if$$ NonDeclarativeExpression BlockExpression ElseExpression?

    ElseExpression ::=
        $$else$$ (IfExpression | BodyBlockExpression)

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

.. _hash_tTS2rltCjlbT:

Imports
-------

.. rubric:: Syntax

.. syntax::
    Import ::=
        $$import$$ $$($$ StringLiteral $$)$$

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

.. _hash_CAfcmZP6nqhj:

Types in Expressions
--------------------

.. rubric:: Syntax

.. syntax::

    TypeExpression ::=
        $$type$$ Type

.. _hash_udHYbgicfx0C:

Macro Invocations as Expressions
--------------------------------

.. rubric:: syntax

.. syntax::
    ExpressionMacroInvocation ::= 
        MacroInvocationHeader NonDeclarativeExpression
