---
title: The FamilySearch GEDCOM Specification
subtitle: 7.0.4
email: GEDCOM@ChurchOfJesusChrist.org
copyright: |
    :::{style="page-break-after: always;page-break-before: always;"}
    Copyright 1984–2021 Intellectual Reserve, Inc. All rights reserved. A service provided by The Church of Jesus Christ of Latter-day Saints.
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
    > <http://www.apache.org/licenses/LICENSE-2.0>
    
    Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
    
     
    
    In accordance with the Apache 2.0 license that governs this work, any other work that is based on or derived from this work must include a readable copy of the following NOTICE. For more information, please refer to the full copy of the Apache 2.0 license.
    
    > NOTICE:
    > 
    > This work comprises, is based on, or is derived from the FAMILYSEARCH GEDCOM™ Specification, © 1984-2021 Intellectual Reserve, Inc. All rights reserved.
    >
    > "FAMILYSEARCH GEDCOM™" and "FAMILYSEARCH®" are trademarks of Intellectual Reserve, Inc. and may not be used except as allowed by the Apache 2.0 license that governs this work or as expressly authorized in writing and in advance by Intellectual Reserve, Inc.
    :::
    
author:
  - |
    Prepared by the
    
    :::{style="font-size:130%"}
    Family History Department<br/>
    The Church of Jesus Christ of Latter-day Saints
    :::
address: |
    **Family History Department**<br/>
    15 East South Temple Street<br/>
    Salt Lake City, UT 84150 USA
toc-title: Contents
lang: en
...


# Introduction {.unnumbered}

FamilySearch GEDCOM 7.0 was released in 2021 as the latest version of the GEDCOM format for the transmission and storage of genealogical information.
GEDCOM was developed by the Family History Department of The Church of Jesus Christ of Latter-day Saints to provide a flexible, uniform format for exchanging computerized genealogical data.
Its first purpose is to foster sharing genealogical information and to develop a wide range of inter-operable software products to assist genealogists, historians, and other researchers.
Its second purpose is as a long-term storage format for preserving genealogical information in an open, standard format that will be accessible and understood by future genealogists and the systems they use.

"GEDCOM" is an acronym for <u>**GE**</u>nealogical <u>**D**</u>ata <u>**COM**</u>munication and is traditionally pronounced "ˈdʒɛdkɑm."

## Purpose and Content of *The FamilySearch GEDCOM Specification*  {.unnumbered}

*The FamilySearch GEDCOM Specification* is a technical document written for computer programmers, system developers, and technology-aware users.
This document describes a document and file format as follows:

