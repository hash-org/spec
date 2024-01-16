.. default-domain:: spec

.. _hash_5weSTZ4zQXJ2:

Lexical Elements
================

.. spec:informational-section:: 

:dp:`hash_OVwRu8sEw8QB`
The text of a Hash program consists of :t:`[module]s` organised into 
:t:`[source file]s`. The text of a :t:`source file` is a sequence of separate :t:`[lexical element]s`,
each composed of characters, whose rules are defined in this section.

.. _hash_9NuHRsGR7xNB:

Character Set
-------------

:dp:`hash_M7TYziurnCCB` 
The program text of a Hash program is a sequence of :t:`Unicode` characters.

.. rubric:: Syntax

:dp:`hash_aaa6EG5BglUi`
A character is defined by this document for each cell in the coding space described
by :t:`Unicode`, regardless of whether or not :t:`Unicode` allocates a character to that cell.

:dp:`hash_jR1ikqVXacF3`
A :dt:`whitespace character` is one of the following characters:

* :dp:`hash_7MrlRWGmm5db` ``0x09`` (horizontal tab ``\t``)
* :dp:`hash_pVGbJjIV3t0R` ``0x0A`` (line feed ``\n``)
* :dp:`hash_3jbfkCSkqG1r` ``0x0B`` (vertical tab ``\v``)
* :dp:`hash_pq3tCcjyaa6B` ``0x0C`` (form feed ``\f``)
* :dp:`hash_fJcCsJp2TUBU` ``0x0D`` (carriage return ``\r``)
* :dp:`hash_XrXkD1I58gET` ``0x20`` (space)
* :dp:`hash_1AmxDqJPPgxs` ``0x200E`` (left-to-right mark)
* :dp:`hash_1T602sxzPHsJ` ``0x200F`` (right-to-left mark)
* :dp:`hash_PZFaK9pXE9d1` ``0x2028`` (line separator)
* :dp:`hash_S6tdnEO6W1NK` ``0x2029`` (paragraph separator)

:dp:`hash_8MnccTGZWEGg`
A :dt:`whitespace string` is a sequence of one or more :t:`[whitespace character]s`.

:dp:`hash_n203jgJb6wh1`
a :ds:`AsciiCharacter` is any :t:`Unicode` character in the range ``0x00`` to ``0x7F``, inclusive.

.. rubric:: Legality Rules

:dp:`hash_13EFD5NrYi2o`
The coded representation of a character is tool defined.

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


.. rubric:: Legality Rules

:dp:`hash_Fm1Hl48p1mhx`
The text of a :t:`source file` is a sequence of separate :t:`[lexical element]s`.
The meaning of a program depends only on the particular sequence of :t:`[lexical element]s`.

:dp:`hash_pl00dI8sig9h`
A :t:`lexical element` is the most basic syntactic element in program text.

:dp:`hash_RHnUyXidyQ71`
A :t:`line` is a sequence of zero or more characters followed by an end of line.

:dp:`hash_mGcaKhwItOwL`
The representation of an end of line is tool defined (i.e. specific to an operating system).

:dp:`hash_VMvtGldSZvya`
A :t:`separator` is a character or string that separates adjacent :t:`[lexical element]s`.
A :t:`whitespace string` is a :t:`separator`.

:dp:`hash_9PGgxi7vhffl`
A :dt:`simple punctuator` is one of the following characters:

.. syntax::
     $$+$$
     $$-$$
     $$*$$
     $$/$$
     $$%$$
     $$^$$
     $$&$$
     $$|$$
     $$~$$
     $$<$$
     $$>$$
     $$=$$
     $$!$$
     $$;$$
     $$,$$
     $$:$$
     $$?$$
     $$@$$
     $$#$$
     $$$$$
     $$.$$
     $${$$
     $$}$$
     $$[$$
     $$]$$
     $$($$
     $$)$$
     $$_$$

:dp:`hash_rHCcXLuL54bN`
A :dt:`compound punctuator` is one of the following two or more adjacent special 
characters:

.. syntax::
     $$&&$$
     $$||$$
     $$^^$$
     $$==$$
     $$!=$$
     $$<=$$
     $$>=$$
     $$=>$$
     $$+=$$
     $$-=$$
     $$*=$$
     $$/=$$
     $$%=$$
     $$^=$$
     $$^^=$$
     $$>>=$$
     $$<<=$$
     $$|=$$
     $$||=$$
     $$&=$$
     $$&&=$$
     $$~=$$
     $$..$$
     $$...$$
     $$..<$$
     $$::$$
     $$->$$
     $$=>$$

