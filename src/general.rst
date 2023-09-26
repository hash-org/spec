.. default-domain:: spec

.. informational-page::

.. _hash_ftMIIovhjfOS:

General
=======

:dp:`hash_kOrmv80ZDLPK`
The style of this document is influenced by the `Ferrocene Language Specification <https://spec.ferrocene.dev/>`_.

:dp:`hash_hAgF6bkI8YTx`
Parts of these documents have been copied, in whole or in part, in particular but not limited 
to:

* :dp:`hash_3pRcncKTLSu1` The outline and structure of the documents;

* :dp:`hash_O9Y7oHhUPV55` The title, outline, organisation, and numbering of 
  chapters;

* :dp:`hash_dtKHLkVjDnS9` The structure, formality, wording, and numbering of 
  paragraphs;

* :dp:`hash_edekOFCpmN5O` The definitions and uses of terms;

* :dp:`hash_4yR6m9NpRAXA` The categories of syntactic and semantic rules.

.. _hash_kFWfRKHn1ppa:

Scope
-----

:dp:`hash_fFG297GpiWNe`
This document specifies the form and meaning of program written in the programming language 
Hash, as implemented by the `hashc <https://github.com/hash-org/hashc>`_ compiler. It documents 
the current understanding for the purposes of implementation and standardisation.

:dp:`hash_YMGXanPU6neO`
This document is made available public as it is useful for understanding the language and
its implementation. It is not intended to be a tutorial or a guide for learning the language.
It is intended that this document be use as a discussion ground for language features and
evolution. It is intended as a document enabling conformance between tools and compilers 
which interact with the language.

:dp:`hash_AVo5zrtaJH2m`
Contribution and review is managed by the Hash Organisation.


.. _hash_pZOw7qE8wyqU:

Extent
~~~~~~

:dp:`hash_vZIQ9UqeIxHb`
This document specifies:

* :dp:`hash_jALKpUSTEC09` The form of a program written in Hash;

* :dp:`hash_WvNlHwTmRLK5` The effect of translating and executing such a program;

* :dp:`hash_8PRRFSpJSwDg` The language-defined libraries that a confirming tool is required to supply;

* :dp:`hash_7CxNhI70sYnm` The violations that a conforming tool is required to detect, and the effect of attempting to translate or execute a program containing such violations;

* :dp:`hash_zDIIyurAgtGp` The violations that a confirming tool is not required to detect.

:dp:`hash_EZEyTa8Y6XHL`
This document does not specify:

* :dp:`hash_8A5LYKtsqM3M` The means by which a Hash program is transformed into object code executable by a processor;

* :dp:`hash_M2zI9WRGz2HO` The means by which translation or execution of Hash programs is invoked and the executing unite are controlled;

* :dp:`hash_g9WvLl709WS0` The size of speed of the object code, or the relative execution speed of different language constructs;

* :dp:`hash_89D0qJO1CVXA` The form or content of any listings produced by a tool; in particular, the form or contents of error or warning messages;

* :dp:`hash_xYjTodcI70ht` The size of a program or program unit that will exceed the capacity of a conforming tool.
  
.. _hash_fdveazHsmDky:

Structure
~~~~~~~~~

:dp:`hash_OOfvbaHpeChJ`
This document contains 16 chapters, 1 appendix, and an index.

:dp:`hash_WAuHwXdztLfz`
The specification of the Hash language is separated into:

* :dp:`hash_30jmfudqD4Pp` Chapters 1 through 16,

* :dp:`hash_SHP5S0WSyrde` 
  :doc:`glossary`


:dp:`hash_B3FnZ5OMUIHg`
Each chapter is divided into subchapters that have a common structure. Each chapter and subchapter is then 
organised to include the following segments as is relevant to the topic:

.. rubric:: Syntax

:dp:`hash_JlkX0E6EvxN5`
The syntax representation of a :t:`construct`.

.. rubric:: Legality Rules

:dp:`hash_I4FHGeftnAWY`
Compile-time rules and facts for each :t:`construct`, A :t:`construct` is legal if it obeys 
all of the Legality Rules.

:dp:`hash_6TxU2HtRfHK0`
Legality rules are verified at various stages of the compilation process. The specification 
may not explicitly state when each legality rule is verified. Conforming tools must only 
respect the order of verification when it is explicitly stated.

.. rubric:: Dynamic Semantics

:dp:`hash_1NnN0xJjxAv6`
Run-time effects of each :t:`construct`.

.. rubric:: Implementation Requirements

:dp:`hash_GJQFXarjRyry`
Additional requirements for conforming tools.

.. rubric:: Examples

:dp:`hash_zPgLuwdAFIqw`
Examples illustrating the possible forms of a :t:`construct`. This material is informative.


.. _hash_G7J24ovihGlJ:

Conformity
~~~~~~~~~~

.. rubric:: Implementation Requirements

:dp:`hash_4jzGJBH3cc5e`
A conforming tool shall:

* :dp:`hash_iG6UwvtriZCn` Translate and correctly execute legal programs written in Hash, provided that they are not so large as  to exceed 
  the capacity of the tool,

* :dp:`hash_YaibhFoubm4S` Identify all programs or program units that are so large as to exceed the capacity of 
  the tool (or raise an appropriate exception at runtime).

* :dp:`hash_pnXZkbD4YxJW` Identify all programs or program units that contain errors whose detection is required by this document.

* :dp:`hash_QZ75kUjDHKBY` Supply all language-defined library units required by this document.

* :dp:`hash_uTUrIv74m69t` Contain no variations except those explicitly permitted by this document, or those that 
  are impossible or impractical to avoid given the tool's execution environment.

