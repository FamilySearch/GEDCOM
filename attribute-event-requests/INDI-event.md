# Individual Events

This document tracks the set of Individual Events, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| `ADOP` | 3.0 | [Adoption](#adoption) |  |
| `CHRA` | 3.0 | [Adult Christening](#adult-christening) |  |
| `BAPM` | 3.0 | [Baptism](#baptism) |  |
| `BARM` | 4.0 | [Bar Mitzvah](#bar-mitzvah) |  |
| `BASM` | 4.0 | [Bat Mitzvah](#bat-mitzvah) |  |
| `BIRT` | 3.0 | [Birth](#birth) | Enumerated `BIRT.TYPE` values. |
| `BLES` | 3.0 | [Blessing](#blessing) |  |
| `BURI` | 3.0 | [Burial](#burial) |  |
| `CHR` | 3.0 | [Christening](#christening) |  |
| `CONF` | 3.0 | [Confirmation](#confirmation) |  |
| `CREM` | 5.4 | [Cremation](#cremation) | see "Burial" |
| `DEAT` | 3.0 | [Death](#death) |  |
| `EMIG` | 3.0 | [Emigration](#emigration) |  |
| `FCOM` | 4.0 | [First Communiion](#first-communiion) |  |
| `GRAD` | 4.0 | [Graduation](#graduation) |  |
| `IMMI` | 3.0 | [Immigration](#immigration) |  |
| `MEDI` | Proposed | [Medical Health](#medical-health) | This tag can be either an attribute or an event.  Some of these "types" could be an event or an attribute. |
| `NATU` | 3.0 | [Naturalization](#naturalization) |  |
| `ORDN` | 3.0 | [Ordination](#ordination) |  |
| `PROB` | 3.0 | [Probate](#probate) |  |
| `RETI` | 4.0 | [Retirement](#retirement) |  |
| \* | Proposed | [Stillbirth](#stillbirth) | see [Birth](#birth) `BIRT.TYPE` |
| `WILL` | 3.0 | [Will](#will) |  |
# Details
--------------------------
## Adoption
### Description
Creation of a legally approved child-parent relationship that does not exist biologically.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Adoption
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Adult Christening
### Description
Baptism or naming events for an adult person.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/AdultChristening
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Baptism
### Description
Baptism, performed in infancy or later. (See also [`BAPL`](#latter-day-saint-ordinances) and `CHR`.)

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI `http://gedcomx.org/Baptism`
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Bar Mitzvah
### Description
The ceremonial event held when a Jewish boy reaches age 13.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with http://gedcomx.org/BarMitzvah
- Used by the FamilySearch API via GEDCOM X
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/BarMitzvah`

--------------------------
## Bat Mitzvah
### Description
The ceremonial event held when a Jewish girl reaches age 13, also known as "Bat Mitzvah."

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/BatMitzvah
- Used by the FamilySearch API via GEDCOM X
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/BatMitzvah`

--------------------------
## Birth
### Description
- Birth/Born can be defined as coming into existence. This could mean either "Live Birth" or "Still Born".

-BIRT.TYPE enumeration options {Vaginal Birth, Cesarean Birth, Still Birth}

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with http://gedcomx.org/Birth
- Used by the FamilySearch API via GEDCOM X
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Birth`

--------------------------
## Blessing
### Description
Bestowing divine care or intercession. Sometimes given in connection with a naming ceremony.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Blessing
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Burial
### Description
Disposing of the mortal remains of a deceased person.

- Burial can be defined as the disposition of a decedent which can include: Inhumation, Burial at Sea, Cremation, Donation to Research, Lost, Natural, Green, Burial Tree or Scaffolding, cave and probably many other ones depending on culture. 
-The BURI event can can therefore have BURI.TYPE enumerations of: a) Inhumation, b) Burial at Sea, c) Cremation, d) Donation to Research, e) Lost, f) Natural, g) Green, h) Burial Tree or Scaffolding, i) cave, j) other/phrase

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with `http://gedcomx.org/Burial`
- Used by the FamilySearch API via GEDCOM X
*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md)* with URI `http://gedcomx.org/Burial`

--------------------------
## Christening
### Description
Baptism or naming events for a child.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with http://gedcomx.org/Christening
- Used by the FamilySearch API via GEDCOM X
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Christening`

--------------------------
## Confirmation
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Confirmation
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Cremation
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Cremation
- Used by the FamilySearch API via GEDCOM X
- Closely related to the Burial event if the `BURI.TYPE` enumeration was implemented.
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Cremation`

--------------------------
## Death
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Death
- Used by the FamilySearch API via GEDCOM X
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Death`

--------------------------
## Emigration
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Emigration
- Used by the FamilySearch API via GEDCOM X

--------------------------
## First Communiion
### Description
	A fact of a person's first communion in a church.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with http://gedcomx.org/FirstCommunion
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Graduation
### Description
A fact of a person's graduation from a scholastic institution, may include, public, private, trade, or other schools of study.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI `http://gedcomx.org/Graduation`
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Immigration
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Immigration
- Used by the FamilySearch API via GEDCOM X
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Immigration`

--------------------------
## Medical Health
### Description
Any medical or health related events/attributes that people like to record.  Since this can be a very open ended list, an Other/Phrase component as part of typification must be included as well as allowing for an `Event` to have a text value!

### Value
Found in the following historical records:

- Public Records
- Military Records
- Private journals, biographies, bibles, and obituaries

### Absence
- Found in many GEDCOM files in the wild.

### Used
- `MEDI.TYPE`: can provide a user-language-specific indication of the various concepts found in private and governmental documents.  A single event (this could be an attribute too!) HEAL with Typification of, a) disease, b) hospitalization, c) other/phrase (NOTE: It has been seen in the wild multiple cases where medical/health related events and attributes have been documented)

For Example:
```
1 MEDI amputation of right leg
2 TYPE surgery
```
```
1 MEDI contracted consumption as a child
2 TYPE disease
```

--------------------------
## Naturalization
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Naturalization
- Used by the FamilySearch API via GEDCOM X
- In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Naturalization`

--------------------------
## Ordination
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Ordination
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Probate
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Probate
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Retirement
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Retirement
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Stillbirth
### Description
Born dead or died shortly after birth (exact definitions vary by culture and time period).

In GEDCOM X as "A fact of a person's stillbirth."

### Value
Found in the following historical records:
*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's stillbirth."

### Absence
The most closely related structures are:

- `DEAT.AGE`: can express any specific meaning (< 0y, < 0d, etc), and had a special value for "stillborn" in 5.5.1 and before: that special value was removed from `AGE` payloads in 7.0 because it was not a valid age in any other context.
- `BIRT.TYPE`: can provide a user-language-specific indication of stillbirth; this is used as an example of `TYPE` in the 7.0 specification.

There are no similar proposals here.

### Used
- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/StillBirth`
- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X
- *In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's stillbirth."

--------------------------
## Will
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Will'
- Used by the FamilySearch API via GEDCOM X

--------------------------
