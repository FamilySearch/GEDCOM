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
| `BIRT` | 3.0 | [Birth](#birth) | Enumerated `BIRT.TYPE` values. |
| `BLES` | 3.0 | Blessing | |
| `BURI` | 3.0 | [Burial](#burial) |Enumerated `BURI.TYPE` values. |
| `CENS` | 3.0 | Census | |
| `CHR`  | 3.0 | [Christening](#christening) | |
| `CONF` | 3.0 | Confirmation | |
| `CREM` | 5.4 | [Cremation](#cremation) | |
| `DEAT` | 3.0 | [Death](#death) | |
| `EMIG` | 3.0 | Emigration | |
| `FCOM` | 4.0 | First Communion | |
| `GRAD` | 4.0 | Graduation | |
|  |  | [Health](#health) | Enumerated `HEAL.TYPE` values. |
| `IMMI` | 3.0 | [Immigration](#immigration) | |
|  |  | [Military Service](#military-service) | Enumerated `MILT.TYPE` values. |
| `NATU` | 3.0 | [Naturalization](#naturalization) | |
| `ORDN` | 3.0 | Ordination | |
| `PROB` | 3.0 | Probate | |
| `RETI` | 4.0 | Retirement | |
| | | [Stillbirth](#stillbirth) | perhaps `BIRT`.`TYPE Stillborn` or `DEAT`.`AGE 0y`? |
| `WILL` | 3.0 | Will  | |


# Details

--------------------------

## Bar Mitzvah

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/BarMitzvah`

--------------------------

## Bat Mitzvah

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/BatMitzvah`

--------------------------

## Birth

### Description

-Birth/Born can be defined as coming into existence.  This could mean either "Live Birth" or "Still Born". 

-`BIRT.TYPE` enumeration options {Vaginal Birth, Cesarean Birth, Still Birth}  
 
-In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Birth`

--------------------------

## Burial

### Description

-Burial can be defined as the disposition of a decedent which can include: Inhumation, Burial at Sea, Cremation, Donation to Research, Lost, Natural, Green, Burial Tree or Scaffolding, cave and probably many other ones depending on culture.
-The BURI event can can therefore have `BURI.TYPE` enumerations of: a) Inhumation, b) Burial at Sea, c) Cremation, d) Donation to Research, e) Lost, f) Natural, g) Green, h) Burial Tree or Scaffolding, i) cave, j) other/phrase

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Burial`

The most closely related structures are:

- `BURI`.`TYPE`: can provide a user-language-specific indication of multiple ways that a decedent can be "put to rest". 

--------------------------

## Christening

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Christening`

--------------------------

## Cremation

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Cremation`

The most closely related structures are:

-Closely related to the Burial event if the `BURI.TYPE` enumeration was implemented.

--------------------------

## Death

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Death`

--------------------------

## Health

### Description

Any health or medial related events/attributes that people like to record.  Since this can be a very open ended list, an Other/Phrase component as part of typification must be included as well as allowing for an `Event` to have a text value!

### Value

Found in the following historical records:

- Public Records
- Military Records
- Private journals, biographies, bibles, and obituaries

### Absence

The most closely related structures are:

- 

Related proposals include


### Used

-Several application have created a custom event called _MILT to support some aspect of Military Service

- `HEAL`.`TYPE` (or `MEDI.TYPE`: can provide a user-language-specific indication of the various concepts found in private and governmental documents.  A single event (this could be an attribute too!) HEAL with Typification of, a) disease, b) hospitalization, c) other/phrase (NOTE: It has been seen in the wild multiple cases where medical/health related events and attributes have been documented)

For Example:
```
1 HEAL amputation of right leg
2 TYPE surgery
```
--------------------------

## Immigration

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Immigration`

--------------------------

## Military Service

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's military service."

### Value

Found in the following historical records:

- Military induction papers
- Military records
- Military discharge papers
- Military awards and recognition
- Veteran registries and group memberships
- Private journals, biographies, and obituaries

### Absence

The most closely related structures are:

- 

Related proposals include

- GEDCOM-X has events "Military Induction" and "Military Discharge" which define the start and end of the military service

### Used

-Several application have created a custom event called _MILT to support some aspect of Military Service

- `MILT`.`TYPE`: can provide a user-language-specific indication of the various concepts found in serving in the military.  GEDCOM-X suggests multiple additions that are “military based” events. A single event MILT with Typification of, a) induction, b) rank, c) discharge, d) engagement, e) registration, f) deployment, g) other/phrase (NOTE: GEDCOM X has a dozen or more of these, some are subset of others (there are over 300 separation codes as part of a “discharge”. AWOL, Desertion being one)

For Example:
```
1 MILT
2 TYPE Induction
```

```
1 MILT Sergeant
2 TYPE Rank
```

```
1 MILT Battle of <name>
2 TYPE Engagement
```

--------------------------

## Naturalization

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Naturalization`

--------------------------

## Religion

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Religion`

--------------------------

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