- A hierarchical container format (see [Chapter 1](#container))
- A set of data types (see [Chapter 2](#datatypes))
- A set of genealogical structures (see [Chapter 3](#gedcom-structures))
- The FamilySearch GEDZIP file format (see [Chapter 4](#gedzip))

Chapter 1 describes a hierarchical container format.
This container format is a general-purpose data representation language for representing any kind of structured information in a sequential medium,
similar to XML, JSON, YAML, or SDLang.
Chapter 1 discusses the syntax and identification of structured information in general,
but it does not deal with the semantic content of any particular kind of data.

Chapter 2 describes several data types used to represent genealogical information,
such as a date format that permits dating in multiple calendar systems.

Chapter 3 describes a set of nested genealogical structures
for representing
historical claims, such as individuals, families, and events;
sourcing information, such as sources, repositories, and citations;
and research metadata, such as information about researchers and rights.

A set of structures conforming to the first 3 chapters of *The FamilySearch GEDCOM Specification* is called a FamilySearch GEDCOM dataset.
A string of octets encoding a dataset is called a data stream.

Chapter 4 describes a file format for bundling a dataset
with a set of media files or other supporting documents.

:::note
Prior to 7.0:

- The container format was called "the GEDCOM data format."
- The data types were unnamed and described in various places throughout the document.
- The genealogical structures were known as "the Lineage-Linked GEDCOM Form."
:::

In addition to this specification itself, additional supplimental material can be found at <https://gedcom.io>, including:

- [Links to example and supporting software](https://gedcom.io/tools/)
- Frequently asked questions for [users](https://gedcom.io/generalfaqs) and [developers](https://gedcom.io/techfaqs)
- A [guide to migrating from 5.5.1 to 7.0](https://gedcom.io/migrate)
- [Ways to engage in the community](https://gedcom.io/community/)



## Purpose for Version 7.x {.unnumbered}

There have been multiple prior releases of this specification, with somewhat idiosyncratic version numbering.
The first public comment draft was released in 1984.
The previous major version was 5.5.1 which was released in draft status in November 1999
and re-released as a standard in October 2019.

Version 7.0 has a number of goals, including

- Clarify ambiguities in the specification.
- Simplify implementations by removing special-case handling.
- Modernize character encoding, length restrictions, and specification wording.
- Introduce semantic versioning (see <https://semver.org/>).
- Add better multimedia handling, negative assertions, and notes with markup.
- Add support for common extensions to 5.5.1.
- Provide tools for better interoperability of extensions.

Version 7.0 introduces several breaking changes with version 5.5.1;
5.5.1 files are, in general, not valid 7.0 files and *vice versa*.
These breaking changes were necessary to remove complicated constructs left over from earlier versions.
For a complete list of changes, see the accompanying changelog.

## A Guide to Version Numbers {.unnumbered}

Starting with version 7.0.0, version numbers use [semantic versioning](https://semver.org/).
The 3 numbers are titled *major*.*minor*.*patch*.

A new *major* version may make arbitrary changes to the specification. Distinct major versions are not in general either forward or backward compatible with one another.

A new *minor* version will preserve the validity of data from all previous minor versions. It may make additional data valid, for example by adding new structure types, allowing current structures in new contexts, or adding new enumerated values or calendars. A minor release will not change the semantic meaning of data from previous minor releases, so for example a 7.0 document is also a valid 7.1 document and represents the same information in both.

A new *patch* version is a clarified or improved specification for the same data and introduces no changes in the data itself. Any software that correctly implements *X*.*Y*.*Z* also correctly implements *X*.*Y*.*W*. If there is an ambiguity or contradiction in the specification, it will be resolved in a patch version unless it is known that implementations interpreted the spec differently and that clarifying the intended meaning would cause incompatibilities between those implementations.

It is recommended that implementations accept all data at their own or a lesser minor version, regardless of the patch version.
It is also recommended that they import data from subsequent minor versions by treating any unexpected structures, enumerations, or calendars as if they were [extensions].

## URIs and Prefix Notation {.unnumbered}

This document defines [Uniform Resource Identifiers (URIs)](https://www.rfc-editor.org/info/rfc3986) to unambiguously identify various concepts, including structure types, data types, calendars, enumerated values, and so on.
In a few places, existing URIs defined by other bodies are used, following the best practice that a new URI should not be introduced for a concept for which a URI is known.

Rather than write out URIs in full, we use prefix notation:
any URI beginning with 1 of the following short prefixes followed by a colon
is shorthand for a URI beginning with the corresponding URI prefix

| Short Prefix | URI Prefix                          |
|:-------------|:------------------------------------|
| `g7`         | `https://gedcom.io/terms/v7/`       |
| `xsd`        | `http://www.w3.org/2001/XMLSchema#` |
| `dcat`       | `http://www.w3.org/ns/dcat#`        |

:::example
When the specification says `xsd:string`, it means `http://www.w3.org/2001/XMLSchema#string`.
This is a specification shorthand only; the string "`xsd:string`" is not the URI defining this concept, `http://www.w3.org/2001/XMLSchema#string` is.
:::


# Hierarchical container format {#container}

## Characters

Each data stream is a sequence of octets or bytes.
The octets encode a sequence of characters according to the UTF-8 character encoding as described in §10.2 of [ISO/IEC 10646:2020](https://www.iso.org/standard/76835.html) and in [RFC 3629](https://www.rfc-editor.org/info/rfc3629).

:::note
Previous versions allowed multiple character encodings, defaulting to ANSEL.
7.0 only uses the UTF-8 character encoding.
:::

A file containing a FamilySearch GEDCOM data stream should use the filename extension `.ged`.

The first character in each data stream should be U+FEFF, the byte-order mark.
If present, this initial character has no meaning within this specification but serves to indicate to other systems that the file uses the UTF-8 character encoding.

Certain characters must not appear anywhere within a data stream:

- The C0 control characters other than tab and line endings (U+0000--U+001F except U+0009, U+000A and U+000D)
- The DEL character (U+007F)
- Surrogates (U+D800--U+DFFF)
- Invalid code points (U+FFFE and U+FFFF)

Implementations should be aware that bytes per character and characters per glyph are both variable when using UTF-8.
Use of Unicode-aware processing and display libraries is recommended.

Character-level grammars are specified in this document using
Augmented Bakaus-Naur Form (ABNF)
as defined in [STD 68](https://www.rfc-editor.org/info/std68)
and modified in [RFC 7405](https://www.rfc-editor.org/info/rfc7405).
We use the term "production" to refer to an ABNF rule, supported by any other rules it references.

:::note
The following is a brief summary of the parts of ABNF, as defined by STD 68 and RFC 7405, that are used in this document:

- A rule consists of a rulename, an equals sign `=`, and 1 or more alternative matches.
- Alternatives are separated by slashes `/`.
- The first line of a rule must not be indented; the second and subsequent lines of a rule must be indented.
- Comments are introduced with a semi-colon `;`.
- Unicode codepoints are given in hexadecimal preceded by `%x`. Ranges of allowed codepoints are given with a hyphen `-`.
- Double-quote delimit literal strings. Literal strings are case-insensitive unless they are preceded by `%s`.
- Parentheses `()` group elements. Brackets `[]` mark optional content. Preceding a group or element by `*` means any number may be included. Preceding a group or element by `1*` means 1 or more may be included.
:::

The banned characters can be expressed in ABNF as production `banned`:

```abnf
banned = %x00-08 / %x0B-0C / %x0E-1F ; C0 other than LF CR and Tab
       / %x7F                        ; DEL
       / %x80-9F                     ; C1
       / %xD800-DFFF                 ; Surrogates
       / %xFFFE-FFFF                 ; invalid
; All other rules assume the absence of any banned characters
```

All other ABNF expressions in this document assume the absence of any characters matching production `banned`.

This document additionally makes use of the following named character sets in ABNF:


```abnf
digit       = %x30-39   ; 0 through 9
nonzero     = %x31-39   ; 1 through 9
ucletter    = %x41-5A   ; A through Z
underscore  = %x5F      ; _
atsign      = %x40      ; @
```

## Structures

A **structure** consists of a structure type, an optional **payload**, and a collection of substructures.
The payload is a value expressed as a string using 1 of several data types, as described in [Chapter 2](#datatypes).

Every structure is either a **record**, meaning it is not contained in any other structure's collection of substructures,
or it is a **substructure** of exactly 1 other structure. The other structure is called its **superstructure**.
Each substructure either refines the meaning of its superstructure, provides metadata about its superstructure, or introduces new data that is closely related to its superstructure.

The collection of substructures is partially ordered.
Substructures with the same structure type are in a fixed order,
but substructures with different structure types may be reordered.
The order of substructures of a single type indicates user preference, with the first substructure being the most-preferred value,
unless a different meaning is explicitly indicated in the structure's definition.

A structure must have either a non-empty payload or at least 1 substructure.
Empty payloads and missing payloads are considered equivalent. The remainder of this document uses "payload" as shorthand for "non-empty payload".

:::note
Unlike structures, pseudo-structures needn't have either payloads or substructures. `TRLR` never has either, and `CONT` doesn't when payloads contain empty lines.
:::

A structure is a representation of data about its **subject**. Examples include the entity, event, claim, or activity that the structure describes.

Datasets also contain 3 types of pseudo-structures:

- The header resembles a record, comes first in each document, and contains metadata about the entire document in its substructures.
    See [The Header](#the-header) for more.

- The trailer resembles a record, comes last in each document, and cannot contain substructures.

- A line continuation resembles a substructure, comes before any other substructures, is used to encode multi-line payloads, and cannot contain substructures.

Previous versions limited the number of characters that could appear in a structure, record, and payload. Those restrictions were removed in 7.0.

## Lines

A **line** is a string representation of (part of) a *structure*.
A line consists of a level, optional cross-reference identifier, tag, optional line value, and line terminator.
It matches the production `Line`:

```abnf
Line    = Level D [Xref D] Tag [D LineVal] EOL

Level   = "0" / nonzero *digit
D       = %x20                            ; space
Xref    = atsign 1*tagchar atsign         ; but not "@VOID@"
Tag     = stdTag / extTag
LineVal = pointer / lineStr
EOL     = %x0D [%x0A] / %x0A              ; CR-LF, CR, or LF

stdTag  = ucletter *tagchar
extTag  = underscore 1*tagchar
tagchar = ucletter / digit / underscore

pointer = voidPtr / Xref
voidPtr = %s"@VOID@"

nonAt   = %x09 / %x20-3F / %x41-10FFFF    ; non-EOL, non-@
nonEOL  = %x09 / %x20-10FFFF              ; non-EOL
lineStr = (nonAt / atsign atsign) *nonEOL ; leading @ doubled
```

The **level** matches production `Level` and is used to encode substructure relationships.
Any line with level $0$ encodes a record or a record-like pseudo-structure.
Any line with level $x > 0$ encodes a substructure of the structure encoded by the nearest preceding line with level $x-1$.

:::note
Previous versions allowed spaces and blank lines to precede the level of a line.
That permission was removed from 7.0 to simplify parsing.
:::

The **cross-reference identifier** matches production `Xref` (but not `voidPtr`) and indicates that this is a structure to which pointer-type payloads may point.
Each cross-reference identifier must be unique within a given data document.
Cross-reference identifiers are not retained between data streams and should not be made visible to the user to avoid them referring to transient data within notes or other durable data.

Each record to which other structures point must have a cross-reference identifier.
A record to which no structures point may have a cross-reference identifier, but does not need to have one.
A substructure or pseudo-structure must not have a cross-reference identifier.

The **tag** matches production `Tag` and encodes the structure's type.
Tags that match the production `stdTag` are defined in this document.
Tags that match `extTag` are defined according to [Extensions].

The **line value** matches production `LineVal` and encodes the structure's payload.
Line value content is sufficient to distinguish between pointers and line strings.
Pointers are encoded as the cross-reference identifier of the pointed-to structure.
Each non-pointer payload may be encoded in 1 or more line strings (line continuations encode multi-line payloads in several line strings).
The exact encoding of non-pointer payloads is dependent on the datatype of the payload, as determined by the structure type.
The datatype of non-pointer payloads cannot be fully determined by line value content alone.

If a line value matches production `Xref`, the same value must occur as the cross-reference identifier of a structure within the document.
The special `voidPtr` production is provided to encode null pointers.

If the first character of the string stored in a line string is U+0040 (`@`), the line string must escape that character by doubling that `@`.

:::note
Previous versions required doubling all `@` in a line value, but such doubling was not widely implemented in practice.
`@` is only doubled in this version if it is the first character of a line string.
:::

:::example
A structure with tag `NOTE`, level 1, and a 2-line payload where the first line is "`me@example.com is my email`" and the second line is "`@me and @I are my social media handles`" would be encoded as

```gedcom
1 NOTE me@example.com is my email
2 CONT @@me and @I are my social media handles
```
:::

:::note
Line values that match neither `Xref` nor `lineStr` are prohibited. They have been used in previous versions (for example, a line value beginning `@#D` was a date in versions 4.0 through 5.5.1) and may be used again in a future version if an appropriate need arises.
:::

The components of a line are each separated by a single **delimiter** matching production `D`. A delimiter is always a single space character (U+0020). Using multiple delimiters between components of a line is prohibited. Thus if the tag is followed by 2 spaces, the first space is a delimiter and the second space is part of the line value.

All characters in a payload must be preserved in the corresponding line value, including preserving any leading or trailing spaces.

Each line is ended by a **line terminator** matching production `EOL`. A line terminator may be a carriage return U+000D, line feed U+000A, or a carriage return followed by a line feed. The same line terminator should be used on every line of a given document.

Line values cannot contain internal line terminators, but some payloads can.
If a payload contains a line terminator, the payload is split on the line terminators into several payloads.
The first of these split payloads is encoded as the line value of the structure's line,
and each subsequent split payload is encoded as the line value of a **line continuation** pseudo-structure placed immediately following, and with one greater level than, the structure's line.
The tag of a line continuation pseudo-structure is `CONT`.
The order of the line continuation pseudo-structures matches the order of the lines of text in the payload.

Line continuation pseudo-structures are not considered to be structures.
While they match production `Line` and their level and position makes them appear to be substructures of the structure, they are actually a continuation of the encoding of the structure's payload and are not part of a structure's collection of substructures.
They must appear immediately following the line whose payload they are encoding and before any other line.

Because line terminators in payloads are encoded using line continuations, it is not possible to distinguish between U+000D and U+000A in payloads.

:::note
Previous versions limited the number of characters that could appear in a tag, cross-reference identifier, and line-value.
Those restrictions were removed in version 7.0.
The `CONC` pseudo-structure, which allowed line values to have a shorter length restriction than payloads, was also removed.
:::

:::example
The following are examples of valid but unrelated lines:

- level 0, cross-reference identifier `@I1234@`, tag `INDI`, no line value.

    ````gedcom
    0 @I1234@ INDI
    ````

- level 1, no cross-reference identifier, tag `CHIL`, pointer line value pointing to the structure with cross-reference identifier "`@I1234@`".

    ````gedcom
    1 CHIL @I1234@
    ````

- level 1, no cross-reference identifier, tag `NOTE`, and line value + continuation pseudo-structure to encode a 4-line payload string: "`This is a note field that`", "`  spans four lines.`", “”, and "`(the third line was blank)`". Note that leading and trailing spaces are preserved.

    ````gedcom
    1 NOTE This is a note field that
    2 CONT   spans four lines.
    2 CONT
    2 CONT (the third line was blank)
    ````
:::

##  The Header and Trailer {#the-header}

Every dataset must begin with a header pseudo-structure and end with a trailer pseudo-structure.

The trailer pseudo-structure has level `0`, tag `TRLR` and no line value or substructures.
The trailer has no semantic meaning; it is present only to mark the end of the dataset.

The header pseudo-structure has level `0`, tag `HEAD`, and no line value.
The substructures of the header pseudo-structure provide metadata about the entire dataset.
Some of those substructures are defined here;
others are defined in [Chapter 3](#gedcom-structures) or by extensions.

Every header must contain a substructure with a known tag that identifies the specification to which the dataset complies.
For FamilySearch GEDCOM 7.0, this is the `GEDC` structure described in [Chapter 3](#GEDC).

A header should contain an extension schema structure with tag `SCHMA`
as described in [Extensions].

##  Extensions

A **standard structure** is a structure whose type, tag, meaning, superstructure, and cardinality within the superstructure are described in this document. This includes records such as `INDI` and substructures such as `INDI`.`NAME`.

The recommended way to go beyond the set of standard structure types in this specification or to expand their usage is to submit a feature request on the [FamilySearch GEDCOM development page](https://github.com/FamilySearch/GEDCOM/issues) so that the ramifications of the proposed addition and its interplay with other proposals may be discussed and the addition may be included in a subsequent version of this specification.

This specification also provides multiple ways to for extension authors to go beyond the specification without submitting a feature request, which are described in the remainder of this section.

A **tagged extension structure** is a structure whose tag matches production `extTag`. Tagged extension structures may appear as records or substructures of any other structure. Their meaning is defined by their tag, as is discussed more fully in the section [Extension Tags].

Any substructure of a tagged extension structure that uses a tag matching `stdTag` is an **extension-defined substructure**.
Substructures of an extension-defined substructure that uses a tag matching `stdTag` are also extension-defined substructures.
The meaning and use of each extension-defined substructure is defined by the tagged extension structure it occurs within, not by its tag alone nor by this specification.

:::example
In the following

```gedcom
0 @P1@ _LOC
1 NAME Βυζάντιον
2 DATE FROM 667 BCE TO 324
1 _POP 15149358
2 DATE 31 DEC 2020
0 @I1@ INDI
1 BIRT
2 _LOC @P1@
```

- Both uses of `_LOC` are tagged extension structures, as is `_POP`.
- `_LOC`.`NAME` and `_LOC`.`NAME`.`DATE` are both extension-defined substructures. Their meaning is defined by the specification defining `_LOC`.
- `_POP`.`DATE` is an extension-defined substructure. Its meaning is defined by the specification defining `_POP`.
- Even though both `DATE`s appear to have `g7:type-DATE` payloads, we can't know that is the intended datatype without consulting the defining specifications of `_LOC` and `_POP`, respectively. The first might be a `g7:type-DATE#period` and the second a `g7:type-DATE#exact`, for example.
:::

If an extension-defined substructure has a tag that is also used by one or more standard structures, its meaning and payload type should match at least one of those standard structure types.

:::example
An extension-defined substructure with tag "`DATE`" should provide a date or date period relevant to its superstructure, as do all `DATE`-tagged structures in this specification. Extensions should not use "`DATE`" to tag a structure describing anything else (even something that might reasonably be abbreviated "date", such as someone an individual dated).
:::

As a special case, a tagged extension structure can be defined to have a standard structure type.
These are called **relocated standard structures** and can only appear with superstructures that are not documented as a superstructure of that structure type in this specification.
The extension-defined substructures of a relocated standard structure are the substructure types documented in this specification for that structure type, including usual limitations on cardinality, payloads, substructures, etc.

:::example
Suppose `_DATE` is defined to mean a `g7:DATE` (using a [documented extension tag](#extension-tags)). Then in the following

```gedcom
0 @I1@ INDI
1 NAME John /Doe/
2 _DATE FROM 6 APR 1917 TO 11 NOV 1918
3 PHRASE During America's involvement in the Great War
1 BIRT
2 PLAC Queens, New York, New York, USA
```

- `_DATE` is a relocated standard structure with type `g7:DATE`, with the usual payload type and meaning of a `g7:DATE`.
- `PHRASE` is the structure type expected with that tag as a substructure of `g7:DATE`: namely, `g7:PHRASE`.
- `_DATE` can not be used as a substructure of `BIRT` because `BIRT` has a documented `g7:DATE` substructure with tag `DATE`.
- `BIRT` can not be used as a substructure of `_DATE` or `_DATE`.`PHRASE` because neither structure type has a documented substructure with tag `BIRT`.
:::

All other non-standard structures are prohibited. Examples of prohibited structures include, but are not limited to,

- a record or substructure of a standard structure using a tag matching production `stdTag` that is not defined in this document;
- any substructure with cardinality `{0:1}` appearing more than once;
- a standard substructure appearing as a record or vice-versa;
- a standard structure whose payload does not match the requirements of this document.

:::note
In some cases, an extension may need to allow multiple structures where this document allows only 1. The recommended way to do this is to create an extension tag and URI and serve a page describing how the semantics of the structure have been extended to allow multiple instances.

:::example
Suppose I have multiple sources that give different ages of the wife at a wedding; however, this specification allows only 1 `MARR`.`WIFE`.`AGE`. An extension could not include multiple `MARR`.`WIFE` nor `MARR`.`WIFE`.`AGE`, but could define a new extension `_AGE`, give it a URL, and provide the following definition of this extension structure type at that URL:

> Alternate age: an age attested by some source, but not accepted by the researcher as the actual age of the individual. If the age is accepted by the researcher, the standard tag `AGE` should be used instead.

This alternate age extension structure could be used as follows:

```gedcom
1 MARR
2 WIFE
3 AGE 27y
3 _AGE 22y
```
:::
:::

Enumerated values may be extended with new values that match production `extTag`.
Enumerations may not use standard values from other enumeration sets.

:::example
The following is not allowed because `PARENT` is defined as a value for `ROLE`, not for `RESN`

```gedcom
0 @BAD@ INDI
1 RESN PARENT
1 NOTE The above enumeration value is not allowed
```
:::

Dates may be extended provided they use a calendar that matches production `extTag`.
Dates with extension calendars may also use extension months and epochs.


### Extension Tags

Each use of the `extTag` production is called an extension tag,
including when used as a tag, calendar, month, epoch, or enumerated value.
Each `extTag` is either a *documented extension tag* or an *undocumented extension tag*.
It is recommended that documented extension tags be used instead of undocumented extension tags wherever possible.

A **documented extension tag** is a tag that is mapped to a URI using the schema structure.
The schema structure is a substructure of the header with tag `SCHMA`.
It should appear within the document before any extension tags.
The schema's substructures are tag definitions.

A tag definition is a structure with tag `TAG`.
Its payload is an extension tag, a space, and a URI
and defines that extension tag to be an abbreviation for that URI within the current document.

:::example
The following header

```gedcom
0 HEAD
1 SCHMA
2 TAG _SKYPEID http://xmlns.com/foaf/0.1/skypeID
2 TAG _MEMBER http://xmlns.com/foaf/0.1/member
```

defines the following tags

| Tag   | Means |
| :---- | :---- |
| `_SKYPEID` | `http://xmlns.com/foaf/0.1/skypeID` |
| `_MEMBER` | `http://xmlns.com/foaf/0.1/member` |
:::

The meaning of a documented extension tag is identified by its URI, not its tag.
Documented extension tags can be changed freely by modifying the schema,
though it is recommended that documented extension tags not be changed.
However, a tag change may be necessary if a product picks the same tags for URIs that another product uses for different URIs.

:::example
The following 2 document fragments are semantically equivalent
and a system importing one may export it as the other without change of meaning.

```gedcom
0 HEAD
1 SCHMA
2 TAG _SKYPEID http://xmlns.com/foaf/0.1/skypeID
0 @I0@ INDI
1 _SKYPEID example.person
```

```gedcom
0 HEAD
1 SCHMA
2 TAG _SI http://xmlns.com/foaf/0.1/skypeID
0 @I0@ INDI
1 _SI example.person
```
:::

An extension tag that is not given a URI in the schema structure is called an **undocumented extension tag**.
The meaning of an undocumented extension tag is identified by its tag.


### Requirements and Recommendations

- It is recommended that applications not use undocumented extension tags.
- It is required that each tag definition's extension tag be unique within the document.
- It is recommended that each documented extension tag's URI be unique within the document.
- It is recommended that extension creators use URLs as their URIs
and serve a page describing the meaning of an extension at its URL.

Future versions may include additional recommendations relating to documentation, machine-readable documentation, or embedded metadata about extensions within the schema.

### Extension versus Standard

Standard structures take priority over extensions.
Data contained in extension tags will not be interpreted by other systems correctly unless the other system supports that particular extension.
In particular, those supporting extensions should keep in mind the following:

- If a standard structure is present that contradicts an extension that is present, the standard structure has priority and the extension should be updated to align with it.
    
    <div class="example">
    
    If a document has an extension `_ISODATE` in ISO 8601 format that disagrees with a `DATE` in the `DateValue` format, the `DATE` shall be taken as more correct and the `_ISODATE` updated to reflect that.
    
    </div>

- If a standard structure can be extracted as a subset of the semantics of an extension, the standard tag must be generated along with the extension and kept in sync with it by systems understanding the extension.

    <div class="example">
    
    If a document has an extension `_LOC` providing a detailed hierarchical place representation with historical names, boundaries, and the like, it must also generate the corresponding `PLAC` structures with the subset of that information which `PLAC` can represent.
    
    </div>

- If an extension can be extracted as a subset of the semantics of a standard structure, or if the extension and standard structure only sometimes align, then the standard structure should be included if and only if the semantics align in this case.
    
    <div class="example">
    
    If a document has an extension `_PARTNER` that generalizes `HUSB` and `WIFE` and some `ASSO` `ROLE`s, then it should pair the extension with those standard structures if and only if it knows which one applies.
    
    </div>

    <div class="example">
    
    If a document has an extension `_HOUSEHOLD` that is the same as `FAM` in some situations but not in others, then it should keep the `_HOUSEHOLD` and `FAM` in sync if and only if they align.
    
    </div>

-   Six standard structure types are exceptions to these rules:
    `NOTE`,` SNOTE`, `INDI`.`EVEN`, `FAM`.`EVEN`, `INDI`.`FACT`, and  `FAM`.`FACT`.
    Each of these allows human-readable text to describe information that cannot be captured in more-specific structures.
    As such, all other structures express information that could be described using 1 or more of those structure types.
    Extensions do not need to duplicate their information using any of those structures.

    <div class="example">
    
    If a document has an extension `_MEMBER` that indicates membership in clubs, boards, and other groups,
    it is not required to duplicate that information in an `INDI`.`FACT`
    because `INDI`.`FACT` is 1 of the 6 special structure types listed above.
    
    </div>

    <div class="example">
    
    If a document has an extension `_WEIGHT` that describes the weight of a person,
    it must duplicate that information in an `INDI`.`DSCR`
    because `INDI`.`DSCR` is not 1 of the 6 generic structure types.

    </div>

## Removing data

There may be situations where data needs to be removed from a dataset, such as when a user requests its deletion or marks it as confidential and not for export.

In general, removed data should result in removed structures.

Pointers to a removed structure should be replaced with `voidPtr`s.

If removal of a structure makes the superstructure invalid because the superstructure required the substructure, the structure should instead be retained and have its payload changed to a `voidPtr` if a pointer, or to a datatype-appropriate empty value if a non-pointer.

If removing a structure leaves its superstructure with no payload and no substructures, the superstructure should also be removed.



# Data types {#datatypes}

Every line value (with any continuation pseudo-structures) is a string.
However, those strings can encode 1 of several conceptual datatypes.

## Text

A free-text string is text in a human language.
Conceptually, it may be either a user-generated string or a source-generated string.
Programmatically, both are treated as unconstrained sequences of characters with an associated language.

```abnf
anychar = %x09-10FFFF ; but not banned, as with all ABNF rules
Text    = *anychar
```

The URI for the `Text` datatype is `xsd:string`.

## Integer

An integer is a non-empty sequence of ASCII decimal digits
and represents a non-negative integer in base-10.
Leading zeros have no semantic meaning and should be omitted.

```abnf
Integer = 1*digit
```

Negative integers are not supported by this specification.

The URI for the `Integer` datatype is `xsd:nonNegativeInteger`.

## Enumeration

An enumeration is a selection from a set of options.
They are represented as a string matching the same production as a tag.

```abnf
Enum    = Tag
```

Each structure type with an enumeration payload also defines specific payload values it permits.
These permitted payloads match production `stdTag` and should each have a defined URI.
Payload values that match production `extTag` are always permitted in structures with an enumeration payload
and have their URI defined by the schema.

Each enumeration value has a distinct meaning
as identified by its corresponding URI.

The URI for the `Enum` datatype is `g7:type-Enum`.

## Date

The date formats defined in this specification
include the ability to store approximate dates, date periods, and dates expressed in different calendars.

Technically, there are 3 distinct date datatypes:

- `DateValue` is a generic type that can express many kinds of dates.
- `DateExact` is used for timestamps and other fully-known dates.
- `DatePeriod` is used to express time intervals that span multiple days.


```abnf
DateValue   = date / DatePeriod / dateRange / dateApprox
DateExact   = day D month D year  ; in Gregorian calendar
DatePeriod  = %s"FROM" D date [D %s"TO" D date]
            / %s"TO" D date

date        = [calendar D] [[day D] month D] year [D epoch]
dateRange   = %s"BET" D date D %s"AND" D date
            / %s"AFT" D date
            / %s"BEF" D date
dateApprox  = (%s"ABT" / %s"CAL" / %s"EST") D date

dateRestrict = %s"FROM" / %s"TO" / %s"BET" / %s"AND" / %s"BEF"
            / %s"AFT" / %s"ABT" / %s"CAL" / %s"EST" / %s"BCE"

calendar = %s"GREGORIAN" / %s"JULIAN" / %s"FRENCH_R" / %s"HEBREW"
         / extTag

day     = Integer
year    = Integer
month   = stdTag / extTag  ; constrained by calendar
epoch   = %s"BCE" / extTag ; constrained by calendar
```

In addition to the constraints above:

- The allowable `month`s and `epoch`s are determined by the `calendar`.
- No calendar names, months, or epochs match `dateRestrict`.
- Extension calendars (those with `extTag` for their `calendar`) must use `extTag`, not `stdTag`, for months.

An absent `calendar` is equivalent to the calendar `GREGORIAN`.

The grammar above allows for `date`s to be preceded by various words. The meaning of these words is given as follows:

|Production| Meaning                                    |
|:---------|:-------------------------------------------|
|`FROM` *x*|Lasted for multiple days, beginning on *x*. |
|`TO` *x*  |Lasted for multiple days, ending on *x*.    |
|`BET` *x*<br/>`AFT` *x*|Exact date unknown, but no earlier than *x*.|
|`AND` *x*<br/>`BEF` *x*|Exact date unknown, but no later than *x*.  |
|`ABT` *x* |Exact date unknown, but near *x*.           |
|`CAL` *x* |*x* is calculated from other data.          |
|`EST` *x* |Exact date unknown, but near *x*; and *x* is calculated from other data.|

Known calendars and tips for handling dual dating and extension calendars are given in [Appendix A: Calendars and Dates](#A-calendars).

Date payloads may also be omitted entirely if no suitable form is known but a substructure (such as a `PHRASE` or `TIME`) is desired.

:::note
Versions 5.3 through 5.5.1 allowed phrases inside `DateValue` payloads.
Date phrases were moved to the `PHRASE` substructure in version 7.0.
:::

:::note
As defined by the grammar above, every date must have a year.
If no year is known, the entire date may be omitted.

:::example
The following is an appropriate way to handle a missing year

```gedcom
2 DATE
3 PHRASE 5 January (year unknown)
```
:::
:::

The URI for the `DateValue` datatype is `g7:type-Date`.

The URI for the `DateExact` datatype is `g7:type-Date#exact`.

The URI for the `DatePeriod` datatype is `g7:type-Date#period`.

## Time

Time is represented on a 24-hour clock (for example, 23:00 rather than 11:00 PM).
It may be represented either in event-local time or in Coordinated Universal Time (UTC).
UTC is indicated by including a `Z` (U+005A) after the time value; event-local time is indicated by its absence.

```abnf
Time     =  hour ":" minute [":" second ["." fraction]] [%s"Z"]

hour     = digit / ("0" / "1") digit / "2" ("0" / "1" / "2" / "3")
minute   = ("0" / "1" / "2" / "3" / "4" / "5") digit
second   = ("0" / "1" / "2" / "3" / "4" / "5") digit
fraction = 1*digit
```

:::note
The above grammar prohibits end-of-day instant `24:00:00` and leap-seconds. It allows both `02:50` and `2:50` as the same time.
:::

The URI for the `Time` datatype is `g7:type-Time`.

## Age

Ages are represented by counts of years, months, weeks, and days.

```abnf
Age         = [ageBound D] ageDuration

ageBound    = "<" / ">"
ageDuration = years [D months] [D weeks] [D days]
            / months [D weeks] [D days]
            / weeks [D days]
            / days

years   = Integer %x79    ; 35y
months  = Integer %x6D    ; 11m
weeks   = Integer %x77    ; 8w
days    = Integer %x64    ; 21d
```

Where

|Production |Meaning                                           |
|:----------|:-------------------------------------------------|
|`<`        | The real age was less than the provided age      |
|`>`        | The real age was greater than the provided age   |
|`years`    | a number of years                                |
|`months`   | a number of months                               |
|`weeks`    | a number of weeks                                |
|`days`     | a number of days                                 |

Non-integer numbers should be rounded down to an integer. Thus, if someone has lived for 363.5 days, their age might be written as `363d`, `51w 6d`, `51w`, `0y`, etc.

Because numbers are rounded down, `>` effectively includes its endpoint; that is, the age `> 8d` includes people who have lived 8 days + a few seconds.

Different cultures count ages differently. Some increment years on the anniversary of birth and others at particular seasons. Some round to the nearest year, others round years down, others round years up. Because users may be unaware of these traditions or may fail to convert them to the round-down convention, errors in age of up to a year are common.

Age payloads may also be omitted entirely if no suitable form is known but a substructure (such as a `PHRASE`) is desired.

:::note
Versions 5.5 and 5.5.1 allowed a few specific phrases inside `Age` payloads.
Age phrases were moved to the `PHRASE` substructure in 7.0.
:::

The URI for the `Age` datatype is `g7:type-Age`.


## List

A list is a meta-syntax representing a sequence of values with another datatype.
Two list datatypes are used in this document: List:Text and List:Enum.
Lists are serialized in a comma-separated form, delimited by a comma (U+002C `,`) and any number of spaces (U+0020) between each item.
It is recommended that a comma-space pair (U+002C U+0020) be used as the delimiter.

```abnf
List      = listItem *(listDelim listItem)
listItem  = "" / nocommasp / nocommasp *nocomma nocommasp
listDelim = *D "," *D
nocomma   = %x09-2B / %x2D-10FFFF
nocommasp = %x09-1D / %x21-2B / %x2D-10FFFF

List-Text = List
List-Enum = Enum *(listDelim Enum)
```

If valid for the underlying type, empty strings may be included in a list by having no characters between delimiters.

:::example
A `List:Text` with value "`, , one, more,`" has 5 `Text`-type values: 2 empty strings, the string "`one`", the string "`more`", and 1 more empty string.
:::

There is no escaping mechanism to allow lists of entries that begin or end with spaces or that contain comma characters.

The URI for the `List:Text` datatype is `g7:type-List#Text`.

The URI for the `List:Enum` datatype is `g7:type-List#Enum`.


## Personal Name

A personal name is mostly free-text. It should be the name as written in the culture of the individual and should not contain line breaks, repeated spaces, or characters not part of the written form of a name (except for U+002F as explained below).

```abnf
NamePersonal = nameStr
             / [nameStr] "/" [nameStr] "/" [nameStr]

nameChar     = %x20-2E / %x30-10FFFF  ; any but '/' and '\t'
nameStr      = 1*nameChar
```

The character U+002F (`/`, slash or solidus) has special meaning in a personal name, being used to delimit the portion of the name that most closely matches the concept of a surname, family name, or the like.
This specification does not provide any standard way of representing names that contain U+002F.

The URI for the `PersonalName` datatype is `g7:type-Name`.

## Language

The language datatype represents a human language or family of related languages, as defined in [BCP 46](https://www.rfc-editor.org/info/bcp47).
It consists of a sequence of language subtags separated by hyphens,
where language subtags are [registered by the IANA](https://www.iana.org/assignments/language-subtag-registry).

The ABNF grammar for language tags is given in BCP 47, section 2.1, production `Language-Tag`.

The URI for the `Language` datatype is `xsd:Language`.

## Media Type

The media type datatype represents the encoding of information in bytes or characters, as defined in [RFC 2045](https://www.rfc-editor.org/info/rfc2045) and [registered by the IANA](http://www.iana.org/assignments/media-types/).

The official grammar for media type is given in RFC 2045, section 5.1.
However, that document does not give stand-alone ABNF, instead referring to registration rules and describing some components in English.
The programmatic parts of the media type grammar can be summarized as follows:

```abnf
MediaType    = mt-type "/" mt-subtype *(";" mt-parameter)

mt-type      = mt-token
mt-subtype   = mt-token
mt-parameter = mt-attribute "=" mt-value
mt-token     = 1*mt-char
mt-attribute = mt-token
mt-value     = mt-token / quoted-string
mt-char      = %x20-21 / %x23-27 / %x2A-2B / %x2D-2E ; not "(),/
             / %x30-39 / %x41-5A / %x5E-7E           ; not :;<=>?@[\]

mt-qstring   = %x22 *(mt-qtext / mt-qpair) %x22
mt-qtext     = %x09-0A / %x20-21 / %x23-5B / %x5D-7E ; not CR "\
mt-qpair     = "\" %x09-7E
```

The URI for the `MediaType` datatype is `dcat:mediaType`.

## Special

The special datatype is a string conforming to a case-specific standard or constraints. The constraints on each special datatype instance are either unique to that structure type or are not simply expressed.
For example, the payload of an `IDNO` structure may obey different rules for each possible `TYPE` substructure.

Each special datatype is distinct.
The URI for the generic datatype subsuming all `Special` datatypes is `xsd:string` (the same as the `Text` datatype).

```abnf
Special = Text
```


# Genealogical structures {#gedcom-structures}

This chapter describes a set of structure types for exchanging family-based lineage-linked genealogical information.
Lineage-linked data pertains to individuals linked in family relationships across multiple generations.

The genealogical structures defined in this chapter are based on the general framework of the container format and data types defined in Chapters 1 and 2.

Historically, these genealogical structures were used as the only form approved for exchanging data with Ancestral File, TempleReady and other Family History resource files.
Those systems were all replaced between 1999 and 2019, and [GEDCOM-X](https://gedcomx.org) was introduced as the new syntax for communication with their replacements.
FamilySearch GEDCOM 7.0 and GEDCOM-X have similar expressive power,
but as of 2021 GEDCOM is more common for exchanging single-researcher files between applications
and GEDCOM-X is more common for transferring bulk data and communication directly between applications.

The basic description of the genealogical structures' organization is presented in the following 3 major sections:

* "[Structure Organization]" describes records and other nested structures.
* "[Structure Meaning]" provides a definition of each structure by its tag.
* "[Enumeration Values]"  provides a definition of each enumeration value by its containing structure.

## A Metasyntax for Structure Organization

The structures, with their payloads and substructures,
are represented using a custom metasyntax.
The intent of this metasyntax is to resemble the line encoding of allowable structures. In the metasyntax:

- Options are placed between brackets `[` and `]` and have choices separated by pipes `|`.
- Named sets of rules are indicated with a name followed by `:=`.
- Level markers are used to indicate substructure relationships.
    - `0` means "must be a record".
    - `n` means "level inherited from rule instantiation".
    - `+1`, `+2`, etc., indicate nesting within nearest preceding structure with lesser level.
- Four cardinality markers are used: `{0:1}`, `{1:1}`, `{0:M}`, and `{1:M}`.
    - `{0:` means "optional" -- the structure may be omitted
    - `{1:` means "required" -- at least 1 must appear
    - `:M}` means "any number" -- 1 or more structures may appear.
        Unless otherwise specified, the first is the most-preferred value.
        If an application needs to display just 1 of several `NAME`s, `BIRT`s, etc, they should show the first such structure unless more specific selection criteria are available.
    - `:1}` means "singular" -- at most 1 may appear; a second must not be present.
    
    Systems interested in violating the cardinality rules should instead create [extension structures](#extensions) with different cardinality.
- Rule instantiation is indicated by the rule name in double angle-brackets (such as `<<`rule name`>>`) and a cardinality marker.
    
    The cardinality markers of rule instantiations and their referenced line templates are combined such that the resulting cardinality
    is required only if both combined cardinalities are required
    and singular only if both combined cardinalities are singular.
    
    <div class="example">
    The definition of the `FAM` record has the line

    ````gedstruct
      +1 <<CREATION_DATE>>                     {0:1}
    ````
    
    and the `CREATION_DATE` rule begins

    ````gedstruct
    n CREA                                     {1:1}  g7:CREA
    ````
    
    Thus, a `FAM` record has an optional singular `CREA` substructure
    (such as cardinality `{0:1}`).
    </div>
    
- Line templates have several parts:
    - An optional cross-reference template `@XREF:`tag`@`, meaning this structure may be pointed to by other structures.
        
        Structures that are not pointed to by other structures need not have a [cross-reference identifier](#lines) even if their line template has a cross-reference template.
    - The standard tag for this structure.
    - An optional payload descriptor; if present this is 1 of the following:
        
        - `@<XREF:`tag`>@` means a pointer to a structure with this cross-reference template; `@VOID@` is also permitted.
        - `<`datatype`>` means a non-pointer payload, as described in [Data types](#datatypes). If the datatype allows the empty string, the payload may be omitted.
        - `[`text`|<NULL>]` means the payload is optional but if present must be the given text.
        
        If there is a payload descriptor, a payload that matches the payload is required of the described structure unless the descriptor says the payload is optional.

        If there is no payload descriptor, the described structure must not have a payload.
        
    - A cardinality marker.
    - The URI of this structure type.
        
        Pseudo-structures do not have a URI.

The context of a structure's superstructure may be necessary in addition to the structure's standard tag to fully determine its structure type.
To refer to a structure in the context of its superstructure,
tags are written with intervening periods.
For example, `GEDC`.`VERS` refers to a structure with tag `VERS`
and a superstructure with tag `GEDC`.


## Structure Organization

### Document

#### Dataset := {-}

```gedstruct
0 <<HEADER>>                               {1:1}
0 <<RECORD>>                               {0:M}
0 TRLR                                     {1:1} 
```

#### `RECORD` :=

```gedstruct
[
n <<FAMILY_RECORD>>                        {1:1}
|
n <<INDIVIDUAL_RECORD>>                    {1:1}
|
n <<MULTIMEDIA_RECORD>>                    {1:1}
|
n <<REPOSITORY_RECORD>>                    {1:1}
|
n <<SHARED_NOTE_RECORD>>                   {1:1}
|
n <<SOURCE_RECORD>>                        {1:1}
|
n <<SUBMITTER_RECORD>>                     {1:1}
]
```

#### `HEADER` :=

```gedstruct
n HEAD                                     {1:1} 
  +1 GEDC                                  {1:1}  g7:GEDC
     +2 VERS <Special>                     {1:1}  g7:GEDC-VERS
  +1 SCHMA                                 {0:1}  g7:SCHMA
     +2 TAG <Special>                      {0:M}  g7:TAG
  +1 SOUR <Special>                        {0:1}  g7:HEAD-SOUR
     +2 VERS <Special>                     {0:1}  g7:VERS
     +2 NAME <Text>                        {0:1}  g7:NAME
     +2 CORP <Text>                        {0:1}  g7:CORP
        +3 <<ADDRESS_STRUCTURE>>           {0:1}
        +3 PHON <Special>                  {0:M}  g7:PHON
        +3 EMAIL <Special>                 {0:M}  g7:EMAIL
        +3 FAX <Special>                   {0:M}  g7:FAX
        +3 WWW <Special>                   {0:M}  g7:WWW
     +2 DATA <Text>                        {0:1}  g7:HEAD-SOUR-DATA
        +3 DATE <DateExact>                {0:1}  g7:DATE-exact
           +4 TIME <Time>                  {0:1}  g7:TIME
        +3 COPR <Text>                     {0:1}  g7:COPR
  +1 DEST <Special>                        {0:1}  g7:DEST
  +1 DATE <DateExact>                      {0:1}  g7:HEAD-DATE
     +2 TIME <Time>                        {0:1}  g7:TIME
  +1 SUBM @<XREF:SUBM>@                    {0:1}  g7:SUBM
  +1 COPR <Text>                           {0:1}  g7:COPR
  +1 LANG <Language>                       {0:1}  g7:HEAD-LANG
  +1 PLAC                                  {0:1}  g7:HEAD-PLAC
     +2 FORM <List:Text>                   {1:1}  g7:HEAD-PLAC-FORM
  +1 <<NOTE_STRUCTURE>>                    {0:1}
```

The header pseudo-structure provides metadata about the entire dataset.
A few substructures of note:

- `GEDC` identifies the specification that this document conforms to.
- `SCHMA` gives the meaning of extension tags; see [Extensions](#extensions) for more.
- `SOUR` describes the originating software.
    - `CORP` describes the corporation creating the software.
    - `HEAD`.`SOUR`.`DATA` describes a larger database this data is extracted from.
- `LANG` and `PLAC` give a default value for the rest of the document.


### Records

#### `FAMILY_RECORD` :=

```gedstruct
n @XREF:FAM@ FAM                           {1:1}  g7:record-FAM
  +1 RESN <List:Enum>                      {0:1}  g7:RESN
  +1 <<FAMILY_ATTRIBUTE_STRUCTURE>>        {0:M}
  +1 <<FAMILY_EVENT_STRUCTURE>>            {0:M}
  +1 <<NON_EVENT_STRUCTURE>>               {0:M}
  +1 HUSB @<XREF:INDI>@                    {0:1}  g7:FAM-HUSB
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 WIFE @<XREF:INDI>@                    {0:1}  g7:FAM-WIFE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 CHIL @<XREF:INDI>@                    {0:M}  g7:CHIL
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<ASSOCIATION_STRUCTURE>>             {0:M}
  +1 SUBM @<XREF:SUBM>@                    {0:M}  g7:SUBM
  +1 <<LDS_SPOUSE_SEALING>>                {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The `FAM` record was originally structured to represent families where a male `HUSB` (husband or father) and female `WIFE` (wife or mother) produce `CHIL` (children).
The `FAM` record may also be used for cultural parallels to this,
including nuclear families, marriage, cohabitation, fostering, adoption, and so on, regardless of the gender of the partners.
Sex, gender, titles, and roles of partners should not be inferred based on the partner that the `HUSB` or `WIFE` structure points to.

The individuals pointed to by the `HUSB` and `WIFE` are collectively referred to as "partners", "parents" or "spouses".

Some displays may be unable to display more than 2 partners.
Displays may use `HUSB` and `WIFE` as layout hints,
for example, by consistently displaying the `HUSB` on the same side of the `WIFE` in a tree view.
Family structures with more than 2 partners
may either use several `FAM` records
or use `ASSOCIATION_STRUCTURE`s to indicate additional partners.

:::note
The `FAM` record will be revised in a future version to more fully express the diversity of human family relationships.
:::

The order of the `CHIL` (children) pointers within a `FAM` (family) structure should be chronological by birth;
this is an exception to the usual "most preferred value first" rule.
A `CHIL` with a `voidPtr` indicates a placeholder for an unknown child in this birth order.

If a `FAM` record uses `HUSB` or `WIFE` to point to an `INDI` record,
the `INDI` record must use `FAMS` to point to the `FAM` record.
If a `FAM` record uses `CHIL` to point to an `INDI` record,
the `INDI` record must use a `FAMC` to point to the `FAM` record.



#### `INDIVIDUAL_RECORD` :=

```gedstruct
n @XREF:INDI@ INDI                         {1:1}  g7:record-INDI
  +1 RESN <List:Enum>                      {0:1}  g7:RESN
  +1 <<PERSONAL_NAME_STRUCTURE>>           {0:M}
  +1 SEX <Enum>                            {0:1}  g7:SEX
  +1 <<INDIVIDUAL_ATTRIBUTE_STRUCTURE>>    {0:M}
  +1 <<INDIVIDUAL_EVENT_STRUCTURE>>        {0:M}
  +1 <<NON_EVENT_STRUCTURE>>               {0:M}
  +1 <<LDS_INDIVIDUAL_ORDINANCE>>          {0:M}
  +1 FAMC @<XREF:FAM>@                     {0:M}  g7:INDI-FAMC
     +2 PEDI <Enum>                        {0:1}  g7:PEDI
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
     +2 STAT <Enum>                        {0:1}  g7:FAMC-STAT
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
     +2 <<NOTE_STRUCTURE>>                 {0:M}
  +1 FAMS @<XREF:FAM>@                     {0:M}  g7:FAMS
     +2 <<NOTE_STRUCTURE>>                 {0:M}
  +1 SUBM @<XREF:SUBM>@                    {0:M}  g7:SUBM
  +1 <<ASSOCIATION_STRUCTURE>>             {0:M}
  +1 ALIA @<XREF:INDI>@                    {0:M}  g7:ALIA
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 ANCI @<XREF:SUBM>@                    {0:M}  g7:ANCI
  +1 DESI @<XREF:SUBM>@                    {0:M}  g7:DESI
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The individual record is a compilation of facts or hypothesized facts about an individual.
These facts may come from multiple sources.
Source citations and notes allow documentation of the source where each of the facts were discovered.

A single individual may have facts distributed across multiple individual records, connected by `ALIA` (alias, in the computing sense not the pseudonym sense) pointers.
See `ALIA` for more.

Individual records are linked to Family records by use of bi-directional pointers.
Details about those links are stored as substructures of the pointers in the individual record.

Other associations or relationships are represented by the `ASSO` (association) tag.
The person's relation or associate is the person being pointed to.
The association or relationship is stated by the value on the subordinate `ROLE` line.

:::example
The following example refers to 2 individuals, `@I1@` and `@I2@`,
where `@I2@` is a godparent of `@I1@`:

```gedcom
0 @I1@ INDI
1 ASSO @I2@
2 ROLE GODP
```
:::

Events stored as facts within an `INDI` record may also have `FAMC` or `ASSO` tags to indicate families and individuals that participated in those events.
For example,
a `FAMC` pointer subordinate to an adoption event indicates a relationship to family by adoption;
biological parents can be shown by a `FAMC` pointer subordinate to the birth event;
the eulogist at a funeral can be shown by an `ASSO` pointer subordinate to the burial event;
and so on.



#### `MULTIMEDIA_RECORD` :=

```gedstruct
n @XREF:OBJE@ OBJE                         {1:1}  g7:record-OBJE
  +1 RESN <List:Enum>                      {0:1}  g7:RESN
  +1 FILE <Special>                        {1:M}  g7:FILE
     +2 FORM <MediaType>                   {1:1}  g7:FORM
        +3 MEDI <Enum>                     {0:1}  g7:MEDI
           +4 PHRASE <Text>                {0:1}  g7:PHRASE
     +2 TITL <Text>                        {0:1}  g7:TITL
     +2 TRAN <Special>                     {0:M}  g7:FILE-TRAN
        +3 FORM <MediaType>                {1:1}  g7:FORM
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The multimedia record refers to 1 or more external digital files, and may provide some additional information about the files and the media they encode.

The file reference can occur more than once to group multiple files together. Grouped files should each pertain to the same context. For example, a sound clip and a photo both of the same event might be grouped in a single `OBJE`.

The change and creation dates should be for the `OBJE` record itself,
not the underlying files.



#### `REPOSITORY_RECORD` :=

```gedstruct
n @XREF:REPO@ REPO                         {1:1}  g7:record-REPO
  +1 NAME <Text>                           {1:1}  g7:NAME
  +1 <<ADDRESS_STRUCTURE>>                 {0:1}
  +1 PHON <Special>                        {0:M}  g7:PHON
  +1 EMAIL <Special>                       {0:M}  g7:EMAIL
  +1 FAX <Special>                         {0:M}  g7:FAX
  +1 WWW <Special>                         {0:M}  g7:WWW
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The repository record provides information about an institution or person that has a collection of sources.
Informal repositories include the owner of an unpublished work or of a rare published source, or a keeper of personal collections.
An example would be the owner of a family Bible containing unpublished family genealogical entries.

Layered repositories, such as an archive containing copies of a subset of records from another archive or archives that have moved or been bought by other archives, are not modeled in this version of the specification.
It is expected they will be added in a later version.
Until such time, it is recommended that the repository record store current contact information, if known.


#### `SHARED_NOTE_RECORD` :=

```gedstruct
n @XREF:SNOTE@ SNOTE <Text>                {1:1}  g7:record-SNOTE
  +1 MIME <MediaType>                      {0:1}  g7:MIME
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TRAN <Text>                           {0:M}  g7:NOTE-TRAN
     +2 MIME <MediaType>                   {0:1}  g7:MIME
     +2 LANG <Language>                    {0:1}  g7:LANG
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

A catch-all location for information that does not fully fit within other structures.
It may include research notes, additional context, alternative interpretations, reasoning, and so forth.

A shared note record may be pointed to by multiple other structures. Shared notes should only be used if editing the note in one place should edit it in all other places. If each instance of the note may be edited separately, a `NOTE` should be used instead.

Each [`SNOTE`.`TRAN`](#NOTE-TRAN) must have either a `MIME` or `LANG` substructure or both.

:::example
The origin of a name might be a reasonable shared note, while the reason a particular person was given that name may make more sense as a non-shared note.

```gedcom
0 @GORDON@ SNOTE "Gordon" is a traditional Scottish surname.
1 CONT It became a given name in honor of Charles George Gordon.
1 SOUR @VOID@
2 NOTE https://en.wikipedia.org/wiki/Gordon_(given_name)
0 @I1@ INDI
1 NAME Gordon /Jones/
2 NOTE Named after the astronaut Gordon Cooper
2 SNOTE @GORDON@
```
:::

:::note
The ability to have multiple structures share a single note using pointers was introduced in version 5.0 in 1991.
However, as of 2021 relatively few applications have a user interface that presents shared notes as such to users. It is recommended that `SNOTE` be avoided when `NOTE` will suffice.
:::

A `SHARED_NOTE_RECORD` may contain a pointer to a `SOURCE_RECORD` and vice versa. Applications must not create datasets where these mutual pointers form a cycle. Applications should also ensure they can handle invalid files with such cycles in a safe manner.


#### `SOURCE_RECORD` :=

```gedstruct
n @XREF:SOUR@ SOUR                         {1:1}  g7:record-SOUR
  +1 DATA                                  {0:1}  g7:DATA
     +2 EVEN <List:Enum>                   {0:M}  g7:DATA-EVEN
        +3 DATE <DatePeriod>               {0:1}  g7:DATA-EVEN-DATE
           +4 PHRASE <Text>                {0:1}  g7:PHRASE
        +3 <<PLACE_STRUCTURE>>             {0:1}
     +2 AGNC <Text>                        {0:1}  g7:AGNC
     +2 <<NOTE_STRUCTURE>>                 {0:M}
  +1 AUTH <Text>                           {0:1}  g7:AUTH
  +1 TITL <Text>                           {0:1}  g7:TITL
  +1 ABBR <Text>                           {0:1}  g7:ABBR
  +1 PUBL <Text>                           {0:1}  g7:PUBL
  +1 TEXT <Text>                           {0:1}  g7:TEXT
     +2 MIME <MediaType>                   {0:1}  g7:MIME
     +2 LANG <Language>                    {0:1}  g7:LANG
  +1 <<SOURCE_REPOSITORY_CITATION>>        {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

A source record describes an entire source.
A source may also point to `REPO`s to describe repositories or archives where the source document may be found.
The part of a source relevant to a specific fact, such as a specific page or entry, is indicated in a `SOURCE_CITATION` that points to the source record.

:::note
This sourcing model is known to be insufficient for some use cases and may be refined in a future version of this specification.
:::

A `SOURCE_RECORD` may contain a pointer to a `SHARED_NOTE_RECORD` and vice versa. Applications must not create datasets where these mutual pointers form a cycle. Applications should also ensure they can handle invalid files with such cycles in a safe manner.

#### `SUBMITTER_RECORD` :=

```gedstruct
n @XREF:SUBM@ SUBM                         {1:1}  g7:record-SUBM
  +1 NAME <Text>                           {1:1}  g7:NAME
  +1 <<ADDRESS_STRUCTURE>>                 {0:1}
  +1 PHON <Special>                        {0:M}  g7:PHON
  +1 EMAIL <Special>                       {0:M}  g7:EMAIL
  +1 FAX <Special>                         {0:M}  g7:FAX
  +1 WWW <Special>                         {0:M}  g7:WWW
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 LANG <Language>                       {0:M}  g7:SUBM-LANG
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The submitter record identifies an individual or organization that contributed information contained in the dataset.
All records in the document are assumed to be contributed by the
submitter referenced in the `HEAD`,
unless a `SUBM` structure inside a specific record points at a different submitter record.

### Substructures

#### `ADDRESS_STRUCTURE` :=

```gedstruct
n ADDR <Special>                           {1:1}  g7:ADDR
  +1 ADR1 <Special>                        {0:1}  g7:ADR1
  +1 ADR2 <Special>                        {0:1}  g7:ADR2
  +1 ADR3 <Special>                        {0:1}  g7:ADR3
  +1 CITY <Special>                        {0:1}  g7:CITY
  +1 STAE <Special>                        {0:1}  g7:STAE
  +1 POST <Special>                        {0:1}  g7:POST
  +1 CTRY <Special>                        {0:1}  g7:CTRY
```

A specific building, plot, or location.
The payload is the full formatted address as it would appear on a mailing label, including appropriate line breaks (encoded using `CONT` tags).
The expected order of address components varies by region; the address should be organized as expected by the addressed region.

Optionally, additional substructures such as `STAE` and `CTRY` are provided to be used by systems that have structured their addresses for indexing and sorting. If the substructures and `ADDR` payload disagree, the `ADDR` payload shall be taken as correct.
Because the regionally-correct order and formatting of address components cannot be determined from the substructures alone, the `ADDR` payload is required, even if its content appears to be redundant with the substructures.


#### `ASSOCIATION_STRUCTURE` :=

```gedstruct
n ASSO @<XREF:INDI>@                       {1:1}  g7:ASSO
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
  +1 ROLE <Enum>                           {1:1}  g7:ROLE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
```

An individual associated with the subject of the superstructure.
The nature of the association is indicated in the `ROLE` substructure.

A `voidPtr` and `PHRASE` can be used to describe associations to people not referenced by any `INDI` record.

:::example
The following indicates that "Mr Stockdale" was the individual's teacher
and that individual `@I2@` was the clergy officiating at their baptism.

```gedcom
0 @I1@ INDI
1 ASSO @VOID@
2 PHRASE Mr Stockdale
2 ROLE OTHER
3 PHRASE Teacher
1 BAPM
2 DATE 1930
2 ASSO @I2@
3 ROLE CLERGY
```
:::

#### `CHANGE_DATE` :=

```gedstruct
n CHAN                                     {1:1}  g7:CHAN
  +1 DATE <DateExact>                      {1:1}  g7:DATE-exact
     +2 TIME <Time>                        {0:1}  g7:TIME
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

The date of the most recent modification of the superstructure, optionally with notes about that modification.

The `NOTE` substructure may describe previous changes as well as the most recent, although only the most recent change is described by the `DATE` substructure.

#### `CREATION_DATE` :=

```gedstruct
n CREA                                     {1:1}  g7:CREA
  +1 DATE <DateExact>                      {1:1}  g7:DATE-exact
     +2 TIME <Time>                        {0:1}  g7:TIME
```

The date of the initial creation of the superstructure.
Because this refers to the initial creation, it should not be modified after the structure is created.

#### `EVENT_DETAIL` :=

```gedstruct
n DATE <DateValue>                         {0:1}  g7:DATE
  +1 TIME <Time>                           {0:1}  g7:TIME
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
n <<PLACE_STRUCTURE>>                      {0:1}
n <<ADDRESS_STRUCTURE>>                    {0:1}
n PHON <Special>                           {0:M}  g7:PHON
n EMAIL <Special>                          {0:M}  g7:EMAIL
n FAX <Special>                            {0:M}  g7:FAX
n WWW <Special>                            {0:M}  g7:WWW
n AGNC <Text>                              {0:1}  g7:AGNC
n RELI <Text>                              {0:1}  g7:RELI
n CAUS <Text>                              {0:1}  g7:CAUS
n RESN <List:Enum>                         {0:1}  g7:RESN
n SDATE <DateValue>                        {0:1}  g7:SDATE
  +1 TIME <Time>                           {0:1}  g7:TIME
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
n <<ASSOCIATION_STRUCTURE>>                {0:M}
n <<NOTE_STRUCTURE>>                       {0:M}
n <<SOURCE_CITATION>>                      {0:M}
n <<MULTIMEDIA_LINK>>                      {0:M}
n UID <Special>                            {0:M}  g7:UID
```

Substructures that may be shared by most individual and family events and attributes.

Note that many of these substructures are limited to 1 per event.
Conflicting event information should be represented by placing them in separate event structures (with appropriate source citations) rather than by placing them under the same enclosing event.

#### `FAMILY_ATTRIBUTE_STRUCTURE` :=

```gedstruct
[
n NCHI <Integer>                           {1:1}  g7:FAM-NCHI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n RESI <Text>                              {1:1}  g7:FAM-RESI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n FACT <Text>                              {1:1}  g7:FAM-FACT
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
]
```

Family attributes; see [Family Attributes](#family-attributes) for more.

:::note
Family attribute structures vary as follows:

- `FAM`.`NCHI` has an [Integer](#integer) payload; others have [Text](#text) payloads
- `FAM`.`FACT` requires `TYPE`; it's optional for others
:::


#### `FAMILY_EVENT_DETAIL` :=

```gedstruct
n HUSB                                     {0:1}  g7:HUSB
  +1 AGE <Age>                             {1:1}  g7:AGE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
n WIFE                                     {0:1}  g7:WIFE
  +1 AGE <Age>                             {1:1}  g7:AGE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
n <<EVENT_DETAIL>>                         {0:1}
```

Substructures shared by most family events and attributes.

#### `FAMILY_EVENT_STRUCTURE` :=

```` {.gedstruct .long}
[
n ANUL [Y|<NULL>]                          {1:1}  g7:ANUL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n CENS [Y|<NULL>]                          {1:1}  g7:FAM-CENS
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n DIV [Y|<NULL>]                           {1:1}  g7:DIV
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n DIVF [Y|<NULL>]                          {1:1}  g7:DIVF
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n ENGA [Y|<NULL>]                          {1:1}  g7:ENGA
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARB [Y|<NULL>]                          {1:1}  g7:MARB
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARC [Y|<NULL>]                          {1:1}  g7:MARC
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARL [Y|<NULL>]                          {1:1}  g7:MARL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARS [Y|<NULL>]                          {1:1}  g7:MARS
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARR [Y|<NULL>]                          {1:1}  g7:MARR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n EVEN <Text>                              {1:1}  g7:FAM-EVEN
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
]
````

Family events; see [Family Events](#family-events) for more.

An event structure may be used to discuss an event even if the event is not known to have occurred.
See [Events] for a discussion of how `DATE`, `PLAC`, and the optional `Y` payload indicate whether the structure is asserting the event occurred.
See the `NON_EVENT_STRUCTURE` for how to state an event did not occur.

:::note
Family event structures vary as follows:

- `FAM`.`EVEN` has a [Text](#text) payload; others may have a `Y` payload
- `FAM`.`EVEN` requires `TYPE`; it's optional for others
:::


#### `IDENTIFIER_STRUCTURE` :=

```gedstruct
[
n REFN <Special>                           {1:1}  g7:REFN
  +1 TYPE <Text>                           {0:1}  g7:TYPE
|
n UID <Special>                            {1:1}  g7:UID
|
n EXID <Special>                           {1:1}  g7:EXID
  +1 TYPE <Special>                        {0:1}  g7:EXID-TYPE
]
```

Each of these provides an identifier for a structure or its subject,
and each is different in purpose:

- `REFN` is a user-generated identifier for a structure.

- `UID` is a globally-unique identifier for a structure.

- `EXID` is an identifier maintained by an external authority that applies to the subject of the structure.

#### `INDIVIDUAL_ATTRIBUTE_STRUCTURE` :=

```` {.gedstruct .long}
[
n CAST <Text>                              {1:1}  g7:CAST
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n DSCR <Text>                              {1:1}  g7:DSCR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n EDUC <Text>                              {1:1}  g7:EDUC
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n IDNO <Special>                           {1:1}  g7:IDNO
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NATI <Text>                              {1:1}  g7:NATI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NCHI <Integer>                           {1:1}  g7:INDI-NCHI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NMR <Integer>                            {1:1}  g7:NMR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n OCCU <Text>                              {1:1}  g7:OCCU
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n PROP <Text>                              {1:1}  g7:PROP
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n RELI <Text>                              {1:1}  g7:INDI-RELI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n RESI <Text>                              {1:1}  g7:INDI-RESI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n SSN <Special>                            {1:1}  g7:SSN
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n TITL <Text>                              {1:1}  g7:INDI-TITL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n FACT <Text>                              {1:1}  g7:INDI-FACT
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
]
````

Individual attributes; see [Individual Attributes](#individual-attributes) for more.

:::note
Individual attribute structures vary as follows:

- `INDI`.`NCHI` and `NMR` have [Integer](#text) payloads; `IDNO` and `SSN` have [Special](#special) payloads; others have [Text](#text) payloads
- `INDI`.`FACT` and `IDNO` require `TYPE`; it's optional for others
:::

#### `INDIVIDUAL_EVENT_DETAIL` :=

```gedstruct
n <<EVENT_DETAIL>>                         {1:1}
n AGE <Age>                                {0:1}  g7:AGE
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
```

Substructures shared by most individual events and attributes.

#### `INDIVIDUAL_EVENT_STRUCTURE` :=

```` {.gedstruct .long}
[
n BAPM [Y|<NULL>]                          {1:1}  g7:BAPM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BARM [Y|<NULL>]                          {1:1}  g7:BARM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BASM [Y|<NULL>]                          {1:1}  g7:BASM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BLES [Y|<NULL>]                          {1:1}  g7:BLES
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BURI [Y|<NULL>]                          {1:1}  g7:BURI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CENS [Y|<NULL>]                          {1:1}  g7:INDI-CENS
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CHRA [Y|<NULL>]                          {1:1}  g7:CHRA
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CONF [Y|<NULL>]                          {1:1}  g7:CONF
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CREM [Y|<NULL>]                          {1:1}  g7:CREM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n DEAT [Y|<NULL>]                          {1:1}  g7:DEAT
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n EMIG [Y|<NULL>]                          {1:1}  g7:EMIG
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n FCOM [Y|<NULL>]                          {1:1}  g7:FCOM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n GRAD [Y|<NULL>]                          {1:1}  g7:GRAD
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n IMMI [Y|<NULL>]                          {1:1}  g7:IMMI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NATU [Y|<NULL>]                          {1:1}  g7:NATU
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n ORDN [Y|<NULL>]                          {1:1}  g7:ORDN
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n PROB [Y|<NULL>]                          {1:1}  g7:PROB
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n RETI [Y|<NULL>]                          {1:1}  g7:RETI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n WILL [Y|<NULL>]                          {1:1}  g7:WILL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n ADOP [Y|<NULL>]                          {1:1}  g7:ADOP
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:ADOP-FAMC
     +2 ADOP <Enum>                        {0:1}  g7:FAMC-ADOP
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
|
n BIRT [Y|<NULL>]                          {1:1}  g7:BIRT
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:FAMC
|
n CHR [Y|<NULL>]                           {1:1}  g7:CHR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:FAMC
|
n EVEN <Text>                              {1:1}  g7:INDI-EVEN
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
]
````

Individual events; see [Individual Events](#individual-events) for more.

An event structure may be used to discuss an event even if the event is not known to have occurred.
See [Events] for a discussion of how `DATE`, `PLAC`, and the optional `Y` payload indicate whether the structure is asserting the event occurred.
See the `NON_EVENT_STRUCTURE` for how to state an event did not occur.

:::note
Individual event structures vary as follows:

- `INDI`.`EVEN` has a [Text](#text) payload; others may have a `Y` payload
- `INDI`.`EVEN` requires `TYPE`; it's optional for others
- `BIRT` and `CHR` may have a `FAMC` with no substructures; `ADOP` may have a `FAMC` with an optional `ADOP` substructure; others may not have a `FAMC` substructure
:::



#### `LDS_INDIVIDUAL_ORDINANCE` :=

```gedstruct
[
n BAPL                                     {1:1}  g7:BAPL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n CONL                                     {1:1}  g7:CONL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n ENDL                                     {1:1}  g7:ENDL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n INIL                                     {1:1}  g7:INIL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n SLGC                                     {1:1}  g7:SLGC
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
  +1 FAMC @<XREF:FAM>@                     {1:1}  g7:FAMC
]
```

Ordinances performed by members of The Church of Jesus Christ of Latter-day Saints; see [Latter-day Saint Ordinances] for more.

#### `LDS_ORDINANCE_DETAIL` :=

```gedstruct
n DATE <DateValue>                       {0:1}  g7:DATE
  +1 TIME <Time>                         {0:1}  g7:TIME
  +1 PHRASE <Text>                       {0:1}  g7:PHRASE
n TEMP <Text>                            {0:1}  g7:TEMP
n <<PLACE_STRUCTURE>>                    {0:1}
n STAT <Enum>                            {0:1}  g7:ord-STAT
  +1 DATE <DateExact>                    {1:1}  g7:DATE-exact
     +2 TIME <Time>                      {0:1}  g7:TIME
n <<NOTE_STRUCTURE>>                     {0:M}
n <<SOURCE_CITATION>>                    {0:M}
```

Dates for these ordinances should be in the default (`GREGORIAN`) calendar and be 1830 or later.
These ordinances can be performed posthumously by proxy, and the date may reflect that posthumous date.

#### `LDS_SPOUSE_SEALING` :=

```gedstruct
n SLGS                                     {1:1}  g7:SLGS
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
```

Ordinances performed by members of The Church of Jesus Christ of Latter-day Saints; see [Latter-day Saint Ordinances] for more.

#### `MULTIMEDIA_LINK` :=
```gedstruct
n OBJE @<XREF:OBJE>@                       {1:1}  g7:OBJE
  +1 CROP                                  {0:1}  g7:CROP
     +2 TOP <Integer>                      {0:1}  g7:TOP
     +2 LEFT <Integer>                     {0:1}  g7:LEFT
     +2 HEIGHT <Integer>                   {0:1}  g7:HEIGHT
     +2 WIDTH <Integer>                    {0:1}  g7:WIDTH
  +1 TITL <Text>                           {0:1}  g7:TITL
```

Links the superstructure to the `MULTIMEDIA_RECORD` with the given pointer.

The optional `CROP` substructure indicates that a subregion of an image represents or applies to the superstructure.

The optional `TITL` substructure supersedes any `OBJE.FILE.TITL` substructures included in the `MULTIMEDIA_RECORD`.

#### `NON_EVENT_STRUCTURE` :=

```gedstruct
n NO <Enum>                                {1:1}  g7:NO
  +1 DATE <DatePeriod>                     {0:1}  g7:NO-DATE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
```

Indicates that a specific type of event, given in the payload, did not happen within a given date period
(or never happened if there is no `DATE` substructure).

Substructures may provide discussion about the non-occurrence of the event
but must not limit the meaning of what did not occur.
No substructure other than `DATE` may restrict the breadth of that negative assertion.

:::example
`1 NO MARR`{.gedcom} means "no marriage occurred"
:::

:::example
```gedcom
1 NO MARR
2 DATE TO 24 MAR 1880
```
means "no marriage had occurred as of March 24^th^, 1880"
:::

#### `NOTE_STRUCTURE` :=

```gedstruct
[
n NOTE <Text>                              {1:1}  g7:NOTE
  +1 MIME <MediaType>                      {0:1}  g7:MIME
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TRAN <Text>                           {0:1}  g7:NOTE-TRAN
     +2 MIME <MediaType>                   {0:1}  g7:MIME
     +2 LANG <Language>                    {0:1}  g7:LANG
  +1 <<SOURCE_CITATION>>                   {0:M}
|
n SNOTE @<XREF:SNOTE>@                     {1:1}  g7:SNOTE
]
```

A catch-all location for information that does not fully fit within other structures.
It may include research notes, additional context, alternative interpretations, reasoning, and so forth.

Each `NOTE`.`TRAN` must have either a `MIME` or `LANG` substructure, and may have both.

See `SHARED_NOTE_RECORD` for advice on choosing between `NOTE` and `SNOTE`.

:::note
Although notes may be tagged with the language that they are written in, this specification does not provide a mechanism for distinguishing between notes with distinct content in distinct languages versus notes with the same content translated into distinct languages. It is expected that a future version of this specification will provide a mechanism for a single note to have multiple language translations.

The same is true for `MIME`: notes differing in `MIME` may contain the same content in a different format or contain distinct content, and this document provides no mechanism for distinguishing those cases.
:::

A `NOTE_STRUCTURE` can contain a `SOURCE_CITATION`, which in turn can contain a `NOTE_STRUCTURE`, allowing potentially unbounded nesting of structures. Because each dataset is finite, this nesting is also guaranteed to be finite.



#### `PERSONAL_NAME_PIECES` :=

```gedstruct
n NPFX <Text>                              {0:M}  g7:NPFX
n GIVN <Text>                              {0:M}  g7:GIVN
n NICK <Text>                              {0:M}  g7:NICK
n SPFX <Text>                              {0:M}  g7:SPFX
n SURN <Text>                              {0:M}  g7:SURN
n NSFX <Text>                              {0:M}  g7:NSFX
```

Optional isolated name parts; see `PERSONAL_NAME_STRUCTURE` for more.

:::example
"Lt. Cmndr. Joseph Allen jr.” might be presented as

```gedcom
1 NAME Lt. Cmndr. Joseph /Allen/ jr.
2 NPFX Lt. Cmndr.
2 GIVN Joseph
2 SURN Allen
2 NSFX jr.
```
:::

#### `PERSONAL_NAME_STRUCTURE` :=

```gedstruct
n NAME <PersonalName>                      {1:1}  g7:INDI-NAME
  +1 TYPE <Enum>                           {0:1}  g7:NAME-TYPE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<PERSONAL_NAME_PIECES>>              {0:1}
  +1 TRAN <PersonalName>                   {0:M}  g7:NAME-TRAN
     +2 LANG <Language>                    {1:1}  g7:LANG
     +2 <<PERSONAL_NAME_PIECES>>           {0:1}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
```

Names of individuals are represented in the manner the name is normally spoken, with the family name, surname, or nearest cultural parallel thereunto separated by slashes (U+002F `/`). Based on the dynamic nature or unknown compositions of naming conventions, it is difficult to provide a more detailed name piece structure to handle every case. The `PERSONAL_NAME_PIECES` are provided optionally for systems that cannot operate effectively with less structured information. The Personal Name payload shall be seen as the primary name representation, with name pieces as optional auxiliary information.

The name may be translated or transliterated into different languages or scripts using the `TRAN` substructure.
It is recommended, but not required, that if the name pieces are used, the same pieces are used in each translation and transliteration.

A `TYPE` is used to specify the particular variation that this name is.
For example; it could indicate that this name is a name taken at immigration or that it could be an ‘also known as’ name.
See [the NAME.TYPE enumeration](#enum-TYPE) for more.

:::note
Alternative approaches to representing names are being considered for future versions of this specification.
:::

#### `PLACE_STRUCTURE` :=

```gedstruct
n PLAC <List:Text>                         {1:1}  g7:PLAC
  +1 FORM <List:Text>                      {0:1}  g7:PLAC-FORM
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TRAN <List:Text>                      {0:M}  g7:PLAC-TRAN
     +2 LANG <Language>                    {1:1}  g7:LANG
  +1 MAP                                   {0:1}  g7:MAP
     +2 LATI <Special>                     {1:1}  g7:LATI
     +2 LONG <Special>                     {1:1}  g7:LONG
  +1 EXID <Special>                        {0:M}  g7:EXID
     +2 TYPE <Special>                     {0:1}  g7:EXID-TYPE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

A place, which can be represented in several ways:

- The payload contains a comma-separated list of region names,
    ordered from smallest to largest.
    The specific meaning of each element is given by the `FORM` substructure,
    or in the `HEAD`.`PLAC`.`FORM` if there is no `FORM` substructure.
    Elements should be left blank if they are unknown, do not apply to the location, or are too specific for the region in question.

    <div class="example">
    A record describing births throughout Oneida county could be recorded as

    ````gedcom
    0 @S1@ SOUR
    1 DATA
    2 EVEN BIRT
    3 PLAC , Oneida, Idaho, USA
    4 FORM City, County, State, Country
    ````
    </div>

- The payload may be translated or transliterated into different languages or scripts using the `TRAN` substructure.
    It should use the same `FORM` as the payload.

- Global coordinates may be presented in the `MAP` substructure

:::note
This specification does not support places where a region name contains a comma. An alternative system for representing locations is likely to be added in a later version.
:::

#### `SOURCE_CITATION` :=

```gedstruct
n SOUR @<XREF:SOUR>@                       {1:1}  g7:SOUR
  +1 PAGE <Text>                           {0:1}  g7:PAGE
  +1 DATA                                  {0:1}  g7:SOUR-DATA
     +2 DATE <DateValue>                   {0:1}  g7:DATE
        +3 TIME <Time>                     {0:1}  g7:TIME
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
     +2 TEXT <Text>                        {0:M}  g7:TEXT
        +3 MIME <MediaType>                {0:1}  g7:MIME
        +3 LANG <Language>                 {0:1}  g7:LANG
  +1 EVEN <Enum>                           {0:1}  g7:SOUR-EVEN
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
     +2 ROLE <Enum>                        {0:1}  g7:ROLE
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
  +1 QUAY <Enum>                           {0:1}  g7:QUAY
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

A citation indicating that the pointed-to source record supports the claims made in the superstructure.
Substructures provide additional information about how that source applies to the subject of the citation's superstructure:

- `PAGE`: where in the source the relevant material can be found.
- `DATA`: the relevant data from the source.
- `EVEN`: what event the relevant material was recording.
- `QUAY`: an estimation of the reliability of the source in regard to these claims.
- `MULTIMEDIA_LINK`: digital copies of the cited part of the source

When no source record is available, a `voidPtr` and accompanying `NOTE` can be used to describe the source.

:::example
```gedcom
1 DSCR Tall enough his head touched the ceiling
2 SOUR @VOID@
3 NOTE His grand-daughter Lydia told me this in 1980
```
:::

A `SOURCE_CITATION` can contain a `NOTE_STRUCTURE`, which in turn can contain a `SOURCE_CITATION`, allowing potentially unbounded nesting of structures. Because each dataset is finite, this nesting is also guaranteed to be finite.


#### `SOURCE_REPOSITORY_CITATION` :=

```gedstruct
n REPO @<XREF:REPO>@                       {1:1}  g7:REPO
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 CALN <Special>                        {0:M}  g7:CALN
     +2 MEDI <Enum>                        {0:1}  g7:MEDI
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
```

This structure is used within a source record to point to a name and address record of the holder of the source document.
Formal and informal repository name and addresses are stored in the
`REPOSITORY_RECORD`.
More formal repositories, such as the Family History Library, should show a call number of the source at that repository.
The call number of that source should be recorded using a `CALN` substructure.



## Structure Meaning

### Events

As a general rule, events are things that happen on a specific date.
Use the `dateRange` form to indicate that an event took place at some time between 2 dates.
In most cases, a `DatePeriod` is inappropriate for an event; if the subject of your recording occurred over a period of time, then it is probably not an event, but rather an attribute.

Event structures can be used to record notes about an event without asserting the event actually occurred.
An event structure asserts the event did occur if any of the following are true:

- There is a `DATE` substructure

    <div class="example">

    ````gedcom
    1 DEAT
    2 DATE 2 OCT 1937
    ````
    
    </div>

- There is a `PLAC` substructure
    
    <div class="example">

    ````gedcom
    1 DEAT
    2 PLAC Cove, Cache, Utah
    ````

    </div>

- The event has a payload.
    A special payload `Y` can be used with some event types to indicate that the event is known to have occurred without providing any additional information about it.
    
    <div class="example">
    
    ````gedcom
    1 DEAT Y
    ````
    
    </div>

If none of the above are true, the structure should be seen as a place for inconclusive research notes about the possibility of the event.
An assertion that an event did not occur should be encoded using the `NO` structure.

#### Individual Events

Tag | Name<br/>URI | Description
--- | ---- | -----------
`ADOP` | adoption<br/>`g7:ADOP` | Creation of a legally approved child-parent relationship that does not exist biologically.
`BAPM` | baptism<br/>`g7:BAPM` | Baptism, performed in infancy or later. (See also [`BAPL`](#latter-day-saint-ordinances) and `CHR`.)
`BARM` | Bar Mitzvah<br/>`g7:BARM` | The ceremonial event held when a Jewish boy reaches age 13.
`BASM` | Bas Mitzvah<br/>`g7:BASM` | The ceremonial event held when a Jewish girl reaches age 13, also known as "Bat Mitzvah."
`BIRT` | birth<br/>`g7:BIRT` | Entering into life.
`BLES` | blessing<br/>`g7:BLES` | Bestowing divine care or intercession. Sometimes given in connection with a naming ceremony.
`BURI` | burial<br/>`g7:BURI` | Disposing of the mortal remains of a deceased person.
`CENS` | census<br/>`g7:INDI-CENS` | Periodic count of the population for a designated locality, such as a national or state census.
`CHR` | christening<br/>`g7:CHR` | Baptism or naming events for a child.
`CHRA` | adult christening<br/>`g7:CHRA` | Baptism or naming events for an adult person.
`CONF` | confirmation<br/>`g7:CONF` | Conferring full church membership.
`CREM` | cremation<br/>`g7:CREM` | Disposal of the remains of a person's body by fire.
`DEAT` | death<br/>`g7:DEAT` | Mortal life terminates.
`EMIG` | emigration<br/>`g7:EMIG` | Leaving one's homeland with the intent of residing elsewhere.
`FCOM` | first communion<br/>`g7:FCOM` | The first act of sharing in the Lord's supper as part of church worship.
`GRAD` | graduation<br/>`g7:GRAD` | Awarding educational diplomas or degrees to individuals.
`IMMI` | immigration<br/>`g7:IMMI` | Entering into a new locality with the intent of residing there.
`NATU` | naturalization<br/>`g7:NATU` | Obtaining citizenship.
`ORDN` | ordination<br/>`g7:ORDN` | Receiving authority to act in religious matters.
`PROB` | probate<br/>`g7:PROB` | Judicial determination of the validity of a will. It may indicate several related court activities over several dates.
`RETI` | retirement<br/>`g7:RETI` | Exiting an occupational relationship with an employer after a qualifying time period.
`WILL` | will<br/>`g7:WILL` | A legal document treated as an event, by which a person disposes of his or her estate. It takes effect after death. The event date is the date the will was signed while the person was alive. (See also `PROB`)

In addition, `INDI`.`EVEN` is a structure for a generic individual event. It must have a `TYPE` substructure to define what kind of event is being provided.

#### Family Events

Tag | Name<br/>URI | Description
--- | ---- | -----------
`ANUL` | annulment<br/>`g7:ANUL` | Declaring a marriage void from the beginning (never existed).
`CENS` | census<br/>`g7:FAM-CENS` | Periodic count of the population for a designated locality, such as a national or state census.
`DIV` | divorce<br/>`g7:DIV` | Dissolving a marriage through civil action.
`DIVF` | divorce filed<br/>`g7:DIVF` | Filing for a divorce by a spouse.
`ENGA` | engagement<br/>`g7:ENGA` | Recording or announcing an agreement between 2 people to become married.
`MARB` | marriage bann<br/>`g7:MARB` | Official public notice given that 2 people intend to marry.
`MARC` | marriage contract<br/>`g7:MARC` | Recording a formal agreement of marriage, including the prenuptial agreement in which marriage partners reach agreement about the property rights of 1 or both, securing property to their children.
`MARL` | marriage license<br/>`g7:MARL` | Obtaining a legal license to marry.
`MARR` | marriage<br/>`g7:MARR` | A legal, common-law, or customary event such as a wedding or marriage ceremony that joins 2 partners to create or extend a family unit.
`MARS` | marriage settlement<br/>`g7:MARS` | Creating an agreement between 2 people contemplating marriage, at which time they agree to release or modify property rights that would otherwise arise from the marriage.

In addition, `FAM`.`EVEN` is a structure for a generic family event. It must have a `TYPE` substructure to define what kind of event is being provided.


### Attributes

Unlike events, the presence of an attribute is sufficient to assert the attribute applied to the individual, regardless of the attribute's substructures and payload.

#### Individual Attributes

Tag | Name<br/>URI | Description
--- | ---- | -----------
`CAST` | caste<br/>`g7:CAST` | The name of an individual's rank or status in society which is sometimes based on racial or religious differences, or differences in wealth, inherited rank, profession, or occupation.
`DSCR` | physical description<br/>`g7:DSCR` | The physical characteristics of a person.
`EDUC` | education<br/>`g7:EDUC` | Indicator of a level of education attained.
`IDNO` | identifying number<br/>`g7:IDNO` | A number or other string assigned to identify a person within some significant external system. It must have a `TYPE` substructure to define what kind of identification number is being provided.
`NATI` | nationality<br/>`g7:NATI` | The national heritage of an individual.
`NCHI` | number of children<br/>`g7:INDI-NCHI` | The number of children that this person is known to be the parent of (all marriages).
`NMR` | number of marriages<br/>`g7:NMR` | The number of times this person has participated in a family as a spouse or parent.
`OCCU` | occupation<br/>`g7:OCCU` | The type of work or profession of an individual.
`PROP` | property<br/>`g7:PROP` | Pertaining to possessions such as real estate or other property of interest.
`RELI` | religion<br/>`g7:INDI-RELI` | A religious denomination to which a person is affiliated or for which a record applies.
`RESI` | residence<br/>`g7:INDI-RESI` | An address or place of residence where an individual resided.
`SSN` | social security number<br/>`g7:SSN` | A number assigned by the United States Social Security Administration, used for tax identification purposes. It is a type of `IDNO`.
`TITL` | title<br/>`g7:INDI-TITL` | A formal designation used by an individual in connection with positions of royalty or other social status, such as Grand Duke.

In addition, `INDI`.`FACT` is a structure for a generic individual attribute. It must have a `TYPE` substructure to define what kind of attribute is being provided.

#### Family Attributes

Tag | Name<br/>URI | Description
----|--------------|-----------------
`NCHI` | number of children<br/>`g7:FAM-NCHI` | The number of children that belong to this family.
`RESI` | residence<br/>`g7:FAM-RESI` | An address or place of residence where a family resided.

In addition, `FAM`.`FACT` is a structure for a generic family attribute. It must have a `TYPE` substructure to define what kind of attribute is being provided.

### Latter-day Saint Ordinances

The structures describing ordinances performed by The Church of Jesus Christ of Latter-day Saints are unlike regular events in that they might either be performed during life or by proxy on the behalf of a deceased individual.

Proxy ordinances on behalf of deceased persons were once requested and officially recorded using an earlier version of GDCOM.
This is no longer the case, but when it was the case the following principles held:

- `PLAC` was used only for ordinances that were performed by the recipient in life.
- `TEMP` was used with all `ENDL`, `SLGC`, and `SLGS`, but only with posthumous proxy `BAPL` and `CONL`.


Tag | Name<br/>URI | Description
----|------|-----------------
`BAPL` | baptism<br/>`g7:BAPL` | The event of baptism performed at age 8 or later by priesthood authority of The Church of Jesus Christ of Latter-day Saints. (See also [`BAPM`](#individual-events))
`CONL` | confirmation<br/>`g7:CONL` | The religious event by which a person receives membership in The Church of Jesus Christ of Latter-day Saints. (See also [`CONF`](#individual-events))
`INIL` | initiatory<br/>`g7:INIL` | A religious event where an initiatory ordinance for an individual was performed by priesthood authority in a temple of The Church of Jesus Christ of Latter-day Saints.
`ENDL` | endowment<br/>`g7:ENDL` | A religious event where an endowment ordinance for an individual was performed by priesthood authority in a temple of The Church of Jesus Christ of Latter-day Saints.
`SLGC` | sealing child<br/>`g7:SLGC` | A religious event pertaining to the sealing of a child to his or her parents in a temple ceremony of The Church of Jesus Christ of Latter-day Saints.
`SLGS` | sealing spouse<br/>`g7:SLGS` | A religious event pertaining to the sealing of a husband and wife in a temple ceremony of The Church of Jesus Christ of Latter-day Saints. (See also [`MARR`](#family-events))



### Structure types

Strutures types are listed in this section alphabetically by tag.
When the same tag is used for different structure types in different contexts, they may be distinguished by their URI.

#### `ABBR` (Abbreviation) `g7:ABBR`

A short name of a title, description, or name used for sorting, filing, and retrieving records.

#### `ADDR` (Address) `g7:ADDR`

The location of, or most relevant to, the subject of the superstructure.
See `ADDRESS_STRUCTURE` for more.

#### `ADOP` (Adoption) `g7:ADOP`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `ADOP` (Adoption) `g7:FAMC-ADOP`

An [enumerated value](#enum-ADOP) indicating which parent(s) in the family adopted this individual.

#### `ADR1` (Address Line 1) `g7:ADR1`

The first line of the address, used for indexing.
This is the value of the line corresponding to the `ADDR` tag line in the address structure.
See `ADDRESS_STRUCTURE` for more.

#### `ADR2` (Address Line 2) `g7:ADR2`

The second line of the address, used for indexing.
This is the value of the first `CONT` line subordinate to the `ADDR` tag in the address structure.
See `ADDRESS_STRUCTURE` for more.

#### `ADR3` (Address Line 3) `g7:ADR3`

The third line of the address, used for indexing.
This is the value of the second `CONT` line subordinate to the `ADDR` tag in the address structure.
See `ADDRESS_STRUCTURE` for more.

#### `AGE` (Age at event) `g7:AGE`

The age of the individual at the time an event occurred, or the age listed in the document.

#### `AGNC` (Responsible agency) `g7:AGNC`

The organization, institution, corporation, person, or other entity that has responsibility for the associated context.
Examples are an employer of a person of an associated occupation, or a church that administered rites or events, or an organization responsible for creating or archiving records.

#### `ALIA` (Alias) `g7:ALIA`

A single individual may have facts distributed across multiple individual records, connected by `ALIA` pointers
(named after "alias" in the computing sense, not the pseudonym sense).

:::note
This specification does not define how to connect `INDI` records with `ALIA`.
Some systems organize `ALIA` pointers to create a tree structure, with the root `INDI` record containing the composite view of all facts in the leaf `INDI` records.
Others distribute events and attributes between `INDI` records mutually linked by symmetric pairs of `ALIA` pointers.
A future version of this specification may adjust the definition of `ALIA`.
:::

#### `ANCI` (Ancestor interest) `g7:ANCI`

Indicates an interest in additional research for ancestors of this individual.
(See also `DESI`).

#### `ANUL` (Annulment) `g7:ANUL`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `ASSO` (Associates) `g7:ASSO`

A pointer to an associated individual.
See `ASSOCIATION_STRUCTURE` for more.

#### `AUTH` (Author) `g7:AUTH`

The person, agency, or entity who created the record. For a published work, this could be the author, compiler, transcriber, abstractor, or editor. For an unpublished source, this may be an individual, a government agency, church organization, or private organization.

#### `BAPL` (Baptism, Latter-Day Saint) `g7:BAPL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `BAPM` (Baptism) `g7:BAPM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BARM` (Bar Mitzvah) `g7:BARM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BASM` (Bas Mitzvah) `g7:BASM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BRIT` (Birth) `g7:BIRT`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BLES` (Blessing) `g7:BLES`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BURI` (Burial) `g7:BURI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CALN` (Call number) `g7:CALN`

An identification or reference description used to file and retrieve items from the holdings of a repository.
Despite the word "number" in the name, may contain any character, not just digits.

#### `CAST` (Caste)  `g7:CAST`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `CAUS` (Cause) `g7:CAUS`

The reasons which precipitated an event.
It is often used subordinate to a death event to show cause of death, such as might be listed on a death certificate.

#### `CENS` (Census)  `g7:FAM-CENS`

An [Family Event](#family-events).

#### `CENS` (Census)  `g7:INDI-CENS`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CHAN` (Change) `g7:CHAN`

The most recent change to the superstructure.
This is metadata about the structure itself, not data about its subject.
See `CHANGE_DATE` for more.

#### `CHIL` (Child) `g7:CHIL`

The child in a family, whether biological, adopted, foster, sealed, or other relationship.

#### `CHRA` (Christening, adult)  `g7:CHRA`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CHR` (Christening)  `g7:CHR`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CITY` (City) `g7:CITY`

The name of the city used in the address.
See `ADDRESS_STRUCTURE` for more.

#### `CONF` (Confirmation)  `g7:CONF`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CONL` (Confirmation, Latter-Day Saint) `g7:CONL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `CONT` (Continued)

A pseudo-structure to indicate a line break.
See [Lines](#lines) for more.

#### `COPR` (Copyright) `g7:COPR`

A copyright statement, as appropriate for the copyright laws applicable to this data.

#### `CORP` (Corporate name) `g7:CORP`

The name of the business, corporation, or person that produced or commissioned the product.

#### `CREA` (Creation) `g7:CREA`

The initial creation of the superstructure.
This is metadata about the structure itself, not data about its subject.
See `CREATION_DATE` for more.

#### `CREM` (Cremation)  `g7:CREM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CROP` (Crop) `g7:CROP`

A subregion of an image to display.
It is only valid when the superstructure links to a `MULTIMEDIA_RECORD` with at least
1 `FILE` substructure that refers to an external file with a defined pixel unit.

`LEFT` and `TOP` indicate the top-left corner of the region to display.
`WIDTH` and `HEIGHT` indicate how many pixels wide and tall the region to display is.
If omitted, `LEFT` and `TOP` each default to 0;
`WIDTH` defaults to the image width minus `LEFT`;
and `HEIGHT` defaults to the image height minus `TOP`.

If the superstructure links to a `MULTIMEDIA_RECORD` that includes multiple `FILE`
substructures, the `CROP` applies to the first `FILE` to which it can apply,
namely the first external file with a defined pixel unit.

It is recommended that `CROP` be used only with a single-FILE `MULTIMEDIA_RECORD`.

The following are errors:

- `LEFT` or `LEFT` + `WIDTH` exceed the image width.
- `TOP` or `TOP` + `HEIGHT` exceed the image height.
- `CROP` applied to a non-image or image without a defined pixel unit.


#### `CTRY` (Country) `g7:CTRY`

The name of the country that pertains to the associated address.
See `ADDRESS_STRUCTURE` for more.

#### `DATA` (Data) `g7:DATA`

A structure with no payload used to distinguish a description of something from metadata about it.
For example, `SOUR` and its other substructures describe a source itself,
while `SOUR`.`DATA` describes the content of the source.

#### `DATA` (Data) `g7:SOUR-DATA`

See `g7:DATA`.

#### `DATA` (Data) `g7:HEAD-SOUR-DATA`

The electronic data source or digital repository from which this dataset was exported.
The payload is the name of that source,
with substructures providing additional details about the source (not the export).

#### `DATE` (Date) `g7:DATE`

The principal date of the subject of the superstructure.
The payload is a `DateValue`.

#### `DATE` (Date) `g7:DATE-exact`

The principal date of the subject of the superstructure.
The payload is a `DateExact`.

#### `DATE` (Date) `g7:HEAD-DATE`

The `DateExact` that this document was created.

#### `DATE` (Date) `g7:NO-DATE`

The `DatePeriod` during which the event did not occur or the attribute did not apply.

#### `DATE` (Date) `g7:DATA-EVEN-DATE`

The `DatePeriod` covered by the entire source; the period during which this source recorded events.

#### `DEAT` (Death) `g7:DEAT`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `DESI` (Descendant Interest) `g7:DESI`

Indicates an interest in research to identify additional descendants of this individual.
See also `ANCI`.

#### `DEST` (Destination) `g7:DEST`

An identifier for the system expected to receive this document.
See `HEAD`.`SOUR` for guidance on choosing identifiers.

#### `DIVF` (Divorce filing) `g7:DIVF`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `DIV` (Divorce) `g7:DIV`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `DSCR` (Description) `g7:DSCR`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `EDUC` (Description) `g7:EDUC`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `EMAIL` (Email) `g7:EMAIL`

An electronic mail address, as defined by any relevant standard
such as [RFC 3696](https://www.rfc-editor.org/info/rfc3696), [RFC 5321](https://www.rfc-editor.org/info/rfc5321), or [RFC 5322](https://www.rfc-editor.org/info/rfc5322).

If an invalid email address is present upon import, it should be preserved as-is on export.

:::note
The version 5.5.1 specification contained a typo where this tag was sometimes written `EMAI` and sometimes written `EMAIL`. `EMAIL` should be used in version 7.0 and later.
:::

#### `EMIG` (Description) `g7:EMIG`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `ENDL` (Endowment, Latter-Day Saint) `g7:ENDL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `ENGA` (Engagement) `g7:ENGA`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `EVEN` (Event) `g7:FAM-EVEN`

See `g7:INDI-EVEN`.

#### `EVEN` (Event) `g7:INDI-EVEN`

An event: a noteworthy happening related to an individual or family.
If a specific event type exists, it should be used instead of a generic `EVEN` structure.
Each `EVEN` must be classified by a subordinate use of the `TYPE` tag
and may be further described in the structure's payload.

:::example
A person that signed a lease for land dated October 2, 1837 and a lease for mining equipment dated November 4, 1837 would be written as:

```gedcom
0 @I1@ INDI
1 EVEN
2 TYPE Land Lease
2 DATE 2 OCT 1837
1 EVEN Mining equipment
2 TYPE Equipment Lease
2 DATE 4 NOV 1837
```
:::

#### `EVEN` (Event) `g7:DATA-EVEN`

A list of [enumerated values](#enum-EVEN) indicating the types of events that were recorded in a particular source.
Each event type is separated by a comma and space.
For example, a parish register of births, deaths, and marriages would be `BIRT, DEAT, MARR`.

#### `EVEN` (Event) `g7:SOUR-EVEN`

An [enumerated value](#enum-SOUR.EVEN) indicating the type of event or attribute which was responsible for the source entry being recorded.
For example, if the entry was created to record a birth of a child, then the type would be `BIRT` regardless of the assertions made from that record, such as the mother's name or mother's birth date.

#### `EXID` (External Identifier) `g7:EXID`

An identifier for the subject of the superstructure.
The identifier is maintained by some external authority;
the authority owning the identifier is provided in the TYPE substructure; see `EXID`.`TYPE` for more.

Depending on the maintaining authority, an `EXID` may be a unique identifier for the subject, an identifier for 1 of several views of the subject, or an identifier for the externally-maintained copy of the same information as is contained in this structure. However, unlike `UID` and `REFN`, `EXID` does not identify a structure; structures with the same `EXID` may have originated independently rather than by edits from the same starting point.

#### `FAM` (Family record) `g7:record-FAM`

See `FAMILY_RECORD`

#### `FACT` (Fact) `g7:FAM-FACT`

See `g7:INDI-FACT`.

#### `FACT` (Fact) `g7:INDI-FACT`

A noteworthy attribute or fact concerning an individual or family.
If a specific attribute type exists, it should be used instead of a generic `FACT` structure.
Each `FACT` must be classified by a subordinate use of the `TYPE` tag
and may be further described in the structure's payload.

:::example
If the attribute being defined was 1 of the person's skills, such as woodworking, the `FACT` tag would have the value of "Woodworking", followed by a subordinate `TYPE` tag with the value "Skills".

```gedcom
0 @I1@ INDI
1 FACT Woodworking
2 TYPE Skills
```
:::

#### `FAMC` (Family child) `g7:INDI-FAMC`

The family in which an individual appears as a child.
It is also used with a `STAT` substructure to show individuals who are not children of the family.
See `FAM` and `FAMC`.`STAT` for more.

#### `FAMC` (Family child) `g7:FAMC`

The family with which this individual event is associated.

#### `FAMC` (Family child) `g7:ADOP-FAMC`

The individual or couple that adopted this this individual.

Adoption by an individual, rather than a couple, may be represented either by pointing to a `FAM` where that individual is a `HUSB` or `WIFE` and using a `g7:FAMC-ADOP` substructure to indicate which 1 performed the adoption; or by using a `FAM` where the adopting individual is the only `HUSB`/`WIFE`.

#### `FAMS` (Family spouse) `g7:FAMS`

The family in which an individual appears as a partner.
See `FAM` for more.

#### `FAX` (Facsimile) `g7:FAX`

A fax telephone number appropriate for sending data facsimiles.
See `PHON` for more.

#### `FCOM` (First communion) `g7:FCOM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `FILE` (File reference) `g7:FILE`

A reference to an external file.
Syntactically, the payload is a URI reference as defined by [RFC 3986](https://www.rfc-editor.org/info/rfc3986), or a valid URL string as defined by the [WHATWG URL specification](https://url.spec.whatwg.org/).
That is, it can be an absolute or relative URL, optionally with a fragment string.
However, only the following URL types are used:

- A URL with scheme `ftp`, `http`, or `https` refers to a **web-accessible file**.

- A URL with scheme `file` refers to a **machine-local file** as defined by [RFC 8089](https://www.rfc-editor.org/info/rfc8089). Machine-local files must not be used in [FamilySearch GEDZIP](#gedzip) nor when sharing datasets on the web or with unknown parties, but may be used for close collaboration between parties with known similar file structures.

- A URI reference with all of the following:
    - no scheme
    - not beginning with `/` (U+002F)
    - not containing any path segments equal to `..` (U+002E U+002E)
    - not containing a reverse solidus character (U+005C `\`) or `banned` character, either directly or in escaped form
    - no query or fragment
    
    refers to a **local file**. If the dataset is part of a [GEDZIP file](#gedzip), the URL of the local file is a zip archive filename; otherwise, the URL of a local file is resolved with *base* equal to the directory containing the dataset.
    
    It is recommended that local files use the directory prefix `media/`, but doing so is not required.

    For compatibility with [GEDZIP](#gedzip) and related formats, it is recommended that the following `FILE` payloads not be used:
    
    - `gedcom.ged`
    - `MANIFEST.MF`
    - any URL beginning `META-INF/`

The meaning of a `FILE` payload with any format not listed above is not defined by this version of the specification, but may be defined in a subsequent version.

#### `FORM` (Format) `g7:FORM`

The media type of the file referenced by the superstructure.
This should be a valid media type as defined by [BCP 13](https://www.rfc-editor.org/info/bcp13).
A [registry of media types](https://www.iana.org/assignments/media-types/media-types.xhtml) is maintained publicly by the IANA.

#### `FORM` (Format) `g7:PLAC-FORM`

A comma-separated list of jurisdictional titles,
which has the same number of elements and in the same order as the `PLAC` structure.
As with `PLAC`, this shall be ordered from lowest to highest jurisdiction.

:::example
The following represents Baltimore, a city that is not within a county.

```gedcom
2 PLAC Baltimore, , Maryland, USA
3 FORM City, County, State, Country
```
:::

#### `FORM` (Format) `g7:HEAD-PLAC-FORM`

Any `PLAC` with no `FORM` shall be treated as if it has this `FORM`.

#### `GEDC` (GEDCOM) `g7:GEDC`

A container for information about the entire document.

It is recommended that applications write `GEDC` with its required subrecord `VERS` as the first substructure of `HEAD`.

#### `GIVN` (Given name) `g7:GIVN`

A given or earned name used for official identification of a person.

#### `GRAD` (Graduation) `g7:GRAD`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `HEAD` (Header)

A pseudo-structure for storing metadata about the document.
See [The Header and Trailer](#the-header) for more.

#### `HEIGHT` (Height in pixels) `g7:HEIGHT`

How many pixels to display vertically for the image.
See `CROP` for more.

:::note
`HEIGHT` is a number of pixels.
The correct tag for the height of an individual is the `DSCR` attribute.

:::example
```gedcom
0 @I45@ INDI
1 DSCR brown eyes, 5ft 10in, 198 pounds
```
:::
:::

#### `HUSB` (Husband) `g7:HUSB`

A container for information relevant to the subject of the superstructure
specific to the individual described by the associated `FAM`'s `HUSB` substructure.

#### `HUSB` (Husband) `g7:FAM-HUSB`

This is a partner in a `FAM` record.
See `FAMILY_RECORD` for more.

#### `IDNO` (Identification number) `g7:IDNO`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `IMMI` (Immigration) `g7:IMMI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `INDI` (Individual) `g7:record-INDI`

See `INDIVIDUAL_RECORD`.

#### `INIL` (Initiatory, Latter-Day Saint) `g7:INIL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `LANG` (Language) `g7:LANG`

The human language of the superstructure.
The language in which the `Text`-typed payloads of superstructure and its substructures appears.

The payload of the `LANG` structure is a language tag, as defined by [BCP 47](https://www.rfc-editor.org/info/bcp47).
A [registry of component subtags](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) is maintained publicly by the IANA.

#### `LANG` (Language) `g7:HEAD-LANG`

The language in which the `Text`-typed payloads of all structures in the document appear, except as superseded by a `g7:LANG`.

The payload of the `LANG` structure is a language tag, as defined by [BCP 47](https://www.rfc-editor.org/info/bcp47).

#### `LANG` (Language) `g7:SUBM-LANG`

A language the subject of that record understands.

The payload of the `LANG` structure is a language tag, as defined by [BCP 47](https://www.rfc-editor.org/info/bcp47).

#### `LATI` (Latitude) `g7:LATI`

A latitudinal coordinate.
The payload is either `N` (for a coordinate north of the equator) or `S` (for a coordinate south of the equator) followed by a decimal number of degrees.
Minutes and seconds are not used and should be converted to fractional degrees prior to encoding.

:::example
18 degrees, 9 minutes, and 3.4 seconds North would be formatted as `N18.150944`.
:::

#### `LEFT` (Left crop width) `g7:LEFT`

Left is a number of pixels to not display from the left side of the image.
See `CROP` for more.

#### `LONG` (Longitude) `g7:LONG`

A longitudinal coordinate.
The payload is either `E` (for a coordinate east of the prime meridian) or `W` (for a coordinate west of the prime meridian) followed by a decimal number of degrees.
Minutes and seconds are not used and should be converted to fractional degrees prior to encoding.

:::example
168 degrees, 9 minutes, and 3.4 seconds East would be formatted as `E168.150944`.
:::

#### `MAP` (Map) `g7:MAP`

A representative point for a location,
as defined by `LATI` and `LONG` substructures.

Note that `MAP`  provides
neither a notion of accuracy
(for example, the `MAP` for a birth event may be some distance from the point where the birth occurred)
nor a notion of region size
(for example, the `MAP` for a place "Belarus" may be anywhere within that nation's 200,000 square kilometer area).

#### `MARB` (Marriage banns) `g7:MARB`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARC` (Marriage contract) `g7:MARC`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARL` (Marriage license) `g7:MARL`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARR` (Marriage) `g7:MARR`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARS` (Marriage settlement) `g7:MARS`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MEDI` (Medium) `g7:MEDI`

An [enumerated value](#enum-MEDI) providing information about the media or the medium in which information is stored.

#### `MIME` (Media type) `g7:MIME`

Indicates the media type of the payload of the superstructure,
as defined by [BCP 13](https://www.rfc-editor.org/info/bcp13).

As of version 7.0, only 2 media types are supported by this structure:

- `text/plain` shall be presented to the user as-is, preserving all spacing, line breaks, and so forth.

- `text/html` uses HTML tags to provide presentation information.
    Applications should support at least the following:
    
    - `p` and `br` elements for paragraphing and line breaks.
    - `b`, `i`, `u`, and `s` elements for bold, italic, underlined, and strike-through text (or corresponding display in other locales; see [HTML §4.5](https://html.spec.whatwg.org/multipage/text-level-semantics.html) for more).
    - `sup` and `sub` elements for super- and sub-script.
    - The 3 XML entities that appear in text: `&amp;`, `&lt;` `&gt;`.
        Note that `&quote;` and `&apos;` are only needed in attributes.
        Other entities should be represented as their respective Unicode characters instead.
    
    Supporting more of HTML is encouraged.
    Unsupported elements should be ignored during display.

:::note
Applications are welcome to support more XML entities or HTML character references in their user interface.
However, exporting must only use the core XML entities, translating any other entities into their corresponding Unicode characters.
:::

:::note
Applications are welcome to support additional HTML elements,
but they should ensure that content is meaningful if those extra elements are ignored and only their content text is displayed.
:::


:::note
Media types are also used by external files, as described under `FORM`. External file media types are not limited to `text/plain` and `text/html`.
:::

If needed, `text/html` can be converted to `text/plain` using the following steps:

1. Replace any sequence of 1 or more spaces, tabs, and line breaks with a single space
2. Case-insensitively replace each `<p`...`>`, `</p`...`>`, and `<br`...`>` with a line break
3. Remove all other `<`...`>` tags
4. Replace each `&lt;` with `<` and `&gt;` with `>`
4. Replace each `&amp;` with `&`

#### `NAME` (Name) `g7:NAME`

The name of the superstructure's subject, represented as a simple string.

#### `NAME` (Name) `g7:INDI-NAME`

A `PERSONAL_NAME_STRUCTURE` with parts, translations, sources, and so forth.

#### `NATI` (Nationality) `g7:NATI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `NATU` (Naturalization) `g7:NATU`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `NCHI` (Number of children) `g7:FAM-NCHI`

A [Family Attribute](#family-attributes).
See also `FAMILY_ATTRIBUTE_STRUCTURE`.

#### `NCHI` (Number of children) `g7:INDI-NCHI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `NICK` (Nickname) `g7:NICK`

A descriptive or familiar name that is used instead of, or in addition to, one’s proper name.

#### `NMR` (Number of marriages) `g7:NMR`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `NO` (Did not happen) `g7:NO`

An [enumerated value](#enum-NO) identifying an event type which did not occur to the superstructure's subject.
See `NON_EVENT_STRUCTURE` for more.

#### `NOTE` (Note) `g7:NOTE`

A `NOTE_STRUCTURE`, containing additional information provided by the submitter for understanding the enclosing data.

When a substructure of `HEAD`, it should describe the contents of the document in terms of "ancestors or descendants of" so that the person receiving the data knows what genealogical information the document contains.

#### `NPFX` (Name prefix) `g7:NPFX`

Text that appears on a name line before the given and surname parts of a name.

#### `NSFX` (Name suffix) `g7:NSFX`

Text which appears on a name line after or behind the given and surname parts of a name.

#### `OBJE` (Object) `g7:OBJE`

See `MULTIMEDIA_LINK`.

#### `OBJE` (Object) `g7:record-OBJE`

See `MULTIMEDIA_RECORD`.

#### `OCCU` (Occupation) `g7:OCCU`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `ORDN` (Ordination) `g7:ORDN`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `PAGE` (Page) `g7:PAGE`

A specific location within the information referenced. For a published work, this could include the volume of a multi-volume work and the page number or numbers. For a periodical, it could include volume, issue, and page numbers. For a newspaper, it could include a date, page number, and column number. For an unpublished source or microfilmed works, this could be a film or sheet number, page number, or frame number. A census record might have an enumerating district, page number, line number, dwelling number, and family number.

It is recommended that the data in this field be formatted comma-separated with label: value pairs

:::example
```gedcom
2 SOUR @S1@
3 PAGE Film: 1234567, Frame: 344, Line: 28
```
:::

#### `PEDI` (Pedigree) `g7:PEDI`

An [enumerated value](#enum-PEDI) indicating the type of child-to-family relationship represented by the superstructure.

#### `PHON` (Phone) `g7:PHON`

A telephone number.
Telephone numbers have many regional variations and can contain non-digit characters.
Users should be encouraged to use internationalized telephone numbers rather than local versions.
As a starting point for this recommendation, there are international standards that use a "'+'" shorthand for the international prefix (for example, in place of "011" in the US or "00" in the UK).
Examples are `+1 (555) 555-1234` (US) or `+44 20 1234 1234` (UK).

See ITU standards [E.123](https://www.itu.int/rec/T-REC-E.123) and [E.164](https://www.itu.int/rec/T-REC-E.164) for more information.

#### `PHRASE` (Phrase) `g7:PHRASE`

Textual information that cannot be expressed in the superstructure due to the limitations of its datatype.

:::example
A date interpreted from the phrase "The Feast of St John" might be

````gedcom
2 DATE 24 JUNE 1852
3 PHRASE During the feast of St John
````
:::

:::example
A record using `1648/9` to indicate a change in new year might become

````gedcom
2 DATE 30 JAN 1649
3 PHRASE 30th of January, 1648/9
````
:::

:::example
A record using `1648/9` to indicate uncertainty in the year might become

````gedcom
2 DATE BET 1648 AND 1649
3 PHRASE 1648/9
````
:::

:::example
A record using `Q1 1867` to indicate an event occurred sometime within the first quarter of 1867 might become

````gedcom
2 DATE BET 1 JAN 1867 AND 31 MAR 1867
3 PHRASE Q1 1867
````
:::

:::example
A record defining the Maid of Honor in a marriage might become

````gedcom
1 MARR
2 ASSO @I2@
3 ROLE OTHER
4 PHRASE Maid of Honor
````
:::

:::example
A name given to a foundling orphan might be

````gedcom
1 NAME Mary //
2 GIVN Mary
2 TYPE OTHER
3 PHRASE given by orphanage
````
:::


#### `PLAC` (Place) `g7:PLAC`

The principal place in which the superstructure's subject occurred,
represented as a [List] of jurisdictional entities in a sequence from the lowest to the highest jurisdiction.
As with other lists, the jurisdictions are separated by commas.
Any jurisdiction's name that is missing is still accounted for by an empty string in the list.

The type of each jurisdiction is given in the `PLAC`.`FORM` substructure, if present,
or in the `HEAD`.`PLAC`.`FORM` structure.
If neither is present, the jurisdictional types are unspecified
beyond the lowest-to-highest order noted above.

#### `PLAC` (Place) `g7:HEAD-PLAC`

This is a placeholder for providing a default `PLAC`.`FORM`, and must not have a payload.

#### `POST` (Postal code) `g7:POST`

A code used by a postal service to identify an area to facilitate mail handling.
See `ADDRESS_STRUCTURE` for more.

#### `PROB` (Probate) `g7:PROB`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `PROP` (Property) `g7:PROP`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `PUBL` (Publication) `g7:PUBL`

When and where the record was created. For published works, this includes information such as the city of publication, name of the publisher, and year of publication.

For an unpublished work, it includes the date the record was created and the place where it was created, such as the county and state of residence of a person making a declaration for a pension or the city and state of residence of the writer of a letter.

#### `QUAY` (Quality of data) `g7:QUAY`

An [enumerated value](#enum-QUAY) indicating the credibility of a piece of information, based on its supporting evidence.
Some systems use this feature to rank multiple conflicting opinions for display of most likely information first.
It is not intended to eliminate the receivers' need to evaluate the evidence for themselves.

#### `REFN` (Reference) `g7:REFN`

A user-defined number or text that the submitter uses to identify the superstructure.
For instance, it may be a record number within the submitter's automated or manual system, or it may be a page and position number on a pedigree chart.

This is metadata about the structure itself, not data about its subject.
Multiple structures describing different aspects of the same subject must not have the same `REFN` value.

#### `RELI` (Religion) `g7:RELI`

A religious denomination associated with the event or attribute described by the superstructure.

#### `RELI` (Religion) `g7:INDI-RELI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `RESN` (Restriction) `g7:RESN`

A [List] of [enumerated value](#enum-RESN)s signifying access to information may be denied or otherwise restricted.

The `RESN` structure is provided to assist software in filtering data that should not be exported or otherwise used in a particular context. It is recommended that tools provide an interface to allow users to filter data on export
such that certain `RESN` structure payload entries result in the `RESN` structure and its superstructure being removed from the export.
Such removal must abode by some constraints: see [Removing data](#removing-data) for more.

This is metadata about the structure itself, not data about its subject.

#### `REPO` (Repository) `g7:REPO`

See `SOURCE_REPOSITORY_CITATION`.

#### `REPO` (Repository) `g7:record-REPO`

See `REPOSITORY_RECORD`.

#### `RESI` (Residence) `g7:FAM-RESI`

A [Family Attribute](#family-attributes).
See also `FAMILY_ATTRIBUTE_STRUCTURE`.

See `g7:INDI-RESI` for comments on the use of payload strings in `RESI` structures.


#### `RESI` (Residence) `g7:INDI-RESI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

Where possible, the residence should be identified in `PLAC` and/or `ADDR` substructures of the `RESI` structure. The payload text should not duplicate `PLAC` or `ADDR` information, but may be used for residence information that cannot be expressed by those structures.

:::example
The following two examples show situations where a `RESI` payload may be appropriate:

```gedcom
1 RESI living with an aunt
2 DATE ABT MAR 1894
```

```gedcom
1 RESI in a mobile caravan
2 PLAC , , Austro-Hungarian Empire
3 FORM City, County, Country
```
:::


#### `RETI` (Retirement) `g7:RETI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `ROLE` (Role) `g7:ROLE`

An [enumerated value](#enum-ROLE) indicating what role this person played in an event or person's life.

:::example
The following indicates a child's birth record as the source of the mother's name:

```gedcom
0 @I1@ INDI
1 NAME Mary //
2 SOUR @S1@
3 EVEN BIRT
4 ROLE MOTH
```
:::

:::example
The following indicates that a person's best friend was a witness at their baptism:

```gedcom
0 @I2@ INDI
1 ASSO @I3@
2 ROLE FRIEND
3 PHRASE best friend
1 BAPM
2 ASSO @I3@
3 ROLE WITN
```
:::

#### `SCHMA` (Extension schema) `g7:SCHMA`

A container for storing meta-information about the extension tags used in this document.
See [Extensions](#extensions) for more.

#### `SDATE` (Sort date) `g7:SDATE`

A date to be used as a sorting hint.
It is intended for use when the actual date is unknown, but the display order may be dependent on date.

If both a `DATE` and `SDATE` are present in the same structure,
the `SDATE` should be used for sorting and positioning
while the `DATE` should be displayed as the date of the structure.

`SDATE` and its substructures (including `PHRASE`, `TIME`, and any extension structures) should be used only as sorting hints, not to convey historical meaning.

#### `SEX` (Sex) `g7:SEX`

An [enumerated value](#enum-SEX) that indicates the sex of the individual at birth.

#### `SLGC` (Sealing, child) `g7:SLGC`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `SLGS` (Sealing, spouse) `g7:SLGS`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_SPOUSE_SEALING`.

#### `SNOTE` (Shared note) `g7:SNOTE`

A pointer to a note that is shared by multiple structures.
See `NOTE_STRUCTURE` for more.

#### `SNOTE` (Shared note) `g7:record-SNOTE`

A note that is shared by multiple structures.
See `SHARED_NOTE_RECORD` for more.

#### `SOUR` (Source) `g7:SOUR`

A description of the relevant part of a source to support the superstructure's data.
See `SOURCE_CITATION` for more.

#### `SOUR` (Source) `g7:record-SOUR`

A description of an entire source.
See `SOURCE_RECORD` for more.

#### `SOUR` (Source) `g7:HEAD-SOUR`

An identifier for the product producing this dataset.
A registration process for these identifiers existed for a time, but no longer does.
If an existing identifier is known, it should be used.
Otherwise, a URI owned by the product should be used instead.

#### `SPFX` (Surname prefix) `g7:SPFX`

A name piece used as a non-indexing pre-part of a surname.

#### `SSN` (Social security number) `g7:SSN`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `STAE` (State) `g7:STAE`

A geographical division of a larger jurisdictional area, such as a state within the United States of America.
See `ADDRESS_STRUCTURE` for more.

#### `STAT` (Status) `g7:ord-STAT`

An [enumerated value](#enum-Temple.STAT) assessing of the state or condition of an ordinance.

#### `STAT` (Status) `g7:FAMC-STAT`

An [enumerated value](#enum-FAMC.STAT) assessing of the state or condition of a researcher's belief in a family connection.

#### `SUBM` (Submitter) `g7:SUBM`

A contributor of information in the substructure.
This is metadata about the structure itself, not data about its subject.

#### `SUBM` (Submitter) `g7:record-SUBM`

A description of a contributor of information to the document.
See `SUBMITTER_RECORD` for more.

#### `SURN` (Surname) `g7:SURN`

A family name passed on or used by members of a family.

#### `TAG` (Extension tag) `g7:TAG`

Information relating to a single extension tag as used in this document.
See [Extensions](#extensions) for more.

#### `TEMP` (Temple) `g7:TEMP`

The name of a temple of The Church of Jesus Christ of Latter-day Saints.
Previous versions recommended using a set of abbreviations for temple names, but the list of abbreviations is no longer published by the Church and using abbreviations is no longer recommended.

#### `TEXT` (Text from Source) `g7:TEXT`

A verbatim copy of any description contained within the source.
This indicates notes or text that are actually contained in the source document, not the submitter's opinion about the source.
This should be, from the evidence point of view, "what the original record keeper said" as opposed to the researcher's interpretation.

#### `TIME` (Time) `g7:TIME`

A `Time` value in a 24-hour clock format.

#### `TITL` (Title) `g7:TITL`

The title, formal or informal, of the superstructure.

A published work, such as a book, might have a title plus the title of the series of which the book is a part. A magazine article would have a title plus the title of the magazine that published the article.

For an unpublished work, including most digital files, titles should be descriptive and appropriate to the work.

:::example

<p></p>

* The `TITL` of a letter might include the date, the sender, and the receiver.
* The `TITL` of a transaction between a buyer and seller might have their names and the transaction date.
* The `TITL` of a family Bible containing genealogical information might have past and present owners and a physical description of the book.
* The `TITL` of a personal interview would cite the informant and interviewer.

:::

#### `TITL` (Title) `g7:INDI-TITL`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `TOP` (Top crop width) `g7:TOP`

A number of pixels to not display from the top side of the image.
See `CROP` for more.


#### `TRAN` (Translation)

A representation of the superstructure's data in a different format.

In some situations it is desirable to provide the same semantic content in multiple formats.
Where this is desirable, a `TRAN` substructure is used,
where the specific format is given in its language tag substructure, media type substructure, or both.

Different `TRAN` structures are used in different contexts to fully capture the structure of the information being presented in multiple formats.
In all cases, a `TRAN` structure's payload and substructures should provide only information also contained in the `TRAN` structures' superstructure, but provide it in a new language, script, or media type.

Each `TRAN` substructure must have either a language tag or a media type or both.
Each `TRAN` structure must differ from its superstructure
and from every other `TRAN` substructure of its superstructure
in either its language tag or its media type or both.

#### `TRAN` (Translation) `g7:NAME-TRAN`

A type of `TRAN` substructure specific to [Personal Names](#personal-name).
Each `NAME`.`TRAN` must have a `LANG` substructure.
See also `INDI`.`NAME`.

:::example
The following presents a name in Mandarin, transliterated using Pinyin

```gedcom
1 NAME /孔/德庸
2 GIVN 德庸
2 SURN 孔
2 TRAN /Kǒng/ Déyōng
3 GIVN Déyōng
3 SURN Kǒng
3 LANG zh-pinyin
```
:::

#### `TRAN` (Translation) `g7:PLAC-TRAN`

A type of `TRAN` substructure specific to places.
Each `PLAC`.`TRAN` must have a `LANG` substructure.
See also `PLAC`.

:::example
The following presents a place
in Japanese
with a romanji transliteration
and English translation

```gedcom
2 PLAC 千代田, 東京, 日本
3 FORM 区, 都, 国
3 LANG ja
3 TRAN Chiyoda, Tokyo, Nihon
4 LANG ja-Latn
3 TRAN Chiyoda, Tokyo, Japan
4 LANG en
```
:::


#### `TRAN` (Translation) `g7:NOTE-TRAN`

A type of `TRAN` for unstructured human-readable text,
such as is found in `NOTE` and `SNOTE` payloads.
Each `g7:NOTE-TRAN` must have either a `LANG` substructure or a `MIME` substructure or both.
If either is missing, it is assumed to have the same value as the superstructure.
See also `NOTE` and `SNOTE`.

:::example
The following presents the same note in HTML-format English;
in plain-text with the same language as the superstructure (English);
and in Spanish with the same media type as the superstructure (HTML).

```gedcom
1 NAME Arete /Hernandez/
2 NOTE Named after Arete from <i>The Odyssey</i>
3 LANG en
3 MIME text/html
3 TRAN Named after Arete from "The Odyssey"
4 MIME text/plain
3 TRAN Nombrada en honor a Arete de <i>La Odisea</i>
4 LANG es
```
:::

It is recommended that text given in `text/html`
should only be translated into `text/plain`
if the resulting text is different from the text created by the HTML-to-text conversion process defined in `g7:MIME`.

#### `TRAN` (Translation) `g7:FILE-TRAN`

A type of `TRAN` for external media files.
Each `g7:NOTE-TRAN` must have a `FORM` substructure.
See also `FILE`.

:::example
If an mp3 audio file
has been transcoded as an ogg file
and a timestamped transcript has been extracted as a WebVTT file,
the resulting set of files might be presented as follows:

```gedcom
0 @EX@ OBJE
1 FILE media/original.mp3
2 FORM audio/mp3
2 TRAN media/derived.oga
3 FORM auto/ogg
2 TRAN media/transcript.vtt
3 FORM text/vtt
```
:::

Note that `FILE`.`TRAN` refers to translation to a different digital format,
not to translation to a different human language.
Files that differ in the human language of their content
should each be given their own `FILE` structure.


#### `TRLR` (Trailer)

A pseudo-structure marking the end of a dataset.
See [The Header and Trailer](#the-header) for more.

#### `TYPE` (Type) `g7:TYPE`

A descriptive word or phrase used to further classify the superstructure.

When both a `NOTE` and free-text `TYPE` are permitted as substructures of the same structure,
the displaying systems should always display the `TYPE` value
when they display the data from the associated structure;
`NOTE` will typically be visible only in a detailed view.

`TYPE` must be used whenever the generic `EVEN`, `FACT` and `IDNO` tags are used.
It may also be used for any other event or attribute.

Using the subordinate `TYPE` classification method provides a further classification of the superstructure but does not change its basic meaning.

:::example
A `ORDN` with a `TYPE` could clarify what kind of ordination was performed:

```gedcom
0 @I1@ INDI
1 ORDN
2 TYPE Bishop
```

This classifies the entry as an ordination as a bishop, which is still a ordination event. The event could be further clarified with `RELI`, `DATE`, and other substructures.

Other descriptor values might include, for example,

- "Stillborn" as a qualifier to `BIRT` (birth)
- "Civil" as a qualifier to `MARR` (marriage)
- "College" as a qualifier to `GRAD` (graduation)
- "Oral" as a qualifier to `WILL`

See also `FACT` and `EVEN` for additional examples.
:::

#### `TYPE` (Type) `g7:NAME-TYPE`

An [enumerated value](#enum-TYPE) indicating the type of the name.

#### `TYPE` (Type) `g7:EXID-TYPE`

The authority issuing the `EXID`, represented as a URI.
It is recommended that this be a URL.

If the authority maintains stable URLs for each identifier it issues,
it is recommended that the `TYPE` payload be selected such that appending the `EXID` payload to it yields that URL.
However, this is not required and a different URI for the set of issued identifiers may be used instead.

#### `UID` (Unique Identifier) `g7:UID`

A globally-unique identifier of the superstructure,
to be preserved across edits.
If a globally-unique identifier for the record already exists, it should be used without modification, not even whitespace or letter case normalization.
New globally unique identifiers should be created and formatted as described in [RFC 4122](https://www.rfc-editor.org/info/rfc4122).

This is metadata about the structure itself, not data about its subject.
Multiple structures describing different aspects of the same subject would have different `UID` values.

:::note
Some systems used a 16-byte UUID with a custom 2-byte checksum for a total of 18 bytes:

- checksum byte 1 =
  (sum of (byte~*i*~) for *i* 1 through 16) mod 256
- checksum byte 2 =
  (sum of ((16 − *i*) × (byte~*i*~)) for *i* 1 through 16) mod 256

Use of checksums for UIDs is discouraged except in cases where error-prone input is expected and an appropriate action to take in case of an error is known.
:::

#### `VERS` (Version) `g7:VERS`

An identifier that represents the version level assigned to the associated product.
It is defined and changed by the creators of the product.

#### `VERS` (Version) `g7:GEDC-VERS`

The version number of the official specification that this document's data conforms to.
This must include the major and minor version (for example, "`7.0`");
it may include the patch as well (for example, "`7.0.1`"), but doing so is not required.
See [A Guide to Version Numbers] for more.

#### `WIDTH` (Width in pixels) `g7:WIDTH`

How many pixels to display horizontally for the image.
See `CROP` for more.

#### `WIFE` (Wife) `g7:WIFE`

A container for information relevant to the subject of the superstructure
specific to the individual described by the associated `FAM`'s `WIFE` substructure.

#### `WIFE` (Wife) `g7:FAM-WIFE`

A partner in a `FAM` record.
See `FAMILY_RECORD` for more.

#### `WILL` (Will) `g7:WILL`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `WWW` (Web address) `g7:WWW`

A URL or other locator for a World Wide Web page,
as defined by any relevant standard
such as [whatwg/url](https://url.spec.whatwg.org/),
[RFC 3986](https://www.rfc-editor.org/info/rfc3986),
[RFC 3987](https://www.rfc-editor.org/info/rfc3987),
and so forth.

If an invalid or no longer existing web address is present upon import, it should be preserved as-is on export.




## Enumeration Values

Unless otherwise specified in the enumeration description in this section, each enumeration values defined in this section has a URI constructed by concatenating
`g7:enum-` to the enumeration value;
for example, the `HUSB` enumeration value has the URI `http://gedcom.io/terms/v7/enum-HUSB`.

### `FAMC`.`ADOP` {.unlisted .unnumbered #enum-ADOP}

| Value | Meaning |
| :---- | :------ |
| `HUSB` | Adopted by the `HUSB` of the `FAM` pointed to by `FAMC`.<br/>The URI of this value is `g7:enum-ADOP-HUSB` |
| `WIFE` | Adopted by the `WIFE` of the `FAM` pointed to by `FAMC`.<br/>The URI of this value is `g7:enum-ADOP-WIFE` |
| `BOTH` | Adopted by both `HUSB` and `WIFE` of the `FAM` pointed to by `FAMC` |

### `DATA`.`EVEN` {.unlisted .unnumbered #enum-EVEN}

A comma-separated list of event- and attribute-type tag names.
See [Events] and [Attributes].

### `SOUR`.`EVEN` {.unlisted .unnumbered #enum-SOUR.EVEN}

An event- or attribute-type tag names.
See [Events] and [Attributes].

### `MEDI` {.unlisted .unnumbered #enum-MEDI}

| Value        | Meaning                           |
| :----------- | :-------------------------------- |
| `AUDIO`      | An audio recording                |
| `BOOK`       | A bound book                      |
| `CARD`       | A card or file entry              |
| `ELECTRONIC` | A digital artifact                |
| `FICHE`      | Microfiche                        |
| `FILM`       | Microfilm                         |
| `MAGAZINE`   | Printed periodical                |
| `MANUSCRIPT` | Written pages                     |
| `MAP`        | Cartographic map                  |
| `NEWSPAPER`  | Printed newspaper                 |
| `PHOTO`      | Photograph                        |
| `TOMBSTONE`  | Burial marker or related memorial |
| `VIDEO`      | Motion picture recording          |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

### `PEDI` {.unlisted .unnumbered #enum-PEDI}

| Value     | Meaning                                                   |
| :-------- | :-------------------------------------------------------- |
| `ADOPTED` | Adoptive parents                                          |
| `BIRTH`   | Family structure at time of birth                         |
| `FOSTER`  | The child was included in a foster or guardian family     |
| `SEALING` | The child was sealed to parents other than birth parents  |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

:::note
It is known that some users have interpreted `BIRTH` to mean "genetic parent" and others to mean "social parent at time of birth", definition which differ many circumstances (infidelity, surrogacy, sperm donation, and so on). Hence, applications should refrain from asserting it has either meaning in imported data.
:::

:::note
The structures for foster children in particular, and family relationships in general, are known to have undesirable limitations and are likely to change in a future version of this specification.
:::

### `NO` {.unlisted .unnumbered #enum-NO}

A single event-type tag name, but not the generic `EVEN` tag.
See [Events].



### `QUAY` {.unlisted .unnumbered #enum-QUAY}

| Value | Meaning                             |
| :---- | :---------------------------------- |
| `0` | Unreliable evidence or estimated data |
| `1` | Questionable reliability of evidence (interviews, census, oral genealogies, or potential for bias, such as an autobiography) |
| `2` | Secondary evidence, data officially recorded sometime after the event |
| `3` | Direct and primary evidence used, or by dominance of the evidence |

Although the values look like integers, they do not have numeric meaning.

:::note
The structures for representing the strength of and confidence in various claims are known to be inadequate and are likely to change in a future version of this specification.
:::

### `RESN` {.unlisted .unnumbered #enum-RESN}

| Value | Meaning                      |
| :---- | :--------------------------- |
| `CONFIDENTIAL` | This data was marked as confidential by the user. |
| `LOCKED` | Some systems may ignore changes to this data. |
| `PRIVACY` | This data is not to be shared outside of a trusted circle, generally because it contains information about living individuals. |

When a [List] of `RESN` enumeration values are present, all apply.

:::example
The line `1 RESN CONFIDENTIAL, LOCKED` means the superstructure's data is both considered confidential *and* read-only.
:::

### `ROLE` {.unlisted .unnumbered #enum-ROLE}

| Value | Meaning |
| ----- | :------ |
| `CHIL` | Child |
| `CLERGY` | Religious official in event; implies `OFFICIATOR` |
| `FATH` | Father; implies `PARENT` |
| `FRIEND` | Friend |
| `GODP` | Godparent or related role in other religions |
| `HUSB` | Husband; implies `SPOU` |
| `MOTH` | Mother; implies `PARENT` |
| `MULTIPLE` | A sibling from the same pregnancy (twin, triplet, quadruplet, and so on). A `PHRASE` can be used to specify the kind of multiple birth. |
| `NGHBR` | Neighbor |
| `OFFICIATOR` | Officiator of the event |
| `PARENT` | Parent |
| `SPOU` | Spouse |
| `WIFE` | Wife; implies `SPOU` |
| `WITN` | Witness |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

These should be interpreted in the context of the recorded event and its primary participants.
For example, if you cite a child’s birth record as the source of the mother’s name, the value for this field is “`MOTH`.”
If you describe the groom of a marriage, the role is “`HUSB`.”

### `SEX` {.unlisted .unnumbered #enum-SEX}

| Value | Meaning                                     |
| ----- | :------------------------------------------ |
| `M`   | Male                                        |
| `F`   | Female                                      |
| `X`   | Does not fit the typical definition of only Male or only Female |
| `U`   | Cannot be determined from available sources |

This can describe an individual’s reproductive or sexual anatomy at birth.
Related concepts of gender identity or sexual preference
are not currently given their own tag. Cultural or personal gender preference may be indicated using the `FACT` tag.

### `FAMC`.`STAT` {.unlisted .unnumbered #enum-FAMC.STAT}

| Value | Meaning                        |
| ----- | :----------------------------- |
| `CHALLENGED` | Linking this child to this family is suspect, but the linkage has been neither proven nor disproven. |
| `DISPROVEN` | There has been a claim by some that this child belongs to this family, but the linkage has been disproven. |
| `PROVEN` | There has been a claim by some that this child does not belong to this family, but the linkage has been proven. |

:::note
The structures for representing the strength of and confidence in various claims are known to be inadequate and are likely to change in a future version of this specification.
:::

### (Latter-Day Saint Ordinance).`STAT` {.unlisted .unnumbered #enum-Temple.STAT}

These values were formerly used by The Church of Jesus Christ of Latter-day Saints for coordinating between temples and members.
They are no longer used in that way, meaning their interpretation is subject to individual user interpretation

| Value | Meaning                             |
| ----- | :---------------------------------- |
| `BIC` | Born in the covenant, receiving blessing of child to parent sealing. |
| `CANCELED` | Canceled and considered invalid. |
| `CHILD` | Died before 8 years old. |
| `COMPLETED` | Completed, but the date is not known. |
| `EXCLUDED` | Patron excluded this ordinance from being cleared in this submission. |
| `DNS` | This ordinance is not authorized. |
| `DNS_CAN` | This ordinance is not authorized, and the previous ordinance is cancelled. |
| `INFANT` | Died before less than 1 year old, baptism or endowment not required. |
| `PRE_1970` | Ordinance was likely completed because another ordinance for this person was converted from temple records of work completed before 1970. |
| `STILLBORN` | Stillborn, so ordinances not required. |
| `SUBMITTED` | Ordinance was previously submitted. |
| `UNCLEARED` | Data for clearing the ordinance request was insufficient. |

### `NAME`.`TYPE` {.unlisted .unnumbered #enum-TYPE}

| Value | Meaning                       |
| ----- | :---------------------------- |
| `AKA` | Also known as, alias, etc. |
| `BIRTH` | Name given at or near birth. |
| `IMMIGRANT` | Name assumed at the time of immigration. |
| `MAIDEN` | Maiden name, name before first marriage. |
| `MARRIED` | Married name, assumed as part of marriage. |
| `PROFESSIONAL` | Name used professionally (pen, screen, stage name). |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

# The FamilySearch GEDZIP file format {#gedzip}

It is often useful to transmit a dataset together with a set of external files.
The FamilySearch GEDZIP 7.0 file format is provided for this purpose.
Version 7.0 was the first version of GEDZIP released; the version number of a GEDZIP file is the same as the version number of the dataset it contains.

A GEDZIP file is a zip archive, as defined by [the .ZIP File Format Specification](http://www.pkware.com/appnote)
and standardized by [ISO/IEC 21320-1:2015](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=60101).

Each GEDZIP file contains the following entries:

- An entry with name `gedcom.ged` containing a data stream.

- An entry for each *local file* `FILE` structure in `gedcom.ged`, with the same zip *file name* as the corresponding `FILE` payload.
    If there is a local file named `gedcom.ged`, it must be renamed to a new unused filename with the same extension prior to constructing the GEDZIP.

All file names inside a GEDZIP are case-sensitive.

Many other zip-based file formats (such as jar, epub, docx, GEDCOM-X) assign special meaning to the zip directory `META-INF` and the zip file names `MANIFEST.MF` and `META-INF/MANIFEST.MF`. These have no special meaning in GEDZIP and it is recommended that they not be used in a GEDZIP file, both to avoid confusing systems that look inside zip archives to determine their file type, and to leave open the possibility of their addition in a future version of this specification.

When saved as a file, a GEDZIP should use the filename extension `.gdz`.

:::note
A few details about the zip archive format are useful to fully understand GEDZIP:

- An archive can contain 1 or more files.
- Files within an archive can be added, removed, or updated individually without needing to re-process the rest of the archive. Libraries such as [libzip](https://libzip.org) allow applications to operate directly on the zip archive as if it were a normal directory tree.
- What the zip specification calls a "file name" is actually a local path and may contain directories.
- Directory separators are `/` internally and are converted to the appropriate form by the zip processing tool during zipping and unzipping. Because of this, unzipping a GEDZIP in any local directory results in all GEDZIP `FILE` references working as-is for the resulting `gedcom.ged` without the need for any additional processing.
:::



# Contributors

This document was based on *The GEDCOM Standard Release 5.5.1*,
and could not have existed without the contributors to that and previous versions of the specification.
Appreciation is extended to all family history participants that have made FamilySearch GEDCOM the *de facto* standard for saving and transferring genealogical information.

New contributions in this edition  benefited from the input of a large number of people:

<dl><dt>Managing Editors</dt><dd>

- Gordon Clarke, **FamilySearch**
- Luther Tychonievich, **FHISO** and **University of Virginia**

</dd><dt>Taskforce</dt><dd>

- David Pugmire, **FamilySearch**
- Jimmy Zimmerman, **FamilySearch**
- Larry Telford, **FamilySearch**
- Matt Misbach, **FamilySearch**
- Russell Lynch, **FamilySearch**
- Robert Raymond, **FamilySearch**
- Gaylon Findlay, **Ancestral Quest**
- Derek Maude, **Ancestry**
- James Tanner, **The Family History Guide**
- John Cardinal, **Family History Hosting**
- Albert Emmerich, **GEDCOM-L**
- Dave Berdan, **Legacy Family Tree**
- Evgen Zherebniy, **Software Mackiev**
- Jason Fletcher, **Midlera Software**
- Uri Gonen, **MyHeritage**
- Dallan Quass, **OurRoots.org**
- Tony Proctor, **SVG Family-Tree Generator**
- Bill Harten, **Puzzilla**
- Bruce Buzbee and Mike Booth, **RootsMagic**

</dd><dt>Development Teams</dt><dd>

- **Tags team**:
    Luther Tychonievich, Albert Emmerich, Russell Lynch, Tony Proctor, John Cardinal

- **Extensions team**:
    Luther Tychonievich, Tony Proctor, Jimmy Zimmerman

- **Notes team**:
    Dallan Quass, David Pugmire, Jason Fletcher, Russell Lynch

- **External Media team**:
    Dallan Quass, Jason Fletcher, Derek Maude

</dd></dl>




# Appendix A: Known Calendars and Dates {#A-calendars}

## Known Calendars

This specification defines 4 calendars: `GREGORIAN`, `JULIAN`, `FRENCH_R`, and `HEBREW`.
Previous versions also provided for, but did not define the meaning of, `ROMAN` and `UNKNOWN` calendars.

Extension calendars should use the usual rules for extensions, including using `_` as the leading character of the calendar name. Month codes in extension calendars must either be already used for the same month name in another calendar or must start with `_`. Only upper case characters are allowed in month codes.

Each calendar must list its permitted epochs and their meaning.

Each month defined in this section has a URI constructed by concatenating
`g7:month-` to the month code;
for example, the month of Elul has the URI `http://gedcom.io/terms/v7/month-ELL`.

### `GREGORIAN`

The Gregorian calendar is the now-ubiquitous calendar introduced by Pope Gregory XIII in 1582 to correct the Julian calendar which was slowly drifting relative to the seasons.

Permitted months are

|Code   |Name       |
|:------|:----------|
| `JAN` | January   |
| `FEB` | February  |
| `MAR` | March     |
| `APR` | April     |
| `MAY` | May       |
| `JUN` | June      |
| `JUL` | July      |
| `AUG` | August    |
| `SEP` | September |
| `OCT` | October   |
| `NOV` | November  |
| `DEC` | December  |

The epoch marker `BCE` is permitted in this calendar;
year *y* BCE indicates a year *y* years before year 1.
Thus, there is no year 0; year 1 BCE was followed by year 1.

The URI for this calendar is `g7:cal-GREGORIAN`

### `JULIAN`

The Julian calendar was introduced by Julius Caesar in 45 BC and subsequently amended by Augustus in about 8 BC to correct an error in the application of its leap year rule during its first 3 decades. Years had been counted from various starting epochs during the Julian calendar's use; the version specified by this specification uses the same starting epoch as the Gregorian calendar.

This calendar uses the same months as the Gregorian calendar, differing only in which years February has 29 days.

The epoch marker `BCE` is permitted in this calendar;
year *y* BCE indicates a year *y* years before year 1.
Thus, there is no year 0; year 1 BCE was followed by year 1.

The URI for this calendar is `g7:cal-JULIAN`

### `FRENCH_R`

The French Republican calendar or French Revolutionary calendar are the names given to the new calendar adopted in 1794 by the French National Convention. This calendar was adopted on Gregorian day 22 September 1792, which was 1 Vendémiaire 1 in this calendar. It was abandoned 18 years later.

Permitted months are

|Code  |Name               |
|:-----|:------------------|
|`VEND`|Vendemiaire        |
|`BRUM`|Brumaire           |
|`FRIM`|Frimaire           |
|`NIVO`|Nivose             |
|`PLUV`|Pluviose           |
|`VENT`|Ventose            |
|`GERM`|Germinal           |
|`FLOR`|Floreal            |
|`PRAI`|Prairial           |
|`MESS`|Messidor           |
|`THER`|Thermidor          |
|`FRUC`|Fructidor          |
|`COMP`|Jour Complementairs|

No epoch marker is permitted in this calendar.

The URI for this calendar is `g7:cal-FRENCH_R`

### `HEBREW`

The Hebrew calendar is the name given to the calendar used by Jewish peoples around the world which developed into its current form in the early ninth century. It traditionally marks new days at sunset, not midnight. Its first day (1 Tishrei 1) primarily overlapped with Gregorian 7 September 3761 BCE and Julian 7 October 3761 BCE (starting at sunset on the 6th day of those months).

|Code | Name                                                   |
|:----|:-------------------------------------------------------|
|`TSH`| Tishrei (תִּשְׁרֵי) |
|`CSH`| Marcheshvan (מַרְחֶשְׁוָן) or Cheshvan (חֶשְׁוָן) |
|`KSL`| Kislev (כִּסְלֵו) |
|`TVT`| Tevet (טֵבֵת) |
|`SHV`| Shevat (שְׁבָט) |
|`ADR`| Adar I, Adar Rishon, First Adar, or Adar Aleph (אדר א׳) |
|`ADS`| Adar (אֲדָר); or Adar II, Adar Sheni, Second Adar, or Adar Bet (אדר ב׳) |
|`NSN`| Nisan (נִיסָן) |
|`IYR`| Iyar (אִייָר) |
|`SVN`| Sivan (סִיוָן) |
|`TMZ`| Tammuz (תַּמּוּז) |
|`AAV`| Av (אָב) |
|`ELL`| Elul (אֱלוּל) |

To keep the lunar-based months synchronized with the solar-based years, some years have Adar I and others do not, instead proceeding from Shevat directly to Adar II. However, in common (non-leap) years, it is common to simply write "Adar" not "Adar II", which users not aware of the distinction might incorrectly encode as `ADR` instead of `ADS`. It is recommended that systems knowing which years had Adar I and which did not replace `ADR` in common years with `ADS`.

No epoch marker is permitted in this calendar.

The URI for this calendar is `g7:cal-HEBREW`

## Dual dates

The day on which a new year began and the year number increased varied at different times and places during the use of the Gregorian and Julian calendars. For example, England measured the new year as 25 March until 1752, when it switched to 1 January as the new year. In periods of transition, or when writing after a change about dates occurring before a change, it was sometimes common to indicate 2 years with a slash, for example, "30 January 1648/49" meaning "1648 if you count the new year as coming after 30 January, 1649 if you count it as coming before 30 January". Other notations, such as abbreviations for phrases like "new style" and "old style", were also sometimes employed.

```gedcom
2 DATE 30 JAN 1649
3 PHRASE 30 January 1648/49
```

Many nations transitioned from using the Julian calendar to using the Gregorian calendar. This transition caused a change in dates by several days, which (depending on the date in question) could change the month and year as well. In periods of transition, or when writing after a change about dates occurring before a change, it was sometimes common to indicate 2 dates with slashes, for example "23/6 November/December 1907" meaning "Julian 23 November 1907, Gregorian 6 December 1907". Other notations, such as abbreviations for phrases like "new style" and "old style", were also sometimes employed.

```gedcom
2 DATE 6 DEC 1907
3 PHRASE 23/6 November/December 1907
```

Some documents also used slashes to indicate approximate dates, such as writing a birth year as "1903/4" when it was computed from a year-granularity age at a given date.

```gedcom
2 DATE BET 1903 AND 1904
3 PHRASE 1903/4
```


Versions 5.3 through 5.5.1 had special syntax for recording the first of these 3 concepts with a slash in the year. However, because slashes appear in historical documents with all 3 of the above meanings, some users misused this notation to record the other 2 situations as well. The result is ambiguity in the intended meaning of the resulting data. Version 7.0 removed the year slash notation; a `PHRASE` substructure should be used instead to clarify meaning.


## Calendars in date ranges and date periods

Calendars apply to the subsequent `date` production, not to the entire `DateValue`.
Hence,

- `DATE FROM 1670 TO 1800` means `DATE FROM GREGORIAN 1670 TO GREGORIAN 1800`
- `DATE FROM 1670 TO JULIAN 1800` means `DATE FROM GREGORIAN 1670 TO JULIAN 1800`
- `DATE FROM JULIAN 1670 TO 1800` means `DATE FROM JULIAN 1670 TO GREGORIAN 1800`

Because some systems may show dates as-is to users and because not all users understand the above rule, it is recommended that `calendar` tags be included if any `date` is non-`GREGORIAN`. It is recommended that the `calendar` tag be omitted if all `date`s in a payload are in the Gregorian calendar. Hence, the recommended forms of the previous 3 dates are

- `DATE FROM 1670 TO 1800`
- `DATE FROM GREGORIAN 1670 TO JULIAN 1800`
- `DATE FROM JULIAN 1670 TO GREGORIAN 1800`


</main>
