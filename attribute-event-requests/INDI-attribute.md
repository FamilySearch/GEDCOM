# Proposed Individual Attributes

This document tracks various proposed additions to the set of Individual Attributes in FamilySearch GEDCOM 7.
Guides for using this document can be found in the associated [README.md](README.md).


# Table of Proposals

| G7 Tag | v7.x| Name           | URIs | Notes |
|:------:|-----|----------------|------|-------|
|        |     | [Affiliation](#affiliation) | `http://familysearch.org/v1/Affiliation` | |
| `CAST` | 7.0 | Caste | `http://gedcomx.org/Caste` | |
| \*     | 7.0 | Childless | `http://familysearch.org/v1/NoChildren` | in 7.0 as `NCH 0` |
|        |     | [Clan](#clan) | `http://gedcomx.org/Clan` | |
| \*     | 7.0 | Died Before Eight | `http://familysearch.org/v1/DiedBeforeEight` | in 7.0 as `DEAT`.`AGE <8y` |
|        |     | [Ethnicity](#ethnicity) | `http://gedcomx.org/Ethnicity` | |
|        |     | [Heimat](#heimat) | `http://gedcomx.org/Heimat`| |
|        |     | [Life Sketch](#life-sketch) | `http://familysearch.org/v1/LifeSketch` | |
|        |     | [Military Service](#military-service) | `http://gedcomx.org/MilitaryService` | |
| `IDNO` | 7.0 | National Id | `http://gedcomx.org/NationalId` | also `SSN` for USA only |
| `NATI` | 7.0 | Nationality | `http://gedcomx.org/Nationality` | |
| `OCCU` | 7.0 | Occupation | `http://gedcomx.org/Occupation` | |
| `DESC` | 7.0 | Physical Description | `http://gedcomx.org/PhysicalDescription` | |
| `RELI` | 7.0 | Religion | `http://gedcomx.org/Religion` | |
| `RESI` | 7.0 | Residence | `http://gedcomx.org/Residence` | |
| \*     | 7.0 | Single | `http://familysearch.org/v1/NoCoupleRelationships` | in 7.0 as `NMR 0` |
| `TITL` | 7.0 | Title | `http://familysearch.org/v1/TitleOfNobility` | |
|        |     | [Tribe](#tribe) | `http://gedcomx.org/Tribe`<br/>`http://familysearch.org/v1/TribeName` | |

# Details of Proposals


## Affiliation

### Description

*proposed description missing*

*In [FamilySearch API documentation](https://www.familysearch.org/developers/docs/guides/facts)* without a definition

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- 

Related proposals include

- Clan: *difference from Affiliation not yet articulated*
- Tribe: *difference from Affiliation not yet articulated*
- Ethnicity: *difference from Affiliation not yet articulated*
- Heimat: *difference from Affiliation not yet articulated*

### Used

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>




## Clan

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's clan."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- 

Related proposals include

- Tribe: *difference from Clan not yet articulated*
- Ethnicity: *difference from Clan not yet articulated*
- Heimat: a place, often as a disambiguation of family name or lineage. Clan suggests group identity, not geography
- Affiliation: generally by choice or appointment, while clan generally indicates something assigned to a person at birth

### Used

- Part of the GEDCOM X specification

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>



## Ethnicity

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's ethnicity."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- 

Related proposals include

- Tribe: *difference from Ethnicity not yet articulated*
- Clan: *difference from Ethnicity not yet articulated*
- Heimat: a place, often as a disambiguation of family name or lineage. Ethnicity suggests group identity, not geography
- Affiliation: generally an organized group by choice or appointment, while ethnicity generally indicates a broader culture my self-identification

### Used

- Part of the GEDCOM X specification

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>


## Heimat

### Description

A geographic place to which a person is affiliated by birth or ancestry, but not necessarily by residence or property.

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's _heimat_. "Heimat" refers to a person's affiliation by birth to a specific geographic place. Distinct heimaten are often useful as indicators that two persons of the same name are not likely to be closely related genealogically. In English, "heimat" may be described using terms like "ancestral home", "homeland", or "place of origin".


### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- 

Related proposals include

- Ethnicity: ethnicities typically have some geographic association, but generally much larger and less fine-grained than a heimat
- Tribe: members of a tribe may share a heimat, but tribes may be defined by other characteristics too
- Clan: members of a clan may share a heimat, but clans may be defined by other characteristics too
- Affiliation: a person with a given heimat needn't have any affiliation with others with the same heimat

### Used

- Part of the GEDCOM X specification (but not used by the FamilySearch API, the GEDCOM-X implementation with the largest user base; see <https://www.familysearch.org/developers/docs/guides/facts>)



## Life Sketch

### Description

*proposed description missing*

*In [FamilySearch API documentation](https://www.familysearch.org/developers/docs/guides/facts)* without a definition

### Value

Found in the following historical records:

- 

### Absence

The most closely related structures are:

- `NOTE`: a life sketch is not a historical attribute in the usual sense (it lacks a date, place, associated individuals, etc). There is a proposal ([issue #219](https://github.com/FamilySearch/GEDCOM/issues/219)) to add note type to cover this instead of a new attribute.

There are no similar proposals here.

### Used

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>
- Used by Ancestry, under the name "Life Story"
- Used by FindAGrave, under the name "Bio Information"




## Military Service

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's military service."

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

- 

Related proposals include

- GEDCOM-X has events "Military Induction" and "Military Discharge" which define the start and end of the military service

### Used

- Part of the GEDCOM X specification

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>






## Tribe

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's tribe."

*In [FamilySearch API documentation](https://www.familysearch.org/developers/docs/guides/facts)* without a definition, and with a different URI than that used by GEDCOM-X

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- 

Related proposals include

- Clan: *difference from Tribe not yet articulated*
- Ethnicity: *difference from Tribe not yet articulated*
- Heimat: a place, often as a disambiguation of family name or lineage. Tribe suggests group identity, not geography
- Affiliation: generally by choice or appointment, while tribe generally indicates something assigned to a person at birth

### Used

- Part of the GEDCOM X specification

- Used by the FamilySearch API <https://www.familysearch.org/developers/docs/guides/facts>
