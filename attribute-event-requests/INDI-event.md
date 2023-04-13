# Proposed Individual Events

This document tracks various proposed additions to the set of Individual Events in FamilySearch GEDCOM 7.
Guides for using this document can be found in the associated [README.md](README.md).


# Table of Proposals

| G7 Tag | v7.x| Name           | URIs | Notes |
|--------|-----|----------------|------|-------|
| `BARM` | 7.0 | Bar Mitzvah    | `http://gedcomx.org/BarMitzvah` | |
| `BASM` | 7.0 | Bat Mitzvah    | `http://gedcomx.org/BatMitzvah` | |
| `BIRT` | 7.0 | Birth          | `http://gedcomx.org/Birth` | |
| `BURI` | 7.0 | Burial         | `http://gedcomx.org/Burial` | |
| `CHR`  | 7.0 | Christening    | `http://gedcomx.org/Christening` | |
| `CREM` | 7.0 | Cremation      | `http://gedcomx.org/Cremation` | |
| `DEAT` | 7.0 | Death          | `http://gedcomx.org/Death` | |
| `IMMI` | 7.0 | Immigration    | `http://gedcomx.org/Immigration` | |
| `NATU` | 7.0 | Naturalization | `http://gedcomx.org/Naturalization` | |
|        |     | Stillbirth     | `http://gedcomx.org/Stillbirth` | perhaps `BIRT`.`TYPE Stillborn` or `DEAT`.`AGE 0y`? |

# Details of Proposals

## Stillbirth

### Description

Born dead or died shortly after birth (exact definitions vary by culture and time period).

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's stillbirth."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- `DEAT`.`AGE`: can express any specific meaning (`< 0y`, `< 0d`, etc), and had a special value for "stillborn" in 5.5.1 and before: that special value was removed from `AGE` payloads in 7.0 because it was not a valid age in any other context.
- `BIRT`.`TYPE`: can provide a user-language-specific indication of stillbirth; this is used as an example of `TYPE` in the 7.0 specification.

There are no similar proposals here.

### Used

- Part of the GEDCOM X specification <https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md>

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>

