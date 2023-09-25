.. default-domain:: spec

.. _hash_5weSTZ4zQXJ2:

Lexical Elements
================

.. _hash_9NuHRsGR7xNB:

Character Set
-------------

.. rubric:: Syntax


.. _hash_gh1tLCGuC7YY:

Lexical Elements, Separators, and Punctuation
---------------------------------------------

:dp:`hash_xU6U7WVAq3YE`
A :dt:`lexical element` is the most basic syntactic element in program
text.

.. rubric:: Syntax

.. syntax::
     LexicalElement ::= 
            Comment
          | Identifier
          | Keyword
          | Literal
          | Punctuation

     Punctuation ::=
            Delimiter
          | $$+$$
          | $$-$$
          | $$*$$
          | $$/$$
          | $$%$$
          | $$^$$
          | $$^^$$
          | $$&$$
          | $$&&$$
          | $$|$$
          | $$||$$
          | $$~$$
          | $$!$$
          | $$<$$
          | $$>$$
          | $$=$$
          | $$==$$
          | $$!=$$
          | $$<=$$
          | $$>=$$
          | $$=>$$
          | $$+=$$
          | $$-=$$
          | $$*=$$
          | $$/=$$
          | $$%=$$
          | $$^=$$
          | $$^^=$$
          | $$>>=$$
          | $$<<=$$
          | $$|=$$
          | $$||=$$
          | $$&=$$
          | $$&&=$$
          | $$~=$$
          | $$.$$
          | $$..$$
          | $$...$$
          | $$..<$$
          | $$;$$
          | $$,$$
          | $$:$$
          | $$::$$
          | $$?$$
          | $$@$$
          | $$#$$
          | $$$$$
          | $$->$$
          | $$=>$$


     Delimiter ::=
            $${$$
          | $$}$$
          | $$[$$
          | $$]$$
          | $$($$
          | $$)$$

.. _hash_hHXlfhm8tQQc:

Comments
--------

.. rubric:: Syntax

.. syntax::
     Comment ::=
            LineComment
          | BlockComment

     LineComment ::=
          $$//$$ ~[$$\n$$]*

     BlockComment ::=
            $$/*$$ (BlockComment | ~[$$*/$$])* $$*/$$
          | $$/**/$$


.. rubric:: Examples

.. code-block:: rust
     
.. _hash_tN3OCMQNYodO:

Identifiers
-----------

.. rubric:: Syntax

.. syntax::
     Identifier ::= 
          IdentifierStart IdentifierContinue*

     IdentifierList ::= 
          Identifier ( $$,$$ Identifier )* $$,$$?

     IdentifierStart ::= 
          [$$a..z$$ $$A..Z$$ $$_$$]

     IdentifierContinue ::= 
          IdentifierStart | $$0..9$$

.. rubric:: Examples

.. code-block:: rust

.. _hash_4C6G7IU6xxTU:

Keywords
--------

.. rubric:: Syntax

.. syntax::
     Keyword ::=
            $$for$$
          | $$while$$
          | $$loop$$
          | $$if$$
          | $$else$$
          | $$false$$
          | $$match$$
          | $$as$$
          | $$in$$
          | $$trait$$
          | $$enum$$
          | $$struct$$
          | $$continue$$
          | $$break$$
          | $$return$$
          | $$import$$
          | $$raw$$
          | $$unsafe$$
          | $$pub$$
          | $$priv$$
          | $$mut$$
          | $$mod$$
          | $$impl$$
          | $$type$$
          | $$true$$

.. _hash_MOI9vhKHO8yf:

Reserved Keywords
~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
     ReservedKeyword ::=
          $$macro$$
          | $$use$$
          | $$where$$
          | $$ref$$




.. _hash_baTsL9k07MiG:

Literals
-----------

.. rubric:: Syntax

.. syntax::
     Literal ::=
            BooleanLiteral
          | CharacterLiteral
          | StringLiteral
          | NumericLiteral

.. rubric:: Examples

.. code-block:: rust

.. _hash_kmpG33MIe6KI:

Boolean Literals
----------------

.. rubric:: Syntax

.. syntax::
     BooleanLiteral ::=
            $$true$$
          | $$false$$


.. _hash_sokogiPV9Dkk:

Character Literals
------------------

.. rubric:: Syntax

.. syntax::
     CharacterLiteral ::=
          $$'$$ CharacterContent $$'$$

     CharacterContent ::=
            AsciiEscape
          | CharacterContentItem
          | UnicodeEscape

     AsciiEscape ::=
            $$\0$$
          | $$\n$$
          | $$\r$$
          | $$\t$$
          | $$\a$$
          | $$\b$$
          | $$\f$$
          | $$\v$$
          | $$\\$$
          | $$\'$$
          | $$\"$$
          | $$\x$$ OctalDigit HexadecimalDigit


