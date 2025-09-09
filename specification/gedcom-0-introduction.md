---
title: The FamilySearch GEDCOM Specification
subtitle: 7.0.16
email: GEDCOM@FamilySearch.org
copyright: |
    :::{style="page-break-after: always;page-break-before: always;"}
    Copyright 1984–2025 Intellectual Reserve, Inc. All rights reserved. A service provided by The Church of Jesus Christ of Latter-day Saints.
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
    > <http://www.apache.org/licenses/LICENSE-2.0>
    
    Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
    
     
    
    In accordance with the Apache 2.0 license that governs this work, any other work that is based on or derived from this work must include a readable copy of the following NOTICE. For more information, please refer to the full copy of the Apache 2.0 license.
    
    > NOTICE:
    > 
    > This work comprises, is based on, or is derived from the FAMILYSEARCH GEDCOM™ Specification, © 1984-2025 Intellectual Reserve, Inc. All rights reserved.
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