:dp:`hash_wpqgfSerKmaj`
The following :t:`[compound punctuator]s` are :dt:`[flexible compound punctuator]s`:

.. syntax::
     $$&&$$
     $$||$$
     $$<<$$
     $$>>$$


:dp:`hash_1m04TahObgmQ`
A :t:`flexible compound punctuator` may be treated as a :t:`compound punctuator` or 
two adjacent :t:`[simple punctuator]s`.


:dp:`hash_udz6wbA9UAfj`
Each of the special characters listed for single character :t:`punctuator` is a :t:`simple punctuator`
except if the character is being used as part of a :t:`compound punctuator`, or a character 
of a :t:`character literal`, a :t:`comment`, a :t:`numeric literal`, or a :t:`string literal`.

:dp:`hash_T8ZuVGhx81gv`
The following names are used to refer to the :t:`[punctuator]s`:

.. list-table::

     * - :dp:`hash_IWXPcdezxY3I`
       - **punctuator**
       - **name**
     * - :dp:`hash_7Dv2rgfFqBxa`
       - ``+``
       - Plus
     * - :dp:`hash_7Dv2rgfFqBxa`
       - ``-``
       - Minus
     * - :dp:`hash_bPi3Mco8Fu4g`
       - ``*``
       - Star
     * - :dp:`hash_k8Q8pVkYTRx6`
       - ``/``
       - Slash
     * - :dp:`hash_azc6X9ECOkVf`
       - ``%``
       - Modulo
     * - :dp:`hash_WWhPN3ENMlrs`
       - ``^``
       - Caret
     * - :dp:`hash_Q1jBl2r5BpIa`
       - ``^^``
       - Exponent
     * - :dp:`hash_5vUEwwywcIPj`
       - ``!``
       - Bang
     * - :dp:`hash_FpwEzDZE7mTs`
       - ``&``
       - And
     * - :dp:`hash_0tq1m5hyrOhB`
       - ``|`` 
       - Or
     * - :dp:`hash_jYhUlwIJZBXz`
       - ``&&`` 
       - Logical And, Lazy and, And And
     * - :dp:`hash_k1KKxYDhUuCt`
       - ``||`` 
       - Logical Or, Lazy Or, Or Or 
     * - :dp:`hash_sntaHYN4p0X4`
       - ``<`` 
       - Less than
     * - :dp:`hash_idCeWiUUtgne`
       - ``<<`` 
       - Left Shift
     * - :dp:`hash_CpITLLBWC1Ky`
       - ``>`` 
       - Greater than
     * - :dp:`hash_Q9GV6fz4GEeB`
       - ``>>`` 
       - Right shift
     * - :dp:`hash_lWiFVas993t9`
       - ``=`` 
       - Equals, Assign
     * - :dp:`hash_ZjgE4yYy7Ycr`
       - ``==`` 
       - Logical Equals, Double Equals
     * - :dp:`hash_bzWuYUsWIEac`
       - ``!=`` 
       - Logical Not Equals, Not Equals
     * - :dp:`hash_lAZpM7pLB43M`
       - ``<=`` 
       - Less than or Equals
     * - :dp:`hash_apt1b6BzRHl7`
       - ``>=`` 
       - Greater than or Equals
     * - :dp:`hash_QNF6xTsJtWJt`
       - ``<<=`` 
       - Left Shift Assign
     * - :dp:`hash_TwHkny9xSf7r`
       - ``>>=`` 
       - Right Shift Assign
     * - :dp:`hash_Ef9FsvMso81S`
       - ``+=`` 
       - Plus Equals
     * - :dp:`hash_sxMCHCnHG98T`
       - ``-=`` 
       - Minus Equals
     * - :dp:`hash_cNyKypFk8yjm`
       - ``*=`` 
       - Plus Equals
     * - :dp:`hash_5XFtWZQUh6c8`
       - ``/=`` 
       - Minus Equals 
     * - :dp:`hash_uIF2t4d4YDFA`
       - ``%=`` 
       - Percent Equals
     * - :dp:`hash_fJbywhSDVkDZ`
       - ``^=`` 
       - Caret Equals   
     * - :dp:`hash_nLHQvIxzyDaV`
       - ``^^=`` 
       - Exponent Equals
     * - :dp:`hash_nLHQvIxzyDaV`
       - ``@`` 
       - At 
     * - :dp:`hash_Dhj68QmgzP48`
       - ``.`` 
       - Dot
     * - :dp:`hash_xGR3dNWsY7z4`
       - ``..`` 
       - Range, Dot Dot       
     * - :dp:`hash_9zWV0CUCKWNS`
       - ``..<`` 
       - Exclusive Range
     * - :dp:`hash_ArrAzLBEDOZE`
       - ``...`` 
       - Ellipsis, Spread
     * - :dp:`hash_JmIBk1KcOmm8`
       - ``,`` 
       - Comma        
     * - :dp:`hash_NvIqOxVw0qJu`
       - ``;`` 
       - Semi         
     * - :dp:`hash_fqESnQ6AA3T0`
       - ``:`` 
       - Colon         
     * - :dp:`hash_0ZuIcK8rhTtH`
       - ``::`` 
       - Access
     * - :dp:`hash_h34qajcEPTG5`
       - ``->`` 
       - Thin Arrow          
     * - :dp:`hash_ipkbZ4KZbRUX`
       - ``=>`` 
       - Fat Arrow          
     * - :dp:`hash_Q1juqn4LfrDS`
       - ``#`` 
       - Pound
     * - :dp:`hash_hf0jtKV8ff7H`
       - ``$`` 
       - Dollar sign 
     * - :dp:`hash_D2apfpXygGZC`
       - ``?`` 
       - Question Mark 
     * - :dp:`hash_Xt220khBImTt`
       - ``{`` 
       - Left brace
     * - :dp:`hash_NES80bB3M3CJ`
       - ``}`` 
       - Right brace 
     * - :dp:`hash_ThAbkElzSH31`
       - ``[`` 
       - Left bracket 
     * - :dp:`hash_H7xnBgNLgKTh`
       - ``]`` 
       - Right bracket 
     * - :dp:`hash_o6DuzeHGGs8y`
       - ``(`` 
       - Left parenthesis 
     * - :dp:`hash_vVW7Yeyx088s`
       - ``)`` 
       - Right parenthesis 

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


