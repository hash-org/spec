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


.. _hash_10KrB2F6pdlG:

Type Function Definitions
-------------------------

.. rubric:: Syntax

.. syntax::
    TypeFunctionDefinition ::=
        DefinitionParameterList ($$->$$ Type)? $$=>$$ TypeFunctionBody

    TypeFunctionBody ::=
        NonDeclarativeExpression

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

.. _hash_D5a1y4BYMQpc:

Module Definitions
------------------

.. rubric:: Syntax

.. syntax::
    ModuleDefinition ::=
        $$mod$$ DefinitionParameterList? $${$$ ModuleMemberList $$}$$
    
    ModuleMemberList ::=
        StatementList

.. _hash_gCrbjVEL55Qt:

Implementation Definitions
--------------------------

.. rubric:: Syntax

.. syntax::
    ImplDefinition ::=
        $$impl$$ DefinitionParameterList? $${$$ ImplMemberList $$}$$

        ImplMemberList ::=
            StatementList

.. _hash_jok00upP4s4V:

Definition Parameters
---------------------

.. rubric:: Syntax

.. syntax::

    DefinitionParameterList ::= 
        $$<$$ TypeParameterList? $$>$$
