# Family Attributes

This document tracks the set of Family Attributes, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| \*     | 5.0 | [Childless](#childless) | encoded as `NCHI 0` |
| | | [Lived Together](#lived-together) | perhaps `RESI`? |
| `NCHI` | 5.0 | Number of children | |
| `RESI` | 3.0 | Residence | |
| | | [Separated](#separated) | |

# Details

## Childless

The assertion that a family does not have children can be made using the `NCHI` structure with payload "`0`".
This is distinct from simply not having any `CHIL` structures,
which might mean there are children that have not yet been added to the data.

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as a distinct stucture with URI `http://familysearch.org/v1/CoupleNeverHadChildren`

## Lived together

### Description

*proposed description missing*

*In [FamilySearch API documentation](https://www.familysearch.org/developers/docs/guides/facts)* without a definition

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- `FAM`.`RESI`: provides the place of residence for the couple, which generally implies they lived together. However, "lived together" is sometimes used as a euphemism for "acted as a couple without a preceding marriage ceremony," which is only indirectly implied by the presence of a `FAM`.`RESI`.
- `MARR`: some interpretations of living together as a couple and some definitions of marriage make living together a type of marriage; other definitions do not.

Related proposals include

- Common Law Marriage (in the Family Events document): some interpretations of common law marriage and cohabitation are very similar to one another


### Used

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/LivedTogether`

## Separated

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a couple's separation."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

There is no other structure that covers this event, as it can apply to couples that cohabitate
and are not married as well as to those who are married in some manner. And for those who are
married, some couples may separate and never actually file for or go through with a formal divorce.

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Separation`

- The CompGen [CompGen](https://www.compgen.de/) table of [custom GEDCOM tags](https://wiki.genealogy.net/GEDCOM/_Nutzerdef-Tag) shows:

    1. `_SEPR` used by Brother's Keeper for Windows 6, WebTrees, and Family Tree Maker for both DOS and Windows

    2. `SEPA` used by Reunion for MAC and Legacy
