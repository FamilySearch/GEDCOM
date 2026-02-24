
## Enumeration Values

Each set of enumeration values has its own URI.

### `g7:enumset-ADOP`

| Value | URI | Meaning |
| :---- | :---| :------ |
| `HUSB` | `g7:enum-ADOP-HUSB` | Adopted by the `HUSB` of the `FAM` pointed to by `FAMC` |
| `WIFE` | `g7:enum-ADOP-WIFE` | Adopted by the `WIFE` of the `FAM` pointed to by `FAMC` |
| `BOTH` | `g7:enum-BOTH` | Adopted by both `HUSB` and `WIFE` of the `FAM` pointed to by `FAMC` |

### `g7:enumset-EVEN`

An event-type tag name, but not the generic `EVEN` tag.
See [Events].

Most values in this enumeration set use the same tag and URI as the corresponding event,
except for tags used with different URIs for `FAM` vs `INDI`:

| Value  | URI            | Meaning                                                |
| :----- | :------------- | :----------------------------------------------------- |
| `CENS` | `g7:enum-CENS` | A census event; either `g7:INDI-CENS` or `g7:FAM-CENS` |


### `g7:enumset-EVENATTR`

An event- or attribute-type tag name.
See [Events] and [Attributes].

Most values in this enumeration set use the same tag and URI as the corresponding event or attribute,
except for tags used with different URIs for `FAM` vs `INDI`:

| Value  | URI            | Meaning                                                |
| :----- | :------------- | :----------------------------------------------------- |
| `CENS` | `g7:enum-CENS` | A census event; either `g7:INDI-CENS` or `g7:FAM-CENS` |
| `NCHI` | `g7:enum-NCHI` | A count of children; either `g7:INDI-NCHI` or `g7:FAM-NCHI` |
| `RESI` | `g7:enum-RESI` | A residence attribute; either `g7:INDI-RESI` or `g7:FAM-RESI` |
| `FACT` | `g7:enum-FACT` | A generic attribute; either `g7:INDI-FACT` or `g7:FAM-FACT` |
| `EVEN` | `g7:enum-EVEN` | A generic event; either `g7:INDI-EVEN` or `g7:FAM-EVEN` |


### `g7:enumset-MEDI`

| Value       | URI                 | Meaning                           |
| :---------- | :------------------ | :-------------------------------- |
| `AUDIO`     | `g7:enum-AUDIO`     | An audio recording                |
| `BOOK`      | `g7:enum-BOOK`      | A bound book                      |
| `CARD`      | `g7:enum-CARD`      | A card or file entry              |
| `ELECTRONIC`| `g7:enum-ELECTRONIC`| A digital artifact such as a computer file or a scan |
| `FICHE`     | `g7:enum-FICHE`     | Microfiche                        |
| `FILM`      | `g7:enum-FILM`      | Microfilm                         |
| `MAGAZINE`  | `g7:enum-MAGAZINE`  | Printed periodical                |
| `MANUSCRIPT`| `g7:enum-MANUSCRIPT`| Written pages                     |
| `MAP`       | `g7:enum-MAP`       | Cartographic map                  |
| `NEWSPAPER` | `g7:enum-NEWSPAPER` | Printed newspaper                 |
| `PHOTO`     | `g7:enum-PHOTO`     | Photograph                        |
| `TOMBSTONE` | `g7:enum-TOMBSTONE` | Burial marker or related memorial |
| `VIDEO`     | `g7:enum-VIDEO`     | Motion picture recording          |
| `OTHER`     | `g7:enum-OTHER`     | A value not listed here; should have a `PHRASE` substructure |

### `g7:enumset-PEDI`

| Value     | URI               | Meaning                                                   |
| :-------- | :---------------- | :-------------------------------------------------------- |
| `ADOPTED` | `g7:enum-ADOPTED` | Adoptive parents                                          |
| `BIRTH`   | `g7:enum-BIRTH`   | Family structure at time of birth                         |
| `FOSTER`  | `g7:enum-FOSTER`  | The child was included in a foster or guardian family     |
| `SEALING` | `g7:enum-SEALING` | The child was sealed to parents other than birth parents  |
| `OTHER`   | `g7:enum-OTHER`   | A value not listed here; should have a `PHRASE` substructure |

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

| Value | URI       | Meaning                             |
| :---- | :-------- | :---------------------------------- |
| `0` | `g7:enum-0` | Unreliable evidence or estimated data |
| `1` | `g7:enum-1` | Questionable reliability of evidence (interviews, census, oral genealogies, or potential for bias, such as an autobiography) |
| `2` | `g7:enum-2` | Secondary evidence, data officially recorded sometime after the event |
| `3` | `g7:enum-3` | Direct and primary evidence used, or by dominance of the evidence |

Although the values look like integers, they do not have numeric meaning.

:::note
The structures for representing the strength of and confidence in various claims are known to be inadequate and are likely to change in a future version of this specification.
:::

### `g7:enumset-RESN`

| Value | URI | Meaning                      |
| :---- | :-- | :--------------------------- |
| `CONFIDENTIAL` | `g7:enum-CONFIDENTIAL` | This data was marked as confidential by the user. |
| `LOCKED` | `g7:enum-LOCKED` | Some systems may ignore changes to this data. |
| `PRIVACY` | `g7:enum-PRIVACY` | This data is not to be shared outside of a trusted circle, generally because it contains information about living individuals. This definition is known to admit multiple interpretations, so use of the `PRIVACY` restriction notice is not recommended. |

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

