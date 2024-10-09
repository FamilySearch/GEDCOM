
## Enumeration Values

Unless otherwise specified in the enumeration description in this section, each enumeration value defined in this section has a URI constructed by concatenating
`g7:enum-` to the enumeration value;
for example, the `HUSB` enumeration value has the URI `http://gedcom.io/terms/v7/enum-HUSB`.

Each set of enumeration values has its own URI.

### `g7:enumset-ADOP`

| Value | Meaning |
| :---- | :------ |
| `HUSB` | Adopted by the `HUSB` of the `FAM` pointed to by `FAMC`.<br/>The URI of this value is `g7:enum-ADOP-HUSB` |
| `WIFE` | Adopted by the `WIFE` of the `FAM` pointed to by `FAMC`.<br/>The URI of this value is `g7:enum-ADOP-WIFE` |
| `BOTH` | Adopted by both `HUSB` and `WIFE` of the `FAM` pointed to by `FAMC` |

### `g7:enumset-EVEN`

An event-type tag name, but not the generic `EVEN` tag.
See [Events].

Most values in this enumeration set use the same tag and URI as the corresponding event,
except for tags used with different URIs for `FAM` vs `INDI`;
these are given generic definitions with URIs constructed by concatenating
`g7:enum-` to the enumeration value:

| Value  | Meaning                                                |
| :----- | :----------------------------------------------------- |
| `CENS` | A census event; either `g7:INDI-CENS` or `g7:FAM-CENS` |


### `g7:enumset-EVENATTR`

An event- or attribute-type tag name.
See [Events] and [Attributes].

Most values in this enumeration set use the same tag and URI as the corresponding event or attribute,
except for tags used with different URIs for `FAM` vs `INDI`;
these are given generic definitions with URIs constructed by concatenating
`g7:enum-` to the enumeration value:

| Value  | Meaning                                                |
| :----- | :----------------------------------------------------- |
| `CENS` | A census event; either `g7:INDI-CENS` or `g7:FAM-CENS` |
| `NCHI` | A count of children; either `g7:INDI-NCHI` or `g7:FAM-NCHI` |
| `RESI` | A residence attribute; either `g7:INDI-RESI` or `g7:FAM-RESI` |
| `FACT` | A generic attribute; either `g7:INDI-FACT` or `g7:FAM-FACT` |
| `EVEN` | A generic event; either `g7:INDI-EVEN` or `g7:FAM-EVEN` |


### `g7:enumset-MEDI`

| Value        | Meaning                           |
| :----------- | :-------------------------------- |
| `AUDIO`      | An audio recording                |
| `BOOK`       | A bound book                      |
| `CARD`       | A card or file entry              |
| `ELECTRONIC` | A digital artifact                |
| `FICHE`      | Microfiche                        |
| `FILM`       | Microfilm                         |
| `MAGAZINE`   | Printed periodical                |
| `MANUSCRIPT` | Written pages                     |
| `MAP`        | Cartographic map                  |
| `NEWSPAPER`  | Printed newspaper                 |
| `PHOTO`      | Photograph                        |
| `TOMBSTONE`  | Burial marker or related memorial |
| `VIDEO`      | Motion picture recording          |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

### `g7:enumset-PEDI`

| Value     | Meaning                                                   |
| :-------- | :-------------------------------------------------------- |
| `ADOPTED` | Adoptive parents                                          |
| `BIRTH`   | Family structure at time of birth                         |
| `FOSTER`  | The child was included in a foster or guardian family     |
| `SEALING` | The child was sealed to parents other than birth parents  |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

:::note
It is known that some users have interpreted `BIRTH` to mean "genetic parent" and others to mean "social parent at time of birth". Definitions differ in many circumstances (infidelity, surrogacy, sperm donation, and so on). Hence, applications should refrain from asserting it has either meaning in imported data.
:::

:::note
The structures for foster children in particular, and family relationships in general, are known to have undesirable limitations and are likely to change in a future version of this specification.
:::

:::note
`SEALING` implies that a `SLGC` event was performed, and it is recommended that
this enumeration value only be used when the `SLGC` event is present in the GEDCOM file.
`ADOPTED`, on the other hand, only implies a social relationship which may or may not have
any associated `ADOP` event.
:::



### `g7:enumset-QUAY`

