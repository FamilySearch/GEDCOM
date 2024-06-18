# Family Events

This document tracks the set of Family Events, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| `ANUL` | 4.0 | [Annulment](#annulment) | |
| `CENS` | 3.0 | [Census](#census) | |
| | | [Child Recognition](#child-recognition) | |
| | | [Civil Union](#civil-union) | |
| | | [Common Law Marriage](#common-law-marriage) | perhaps `MARR`.`TYPE Common law`? |
| `DIV`  | 3.0 | [Divorce](#divorce) | |
| `DIVF` | 4.0 | [Divorce Filed](#divorce-filed) | |
| | | [Domestic Partnership](#domestic-partnership) | |
| `ENGA` | 4.0 | [Engagement](#engagement) | |
| | | [Family Story](#family-story) | perhaps Family Anecdote instead? |
| `MARR` | 3.0 | [Marriage](#marriage) | |
| `MARB` | 4.0 | [Marriage Bann](#marriage-bann) | |
| `MARC` | 4.0 | [Marriage Contract](#marriage-contract) | |
| `MARL` | 4.0 | [Marriage License](#marriage-license) | |
| `MARS` | 4.0 | [Marriage Settlement](#marriage-settlement) | |
| | | [Newspaper Marriage Notice](#newspaper-marriage-notice) | |
| | | [Separation](#separation) | |

# Details

## Annulment

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Annulment`

## Census

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Census`

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

## Civil Union

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "The fact of a civil union."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- `MARR`: can express a marriage of any type, potentially including civil unions.

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/CivilUnion`

- Used by [Find-My-Past](https://www.findmypast.com) but using the term `Civil Partnership` and exported using the `EVEN.CIVILP` tag.

- Used by [MyHeritage](https://www.myheritage.com) but using the term `Civil Marriage` and exported using the `MARL` tag.

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

- Used by [Find-My-Past](https://www.findmypast.com) and exported using the `EVEN.COMMONLAWMARRIAGE` tag.

## Divorce

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Divorce`

## Divorce Filed

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/DivorceFiling`

## Domestic Partnership

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "The fact of a domestic partnership."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- `MARR`: can express a marriage of any type, however a couple cohabitating in a domestic partnership need not be married although after a long enough period of time it may qualify as a common law marriage.

Related proposals include

- Lived Together (in the Family Attributes document)

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/DomesticPartnership`

- Used by [MyHeritage](https://www.myheritage.com) but using the label **Partners** and exported using `EVEN` tag with `TYPE` of `Partners`

## Engagement

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Engagement`

## Family Story

### Description

A story about an incident that happened to a family unit at a point in time.

### Value

Found in the following historical records:

- Interviews.
- Newspaper articles.

### Absence

Would be handled by a generic `EVEN` tag today.

### Used

- Used by [Find-My-Past](https://www.findmypast.com) and exported using `EVEN.FAMSTORY` tag.

- Used by [MyHeritage](https://www.myheritage.com) but using the label **Anecdote** and exported using `EVEN` tag with `TYPE` of `Anecdote`

## Marriage

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Marriage`

## Marriage Bann

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/MarriageBanns`

## Marriage Contract

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/MarriageContract`

## Marriage License

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/MarriageLicense`

## Marriage Settlement

Missing in [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md)

## Newspaper Marriage Notice

### Description

A newspaper article or notice about a marriage.

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) under **MarriageNotice** as* "The fact of a marriage notice."

### Value

Found in the following historical records:

- Newspapers.

### Absence

Would be handled by a generic `EVEN` tag today.

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/MarriageNotice`

- Used by [Find-My-Past](https://www.findmypast.com) and exported using `EVEN.MRRGNOTICE` tag

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

- Used by [Ancestry.com](https://ancestry.com) and exported using `_SEPR` tag.

- Used by [FindMyPast](https://findmypast.com) and exported using `SEPA` tag.

- Used by [MyHeritage](https://www.myheritage.com) and exported using `EVEN` tag with `TYPE` of `Separation`
