# Individual Events

This document tracks the set of Individual Events, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| `ADOP` | 3.0 | Adoption | |
| `CHRA` | 5.0 | Adult Christening | |
| `BAPM` | 3.0 | Baptism | |
| `BARM` | 4.0 | [Bar Mitzvah](#bar-mitzvah) | |
| `BASM` | 4.0 | [Bat Mitzvah](#bat-mitzvah) | |
| `BIRT` | 3.0 | [Birth](#birth) | |
| `BLES` | 3.0 | Blessing | |
| `BURI` | 3.0 | [Burial](#burial) | one of several types of `BURI` |
| `CENS` | 3.0 | Census | |
| `CHR`  | 3.0 | [Christening](#christening) | |
| `CONF` | 3.0 | Confirmation | |
| `CREM` | 5.4 | [Cremation](#cremation) | sometimes encoded as `BURI` prior to 5.4 |
| `DEAT` | 3.0 | [Death](#death) | |
| `BURI` | 3.0 | [Depositing remains](#depositing-remains) | |
| `EMIG` | 3.0 | Emigration | |
| `FCOM` | 4.0 | First Communion | |
| `GRAD` | 4.0 | Graduation | |
| `IMMI` | 3.0 | [Immigration](#immigration) | |
| | | [Memorial Service](#memorial-service) | |
| `NATU` | 3.0 | [Naturalization](#naturalization) | |
| `ORDN` | 3.0 | Ordination | |
| `PROB` | 3.0 | Probate | |
| `RETI` | 4.0 | Retirement | |
| | | [Stillbirth](#stillbirth) | perhaps `BIRT`.`TYPE Stillborn` or `DEAT`.`AGE 0y`? |
| `WILL` | 3.0 | Will  | |


# Details

## Bar Mitzvah

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/BarMitzvah`

## Bat Mitzvah

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/BatMitzvah`

## Birth

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Birth`

## Burial

A subtype of [Depositing remains](#depositing-remains)

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Burial`

## Christening

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Christening`

## Cremation

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Cremation`

## Death

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Death`

## Depositing remains

### Description

Depositing the mortal remains of a deceased person.

### Value

Found in the following historical records:

- Church records
- Grave markers
- Tombs and Crypts
- Urns

### Absence

The most closely related structures are:

- `DEAT`: expresses that an individual died, which generally has a different date and place than the depositing of the remains.
- `CREM`: describes a transformation of the remains by fire; the resulting ashes may still be deposited.

Related proposals here include

- [Burial](#burial), which is one type of depositing remains


### Used

- In GEDCOM since version 3.0 as `BURI`


## Immigration

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Immigration`

## Memorial Service

### Description

An event to mark or remember the death or presumed death of an individual, such as a funeral, wake, celebration of life, or memorial service.

### Value

Found in the following historical records:

- Obituaries
- Memorial announcements and programs
- Church records

### Absence

The most closely related structures are:

- `DEAT`: expresses that an individaul died, which generally has a different date than the memorial.
- `BURI`: describes what was done with the remains of the individual, which may or may not coincide with a memorial serive.

### Used

- Funerals, one type of memorial service, are part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Funeral`



## Naturalization

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Naturalization`

## Religion

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Religion`


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

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/BarMitzvah`

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X

