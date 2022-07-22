> This file almost certainly doesn't belong here, but I'm not sure where it does belong so I'm staging it here for now.

# YAML descriptions

This page documents the organization of YAML documents delivered at the URIs of the standard tags in the FamilySearch GEDCOM 7 specification and the gedcom.io extension tag registry. The YAML documents are not part of the standard itself, and while the intent is that they remain stable and usable in the long term, if a valid reason arises they may be changed independently of the versioning process.

YAML documents in this form are used to define

- Structure types
- Enumeration values
- Calendars
- Months
- Known payloads for URI-valued structures

For ease of presentation, we call whatever a YAML document is describing a "concept".

## Readable YAML

The files are provided in [YAML 1.2](https://yaml.org).
YAML was chosen because it is readily parseable in many programming languages
and it *can* be presented in a human-readable way.
Because YAML provides many formatting options, using a readable style is an option, not a guarantee, and should be considered when preparing the YAML documents.

The YAML should use only [untagged nodes](https://yaml.org/spec/1.2.2/#resolved-tags) with types `seq`, `map`, and `str` from the [fail safe schema](https://yaml.org/spec/1.2.2/#failsafe-schema)
and `null` from the [JSON schema](https://yaml.org/spec/1.2.2/#json-schema).

Long strings should be wrapped to keep the YAML under 80 columns if feasible.
Strings containing newlines should be presented using the [literal block style](https://yaml.org/spec/1.2.2/#literal-style).
Strings without newlines may presented in and [flow style](https://yaml.org/spec/1.2.2/#73-flow-scalar-styles)
(though note the restrictions on [plain style strings](https://yaml.org/spec/1.2.2/#plain-style)).

[Sequences](https://yaml.org/spec/1.2.2/#821-block-sequences) and [mappings](https://yaml.org/spec/1.2.2/#822-block-mappings) should be in the block style unless they are empty, in which case a [flow style](https://yaml.org/spec/1.2.2/#74-flow-collection-styles) should be used instead.
The top-level mapping should have a blank line between each mapping entry.

To ease machine identification of YAML blocks, [document markers](https://yaml.org/spec/1.2.2/#912-document-markers) are recommended. In particular, documents should begin with a YAML directive "`%YAML 1.2`" and directives end marker "`---`" and end with a document end marker "`...`".

## YAML document schemata

Each YAML document is a `map` with `str` keys.
Each has a key "`type`" with one of a small set of strings, listed below, as its value.
For readability, the `type` should be the first entry in the YAML document and both the key and value should be provided as plain scalars.

The valid `type`s are

- `structure`
- `enumeration`
- `calendar`
- `month`
- `datatype`
- `uri` <span style="color:red">I think `uri` is better than `legacy` for registering non-tagged URIs like EXID.TYPEs</span>

| Key | Value Type | Required by `type` | Permitted by `type` |
|-----|------------|-------------|--------------|
| `calendars` | `seq` of *uri* | `month` | |
| `descriptions` | `seq` of `str` | all | |
| `documentation` | `seq` of *uri* | | all |
| `enumeration values` | `map` of *tag* to *uri*<br/> <span style="color:red">change to `seq` of *uri*?</span> | | `structure` |
| `explanation` | `map` of *lang* to `str` | | all |
| `extension tags` | `seq` of *extTag* | | `structure`, `enumeration`, `calendar`, `month` |
| `label` | `map` of *lang* to `str` | | all |
| `months` | `seq` of *uri* | `calendar` | |
| `payload` | *type* | `structure` |
| `standard tag` | *stdTag* | *special* | *special* | 
| `substructures` | `map` of *uri* to *card* | `structure` | |
| `superstructures` | `map` of *uri*\* to *card* | `structure` | |
| `type` | `str` from a set listed here | all | |
| `uri` | *uri* | all | |
| `used by` | `seq` of *uri* | `enumeration` | |

\* `superstructures` (only) permits the string "`HEAD psuedostructure`" as if it were a URI

In the above table,

- *stdTag* means a `str` matching production `stdTag`
- *extTag* means a `str` matching production `extTag`
- *tag* means a `str` matching production `tag`
- *uri* means a `str` that is a URI
- *lang* means a `str` in the datatype Language
- *type* means one of the following:
    - `null`
    - a `str` that is the URI of a datatype
    - a `str` that is the URI of a structure type delimited by `@` characters
    - the specific `str` "`Y|<NULL>'"
- *card* means one of the following four `str`: "`{0:1}`", "`{0:M}`", "`{1:1}`", or "`{1:M}`"

Notes about specific items follow:

- `calendars` is a list (in no particular order) of the URIs of calendars that use this month.
    
    The list may be incomplete, as a new calendar might be defined that uses an existing month.

- `descriptions` is a list (in no particular order) of descriptions of the concept the YAML document is defining. Descriptions may be given in any language; it is recommended that at least one English-language description be included.
    
    Descriptions are generally programmer-centric; for user-centric text, see `label` and `explanation`

- `documentation` may provide one or more external URLs where additional documentation can be found. If there is no such URL, this entry should be omitted.

- `enumeration values` is used when the `payload` is <https://gedcom.io/terms/v7/type-Enum> or <https://gedcom.io/terms/v7/type-List#Enum> and provides a list of URIs of enumeration values supported by the structure.

    The listed URIs needn't identify only enumeration values:
    some structures explicitly enumerate other concepts,
    such as <https://gedcom.io/terms/v7/SOUR-EVEN> enumerating even types.

    The list may be incomplete, as a new enumeration values might be defined that may be included in existing structures.

- `explanation` provides recommended detailed descriptions to show to users, potentially in several languages.

    Explanations are user-centric; for programmer-centric explanations of the concept, see `description`.
    
    Explanations may be lengthy; for brief text to use in UI elements, see `label`.

- `extension tags` are provided in-order, with the most-preferred tag first.

    Standard structures may have an `extension tags` entry to list *fully compatible* extensions that predated the standard and can be converted to the `standard tag` without any other modification.

- `label` provides recommended brief names or labels to show to users, potentially in several languages.

    Labels are user-centric; for programmer-centric explanations of the concept, see `description`.
    
    Labels are short to fit in forms and other constrained-space UI elements; for more detailed text see `explanation`.

- `months` is a list of all of the months used in the given calendar. They are listed in the order they appear in a year to facilitate chronological sorting.
    
    The list should be taken as exhaustive. Extensions may not add new months to existing calendars.

- `payload` indicates the payload type of the given structure.
    Datatypes and "`Y|<NULL>'" have the same meaning they do in the standard.
    `null` means no payload is permitted.
    Pointers are indicated by `@`URI`@` instead of `@<XREF:`tag`>@` to support extensions as well as standard structures.
    
- `standard tag` may only be used for concepts given a tag in the standard document itself.

- `substructures` and `superstructures` express how structures may be nested, and with what cardinality.
    
    Because new structures may be added over time in any order,
    *x* may be a substructure of *y* if
    either *x*'s `superstructures` includes *y* 
    or *y*'s `substructures` includes *x*.
    
    The cardinality of a substructure/superstructure relationship must be the same if it is listed in both a `substructures` entry and a  superstructures` entry.
    
    If `superstructures` is an empty `map`, then the structure is a record and must not appear in any other structure's `substructures`.


- `type` is one of the following values:

    | `type` | YAML describes |
    |--------|---------|
    | `structure`   | a structure type   |
    | `enumeration` | an enumeration value |
    | `calendar`    | a calendar |
    | `month`       | month in some calendar |
    | `datatype`    | payload datatype |
    | `uri`         | another URI of general interest, such as a known `EXID`.`TYPE |

- `uri` is the canonical URI of the concept the YAML document describes.
    
    In general this will not be the same as the URL of the document that describes it; for example the document with URL <https://gedcom.io/terms/v7/type-List.html> describes the datatype with URI `https://gedcom.io/terms/v7/type-List`.
    
    <span style="color:red">How (if at all) should we handle cases where two implementers create distinct URIs for the same concept?</span>

- `used by` lists structure types that are known to use this concepts as an enumeration value.
    
    The list may be incomplete, as a new structure type might be defined re-uses and existing enumeration value.

    <span style="color:red">Should <https://gedcom.io/terms/v7/CHR> have a `used by` entry with <https://gedcom.io/terms/v7/NO> and <https://gedcom.io/terms/v7/SOUR-EVEN> in the list? If not, is there another way to denote that relationship? If so, should we rename "`used by`" to a more descriptive phrase like "`enumerated by`" or "`enumeration value of`"?</span>


