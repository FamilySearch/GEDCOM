# Proposed Family Attributes

This document tracks various proposed additions to the set of Family Attributes in FamilySearch GEDCOM 7.
Guides for using this document can be found in the associated [README.md](README.md).


# Table of Proposals

| G7 Tag | v7.x| Name           | URIs | Notes |
|:------:|-----|----------------|------|-------|
| \*     | 7.0 | Childless | `http://familysearch.org/v1/CoupleNeverHadChildren` | in 7.0 as `NCH 0` |
|        |     | [Lived Together](#lived-together) | `http://familysearch.org/v1/LivedTogether` | perhaps `RESI`? |

# Details of Proposals

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

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>
