# Proposed Family Events

This document tracks various proposed additions to the set of Family Events in FamilySearch GEDCOM 7.
Guides for using this document can be found in the associated [README.md](README.md).


# Table of Proposals

| G7 Tag | v7.x| Name           | URIs | Notes |
|:------:|-----|----------------|------|-------|
| `ANUL` | 7.0 | Annulment | `http://gedcomx.org/Annulment` | |
|        |     | [Common Law Marriage](#common-law-marriage) | `http://gedcomx.org/CommonLawMarriage` | perhaps `MARR`.`TYPE Common law`? |
| `DIV`  | 7.0 | Divorce | `http://gedcomx.org/Divorce` | |
| `MARR` | 7.0 | Marriage | `http://gedcomx.org/Marriage` | |

# Details of Proposals


## Common Law Marriage

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* " The fact of a marriage by common law."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- `MARR`: can express a marriage of any type, potentially including common law marriages. Common law marriages can differ from other marriages, however, in that they may lack a ceremony or event marking the entrance into the married state.

Related proposals include

- Lived Together (in the Family Attributes document): some interpretations of common law marriage and cohabitation are very similar to one another

### Used

- Part of the GEDCOM X specification <https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md>

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>