* :dp:`hash_pMlzKMDJZvor` Specify all such variations in the manner prescribed by this document.

:dp:`hash_4NNb783Djd1Q`
The external effect of the execution of a Hash program is defined in terms of its interactions with its 
external environment. The following are defined as external interactions:

* :dp:`hash_0umRn70SnYc0`  Any call on a foreign :t:`function`, including any :t:`[argument operand]s` passed to it;

* :dp:`hash_0umRn70SnYc1` Any result returned or :t:`panic` propagated from a :t:`main function` or an :t:`exported function`
  to an external caller;

* :dp:`hash_0umRn70SnYc2` The imported and exported values at the time of any other interaction with the external environment.


:dp:`hash_Jw3sp97zzAfZ` 
A tool that conforms to this document shall support each capability required by the language as specified.

:dp:`hash_4bIICknVoY7p`
A tool that conforms to this document may provide additional :t:`[attribute]s` as long as their names are 
not the same as the names of :t:`[built-in attribute]s`.

.. _hash_hyCfh5wZ1PHo:

Method of Description and Syntax Notation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:dp:`hash_pAu6KRs2BY9o`
The form of a Hash program is described by means of a context-free syntax together with 
context-dependent requirements expressed my narrative rules.

:dp:`hash_1UOvwSkOvH7j`
The meaning of a Hash program is described by means of narrative rules defining both the 
effects of each construct and the composition rules for constructs.

:dp:`hash_kdubLUv2Hnyc`
The context-free syntax of Hash is described a simple variant of the Backus-Naur form, In 
particular:

* :dp:`hash_4c6XMcjMYXwt` a ``monospaced`` font is used to denote Hash syntax.

* :dp:`hash_ls2Zgcx22TAu` Non-monospaced fonts are used to denote a syntactic category 
  e.g.

.. syntax::

   IntegerLiteral

* :dp:`hash_hDnucZL5NhLO` Worlds in **bold** font are used to indicate literal words, and 
  :t:`[keyword]s`:

.. syntax::

    $$struct$$
    $$if$$
    $$else$$

* :dp:`hash_rpDDwG7VxaOz` Characters in **bold** font are used to indicate literal characters and literal 
  punctuation, for example:

.. syntax::

    $$1$$
    $$N$$
    $$)$$
    $$->$$
    $$<<=$$

* :dp:`hash_p8zGVhCrd5kp` A character preceded by ``\`` (bold backslash) is used to denote 
  an :t:`[escaped character]`, for example:

.. syntax::
    
    $$\n$$
    $$\t$$
    $$\$$
    $$\"$$ 
    $$\\$$ 

* :dp:`hash_LVYZ1mV3jKOc` A prefix followed by ``?`` (question mark) is used to denoted 
  an optional prefix, for example:

.. syntax::

    IntegerSuffix?


* :dp:`hash_QczROvU6rLoJ` A prefix followed by ``*`` (asterisk) is used to denote a 
  repetition of zero or more occurrences of the prefix, for example:

.. syntax::
    
    TokenTree*


* :dp:`hash_nOoujdagI8PW` A prefix followed by ``+`` (plus sign) is used to denote a 
  repetition of one or more occurrences of the prefix, for example:

.. syntax::

    TokenTree+


* :dp:`hash_j8f7mbQJpCC6` ``[ ]`` (square brackets) indicate any character within, for example:

.. syntax::

     [$$a$$ $$_$$]

* :dp:`hash_DXSi9zLdxNdN` ``~[ ]`` (square brackets preceded by tilde) indicate any character 
  except the  characters within:

.. syntax::

    ~[$$\r$$ $$\n$$ $$:$$]

* :dp:`hash_GopBpoOdWXCS` ``[ - ]`` indicates any character within the specified range, inclusive:

.. syntax::

    [$$a..z$$ $$A..Z$$]

* :dp:`hash_pIO5SCIysLtI` A ``|`` (vertical bar) separates alternative items, for example:

.. syntax::

    Identifier | DecimalLiteral


* :dp:`hash_vFR9l9IvWRcH` ``( )`` (parentheses) are used to group items, for example:

.. syntax::

    ($$,$$ MatchArm)



* :dp:`hash_s7S3yZMAU0ma` Whenever the run-time semantics define certain actions to happen in an arbitrary 
  order, this means that a tool arranges for these actions to occur in a way that is equivalent to some
  sequential order, following the rules that result from that sequential order. This can happen for example,
  if two parameters of a given call expression have side effects.

.. _hash_gtzKeBC1cGwD:

Versioning
----------

:dp:`hash_7NPuEw17R7FE`
The Hash language specification is updated with each new release and version of the 
compiler. Currently, the language has no versioning system because it is under active 
development and is not yet stable.

.. _hash_J5yw7XFVjs0t:

Definitions
-----------

:dp:`hash_1Gjt3s8xdkLx`
Terms are defined throughout this document, indicated by *italic* type. Terms 
explicitly defined in this document are not to be presumed to refer implicitly 
to similar terms defined elsewhere.

:dp:`hash_d0hTUT9Zalj2`
Mathematical terms not defined in this document are to be interpreted according to the 
CRC Concise Encyclopedia of Mathematics, Second Edition.

:dp:`hash_ni31C3XQuQl0`
The definitions of terms are available in :doc:`/glossary`.

:dp:`hash_mcilTYNCtiN8`
A *rule* is a requirement imposed on the programmer, states in normative 
language such as "shall", "shall not", "must", "must not", except for text under 
implementation Requirements heading.

:dp:`hash_iEOvJfrmspBa`
A *fact* us a requirement imposed on a confirming tool, stated in informative language 
such as "is", "is not", "can", "cannot".