.. rubric:: Legality Rules

:dp:`hash_0fukPZ4sMzVl`
A :t:`comment` is a :t:`lexical element` that acts as annotation in the program text.

:dp:`hash_21WUqgVXDUxU`
A :t:`block comment` is a comment that spans one or more :t:`[line]s`.

:dp:`hash_8JgwXJoXV2cQ`
A :t:`line comment` is a comment that spans over one :t:`[line]`.

:dp:`hash_Q6VfEZp90Nnu`
Character 0x0D (carriage return) shall not appear in a comment.

.. rubric:: Examples

.. code-block:: rust

     // This is a comment
     /* This is a block comment */
     /* /* This is a nested block comment */ */
     
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


.. rubric:: Legality Rules

:dp:`hash_tT15AMl3euce`
An :t:`identifier` is a :t:`lexical element` that refers to a name.

:dp:`hash_MykNsjb0YVjr`
Two :t:`[identifier]s` are equivalent if they consist of the 
same sequence of characters.

.. rubric:: Examples

.. code-block:: rust
     
     foo
     bar2
     _identifier

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


:dp:`hash_j1i5wxIfnJ8y`
Reserved keywords are keywords that are reserved for future use, but are not
currently used by the language. The are currently allowed to be used as identifiers,
however they will likely be used in the future, and so it is recommended to avoid
using them as identifiers.


.. _hash_baTsL9k07MiG:

Literals
-----------

.. rubric:: Syntax

.. syntax::
     Literal ::=
          BooleanLiteral
          | ByteLiteral 
          | CharacterLiteral
          | StringLiteral
          | NumericLiteral


.. rubric:: Legality Rules

:dp:`hash_1QmjexiR8lZl`
A :t:`literal` is a fixed value in program text.


.. _hash_kmpG33MIe6KI:

Boolean Literals
----------------

.. rubric:: Syntax

.. syntax::
     BooleanLiteral ::=
          $$true$$
          | $$false$$


.. rubric:: Legality Rules

:dp:`hash_PtjBOmtBX2qc`
A :t:`boolean literal` is a :t:`literal` that denotes the truth values of logic and 
Boolean algebra.

