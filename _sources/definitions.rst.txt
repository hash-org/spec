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
        Name EnumVariantFieldsList? ($$:$$ Type)?

    EnumVariantFieldsList ::= $$($$ ParameterList $$)$$

.. rubric:: Legality Rules

:dp:`hash_iCnZxHvMc2hn`
A :t:`enum type` is an :t:`abstract data type` that contains :t:`[enum variant]s`.

:dp:`hash_rt7r2pROyRz6`
A :t:`zero-variant enum type` has no :t:`[value]s`.

:dp:`hash_3PV0StZzPP83`
An :t:`enum variant` is a :t:`construct` that declares one of the possible variations of an :t:`enum`.

:dp:`hash_iTyE9jZHlt3G`
The :t:`name` of an :t:`enum variant` shall be unique within the related :s:`EnumDefinition`.

:dp:`hash_T8UorbZw575O`
A :t:`discriminant` is an opaque integer that identifies an :t:`enum variant`.

:dp:`hash_JYPaiRgQcZRl`
A :t:`discriminant initialiser` shall be specified via the :c:`discriminant` :t:`attribute`.

:dp:`hash_JBJ2maYTs8nC`
The :t:`type` of the expression :t:`expression` of a :t:`discriminant initialiser` shall be determined 
as follows:

#. :dp:`hash_MXlQzr0NdRBD` The :t:`type` of the :t:`primitive representation` specified by the :t:`attribute` :c:`repr`.

#. :dp:`hash_niBgxbQcws9B` Otherwise, the smallest :t:`integer type` that can represent the full range of discriminant :t:`[value]s`. If 
   the range of discriminant :t:`value` does not contain any :t`negative integer` values, then the :t:`type` of the 
   discriminant shall be the smallest :t:`unsigned integer type`. 


:dp:`hash_dmquzOLCFSgr`
The :t:`value` of a :t:`discriminant` of an :t:`enum variant` is determined as follows: 

#. :dp:`hash_4LRY6oawDeKd` If the :t:`enum variant` has an applied :t:`discriminant initialiser`, then the :t:`value` is the 
   value of its :t:`expression`.

#. :dp:`hash_WqygJ0cakbZ7` Otherwise, if the :t:`enum variant` is the first :t:`enum variant` in the :s:`EnumVariantList`, then the 
   :t:`value` is zero.

#. :dp:`hash_ukNGP8qclZZ5` Otherwise, the :t:`value` is one greater than the :t:`value` of the previous :t:`enum variant`.

:dp:`hash_xVCX6PwX8R2q`
It is a static error if two :t:`[enum variant]s` have the same discriminant.

:dp:`hash_hxt21vrHV1oH`
It is a static error if the :t:`value` of a :t:`discriminant` exceeds the maximum :t:`value` of the :t:`type` of the :t:`expression`
of a :t:`discriminant initialiser`. 


.. rubric:: Examples

.. code-block:: rust

    Foo := enum<T>(
        Bar,
        Baz(i32),
        Qux(i32, f32)
    )

.. code-block:: rust

    ErrorCode := enum(
        None,
        InvalidArgument,
        InvalidState,
        InvalidOperation,
        #[display_name("Invalid Data")]
        InvalidData
    )


.. code-block:: rust

    FloorId := struct(i8);

    EmployeeKind := enum(
        #[discriminant(7)]
        FactoryWorker(FloorId),
        #[discriminant(12)]
        Engineer,
        #[discriminant(83)]
        Hardware,
        #[discriminant(666)]
        Manager,
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

    identity := <T> => (t: T) -> T => t

    identity(3) == 3 == identity<i32>(3)

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
