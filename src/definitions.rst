.. default-domain:: spec

.. _hash_6KGoOb5xb5QY:

Definitions
===========

.. _hash_qKF5flLyU5Wd:

Function Definitions
--------------------

.. rubric:: Syntax

.. syntax::

    FunctionDefinition ::=
        FunctionParameterList ($$->$$ Type)? $$=>$$ FunctionBody

    FunctionBody ::=
        NonDeclarativeExpression

    FunctionParameterList ::=
        FunctionParameter ($$,$$ FunctionParameter)* $$,$$?

    FunctionParameter ::=
        MacroInvocationHeader? FunctionParameterContent

    FunctionParameterContent ::=
        Name $$:$$ Type ($$=$$ NonDeclarativeExpression)?
        | Name $$:$$ Type? $$=$$ NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    foo := (i: i32, j: i32) -> i32 => {
        i + j
    }

    main := () => ()

.. _hash_FX5sGjm80Rpo:

Struct Definitions
------------------

.. rubric:: Syntax

.. syntax::
    StructDefinition ::=
        $$struct$$ DefinitionParameterList? $$($$ StructFieldList $$)$$ 

    StructFieldList ::=
        StructField ($$,$$ StructField)* $$,$$?

    StructField ::=
        MacroInvocationHeader? StructFieldContent

    StructFieldContent ::=
        Name $$:$$ Type? $$=$$ NonDeclarativeExpression
        | Name $$:$$ Type
        | Type

.. rubric:: Examples

.. code-block:: rust

    Foo := struct<T>(
        x: T,
        y: T = 0
        z: f32
    )

    #[repr("c")]
    SizedPointer := struct(&raw u8, usize)

.. _hash_Fg8pLyxXahPO:

Enum Definitions
------------------

.. rubric:: Syntax

.. syntax::
    EnumDefinition ::=
        $$enum$$ DefinitionParameterList? $$($$ EnumVariantList $$)$$

    EnumVariantList ::=
        EnumVariant ($$,$$ EnumVariant)* $$,$$?

    EnumVariant ::=
        MacroInvocationHeader? EnumVariantContent

    EnumVariantContent ::=
        Name EnumVariantFieldsList? ($$:$$ Type)? ($$=$$ NonDeclarativeExpression)?

    EnumVariantFieldsList ::= $$($$ ParameterList $$)$$

.. rubric:: Examples

.. code-block:: rust

    Foo := enum<T>(
        Bar,
        Baz(i32),
        Qux(i32, f32)
    )

    ErrorCode := enum(
        None = 0,
        InvalidArgument = 1,
        InvalidState = 2,
        InvalidOperation = 3,
        #[display_name("Invalid Data")]
        InvalidData = 4
    )

.. _hash_10KrB2F6pdlG:

Implicit Function Definitions
-----------------------------

.. rubric:: Syntax

.. syntax::
    ImplicitFunctionDefinition ::=
        DefinitionParameterList ($$->$$ Type)? $$=>$$ ImplicitFunctionBody

    ImplicitFunctionBody ::=
        NonDeclarativeExpression

.. rubric:: Examples

.. code-block:: rust

    List := <T> => struct(
        #[opaque]
        head: T,
        tail: &List<T>
    )

.. _hash_mM7RfmoAQtt9:

Traits
------

.. warning:: 
    This is work in progress and not yet implemented.

.. _hash_D5a1y4BYMQpc:

Module Definitions
------------------

.. rubric:: Syntax

.. syntax::
    ModuleDefinition ::=
        $$mod$$ DefinitionParameterList? $${$$ ModuleMemberList $$}$$
    
    ModuleMemberList ::=
        StatementList

.. rubric:: Examples

.. code-block:: rust

    pub nested := mod {
        pub Colour := enum(Red, Green, Blue)

        MixedColour := struct(u32);

        priv combine_colours := (a: Colour, b: Colour) -> MixedColour => {
            ...
        }
    }

.. _hash_gCrbjVEL55Qt:

Implementation Definitions
--------------------------

.. warning:: 
    This is work in progress and not yet implemented.

.. _hash_jok00upP4s4V:

Definition Parameters
---------------------

.. rubric:: Syntax

.. syntax::

    DefinitionParameterList ::= 
        $$<$$ TypeParameterList? $$>$$