:dp:`hash_VYYi5fzWROwc` the :t:`type` of a :t:`boolean literal` is :c:`bool`.

.. rubric:: Examples

.. code-block:: rust

     false


.. _hash_9sLPHCB13dUF:

Byte Literals
-------------

.. rubric:: Syntax

.. syntax::
     ByteLiteral ::=
          $$b'$$ ByteContent $$'$$

     ByteContent ::=
          ByteCharacter
          | ByteEscape

     ByteEscape ::=
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
         
:dp:`hash_LJNwHnmPEuvw`
A :ds:`ByteCharacter` is any character in the :s:`AsciiCharacter` except
characters 0x09 (horizontal tab ``\t``), 0x0A (line feed ``\n``), 0x0D (carriage return ``\r``), 0x27 (single quote ``'``),
and 0x5C (backslash ``\``).

.. rubric:: Legality Rules

:dp:`hash_NuXpLr24OiMN`
A :t:`byte literal` is a :t:`literal` that denotes a fixed byte :t:`value`.

:dp:`hash_fN7BIogf6nOG`
The :t:`type` of a :t:`byte literal` is :c:`u8`.

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


.. rubric:: Legality Rules

:dp:`hash_F2LN9Q8XtiMV`
A :t:`character literal` is a :t:`literal` that denoted a fixed :t:`Unicode` character.

:dp:`hash_9PtP1D0uq1QR`
The :t:`type` of a :t:`character literal` is :c:`char`.


.. rubric:: Examples

.. code-block:: rust

     'a'
     '\t'
     '\x1b'
     '\u{1F30}'

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

.. rubric:: Legality Rules

:dp:`hash_IjLAg7jcSEVz`
A :t:`string literal` is where the characters are :t:`Unicode` characters, enclosed in double quotes ``"``.

:dp:`hash_MxYj2ik6cYLU`
The :t:`type` of a :t:`string literal` is :c:`str`.

.. rubric:: Examples

.. code-block:: rust

     ""
     "Москва"
     "cat"
     "\tcol\nrow"
     "bell\x07"
     "\u{B80a}"


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
     IntegerLiteral ::= 
          $$-$$? IntegerContent IntegerSuffix?

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

     BinaryDigit ::= 
          [$$0$$-$$1$$]

     OctalLiteral ::= 
          $$0o$$ OctalDigitOrUnderscore* OctalDigit OctalDigitOrUnderscore*

     OctalDigitOrUnderscore ::= 
          OctalDigit
          | $$_$$

     OctalDigit ::= 
          [$$0$$-$$7$$]

     DecimalLiteral ::= 
          DecimalDigitOrUnderscore* DecimalDigit DecimalDigitOrUnderscore*
     
     DecimalDigitOrUnderscore ::= 
          DecimalDigit
          | $$_$$

     DecimalDigit ::= 
          [$$0$$-$$9$$]

     HexadecimalLiteral ::= 
          $$0x$$ HexadecimalDigitOrUnderscore* HexadecimalDigit HexadecimalDigitOrUnderscore*

     HexadecimalDigitOrUnderscore ::= 
          HexadecimalDigit
          | $$_$$

     HexadecimalDigit ::= 
          [$$0$$-$$9$$ $$a$$-$$f$$ $$A$$-$$F$$]

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

.. rubric:: Legality Rules

:dp:`hash_QM30QEFkPUXz`
An :t:`integer literal` is a :t:`numeric literal` that denotes a whole number.

:dp:`hash_huD6Q29lCWIz`
A :t:`binary literal` is an :t:`integer literal` in base 2.

:dp:`hash_dhdlQd256XkR`
A :t:`octal literal` is an :t:`integer literal` in base 8.

:dp:`hash_ukxSlWZSi6fJ`
A :t:`decimal literal` is an :t:`integer literal` in base 10.

:dp:`hash_qJtRoW3oLttb`
A :t:`hexadecimal literal` is an :t:`integer literal` in base 16.

:dp:`hash_t6qM56PiTpb0`
An :t:`integer suffix` is a component of an :t:`integer literal` that specifies an explicit
:t:`integer type`.

:dp:`hash_or5pdYwGdMkR`
A :t:`suffixed integer` is an :t:`integer literal` with a :t:`integer suffix`.

:dp:`hash_wPiER4pmfgyy`
An :t:`unsuffixed integer` is an :t:`integer literal` without a :t:`integer suffix`.

:dp:`hash_519imsaIyrxU`
The :t:`type` of a :t:`unsuffixed integer` is determined by the :t:`integer suffix` as follows:

* :dp:`hash_I7jOtlVPHxB9` Suffix ``i8`` specifies the type :c:`i8`.

* :dp:`hash_wvzzKEae6YrS` Suffix ``i16`` specifies the type :c:`i16`.

* :dp:`hash_6PWCKYJKc48t` Suffix ``i32`` specifies the type :c:`i32`.
  
* :dp:`hash_D1q23Dib0E0R` Suffix ``i64`` specifies the type :c:`i64`.

* :dp:`hash_qbNp56pMLDNS` Suffix ``i128`` specifies the type :c:`i128`.

* :dp:`hash_Nn45WpnbtlzJ` Suffix ``isize`` specifies the type :c:`isize`.

* :dp:`hash_BB52ORnHly4H` Suffix ``ibig`` specifies the type :c:`ibig`.

* :dp:`hash_gdoWfYrGSD7B` Suffix ``u8`` specifies the type :c:`u8`.

* :dp:`hash_BKhPVLVKK1jV` Suffix ``u16`` specifies the type :c:`u16`.

* :dp:`hash_ENx4XzXxKg0e` Suffix ``u32`` specifies the type :c:`u32`.
  
* :dp:`hash_mOhAN1Qw9SZL` Suffix ``u64`` specifies the type :c:`u64`.

* :dp:`hash_YwAaQxnVRR0P` Suffix ``u128`` specifies the type :c:`u128`.

* :dp:`hash_ahSNOX4HxFeT` Suffix ``usize`` specifies the type :c:`usize`.

* :dp:`hash_xdFvV6RK5K5D` Suffix ``ubig`` specifies the type :c:`ubig`.


:dp:`hash_sG6Yoce3mvLB`
The :t:`type` of a :t:`unsuffixed integer` is determined by :t:`type inference` as follows:

* :dp:`hash_zW4nTkSPVyNY` If a :t:`integer type` can be inferred from the context, then the :t:`unsuffixed integer` has that :t:`type`.

* :dp:`hash_JLlui8JL7yVe` If the program content under-constrains the :t:`type`, then the 
  :t:`inferred type` is :c:`i32`.

* :dp:`hash_IZEFHOlPC4sg` If the program content over-constrains the :t:`type`, then it is considered to be a static error.


.. rubric:: Examples

.. code-block:: rust

     0b0010_1110_u8
     1___2_3
     0xDeAdBeEf_u32
     0o77_52i128

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


.. rubric:: Legality Rules

:dp:`hash_K7NYI9MQp5lp`
A :t:`float literal` is a :t:`numeric literal` that denotes a fractional number.

:dp:`hash_pWICPswNCwor`
A :t:`float suffix` is a component of a :t:`float literal` that specifies an explicit
:t:`floating point type`.

:dp:`hash_RkE1alBodBbi`
A :t:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

:dp:`hash_2hseYe7AJcJS`
An :t:`unsuffixed float` is a :t:`float literal` without a :t:`float suffix`. 

:dp:`hash_gNzO26FgtonJ`
The :t:`type` of a :t:`suffixed float` is determined by the :t:`float suffix` as follows:

* :dp:`hash_yjxW2xkVVchC` Suffix ``f32`` specifies the type :c:`f32`.

* :dp:`hash_gj4Nz0l2rJot` Suffix ``f64`` specifies the type :c:`f64`.

:dp:`hash_ijtZT5oDsZaJ`
The :t:`type` of a :t:`unsuffixed float` is determined by :t:`type inference` as follows:

* :dp:`hash_BMbyx6ETC9PA` If a :t:`floating-point type` can be inferred from the context, then the :t:`unsuffixed float` has that :t:`type`.

* :dp:`hash_lr9sUoFtXl0I` If the program content under-constrains the :t:`type`, then the 
  :t:`inferred type` is :c:`f64`.

* :dp:`hash_wJwClVFeZgu4` If the program content over-constrains the :t:`type`, then it is considered to be a static error.

.. rubric:: Examples

.. code-block:: rust

     45.
     8E+1_820
     3.14e5
     8_031.4_e-12f64