| Value | Meaning                             |
| :---- | :---------------------------------- |
| `0` | Unreliable evidence or estimated data |
| `1` | Questionable reliability of evidence (interviews, census, oral genealogies, or potential for bias, such as an autobiography) |
| `2` | Secondary evidence, data officially recorded sometime after the event |
| `3` | Direct and primary evidence used, or by dominance of the evidence |

Although the values look like integers, they do not have numeric meaning.

:::note
The structures for representing the strength of and confidence in various claims are known to be inadequate and are likely to change in a future version of this specification.
:::

### `g7:enumset-RESN`

| Value | Meaning                      |
| :---- | :--------------------------- |
| `CONFIDENTIAL` | This data was marked as confidential by the user. |
| `LOCKED` | Some systems may ignore changes to this data. |
| `PRIVACY` | This data is not to be shared outside of a trusted circle, generally because it contains information about living individuals. This definition is known to admit multiple interpretations, so use of the `PRIVACY` restriction notice is not recommended. |

It is recommended that applications allow users to chose how `CONFIDENTIAL` and/or `PRIVACY` data is handled
when interfacing with other users or applications,
for example by allowing them to exclude such data when exporting.

When a [List] of `RESN` enumeration values are present, all apply.

:::example
The line `1 RESN CONFIDENTIAL, LOCKED` means the superstructure's data is both considered confidential *and* read-only.
:::

Since `RESN` was introduced in version 5.5
the intent of the `PRIVACY` value has been interpreted differently by different applications.
Known interpretations include

- Some assign `PRIVACY` by algorithm or policy, unlike the user-assigned `CONFIDENTIAL`
- Some use `PRIVACY` to mark records that have already had private data removed
- Some use the English definitions of "privacy" and "confidential" to inform different restrictions for each

There may also be applications using `PRIVACY` with interpretations not listed above.

Because these different interpretations became widespread before they were identified,
determining which one is meant generally requires knowledge of which application applied the `PRIVACY` restriction notice.
It is anticipated that a future version will deprecate the `PRIVACY` option and introduce new values for each of its current use cases.


### `g7:enumset-ROLE`

| Value | Meaning |
| ----- | :------ |
| `CHIL` | Child |
| `CLERGY` | Religious official in event; implies `OFFICIATOR` |
| `FATH` | Father; implies `PARENT` |
| `FRIEND` | Friend |
| `GODP` | Godparent or related role in other religions |
| `HUSB` | Husband; implies `SPOU` |
| `MOTH` | Mother; implies `PARENT` |
| `MULTIPLE` | A sibling from the same pregnancy (twin, triplet, quadruplet, and so on). A `PHRASE` can be used to specify the kind of multiple birth. |
| `NGHBR` | Neighbor |
| `OFFICIATOR` | Officiator of the event |
| `PARENT` | Parent |
| `SPOU` | Spouse |
| `WIFE` | Wife; implies `SPOU` |
| `WITN` | Witness |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

These should be interpreted in the context of the recorded event and its primary participants.
For example, if you cite a child’s birth record as the source of the mother’s name, the value for this field is “`MOTH`.”
If you describe the groom of a marriage, the role is “`HUSB`.”

### `g7:enumset-SEX`

| Value | Meaning                                     |
| ----- | :------------------------------------------ |
| `M`   | Male                                        |
| `F`   | Female                                      |
| `X`   | Does not fit the typical definition of only Male or only Female |
| `U`   | Cannot be determined from available sources |

This can describe an individual’s reproductive or sexual anatomy at birth.
Related concepts of gender identity or sexual preference
are not currently given their own tag. Cultural or personal gender preference may be indicated using the `FACT` tag.

### `g7:enumset-FAMC-STAT`

| Value | Meaning                        |
| ----- | :----------------------------- |
| `CHALLENGED` | Linking this child to this family is suspect, but the linkage has been neither proven nor disproven. |
| `DISPROVEN` | There has been a claim by some that this child belongs to this family, but the linkage has been disproven. |
| `PROVEN` | Linking this child to this family has been proven. |

