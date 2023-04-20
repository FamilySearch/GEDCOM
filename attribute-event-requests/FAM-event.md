# Family Events

This document tracks the set of Family Events, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| `ANUL` | 4.0 | [Annulment](#annulment) | |
| `CENS` | 3.0 | Census | |
| | | [Common Law Marriage](#common-law-marriage) | perhaps `MARR`.`TYPE Common law`? |
| `DIV`  | 3.0 | [Divorce](#divorce) | |
| `DIVF` | 4.0 | Divorce Filed | |
| `ENGA` | 4.0 | Engagement | |
| `MARR` | 3.0 | [Marriage](#marriage) | |
| `MARB` | 4.0 | Marriage Bann | |
| `MARL` | 4.0 | Marriage License | |
| `MARS` | 4.0 | Marriage Settlement | |

# Details

## Annulment

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Annulment`

## Common Law Marriage

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "The fact of a marriage by common law."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- `MARR`: can express a marriage of any type, potentially including common law marriages. Common law marriages can differ from other marriages, however, in that they may lack a ceremony or event marking the entrance into the married state.

Related proposals include

- Lived Together (in the Family Attributes document): some interpretations of common law marriage and cohabitation are very similar to one another

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/CommonLawMarriage`

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X.

## Divorce

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Divorce`

## Marriage

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Marriage`