:dp:`hash_P9dxaBbi8Ttw`
A :ds:`CharacterContentItem` is any :t:`Unicode` codepoint except for the :t:`Unicode`
characters 0x09 (horizontal tab ``\t``), 0x0A (line feed ``\n``), 0x0D (carriage return ``\r``), 0x27 (single quote ``'``),
and 0x5C (backslash ``\``).

:dp:`hash_htCfBsNgx3Nu`
A :ds:`UnicodeEscape` starts with a ``\u{`` literal, followed by 1 to 6 instances of a 
:s:`HexadecimalDigit`, inclusive, followed by a ``}`` character. The literal can represent 
any :t:`Unicode` codepoint between U+000000 and U+10FFFF, inclusive, except :t:`Unicode`
surrogate codepoints, which exist between the range of U+D800 and U+DFFF, inclusive.


.. rubric:: Examples

.. code-block:: rust

.. _hash_fqlLlSMNhvHU:

String Literals
---------------

.. rubric:: Syntax

.. syntax::
     StringLiteral ::=
          $$"$$ StringContent* $$"$$

     StringContent ::=
            AsciiEscape
          | StringContentItem
          | UnicodeEscape
     

:dp:`hash_LcLSTmIfIedx`
A :ds:`StringContentItem` is any :t:`Unicode` codepoint except for the :t:`Unicode`
0x0D (carriage return ``\r``) characters 0x22 (double quote ``"``) and 0x5C (backslash ``\``).


.. rubric:: Examples

.. code-block:: rust


.. _hash_P3baDqFD2Abx:

Numerical Literals
------------------

.. rubric:: Syntax

.. syntax::
     NumericLiteral ::=
            IntegerLiteral
          | FloatLiteral



.. _hash_zxQSvDbV7k11:

Integer Literals
~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
     IntegerLiteral ::= $$-$$? IntegerContent IntegerSuffix?

     IntegerContent ::=
            BinaryLiteral
          | OctalLiteral
          | DecimalLiteral
          | HexadecimalLiteral

     BinaryLiteral ::= 
          $$0b$$ BinaryDigitOrUnderscore* BinaryDigit BinaryDigitOrUnderscore*

     BinaryDigitOrUnderscore ::= 
            BinaryDigit 
          | $$_$$

     BinaryDigit ::= [$$0$$-$$1$$]

     OctalLiteral ::= 
          $$0o$$ OctalDigitOrUnderscore* OctalDigit OctalDigitOrUnderscore*

     OctalDigitOrUnderscore ::= 
            OctalDigit
          | $$_$$

     OctalDigit ::= [$$0$$-$$7$$]

     DecimalLiteral ::= 
          DecimalDigitOrUnderscore* DecimalDigit DecimalDigitOrUnderscore*
     
     DecimalDigitOrUnderscore ::= 
            DecimalDigit
          | $$_$$

     DecimalDigit ::= [$$0$$-$$9$$]

     HexadecimalLiteral ::= 
          $$0x$$ HexadecimalDigitOrUnderscore* HexadecimalDigit HexadecimalDigitOrUnderscore*

     HexadecimalDigitOrUnderscore ::= 
            HexadecimalDigit
          | $$_$$

     HexadecimalDigit ::= [$$0$$-$$9$$ $$a$$-$$f$$ $$A$$-$$F$$]

     IntegerSuffix ::=
            SignedIntegerSuffix
          | UnsignedIntegerSuffix

     SignedIntegerSuffix ::= 
            $$i8$$
          | $$i16$$
          | $$i32$$
          | $$i64$$
          | $$i128$$
          | $$isize$$
          | $$ibig$$

     UnsignedIntegerSuffix ::= 
            $$u8$$
          | $$u16$$
          | $$u32$$
          | $$u64$$
          | $$u128$$
          | $$usize$$
          | $$ubig$$

.. rubric:: Examples

.. code-block:: rust


.. _hash_rYLFAvhv5qwl:

Float Literals
~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::
     FloatLiteral ::= $$-$$? FloatComponent

     FloatComponent ::=
          DecimalLiteral $$.$$
          | DecimalLiteral FloatExponent
          | DecimalLiteral $$.$$ DecimalLiteral FloatExponent?
          | DecimalLiteral ($$.$$ DecimalLiteral)? FloatExponent? FloatSuffix?

     FloatExponent ::=
          ExponentAnnotation ExponentSign? ExponentMagnitude

     ExponentAnnotation ::= 
            $$e$$ 
          | $$E$$

     ExponentSign ::=
            $$+$$ 
          | $$-$$

     ExponentMagnitude ::= 
          DecimalDigitOrUnderscore* DecimalDigit DecimalDigitOrUnderscore*

     FloatSuffix ::=
            $$f32$$
          | $$f64$$


.. rubric:: Examples

.. code-block:: rust
