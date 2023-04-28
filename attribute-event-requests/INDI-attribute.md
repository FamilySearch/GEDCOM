# Individual Attributes

This document tracks the set of Individual Attributes, both those in FamilySearch GEDCOM 7 and those considered for future addition.
Guides for using this document can be found in the associated [README.md](README.md).

# Table

| G7 Tag | Since | Name | Notes |
|:------:|-------|------|-------|
| | | [Affiliation](#affiliation) | |
| | | [Bürgerort](#bürgerort) | see also Heimat |
| `CAST` | 5.0 | [Caste](#caste) | |
| \*     | 5.0 | [Childless](#childless) | encoded as `NCH 0` |
| | | [Clan](#clan) | |
| \* | 3.0 | [Died Before Eight](#died-before-eight) | encoded as `DEAT`.`AGE <8y` |
| `EDUC` | 4.0 | Education | |
| | | [Ethnicity](#ethnicity) | |
| | | [Heimat](#heimat) | see also Bürgerort |
| `IDNO` | 5.3 | [Identifying Number](#identifying-number) | |
| | | [Life Sketch](#life-sketch) | |
| | | [Military Service](#military-service) | |
| `IDNO` | 5.3 | [National ID](#national-id) | see also `SSN` |
| `NATI` | 5.0 | [Nationality](#nationality) | |
| `NCHI` | 5.0 | Number of Children | |
| `NMR`  | 5.0 | Number of Marriages | really number of `FAM`s; marriage not required |
| `OCCU` | 3.0 | [Occupation](#occupation) | |
| `DSCR` | 5.0 | [Physical Description](#physical-description) | |
| `PROP` | 3.0 | Property | |
| `RELI` | 3.0 | [Religion](#religion) | |
| `RESI` | 3.0 | [Residence](#residence) | |
| \*     | 5.0 | [Single](#single) | encoded as `NMR 0` |
| `SSN`  | 5.3 | Social Security Number | the USA's `IDNO` equivalent |
| `TITL` | 3.0 | [Title](#title) | |
| | | [Tribe](#tribe) | |

# Details


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
- Bürgerort: *difference from Affiliation not yet articulated*

### Used

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/Affiliation`

## Bürgerort

### Description

In Switzerland, the place of origin denotes where a Swiss citizen has their municipal citizenship, usually inherited from previous generations. It is not to be confused with the place of birth or place of residence, although two or all three of these locations may be identical depending on the person's circumstances. Literally "home place" or "citizen place" (from Wikipedia)

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
- Affiliation: a person with a given Bürgerort needn't have any affiliation with others with the same Bürgerort 
- Should be combined with other terms such as: German: Heimatort or Bürgerort; French: Lieu d'origine; Italian: Luogo di attinenza

### Used


## Caste

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Caste`


## Childless

The assertion that a family does not have children can be made using the `NCHI` structure with payload "`0`".
This is distinct from simply not having any `CHIL` structures,
which might mean there are children that have not yet been added to the data.

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as a distinct stucture with URI `http://familysearch.org/v1/CoupleNeverHadChildren`


## Clan

### Description

*proposed description missing*

*In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) as* "A fact of a person's clan."

### Value

Found in the following historical records:

- (records not yet identified)

### Absence

The most closely related structures are:

- `NATI` includes "An individual’s national heritage or origin, or other folk, house, kindred, lineage, or tribal interest." Adding `TYPE Clan` would fully capture this information.  

Related proposals include

- Tribe: *difference from Clan not yet articulated*
- Ethnicity: *difference from Clan not yet articulated*
- Heimat: a place, often as a disambiguation of family name or lineage. Clan suggests group identity, not geography
- Affiliation: generally by choice or appointment, while clan generally indicates something assigned to a person at birth
- Bürgerort: a place, often as a disambiguation of family name or lineage. Clan suggests group identity, not geography


### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Clan`

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X.


## Died Before Eight

The assertion that a person died before the end of their eighth year of life can be made using the `DEAT` structure with an `AGE` substructure with payload "`< 8y`".

### Used

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/DiedBeforeEight`


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
- Bürgerort: a place, often as a disambiguation of family name or lineage. Ethnicity suggests group identity, not geography


### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Ethnicity`

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X.


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
- Bürgerort: a place, often as a disambiguation of family name or lineage. Similar to Heimat and other terms from France and Italy


### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Heimat`
  
  *Not* used by the FamilySearch API, the GEDCOM-X implementation with the largest user base; see <https://www.familysearch.org/developers/docs/guides/facts>


## Identifying Number

[GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) has a subset of these (only those issued by nations) under [National Id](#national-id).


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

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/LifeSketch`
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

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/MilitaryService`

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) via GEDCOM X.




## National ID

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/NationalId`.
A special case of [Identifying number](#identifying-number)

## Nationality

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Nationality`

## Occupation

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Occupation`

## Physical Description

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/PhysicalDescription`

## Religion

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Religion`

## Residence

In [GEDCOM X](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Residence`

## Single

The assertion that a person is not a partner in a family can be made using the `NMR` structure with payload "`0`".
This is distinct from simply not having any `FAMS` structures,
which might mean there are relationships that have not yet been added to the data.

### Used

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/NoCoupleRelationships`

## Title

In [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/TitleOfNobility`



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
- Bürgerort: a place, often as a disambiguation of family name or lineage. Tribe suggests group identity, not geography

### Used

- Part of the [GEDCOM X specification](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md) with URI `http://gedcomx.org/Tribe`

- Used by the [FamilySearch API](https://www.familysearch.org/developers/docs/guides/facts) with URI `http://familysearch.org/v1/TribeName`