When these enumeration values were introduced in version 5.5.1 it was assumed, but never specified, that "proven" referred to [the definition provided by the Board for Certification of Genealogists](https://www.familysearch.org/en/wiki/Genealogical_Proof_Standard).
Because that meaning was not specified and other definitions of "proven" exist, existing files might use these values in other ways.

:::note
The structures for representing the strength of and confidence in various claims are known to be inadequate and are likely to change in a future version of this specification.
:::

### `g7:enumset-ord-STAT`

These values were formerly used by The Church of Jesus Christ of Latter-day Saints for coordinating between temples and members.
They are no longer used in that way, meaning their interpretation is subject to individual user interpretation

The definition of some of these values combined with the official policies of the church
mean that some values only make sense under a subset of [ordinance structures](#latter-day-saint-ordinances).
These contexts are identified in the "applies to" column below,
and it is recommended that applications follow those guidelines.
These recommendations were not present when these enumeration values were first introduced in version 5.3
so uses that do not conform to the "applies to" guidelines may be encountered;
if so, they should be treated by applications like any other user-specified but semantically-strange data.

The definition of some of these values combined with the official policies of the church
and the move of the church away from using GEDCOM for handling ordinance requests
make them redundant and/or no longer relevant.
If so, that is indicated in the "status" column below.
Like the "applies to" column, the "status" column is a recommendation, not a requirement,
and applications should be prepared to encounter non-current values.

| Value | Applies to | Meaning                             | Status |
| ----- | ----------- | :---------------------------------- | :----- |
| `BIC` | `SLGC` | Born in the covenant, so child to parent sealing ordinance is not required. | Current |
| `CANCELED` | `SLGS` | Canceled and considered invalid. | Current |
| `CHILD` | All but `SLGC` | Died before 8 years old, so ordinances other than child to parent sealing are not required. | Current |
| `COMPLETED` | All | Completed, but the date is not known. | Deprecated, use `DATE BEF date` instead. This status was defined for use with [TempleReady](https://www.churchofjesuschrist.org/study/ensign/1994/02/news-of-the-church/templeready-now-available) which is no longer in use. |
| `EXCLUDED` | All | Patron excluded this ordinance from being cleared in this submission. | Deprecated. This status was defined for use with TempleReady which is no longer in use. |
| `DNS` | `SLGC`, `SLGS` | This ordinance is not authorized. | Current |
| `DNS_CAN` | `SLGS` | This ordinance is not authorized, and the previous ordinance is cancelled. | Current |
| `INFANT` | All but `SLGC` | Died before less than 1 year old, baptism or endowment not required. | Deprecated. Use `CHILD` instead. |
| `PRE_1970` | All | Ordinance was likely completed because an ordinance for this person was converted from temple records of work completed before 1970. | Deprecated.  Use `DATE BEF 1970` instead. |
| `STILLBORN` | All | Born dead, so no ordinances are required. | Current |
| `SUBMITTED` | All | Ordinance was previously submitted. | Deprecated. This status was defined for use with TempleReady which is no longer in use. |
| `UNCLEARED` | All | Data for clearing the ordinance request was insufficient. | Deprecated. This status was defined for use with TempleReady which is no longer in use. |

### `g7:enumset-NAME-TYPE`

| Value | Meaning                       |
| ----- | :---------------------------- |
| `AKA` | Also known as, alias, etc. |
| `BIRTH` | Name given at or near birth. |
| `IMMIGRANT` | Name assumed at the time of immigration. |
| `MAIDEN` | Maiden name, name before first marriage. |
| `MARRIED` | Married name, assumed as part of marriage. |
| `PROFESSIONAL` | Name used professionally (pen, screen, stage name). |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

### `g71:enumset-SPLAC-TYPE`  

The numbers in the Meaning column, denote the `GOVID` number from GEDCOM_L as in http://gov.genealogy.net/type/list 
| Value |  Meaning  |
|---|---|
|EARTH |  The global level that includes all continents, countries, and regions. It represents the entirety of human civilization and geographical space as the outermost jurisdictional layer. |
|SEA |  A body of saline water more directly associated with a specific landmass or group of landmasses than the vast open oceans.|
|COUNTRY | (34) A nation with its own government, occupying a particular territory.  (e.g., United States, Denmark)|
|STATE | (7) A division within a country, typically large and governed by regional laws. For example, in the U.S., it's the **"state"** (e.g., California), while in Canada, it's the **"province"** (e.g., Ontario).|
|COUNTY | (222) A smaller division within a state or province, often handling local administration. For example, "Los Angeles County" in California.|
|PROVINCE | (45) A division within a country, typically large and governed by regional laws, as in the Netherlands (Also see `STATE`)|
|DISTRICT | (5) A geographical area or administrative region within a county. It often serves to organize larger municipalities or rural areas, especially in places where counties are divided into multiple administrative sections. |
|CODEINSEE | In France, this is the national identification code used for administrative purposes, specifically for geographical divisions such as regions, departments, or cities.|
|CITY | (51) A municipality or large urban area within a county or district, where people live and work. Examples include "Paris" or "New York City." (A city can consist of suburbs, that in turn could have been small villages once)|
|VILLAGE | (54) A smaller settlement than a city, often in rural areas. Examples include "Vejleby" in Denmark. (Small villages maybe later become a suburb of a City).|
|ZIPCODE | A postal code used to identify specific areas for mail delivery, which can also help locate an event. In the U.S., this is typically a five-digit code, e.g., 90210. In the Netherlands a Zipcode, is a small area in a city or a small city itself)|
|LOCATION | Smallest possible "area", indicating an exact place within a city or village, such as a street address, building, or landmark. Can also be a house, a cemetary, a hospital, a Farm etc. Or a place at sea we know not much about.|

Almost all Values are in fact Area's, that go from largest: `EARTH`: (at the top) to smallest: `LOCATION`: (at the bottom). This list might not be complete yet, but its a start.  
The smallest one is called `LOCATION`. As thats also a bit of a reference to `_LOC` of GEDCOM-L. (In fact `LOCATION` is not really an "area".)  
Also `EARTH` is added at the top, so we can give for instance a place at sea, that has no superior than the earth itself, the possibility to also have a superior.

Now GEDCOM-L has around 280 Location `TYPE's`, but a lot of them are in fact of the lowest level, in the above list they are of Type `LOCATION`. (Farm, Cemetary etc)  
So there is an extra SubType-TAG just for `LOCATION`, to further specify the `TYPE` of the `LOCATION`. But as that is a long list the already existing `GOVID` list is used for that, and its not specified here. See `GOVTYP` in the `PERIOD-STRUCTURE` for that.

**For instance:** 

**1 TYPE LOCATION, GEOG, 4, Farm**  
or  
 **1 TYPE LOCATION, RELI, 89, Cemetary**  
Both with their `GOVID` GEDCOM_L number, separated by a comma, after the `SPLAC-TYPE`: `LOCATION` and the Demographical Type. Those numbers point to the GOV list of types. 

If the `GOVID` number is not know, specification could be:  
**1 TYPE LOCATION, GEOG, , Farm**  
So with an empty comma's just as in the original Jurisdiction list of GEDCOM 7.

With this enumset and that GOVLIST we can convert existing GEDCOM's.  
:::  
Maybe the GOV list should have some kind of **"GENERAL"** or **"UNKNOWN"** type, maybe take the value 0 for that. So in case a GEDCOM has no real definition we could write:  

**1 TYPE LOCATION, POLI, 0, Unknown**

@Albertemmerich: Could this list https://gov.genealogy.net/type/list be translated into English, or an English column added? That would make it way easier to use.  
:::

***
### `g71:enumset-DATA-INFO-TYPE`

| Value |  Meaning  |
|---|---|
| SOURCE | The information found here, is as seen from the researcher perspective. So as it is found in information records. No user processing has taken place. |
| USER |  The information found here, is as seen from a conclusion perspective, so after a user has processed the information from certain records, and added his/hers own conclusions.|
| OWN | The information found here did not directly come from any records, but it is the users own work (for instance if someone has a lot of own info about Farms)

`DATA-INFO-TYPE` is used to specify the Source of the data in a `PERIOD_STRUCTURE`. But it is defined in such a way that it could also be used for other things later, hence this name for the enumset.

***
### `g71:enumset-DEMOGRAPHICAL-DATA`

| Value |  Meaning  |
|---|---|
| POPULATION | The Demographical data that was collected, was related to the Population of a certain area.  |
| HOUSEHOLD | The Demographical data that was collected, was related to the number of Households in a certain area. |
| RESIDENT | The Demographical data that was collected, was related to the number of residents of a certain area. |

The `<TYPE_OF_DEMOGRAPHICAL_DATA>` is used to specify the type of data that is gathered for a Census and other collections. It is used in the **`PERIOD'S`** of an `SPLAC record.

***

### `g71:enumset-HIERARCHICAL-TYPE`

| Value |  Meaning  |
|---|---|
| POLI | Political relationship |
| RELI | Religious relationship |
| GEOG | Gegraphical relationship |
| CULT | Cultural relationship |

The `<HIERARCHICAL-TYPE>` is used to specify the type of the relation between an `SPLAC` and its parent, used in the link of the  `SHARED_PLACE_STRUCTURE`. And in the `SPLAC`itself to denote the type of the total `SPLAC` record..
