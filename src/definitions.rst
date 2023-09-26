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
        Name $$:$$ Type
        | Name $$:$$ Type $$=$$ NonDeclarativeExpression
        | Name $$=$$ NonDeclarativeExpression

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

Type Function Definitions
-------------------------

.. rubric:: Syntax

.. syntax::
    TypeFunctionDefinition ::=
        DefinitionParameterList ($$->$$ Type)? $$=>$$ TypeFunctionBody

    TypeFunctionBody ::=
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

.. rubric:: Syntax

.. syntax::
    TraitDefinition ::=
        $$trait$$ DefinitionParameterList? $${$$ TraitMemberList $$}$$

    TraitMemberList ::=
        StatementList

.. rubric:: Examples

.. code-block:: rust

    Sequence := <T> => trait {
        at: (self, index: usize) -> Option<T>
        slice: (self, start: usize, end: usize) -> Self
    }

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

.. rubric:: Syntax

.. syntax::
    ImplDefinition ::=
        $$impl$$ DefinitionParameterList? $${$$ ImplMemberList $$}$$

        ImplMemberList ::=
            StatementList

.. rubric:: Examples

.. code-block:: rust

    Vector3 := struct<T>(x: T, y: T, z: T);

    Vector3 ~= impl<T: Mul ~ Sub> {
        // Cross is an associated function on `Vector3<T>` for any `T: Mul ~ Sub`.
        cross := (self, other: Self) -> Self => {
            Vector3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x,
            )
        }
    }


.. _hash_jok00upP4s4V:

Definition Parameters
---------------------

.. rubric:: Syntax

.. syntax::

    DefinitionParameterList ::= 
        $$<$$ TypeParameterList? $$>$$
