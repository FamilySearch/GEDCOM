# Individual Attributes

This document tracks the set of Individual Attributes, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| \* | Proposed | [Affiliation](#affiliation) | see [Nationality](#nationality) |
| `CAST` | 5.0 | [Caste](#caste) |  |
| \* | 5.0 | [Childless](#childless) | encoded as `NCH 0` |
| \* |  | [Clan](#clan) |  |
| \* | 3.0 | [Died Before Eight](#died-before-eight) | encoded as `DEAT.AGE` <8y |
| `DNA` | Proposed | [DNA](#dna) | enumerated `DNA.TYPE` |
| `EDUC` | 4.0 | [Education](#education) |  |
| \* | Proposed | [Ethnicity](#ethnicity) |  |
| \* | Proposed | [Heimat](#heimat) |  |
| `IDNO` | 5.3 | [Identifying Number](#identifying-number) |  |
| \* | Proposed | [Life Sketch](#life-sketch) |  |
| `MILT` | Proposed | [Military Service](#military-service) | This be an "Event" Enumerate `MILT.TYPE` to add additional military related items. |
| `IDNO` | 5.0 | [National ID](#national-id) | see also `SSN` |
| `NATI` | 5.0 | [Nationality](#nationality) |  |
| `TITL` |  | [Nobility Title](#nobility-title) |  |
| `NCHI` |  | [Number of Children](#number-of-children) |  |
| `NMR` | 5.0 | [Number of Marriages](#number-of-marriages) | really number of `FAMS` links; marriage not required |
| `OCCU` | 3.0 | [Occupation](#occupation) |  |
| `DSCR` | 5.0 | [Physical Description](#physical-description) |  |
| `PROP` | 3.0 | [Property](#property) |  |
| `RELI` | 3.0 | [Religion](#religion) |  |
| `RESI` | 3.0 | [Residence](#residence) |  |
| \* | Proposed | [Single](#single) |  |
| `SSN` |  | [Social Security Number](#social-security-number) | the USA's `IDNO` equivalent |
| \* | Proposed | [Tribe](#tribe) | see [Nationality](#nationality) |
# Details
--------------------------
## Affiliation
### Description
*proposed description missing*

*In [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts)* documentation without a definition

### Value
Found in the following historical records:

- (records not yet identified)

### Absence
The most closely related structures are:

Related proposals include

- Clan: *difference from Affiliation not yet articulated*
- Tribe: *difference from Affiliation not yet articulated*
- Ethnicity: *difference from Affiliation not yet articulated*
- Heimat: *difference from Affiliation not yet articulated*

### Used
- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/Affiliation`

--------------------------
## Caste
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Caste
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Childless
### Description
The assertion that a family does not have children can be made using the `NCHI` structure with payload "0". 
This is distinct from simply not having any `CHIL` structures, which might mean there are children that have not yet been added to the data.

### Value


### Absence


### Used
- Part of the GEDCOM X specification as a distinct stucture with URI http://familysearch.org/v1/CoupleNeverHadChildren

--------------------------
## Clan
### Description
*proposed description missing*
*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as*  "A fact of a person's clan."

### Value
Found in the following historical records:

- (records not yet identified)

### Absence
The most closely related structures are:

Related proposals include

- Tribe: *difference from Clan not yet articulated*
- Ethnicity: *difference from Clan not yet articulated*
- Heimat: *a place, often as a disambiguation of family name or lineage. Clan suggests group identity, not geography*
- Affiliation: *generally by choice or appointment, while clan generally indicates something assigned to a person at birth*

### Used


- [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Clan`
- [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X.

--------------------------
## Died Before Eight
### Description
The assertion that a person died before the end of their eighth year of life can be made using the `DEAT` structure with an AGE substructure with payload "< 8y".

### Value


### Absence


### Used
- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI http://familysearch.org/v1/DiedBeforeEight

--------------------------
## DNA
### Description


### Value


### Absence


### Used
Proposed Use And Examples

-DNA.TYPE: can provide a user-language-specific indication of the various types of DNA

```
1 DNA Haplogroup H
2 TYPE mtDNA
```

```
1 DNA Haplogroup R1
2 TYPE Y-DNA
```

--------------------------
## Education
### Description
A fact of an education or an educational achievement (e.g., diploma, graduation, scholarship, etc.) of a person.

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Education
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Ethnicity
### Description
In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as "A fact of a person's ethnicity."

### Value
Found in the following historical records:

- (records not yet identified)

### Absence
The most closely related structures are:

Related proposals include

- Tribe: *difference from Ethnicity not yet articulated*
- Clan: *difference from Ethnicity not yet articulated*
- Heimat: *a place, often as a disambiguation of family name or lineage. Ethnicity suggests group identity, not geography*
- Affiliation: *generally an organized group by choice or appointment, while ethnicity generally indicates a broader culture my self-identification*

### Used
- [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Ethnicity`
- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X.

--------------------------
## Heimat
### Description
A geographic place to which a person is affiliated by birth or ancestry, but not necessarily by residence or property.

In GEDCOM X as "A fact of a person's _heimat_. "Heimat" refers to a person's affiliation by birth to a specific geographic place. Distinct heimaten are often useful as indicators that two persons of the same name are not likely to be closely related genealogically. In English, "heimat" may be described using terms like "ancestral home", "homeland", or "place of origin".

### Value
Found in the following historical records:

- (records not yet identified)

### Absence
The most closely related structures are:

Related proposals include

- Ethnicity: ethnicities typically have some geographic association, but generally much larger and less fine-grained than a heimat
- Tribe: members of a tribe may share a heimat, but tribes may be defined by other characteristics too
- Clan: members of a clan may share a heimat, but clans may be defined by other characteristics too
- Bürgerort: a place, often as a disambiguation of family name or lineage.
- Affiliation: a person with a given heimat needn't have any affiliation with others with the same heimat

### Used
- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Heimat`
- *Not* used by the FamilySearch API, the GEDCOM-X implementation with the largest user base; see <https://www.familysearch.org/developers/docs/guides/facts>

--------------------------
## Identifying Number
### Description
[GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) has a subset of these (only those issued by nations) under [National Id](#national-id).

### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Adoption
- Used by the FamilySearch API via GEDCOM X
- GEDCOM X has a subset of these (only those issued by nations) under National Id.

--------------------------
## Life Sketch
### Description
*proposed description missing*

*In [FamilySearch API documentation](https://www.familysearch.org/developers/docs/guides/facts)* without a definition

### Value


### Absence
The most closely related structures are:

- `NOTE`: a life sketch is not a historical attribute in the usual sense (it lacks a date, place, associated individuals, etc). There is a proposal ([issue #219](https://github.com/FamilySearch/GEDCOM/issues/219)) to add note type to cover this instead of a new attribute.

There are no similar proposals here

### Used
- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/LifeSketch`
- Used by Ancestry, under the name "Life Story"
- Used by FindAGrave, under the name "Bio Information"

--------------------------
## Military Service
### Description
*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as*  "A fact of a person's military service."

### Value
Found in the following historical records:

- Military induction papers
- Military records
- Military discharge papers
- Military awards and recognitions
- Veteran registries and group memberships
- Private journals, biographies, and obituaries

### Absence
The most closely related structures are:

Related proposals include:

- GEDCOM-X has events "Military Induction" and "Military Discharge" which define the start and end of the military service

### Used
- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/MilitaryService`
- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X.

Several application have created a custom event called _MILT to support some aspect of Military Service

- `MILT`.`TYPE`:  enumeration can provide a user-language-specific indication of the various concepts found in serving in the military.  GEDCOM-X suggests multiple additions that are “military based” events. A single event MILT with Typification of, a) induction, b) rank, c) discharge, d) engagement, e) registration, f) deployment, g) other/phrase (NOTE: GEDCOM X has a dozen or more of these, some are subset of others (there are over 300 separation codes as part of a “discharge”. AWOL, Desertion being one)

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
## National ID
### Description
In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/NationalId`.
A special case of [Identifying number](#identifying-number)

### Value


### Absence


### Used


--------------------------
## Nationality
### Description
An individual’s national heritage or origin, or other folk, house, kindred, lineage, or tribal interest.

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Nationality`

### Value


### Absence


### Used


--------------------------
## Nobility Title
### Description
The title given to or used by a person, especially of royalty or other noble class within a locality.

### Value
In [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/TitleOfNobility`

### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Used by the FamilySearch API http://familysearch.org/v1/TitleOfNobility

--------------------------
## Number of Children
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/NumberOfChildren
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Number of Marriages
### Description


### Value


### Absence


### Used


--------------------------
## Occupation
### Description


### Value
In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Occupation`

### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Occupation
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Physical Description
### Description


### Value
In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/PhysicalDescription`

### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/PhysicalDescription
- Used by the FamilySearch API via GEDCOM X

DESC.TYPE: can provide a user-language-specific indication of multiple aspects of an individual's physical description.  Enumerated example: {height, weight, eye color, tattoos, skin color, hair color, scars, lost limbs, other/phrase}.

For example:
```
1 DESC Brown
2 TYPE Hair Color
```

--------------------------
## Property
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Property
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Religion
### Description


### Value
In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Religion`

### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Religion
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Residence
### Description


### Value
In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Residence`

### Absence


### Used
- Part of the GEDCOM v7.0 Specification
- Part of the GEDCOM X specification with URI http://gedcomx.org/Residence
- Used by the FamilySearch API via GEDCOM X

--------------------------
## Single
### Description
The assertion that a person is not a partner in a family can be made using the `NMR` structure with payload "0". 
This is distinct from simply not having any FAMS structures, which might mean there are relationships that have not yet been added to the data.

### Value


### Absence


### Used
- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI http://familysearch.org/v1/NoCoupleRelationships

--------------------------
## Social Security Number
### Description


### Value


### Absence


### Used
- Part of the GEDCOM v7.0 Specification

--------------------------
## Tribe
### Description
*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's tribe."

*In [FamilySearch API documentation](https://www.familysearch.org/developers/docs/guides/facts)* without a definition, and with a different URI than that used by GEDCOM-X

### Value
Found in the following historical records:

- (records not yet identified)

### Absence
The most closely related structures are:

Related proposals include:

- Clan: *difference from Tribe not yet articulated*
- Ethnicity: *difference from Tribe not yet articulated*
- Heimat: a place, often as a disambiguation of family name or lineage. Tribe suggests group identity, not geography
- Affiliation: generally by choice or appointment, while tribe generally indicates something assigned to a person at birth

### Used
- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Tribe`

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/TribeName`

--------------------------