| Value | URI | Meaning |
| ----- | :-- | :------ |
| `CHIL` | `g7:enum-CHIL` | Child |
| `CLERGY` | `g7:enum-CLERGY` | Religious official in event; implies `OFFICIATOR` |
| `FATH` | `g7:enum-FATH` | Father; implies `PARENT` |
| `FRIEND` | `g7:enum-FRIEND` | Friend |
| `GODP` | `g7:enum-GODP` | Godparent or related role in other religions |
| `HUSB` | `g7:enum-HUSB` | Husband; implies `SPOU` |
| `MOTH` | `g7:enum-MOTH` | Mother; implies `PARENT` |
| `MULTIPLE` | `g7:enum-MULTIPLE` | A sibling from the same pregnancy (twin, triplet, quadruplet, and so on). A `PHRASE` can be used to specify the kind of multiple birth. |
| `NGHBR` | `g7:enum-NGHBR` | Neighbor |
| `OFFICIATOR` | `g7:enum-OFFICIATOR` | Officiator of the event |
| `PARENT` | `g7:enum-PARENT` | Parent |
| `SPOU` | `g7:enum-SPOU` | Spouse |
| `WIFE` | `g7:enum-WIFE` | Wife; implies `SPOU` |
| `WITN` | `g7:enum-WITN` | Witness |
| `OTHER` | `g7:enum-OTHER` | A value not listed here; should have a `PHRASE` substructure |

These should be interpreted in the context of the recorded event and its primary participants.
For example, if you cite a child’s birth record as the source of the mother’s name, the value for this field is “`MOTH`.”
If you describe the groom of a marriage, the role is “`HUSB`.”

### `g7:enumset-SEX`

| Value | URI | Meaning                                     |
| ----- | :-- | :------------------------------------------ |
| `M` | `g7:enum-M` | Male                                        |
| `F` | `g7:enum-F` | Female                                      |
| `X` | `g7:enum-X` | Does not fit the typical definition of only Male or only Female |
| `U` | `g7:enum-U` | Cannot be determined from available sources |

This can describe an individual’s reproductive or sexual anatomy at birth.
Related concepts of gender identity or sexual preference
are not currently given their own tag. Cultural or personal gender preference may be indicated using the `FACT` tag.

### `g7:enumset-FAMC-STAT`

| Value | URI | Meaning                        |
| ----- | :-- | :----------------------------- |
| `CHALLENGED` | `g7:enum-CHALLENGED` | Linking this child to this family is suspect, but the linkage has been neither proven nor disproven. |
| `DISPROVEN` | `g7:enum-DISPROVEN` | There has been a claim by some that this child belongs to this family, but the linkage has been disproven. |
| `PROVEN` | `g7:enum-PROVEN` | Linking this child to this family has been proven. |

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

| Value | URI | Applies to | Meaning                             | Status |
| ----- | --- | ---------- | :---------------------------------- | :----- |
| `BIC` | `g7:enum-BIC` | `SLGC` | Born in the covenant, so child to parent sealing ordinance is not required. | Current |
| `CANCELED` | `g7:enum-CANCELED` | `SLGS` | Canceled and considered invalid. | Current |
| `CHILD` | `g7:enum-CHILD` | All but `SLGC` | Died before 8 years old, so ordinances other than child to parent sealing are not required. | Current |
| `COMPLETED` | `g7:enum-COMPLETED` | All | Completed, but the date is not known. | Deprecated, use `DATE BEF date` instead. This status was defined for use with [TempleReady](https://www.churchofjesuschrist.org/study/ensign/1994/02/news-of-the-church/templeready-now-available) which is no longer in use. |
| `EXCLUDED` | `g7:enum-EXCLUDED` | All | Patron excluded this ordinance from being cleared in this submission. | Deprecated. This status was defined for use with TempleReady which is no longer in use. |
| `DNS` | `g7:enum-DNS` | `SLGC`, `SLGS` | This ordinance is not authorized. | Current |
| `DNS_CAN` | `g7:enum-DNS_CAN` | `SLGS` | This ordinance is not authorized, and the previous ordinance is cancelled. | Current |
| `INFANT` | `g7:enum-INFANT` | All but `SLGC` | Died before less than 1 year old, baptism or endowment not required. | Deprecated. Use `CHILD` instead. |
| `PRE_1970` | `g7:enum-PRE_1970` | All | Ordinance was likely completed because an ordinance for this person was converted from temple records of work completed before 1970. | Deprecated.  Use `DATE BEF 1970` instead. |
| `STILLBORN` | `g7:enum-STILLBORN` | All | Born dead, so no ordinances are required. | Current |
| `SUBMITTED` | `g7:enum-SUBMITTED` | All | Ordinance was previously submitted. | Deprecated. This status was defined for use with TempleReady which is no longer in use. |
| `UNCLEARED` | `g7:enum-UNCLEARED` | All | Data for clearing the ordinance request was insufficient. | Deprecated. This status was defined for use with TempleReady which is no longer in use. |

### `g7:enumset-NAME-TYPE`

| Value | URI | Meaning                       |
| ----- | :-- | :---------------------------- |
| `AKA` | `g7:enum-AKA` | Also known as, alias, etc. |
| `BIRTH` | `g7:enum-BIRTH` | Name given at or near birth. |
| `IMMIGRANT` | `g7:enum-IMMIGRANT` | Name assumed at the time of immigration. |
| `MAIDEN` | `g7:enum-MAIDEN` | Maiden name, name before first marriage. |
| `MARRIED` | `g7:enum-MARRIED` | Married name, assumed as part of marriage. |
| `PROFESSIONAL` | `g7:enum-PROFESSIONAL` | Name used professionally (pen, screen, stage name). |
| `OTHER` | `g7:enum-OTHER` | A value not listed here; should have a `PHRASE` substructure |
