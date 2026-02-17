
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

### `g8:enumset-NAME-TYPE`

| Value | Meaning                       |
| ----- | :---------------------------- |
| `ADOPTED` | Given as part of being adopted into a family. |
| `AKA` | Also known as, alias, etc. |
| `BIRTH` | Name given at or near birth. |
| `DIVORCED` | Name used after a divorce. |
| `FORMAL` | A name only used official, formal settings. |
| `GENERAL` | A name used in a wide variety of settings, both formal and informal. |
| `NICK` | A descriptive or familiar name that is used instead of, or in addition to, one’s official or legal name. Some cultures use this for any name that is not used in legal documents, others only for names that would be inappropriate in formal settings. |
| `IMMIGRANT` | Name assumed at the time of immigration. |
| `INFORMAL` | A name only used in casual, intimate, or informal settings. |
| `LEGAL` | A name used for legal and official documents, but not in daily use. |
| `MAIDEN` | Maiden name, name before first marriage. |
| `MARRIED` | Married name, assumed as part of marriage. |
| `PROFESSIONAL` | Name used professionally (pen, screen, stage name). |
| `RELIGIOUS` | Religious name, name adopted when joining a religious order. |
| `VARIANT` | Different spelling for a name, also spellings based on other languages such as Latin, French. |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure. |

Five of these types deserve additional comparison:

- A `LEGAL` name would be used on a contract but not in formal or informal settings
- A `FORMAL` would be used in formal settings but not informal ones; it is generally also used on contracts unless a different `LEGAL` name is present.
- A `GENERAL` name is used in both formal and informal settings, and on contracts unless a different `LEGAL` name is present.
- An `INFORMAL` name is used in informal settings but not in formal ones.
- A `NICK` is in some way unofficial, though exactly how varies by culture and individual, and may have any of the other types listed here.

### `g8:enumset-NAME-FORM-TYPE`

| Value | Meaning                       |
| ----- | :---------------------------- |
| `FULL` | How a name is displayed when written out in full. Incompatible with `SHORT`. |
| `SHORT` | An abbreviated version of a name. Incompatible with `SHORT`. |
| `INFERRED` | A form not found in a source, but inferred from what was in the source and the local naming patterns. |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure. |

It is expected that many name forms will have no `TYPE`.
The researcher-preferred name form is indicated by its being the first `FORM` of the `NAME`, not by any `TYPE` value.

### `g8:enumset-NAME-PART-TYPE`

| Value | Meaning                       |
| ----- | :---------------------------- |
| `ADOPTED` | Given as part of being adopted into a family. |
| `DIVORCED` | Name used after a divorce. |
| `ESTATE` | House name, farm name, or name after moving into or marrying into a house/farm. Implies `LOCATION`. Incompatible with `SURN`. | |
| `FORMAL` | A name only used official, formal settings. |
| `GENERAL` | A name used in a wide variety of settings, both formal and informal. |
| `GENERATIONAL` | A name part shared by particular generation of a family (i.e., siblings or first cousins, but not their parents or children). Implies a cultural pattern of sharing this part, not just a particular family's aesthetic naming patterns. |
| `GIVN` | A name given to an individual by someone's choice, rather than dictated by the rules of the culture, often to be used to identify that individual that individual and differentiate them from other members of the same family or community. Incompatible with `SURN`. |
| `HONORIFIC` | A word or phrase attached to a name in formal or polite context to indicate station, such as "Miss", "Doctor", "さん", "様", "mademoiselle", and so on. |
| `IMMIGRANT` | Name assumed at the time of immigration. |
| `INFORMAL` | A name only used in casual, intimate, or informal settings. |
| `LEGAL` | A name used for legal and official documents, but not in daily use. |
| `LOCATION` | A name indicating a location of note, such as a city associated with the person. Often includes "of" or "from" type particles. Incompatible with `SURN`. |
| `MAIDEN` | Maiden name, name before first marriage. |
| `MARRIED` | Married name, assumed as part of marriage. |
| `MATERNAL` | A name inherited from the individuals' mother's family. Implies `SURN`. |
| `MATRONYMIC` | A name of the individual's mother, possibly with a matronymic modifier. |
| `NICK` | A descriptive or familiar name that is used instead of, or in addition to, one’s official or legal name. Some cultures use this for any name that is not used in legal documents, others only for names that would be inappropriate in formal settings. |
| `NPFX` | Text that appears on a name line before the given and surname parts of a name. Implies that the person attaches this part to their name, but does not consider it part of the name itself. |
| `NSFX` | Text which appears on a name line after or behind the given and surname parts of a name. Implies that the person attaches this part to their name, but does not consider it part of the name itself. |
| `PARTICLE` | A name part that connects or modifies other name parts but is not itself considered a name, like "of" or "son of". | 
| `PATERNAL` | A name inherited from the individuals' father's family. Implies `SURN`. |
| `PATRONYMIC` | A name of the individual's father, possibly with a patronymic modifier like prefix "bar" or "di ser" or suffix "sen" or "dotter". |
| `PRIMARY` | The name of most prominent in importance among the names of that type. Requires `GIVN`, `SURN`, `NPFX`, or `NSFX`. |
| `PROFESSIONAL` | Name used professionally (pen, screen, stage name). |
| `RANK` | A designation of rank or position, for example in a military ("private first class"), nobility ("viscount de Spoelberch"), or  educational ("Ph.D.") system. |
| `RELIGIOUS` | Religious name, name adopted when joining a religious order. |
| `ROEPNAAM` | A name provided at birth for use in all situations except legal documents. Implies `GIVN` and `BIRTH`. The tag of this value comes from Dutch instead of English because no suitable English word was found; the value does not imply Dutch culture or ancestry. |
| `RUFNAME` | A given name underlined or otherwise indicated on documents as one not to be omitted when only one given name is used. Implies `GIVN` and `PRIMARY`. The tag of this value comes from German instead of English because no suitable English word was found; the value does not imply German culture or ancestry. |
| `SPFX` | A name piece used as a non-indexing pre-part of a surname. Should be displayed as part of surname, but ignored when sorting by surname. |
| `SURN` | A family name passed on or used by members of a family. Because `SURN` was part of GEDCOM before most other non-`GIVN` name part types, some existing data labels name parts as `SURN` that are more correctly labeled as `LOCATION` or `PATRONYMIC`; that use of `SURN` is not recommended for new data. Incompatible with `GIVN`. |
| `UNIFIED` | Unified spelling for a name part. Usually, though not always, paired with `VARIANT` and `SURN`. |
| `VARIANT` | Different spelling for a name, such as an alternative spelling or gendered form; generally used for variants that are not part the name's written forms but may be useful for indexing or searching. |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure. |

See also `g8:enumset-NAME-TYPE` for comparisons of some of these values.
