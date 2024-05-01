# Family Events

This document tracks the set of Family Events, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| `ANUL` | 4.0 | [Annulment](#annulment) | |
| `CENS` | 3.0 | Census | |
| | | [Child recognition](#child-recognition) | |
| | | [Common Law Marriage](#common-law-marriage) | perhaps `MARR`.`TYPE Common law`? |
| `DIV`  | 3.0 | [Divorce](#divorce) | |
| `DIVF` | 4.0 | Divorce Filed | |
| `ENGA` | 4.0 | Engagement | |
| `MARR` | 3.0 | [Marriage](#marriage) | |
| `MARB` | 4.0 | Marriage Bann | |
| `MARL` | 4.0 | Marriage License | |
| `MARS` | 4.0 | Marriage Settlement | |
| | | [Separation](#separation) | |

# Details

## Annulment

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Annulment`

## Child Recognition

### Description

A legal action which grants a parent-child relationship between a child and a parent; often as part of legitimizing a step-parent relationship or as legal recognition of a biological relationship that was not recognized at the time of birth.

### Value

Found in the following historical records

- As "reconnaissance d'enfant" in legal registries in France
- As "Legitimation" in legal registries in Germany

### Absence

The most closely related structures are:

- `ADOP`: both events establish a legal parent relationship after birth. In some countries they are the same as one another; in other countries they have different criteria and/or legal ramifications.

### Used

Applications using this structure have not yet been identified.

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

## Separation

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a couple's separation."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

There is no other structure that covers this event, as it can apply to couples that cohabitate and are not married as well as to those who are married in some manner. And for those who are married, some couples may separate and never actually file for or go through with a formal divorce.

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Separation`

- The CompGen [CompGen](https://www.compgen.de/) table of [custom GEDCOM tags](https://wiki.genealogy.net/GEDCOM/_Nutzerdef-Tag) shows:

    1. `_SEPR` used by Brother's Keeper for Windows 6, WebTrees, and Family Tree Maker for both DOS and Windows

    2. `SEPA` used by Reunion for MAC and Legacy
