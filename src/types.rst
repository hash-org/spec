.. default-domain:: spec

.. _hash_vKkaa5pGi6sA:

Types
=====

.. rubric:: Syntax

.. syntax::
    Type ::=
        | MergeType
        | UnionType
        | SingleType

    SingleType ::=
        NamedType
        | ReferenceType
        | TupleType
        | FunctionType
        | TokenMacroInvocation
        | NeverType
        | AccessType
        | ArrayType
        | ParenthesisedType
        | TypeFunctionType
        | TypeFunctionCall
        | ExpressionInType
        | TypeMacroInvocation

.. _hash_nzY3zeUHNon4:

Named Types
-----------

.. rubric:: Syntax

.. syntax::

    NamedType ::=
        Name

.. rubric:: Examples

.. code-block:: rust

    i32
    Data
    Foo

.. _hash_tkj1CVIUzNKe:

Reference Types
---------------

.. warning::
    This is a work in progress.

.. rubric:: Syntax

.. syntax::

    ReferenceType ::=
        $$&$$ ReferenceModifier? $$mut$$? Type  

.. rubric:: Examples

.. code-block:: rust

    &raw mut i32
    &rc User
    &mut i32

.. _hash_6cpgWsgC4Ryu:

Access Types
------------

.. rubric:: Syntax

.. syntax::
    AccessType ::=
        Type $$::$$ Name

.. rubric:: Examples

.. code-block:: rust

    llvm::AttributeKind

.. _hash_wCvkae6O7Ryl:

Tuple Types
-----------

.. rubric:: Syntax

.. syntax::
    TupleType ::=
        $$($$ SimpleTypeParameterList? $$)$$

.. rubric:: Examples

.. code-block:: rust

    (i32, char, str)
    (count: i32, lookup: char, message: str)

.. _hash_6mgF88dKCbY5:

Function Types
--------------

.. rubric:: Syntax

.. syntax::
    
    FunctionType ::=
        (SimpleTypeParameterList?) $$->$$ Type 

.. rubric:: Examples

.. code-block:: rust

    (i32, str) -> i32
    (offset: i32, message: str) -> i32

.. _hash_Xso6gV8KIXnT:

Never Types
-----------

.. rubric:: Syntax

.. syntax::
    NeverType ::=
        $$!$$

.. rubric:: Examples

.. code-block:: rust

    panic := (message: str) -> ! {
    }

.. _hash_Om15wfaRYWur:

Array Types
-----------

.. rubric:: Syntax

.. syntax::
    ArrayType ::=
        $$[$$ Type LengthSpecifier? $$]$$

    LengthSpecifier ::=
        $$;$$ Expression

.. rubric:: Examples

.. code-block:: rust
    
    [i32]
    [i32; 3]
    [i32; 3 + 4]

.. _hash_yhxfTqIPszdT:

Parenthesised Types
-------------------

.. rubric:: Syntax

.. syntax::
    ParenthesisedType ::=
        $$($$ Type $$)$$

.. rubric:: Examples

.. code-block:: rust

    (i32 | i64)

.. _hash_0uLu8VwkkLMj:

Merge Types
-----------

.. warning::
    This is a work in progress. This is likely to be removed or re-purposed.

.. rubric:: Syntax

.. syntax::
    MergeType ::=
        SingleType ($$~$$ SingleType)*

.. rubric:: Examples

.. code-block:: rust

    Sub ~ Add ~ Mul ~ Div

.. _hash_pr3R3LUK7rJ7:

Union of Types
--------------

.. rubric:: Syntax

.. syntax::

    UnionType ::=
        SingleType ($$|$$ SingleType)*

.. rubric:: Examples

.. code-block:: rust

    i8 | i16 | i32 | i64

.. _hash_wknReDs1eImi:

Type Function Types
-------------------

.. rubric:: Syntax

.. syntax::

    TypeFunctionType ::=
        $$<$$ TypeParameterList? $$>$$ $$->$$ Type

.. rubric:: Examples

.. code-block:: rust

    <T> -> T
    <T := i32, U> -> (T, U)

.. _hash_2uvNLVFKbzeO:

Type Parameters
~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    SimpleTypeParameterList ::=
        SimpleTypeParameter ($$,$$ SimpleTypeParameter)? $$,$$?

    SimpleTypeParameter ::=
        Name ($$:$$ Type)
        | Type

    TypeParameterList ::=
        TypeParameter ($$,$$ TypeParameter)? $$,$$?

    TypeParameter ::=
        MacroInvocationHeader? TypeParameterContent

    TypeParameterContent ::=
        Name $$:$$ Type? $$=$$ Type
        | Name $$:$$ Type
        | Name

.. _hash_eTbHnm2PdsD2:

Type Function Call
------------------

.. rubric:: Syntax

.. syntax::
    TypeFunctionCall ::=
        TypeFunctionCallSubject $$<$$ TypeArgumentList? $$>$$

    TypeFunctionCallSubject ::=
        Type
        | NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    Data := struct<T>(
        id: i32,
        data: T,
    )

    foo := <T> => (data: Data<T>) -> i32 => {
        data.get_id()
    }

.. _hash_bAvzCyt9d3Ih:

Type Arguments
~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

    TypeArgumentList ::=
        TypeArgument ($$,$$ TypeArgument)? $$,$$?

    TypeArgument ::=
        MacroInvocationHeader? Name ($$=$$ Type)?

.. _hash_lnE1CR5DwJx2:

Expressions in Types
--------------------

.. rubric:: Syntax

.. .. @@Todo: Is it non declarative or is a top level expression?

.. syntax::

    ExpressionInType ::=
        $${$$ NonDeclarativeExpression $$}$$
        | Literal

.. rubric:: Examples

.. code-block:: rust

    bar := (arg: { foo() }) => {
        ...
    }

    foo := () -> 1 => {
        1
    }

.. _hash_pSVhBgXUl5jA:

Macro Invocations as Types
--------------------------

.. rubric:: syntax

.. syntax::
    TypeMacroInvocation ::= 
        MacroInvocationHeader SingleType


.. rubric:: Examples

.. code-block:: rust

    Foo := struct<#constrain T>(

    )

    Foo := type #c_union f32 | i32 | i64
