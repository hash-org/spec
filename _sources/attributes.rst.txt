.. default-domain:: spec

.. _hash_bP0ZyLTwgyTk:

Attributes
==========

.. _hash_mgfqjgZk9ZRe:

Built-in Attributes
-------------------

.. rubric:: Syntax


.. .. @@Incomplete

.. syntax::

    BuiltinAttribute ::=
       DiscriminantAttribute
       | ReprAttribute

.. rubric:: Legality Rules

:dp:`hash_FyRYtOIbe83M`
A :t:`built-in attribute` is a language-defined :t:`attribute`.


.. _hash_OZBpOU4mgOTu:

Code Generation Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _hash_C6o933at2sNT:

Attribute ``discriminant``
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

    DiscriminantAttribute ::=
         $$discriminant$$ $$($$ DecimalLiteral $$)$$

.. rubric:: Legality Rules

:dp:`hash_RXzm9Ni9bEkL`
:t:`Attribute` :dc:`discriminant` shall indicate the discriminant :t:`value` of the
related :t:`enum variant`.

.. rubric:: Examples

.. code-block:: rust

    Foo := enum(
        #[discriminant(1)]
        A,
        #[discriminant(100)]
        B,
        #[discriminant(1000)]
        C,
    )


.. _hash_IxnXO0iephPj:

Attribute ``repr``
^^^^^^^^^^^^^^^^^^


.. rubric:: Syntax

.. syntax::

   ReprAttribute ::=
       $$repr$$ $$("$$ Representation $$")$$

   Representation ::=
       RepresentationKind

   RepresentationKind ::=
       PrimitiveRepresentation
     | $$C$$

   PrimitiveRepresentation ::=
       $$i8$$
     | $$i16$$
     | $$i32$$
     | $$i64$$
     | $$i128$$
     | $$isize$$
     | $$u8$$
     | $$u16$$
     | $$u32$$
     | $$u64$$
     | $$u128$$
     | $$usize$$

.. rubric:: Legality Rules

:dp:`hash_w23EvZNG6DTo`
:t:`Attribute` :dc:`repr` shall indicate the :t:`type representation` of the
related :t:`type`.

:dp:`hash_C2rMJfad1qNp`
:t:`Attribute` :c:`repr` value ``"c"`` shall imply that the representation will 
follow the C ABI.

.. .. @@TODO: Add a link to the C ABI.

:dp:`hash_LjPdiKIknlOC`
:t:`Attribute` :c:`repr` shall apply to :t:`[abstract data type]s`.


.. rubric:: Examples

.. code-block:: rust

    #[repr("i32")]
    Foo := enum(
        A,
        B,
        C,
    )

