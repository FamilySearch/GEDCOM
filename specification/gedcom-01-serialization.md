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

Each **structure type** is identified by a URI and defines several properties of any structure with that type, including

- The meaning of structures of this type.
- The payload type of the structure's payload, which shall be one of
    - no payload, or
    - a pointer to a record with a specific structure type, or
    - a [data type](#datatypes);
        if an [enumeration](#enumeration) or [list of enumerations](#list), also a set of permitted enumeration values.
- Which structure types may appear as substructures of the structure and with what **cardinality** they may appear.
    Cardinality is specified by two flags:
    
    - whether a substructure of this type is required or not; and
    - whether multiple substructures of this type are permitted or not.

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

The same tag may be used to represent multiple structure types.
The structure type of each structure is identified by its tag and the type of its superstructure.
The mapping between (superstructure type, tag) pairs and structure types
is given elsewhere in this document (for standard structure types and tags)
or the [schema] and extension authors' documentation (for extension structure types and tags).

:::example
The tag `ADOP` is used in this document to represent two structure types.
Which one is meant can be identified by the superstructure type as follows:

| Superstructure type | Structure type identified by tag `ADOP` |
|------------------|------------------|
| `g7:record-INDI` | `g7:ADOP`        |
| `g7:ADOP-FAMC`   | `g7:FAMC-ADOP`   |

An [extension-defined substructure](#extensions) could also be used to place either of these structure types in extension superstructures.

The `ADOP` tag is also used in the set of enumerated values permitted by the `g7:DATA-EVEN`, `g7:SOUR-EVEN`, and `g7:NO` structure types.
:::

The **line value** matches production `LineVal` and encodes the structure's payload.
Line value content is sufficient to distinguish between pointers and line strings.
Pointers are encoded as the cross-reference identifier of the pointed-to structure.
Each non-pointer payload may be encoded in 1 or more line strings (line continuations encode multi-line payloads in several line strings).
The exact encoding of non-pointer payloads is dependent on the data type of the payload, as determined by the structure type.
The data type of non-pointer payloads cannot be fully determined by line value content alone.

Note that production `LineVal` does not match the empty string.
Because empty payloads and missing payloads are considered equivalent,
both a structure with no payload
and a structure with the empty string as its payload
are encoded with no `LineVal` and no space after the `Tag`.

:::example
The payload of a `MARR` structure has type `[Y|<NULL>]`, which is optional but if present cannot be the empty string.
The payload of a `EVEN` structure has type `Text`, which is not optional but can be the empty string.
The `Line` encoding a no-payload `MARR` is "`1 MARR`"
and the `Line` encoding an empty-payload `EVEN` is "`1 EVEN`";
both `Line`s have no `LineVal` and no trailing space.
:::


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

This specification also provides multiple ways for extension authors to go beyond the specification without submitting a feature request, which are described in the remainder of this section.

Extensions can introduce new structure types, new enumeration values, new calendars with their associated months, and new data types.
They can also extend existing structures with new permitted substructure types and extend existing enumeration-type payloads with new permitted values.
Extensions cannot change existing meanings, cardinalities, or calendars.

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
- Even though both `DATE`s appear to have `g7:type-DATE` payloads, we can't know that is the intended data type without consulting the defining specifications of `_LOC` and `_POP`, respectively. The first might be a `g7:type-DATE#period` and the second a `g7:type-DATE#exact`, for example.
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

Note that at the time of writing, the [FOAF](https://xmlns.com/foaf/spec/20140114.html) URIs used in this example are not URLs.
:::

The meaning of a documented extension tag is identified by its superstructure type and its URI, not its tag.
As such each documented extension tag needs its own URI: it is its URI, not its tag, that defines its meaning.
Documented extension tags can be changed freely by modifying the schema,
though it is recommended that documented extension tags not be changed.
However, a tag change may be necessary if a product picks the same tags for URIs that another product uses for different URIs.
A given schema should map only one tag to each URI.

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

It is recommended that the URIs used for documented extension tags be URLs that can be used to access documentation for the meaning of the tag.

:::note
The W3C has an [interest group note](http://www.w3.org/TR/cooluris/)
that discusses several ways of achieving this URI/URL mapping,
including how a single webpage can describe multiple tags
using either HTTP redirects (which requires some server setup)
or what they call "Hash URIs" (which require no setup).

That interest group note also explains why it might be desirable
to have a separate URIs for a concept and the document describing that concept.
Because of the structure of the schema, that separation is less important for FamilySearch GEDCOM 7
than it is for the semantic web, but it remains good advice where feasible.
:::

An extension tag that is not given a URI in the schema structure is called an **undocumented extension tag**.
The meaning of an undocumented extension tag is identified by its superstructure type and its tag.


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

If removal of a structure makes the superstructure invalid because the superstructure required the substructure, the structure should instead be retained and have its payload changed to a `voidPtr` if a pointer, or to a data type-appropriate empty value if a non-pointer.

If removing a structure leaves its superstructure with no payload and no substructures, the superstructure should also be removed.

A structure can also be removed if it provides no new information.  For example,
```gedcom
0 @I1@ INDI
1 NAME John /Doe/
1 NAME John /Doe/
1 FAMC @F1@
1 FAMC @F1@
0 @F1@ FAM
1 CHIL @I1@
1 CHIL @I1@
```

provides no information beyond the simpler form:
```gedcom
0 @I1@ INDI
1 NAME John /Doe/
```
