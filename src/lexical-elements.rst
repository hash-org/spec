.. default-domain:: spec

.. _hash_5weSTZ4zQXJ2:

Lexical Elements
================
.. informational-section:::dp:`hash_PcGto2uHIz56`The text of a Hash program consists of tokens... _hash_yZUqYtRCFonP:Character Set-------------:dp:`hash_PIDKEm8GiLNL`An :ds:`AsciiCharacter` is any :t:`Unicode` character in the range 0x00 - 0x7F, both inclusive... rubric:: Syntax.. syntax::   LexicalElement ::=     | Keyword     | Delimiter  Keyword ::=       $$while$$  Delimiter ::=       $${$$     | $$}$$     | $$[$$     | $$]$$     | $$($$     | $$)$$:dp:`hash_AiAb8hBMmeAQ`Additionally, tokens can be made of identifiers which are composed of :s:`AsciiCharacter` characters.:dp:`hash_123`Characters are generally considered to be in :s:`ascii <AsciiCharacter>`. Programscan have many :s:`[AsciiCharacter]s`.