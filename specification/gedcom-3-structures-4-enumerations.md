
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


### `g8:enumset-FLEXTYPE` 

### `g8:enumset-FLEXTYPE`

This enumset defines the type of the `CONTENTS` that follows the tag `FLEX`.  
Each `FLEX` block includes a `PHRASE` and a `CONTENTS` line, optionally followed by one or more `CONT` lines. This table describes how `CONTENTS` is interpreted based on its `TYPE`.

| TYPE        | Description                                                                 | Multiline | NOTE-type | CONTENTS Value |
|-------------|-----------------------------------------------------------------------------|-----------|------------|----------------|
| `ACCOUNTNR` | An account number, such as for a bank account. Interpreted as a string.    | ➖        | ➖         | value          |
| `ADDRESS`   | Structured address data. `ADDRESS_STRUCTURE` follows under `CONTENTS`.      | ✅        | ➖         | ADDR           |
| `ADDRPLUS`  | Extended address structure. `ADDRPLUS_STRUCTURE` follows under `CONTENTS`.  | ✅        | ➖         | ADDR           |
| `AMOUNT`    | Raw numeric quantity or size.                                               | ➖        | ➖         | value          |
| `ANNOTATION`| Annotated remark, such as in a census or bible. Treated like an inline `NOTE`. | ✅    | ✅         | NOTE           |
| `ARRAY`     | A tuple array. Only simple 2-column tuples allowed. Multiline required.     | ✅        | ➖         | ARRAY          |
| `BOOLEAN`   | A truth value: `TRUE` or `FALSE`.                                           | ➖        | ➖         | value          |
| `CURR`      | Currency code (ISO 4217), e.g., USD, EUR.                                   | ➖        | ➖         | value          |
| `DATETIME`  | A DateValue, combined date and time using `1 DATE` and `2 TIME`.            | ✅        | ➖         | DATE + TIME    |
| `DATExx`    | GEDCOM-compliant date where `xx` clarifies intent: `DATEV`, `DATEE`, `DATEP`, etc. | ➖ | ➖         | DATE           |
| `DECIMAL`   | Decimal number, e.g., 12500.00                                              | ➖        | ➖         | value          |
| `DESCRIPT`  | Short description. One-liner. For longer text, use `NOTE`.                  | ➖        | ➖         | value          |
| `HEX`       | Hexadecimal string.                                                         | ➖        | ➖         | value          |
| `INTEGER`   | Whole number without decimals.                                              | ➖        | ➖         | value          |
| `LANDSIZE`  | Area or size of land or estate. May include units (e.g., "5 acres").       | ➖        | ➖         | value          |
| `MATERIAL`  | Material of an object (e.g., "wood", "linen").                            | ➖        | ➖         | value          |
| `NAME`      | Full name without structure parsing.                                        | ➖        | ➖         | value          |
| `NOTE`      | Free-text remark. Treated like an inline `NOTE`.                            | ✅        | ✅         | NOTE           |
| `OBJECT`    | Label or ID of a tangible item. Not a pointer.                              | ➖        | ➖         | value          |
| `PERCENT`   | Percent (0–100), can include decimals.                                      | ➖        | ➖         | value          |
| `PERCENTR`  | Percent ratio, may exceed 100%.                                             | ➖        | ➖         | value          |
| `REGNUMBER` | Identifying registration or case number. May include alphanumerics.        | ➖        | ➖         | value          |
| `ROLE`      | Functional role or designation (e.g., heir, witness).                       | ➖        | ➖         | value          |
| `TEXT`      | Fallback free-text. Not for structured data.                                | ✅        | ✅         | NOTE           |
| `TITLE`     | Honorific or title (e.g., "Dr.", "Queen").                               | ➖        | ➖         | value          |
| `UNIT`      | Unit of measurement (e.g., acre, meter, foot, pennyweight).                 | ➖        | ➖         | value          |
| `URL`       | Valid file path or web URL.                                                 | ➖        | ➖         | value          |

#### 🧾 Notes

- The **`Multiline`** column indicates whether the type supports/encourages `CONT` lines after `CONTENTS`.
- The **`NOTE-type`** column marks types that behave like inline `NOTE`s — they render and wrap identically and allow `CONT`.
- The **`CONTENTS Value`** column shows what the `CONTENTS` line itself should contain:
  - `value` means raw content (e.g., number, string).
  - `NOTE`, `ADDR`, or `ARRAY` means that tag name appears literally in the `CONTENTS` line.
- ⚠️ Parsers must distinguish between `value` and tagname in `CONTENTS`.
- 🧠 `DATExx` supports disambiguation when the DATE's meaning (exact/approx/range/etc.) isn't clear from context, unlike regular GEDCOM event structures.

#### 💬 Suffixes for `DATExx`

| Suffix   | Meaning                            |
|----------|-------------------------------------|
| `DATEV`  | General DateValue                   |
| `DATEE`  | Exact date                          |
| `DATEA`  | Approximate date                    |
| `DATEP`  | Period (e.g., "BET 1890 AND 1900") |
| `DATER`  | Date range                          |
| `DATERs` | Date restriction (e.g., "BEF 1860") |

***
### `g8:enumset-FLEXTYPE`

This enumset defines the type of the `CONTENTS` that follows the tag `FLEX`.  
Each `FLEX` block includes a `PHRASE` and a `CONTENTS` line, optionally followed by one or more `CONT` lines. This table describes how `CONTENTS` is interpreted based on its `TYPE`.

| TYPE        | Description   | Multiline | NOTE-type | CONTENTS Value |
|-------------|---------------|-----------|-----------|----------------|
| `ACCOUNTNR` | An account number, such as for a bank account. Interpreted as a string. | ➖ | ➖ | value |
| `ADDRESS`   | Structured address data. `ADDRESS_STRUCTURE` follows under `CONTENTS`.| ✅ | ➖ | ADDR   |
| `ADDRPLUS`  | Extended address structure. `ADDRPLUS_STRUCTURE` follows under `CONTENTS`. | ✅ | ➖ | ADDR |
| `AMOUNT`    | Raw numeric quantity or size.    | ➖        | ➖         | value          |
| `ANNOTATION`| Annotated remark, such as in a census or bible. Treated like an inline `NOTE`. | ✅ | ✅ | NOTE|
| `ARRAY`     | A tuple array. Only simple 2-column tuples allowed. Multiline required. | ✅| ➖ | ARRAY  |
| `BOOLEAN`   | A truth value: `TRUE` or `FALSE`.     | ➖        | ➖         | value          |
| `CURR`      | Currency code (ISO 4217), e.g., USD, EUR. | ➖        | ➖         | value          |
| `DATETIME`  | A DateValue, combined date and time using `1 DATE` and `2 TIME`. | ✅   | ➖  | DATE + TIME |
| `DATExx`    | GEDCOM-compliant date where `xx` clarifies intent: `DATEV`, `DATEE`, `DATEP`, etc.|➖|➖| DATE|
| `DECIMAL`   | Decimal number, e.g., 12500.00 | ➖        | ➖         | value          |
| `DESCRIPT`  | Short description. One-liner. For longer text, use `NOTE`.  | ➖ | ➖ | value          |
| `HEX`       | Hexadecimal string.    | ➖        | ➖         | value          |
| `INTEGER`   | Whole number without decimals. | ➖        | ➖         | value          |
| `LANDSIZE`  | Area or size of land or estate. May include units (e.g., "5 acres").| ➖ | ➖ | value    |
| `MATERIAL`  | Material of an object (e.g., "wood", "linen").   | ➖        | ➖         | value          |
| `NAME`      | Full name without structure parsing.  | ➖        | ➖         | value          |
| `NOTE`      | Free-text remark. Treated like an inline `NOTE`.| ✅        | ✅         | NOTE           |
| `OBJECT`    | Label or ID of a tangible item. Not a pointer.  | ➖        | ➖         | value          |
| `PERCENT`   | Percent (0–100), can include decimals. | ➖        | ➖         | value          |
| `PERCENTR`  | Percent ratio, may exceed 100%.   | ➖        | ➖         | value          |
| `REGNUMBER` | Identifying registration or case number. May include alphanumerics.| ➖ | ➖ | value     |
| `ROLE`      | Functional role or designation (e.g., heir, witness).| ➖        | ➖         | value          |
| `TEXT`      | Fallback free-text. Not for structured data.| ✅        | ✅         | NOTE           |
| `TITLE`     | Honorific or title (e.g., "Dr.", "Queen").  | ➖        | ➖         | value          |
| `UNIT`      | Unit of measurement (e.g., acre, meter, foot, pennyweight). | ➖  | ➖  | value   |
| `URL`       | Valid file path or web URL.   | ➖        | ➖         | value          |

#### 🧾 Notes

- The **`Multiline`** column indicates whether the type supports/encourages `CONT` lines after `CONTENTS`.
- The **`NOTE-type`** column marks types that behave like inline `NOTE`s — they render and wrap identically and allow `CONT`.
- The **`CONTENTS Value`** column shows what the `CONTENTS` line itself should contain:
  - `value` means raw content (e.g., number, string).
  - `NOTE`, `ADDR`, or `ARRAY` means that tag name appears literally in the `CONTENTS` line.
- ⚠️ Parsers must distinguish between `value` and tagname in `CONTENTS`.
- 🧠 `DATExx` supports disambiguation when the DATE's meaning (exact/approx/range/etc.) isn't clear from context, unlike regular GEDCOM event structures.

#### 💬 Suffixes for `DATExx`

| Suffix   | Meaning                            | TAGS |
|----------|-------------------------------------|--|
| `DATE`   | date                                |  [calendar D] [[day D] month D] year [D epoch] |
| `DATEV`  | General DateValue                   |  [ date / DatePeriod / dateRange / dateApprox ] |
| `DATEE`  | Exact date                          | day D month D year  |
| `DATEA`  | Approximate date                    |  (%s"ABT" / %s"CAL" / %s"EST") D date |
| `DATEP`  | Period (e.g., "BET 1890 AND 1900") |  [ %s"TO" D date ] <br> / %s"FROM" D date [ D %s"TO" D date ] |
| `DATER`  | Date range                          |  %s"BET" D date D %s"AND" D date<br> / %s"AFT" D date<br> / %s"BEF" D date |
| `DATERS` | Date restriction (e.g., "BEF 1860") |  %s"FROM" / %s"TO" / %s"BET" / %s"AND" / %s"BEF" <br>/ %s"AFT" / %s"ABT" / %s"CAL" / %s"EST" |

- This enumeration defines the list of valid types that can appear in a `FLEX` structure's `TYPE` line.
- New types may be added over time. Unrecognized types must be ignored or flagged.
- Each type adds meaning to the associated `CONTENTS` value(s). Parsers and tools must validate types against this list for interoperability.
- 🧾 `TEXT` must not be used to encode structured values (like numbers, currency, or dates) in string form. Always use the appropriate type. `TEXT` is a fallback only.  
- (`NOTE`-like enum value), this means this `FLEX`-type is to be handled like an **inline** `NOTE` including the tag `NOTE`.
- **Multiline**, this `FLEX` type is a multiline type, like `NOTE` or `ARRAY`, see the examples.

#### 💬 Comments on FLEX Type Handling

- ⚠️ Parsers must validate that the number of `TYPE` entries matches the structure of `CONTENTS` values.
- ⚖️ `LANDSIZE` may include implicit or explicit units (e.g., `10.5 ACRE`), but software should gracefully handle unitless values when the historical context is uncertain.
  - The units are only present because they appeared on the original document, and do not have to be interpreted by software.
- ♾️ `UNIT`, for old measurements see: https://en.wikipedia.org/wiki/Medieval_weights_and_measures or https://en.wikipedia.org/wiki/List_of_obsolete_units_of_measurement.
  - Here too: units do not have to be interpreted by software.

:::example  
These are examples for a `NOTE`, an `ARRAY`, and an `ANNOTATION`:
```gedcom
1 FLEX NOTE                   /* FLEX re4placement of a normal inline NOTE */
2 PHRASE description on form
2 CONTENTS NOTE
3 CONT First line of text
3 CONT another textline
```
```gedcom
1 FLEX ARRAY                  /* DNA values */
2 PHRASE DNA values
2 CONTENTS ARRAY
3 CONT (rs123456, A)
3 CONT (rs234567, T)
3 CONT (rs345678, G)
```
```gedcom
1 FLEX ANNOTATION             /* An annotation, which is always of type NOTE */
2 PHRASE Annotation in a Census
2 CONTENTS NOTE
3 CONT First line of annotation
3 CONT another annotated line
```
These are examples for `DATEP`, `DATETIME` and an `ADDRESS`:
```gedcom
1 FLEX DATEP                  /* A Dateperiod */
2 PHRASE Dateperiod of event
2 CONTENTS FROM 1850 TO 1880

1 FLEX DATETIME
2 PHRASE Birth Date and time
2 CONTENTS DATETIME
3 DATE 18 SEP 1832
3 TIME 12:45

1 FLEX ADDRESS
2 PHRASE Address of laboratory
2 CONTENTS ADDR 43 Mainstreet /* ADDR1, ADDR2, ADDR3 are deprecated so street and nr follow ADDR!! */
3 CITY Cristal Lake
~ ~ ~                         /* Other lines of the address structure */
```
:::  

:::note  
During draft there was also an `ENUM`:
- ENUM: A value from a predefined list of allowed values. (Use cautiously.)
- If used, `CONTENTS` must reference a known enum value, and we’d likely need a way to specify which enum set is being used (like `PEDI`, `SEX`, or a user-defined list).
- 🚫 `ENUM` has been excluded for now due to the need for explicit reference to an enumeration list, which is not yet defined in the spec. It could be used/defined as `1 FLEX ENUM, PEDI, ADOPTED`

$\color{Coral}{\textsf{`ENUM` might be too ambiguous. Might want to drop for now unless a specific use-case exists.}}$

:::

#### Some other `FLEX-TYPE` Specifications

- Each `FLEX-TYPE` value defines the structure and interpretation of the associated `CONTENTS`. This section describes the expected format and usage rules for common `FLEX-TYPE` values.
- Each value in a multi-part `CONTENTS` line must exactly match its corresponding type in the `FLEX` declaration, by position.

| `FLEX-TYPE` | Description     | Example  |
|-------------|-----------------|----------|
| **BOOLEAN** | Must be one of: `TRUE`, `FALSE` (uppercase).| Example: `1 CONTENTS TRUE` |
| **CODE** | A short, predefined value from a controlled vocabulary or government list.| Example: `1 CONTENTS "C-01"` (case and format depend on the code system used)|
| **CURR** | Currency code following [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Always combined with `DECIMAL` or `INTEGER`| Example: `1 CONTENTS INTEGER, USD` or `1 CONTENTS DECIMAL, EUR`|
| **LANDSIZE** | Land size measurement. First value must be numeric (`DECIMAL`); second value is a unit label (`TEXT`).| Example: `1 CONTENTS 3.75, ACRE`<br> Non-SI or historical units (e.g., `"BUNDER"`, `"MORGEN"`, `"MUD"`) are permitted as quoted text.|
| **PERCENT** | A numeric value representing a percentage. | Example: `1 CONTENTS 25.0` (meaning 25%)|

### `g8:enumset-GROUP-TYPE`

These values define the allowed `TYPE` values for the `GROUP` record.  
A `GROUP` represents a named social, ancestral, or occupational unit that may span across families and generations — such as a clan, caste, guild, religious order, or a sports team etc. that may span across families and generations.  
Each individual `GROUP` must declare exactly one `TYPE` value.

| ICO | `TYPE`    | Description          | Examples (with  PHRASE)    |
|-----|-----------|----------------------|--------------|
| 🧬 | `CASTE`   | Stratified hereditary social class, tied to status, often with legal or ritual restrictions; commonly used in hierarchical societies. | Brahmin (India), Burakumin (Japan), artisan castes in West Africa. "Vaishya trading caste of Bengal" or "Brahmin priestly caste of Varanasi"|
| 🏞️ | `CLAN`    | Kin-based lineage group, typically connected to shared ancestry and territorial rights   | Clan MacLeod (Scotland), O'Neill (Ireland), Dlamini clan (Eswatini)  "MacKenzie clan of the Highlands" or "Clan Donnachaidh (Robertsons)"|
| ⚔️ | `FACTION` | Political or ideological group formed for power, dissent, or advocacy | Jacobites (UK), Bolsheviks (Russia), modern activist coalitions.  "Anti-Reform Resistance, 1832" or "Bolsheviks, 1917"|
| 🚜 | `FARM`    | Family unit associated with a named homestead or farmstead |   Gården "Storlien" (Norway), Boerderij "De Veenhof" (Netherlands)  "Boerderij De Veenhof, Overijssel" or "Gården Storlien, Trøndelag"|
| 🛠️ | `GUILD`   | Occupational or trade-based group with formal training, rights, or charters. May include rank.  | Blacksmiths, merchants, tailors, trade societies, craftsman. E.g.: Weavers' Guild (Leiden), Worshipful Company of Goldsmiths' Guild (UK), Hanseatic League. "Butchers' Guild of Bruges" or "Guild of Tailors, Haarlem"|
| ⛪ | `ORDER`   | Religious, spiritual, monastic, or honorary group with a shared mission  | Knights Templar, Jesuit Order, Benedictines, Order of the Garter. "Order of Saint John, Malta" or "Order of Saint Augustine"|
| 🗳️ | `PARTY`   | Political party, faction, or electoral group |  Labour Party (UK), Democrats (USA) "Green Progressive Alliance, Utrecht chapter" or "Labour Party, UK"|
| 🔯 | `SECT`    | Religious subgroup or denomination, often with distinctive doctrine or practices. Often diverging from a mainstream belief system   | Old Order Amish, Sufi orders, Hasidic sects, Sunni, Cathars, Shakers "Old Order Amish of Lancaster" or "Old Order Mennonites, Lancaster County"|
| 🎓 | `SOCIETY` | Voluntary cultural, social, scholarly, or scientific association  | Royal Astronomical Society, Esperanto Club  "Historical Society of Drenthe" or "Royal Astronomical Society"|
| 🏅| `TEAM`    |  Group formed for sport, art, cooperative performance, or competition-based group  | 1908 Dutch Olympic Rowing Team, Harlem Globetrotters, FC Barcelona, Comédie-Française acting troupe. "Royal Ballet touring company, 1951" or "Rijksmuseum Curling Club"|
| 🐾| `TRIBE`   |  Ethnic or ancestral group often encompassing multiple clans; with shared language and territory, and cultural or linguistic unity.    | Cherokee Nation, Navajo, Berber, Dakota Sioux, Zulu, Sámi    "Dakota Sioux of the Great Plains|
| 🌀 | `OTHER`   | Custom type not listed here (must include a `PHRASE`)  | Fellowship of Historical Gardeners, or "Ski Patrol volunteers"  |"Fellowship of Historical Gardeners" or "Railway Enthusiasts of East Anglia"|

> 🧠 **Note on `FARM` and `CLAN` crossovers**:  
> In rural Norway 🇳🇴, Germany 🇩🇪, and the Netherlands 🇳🇱, individuals were historically identified by the **name of the farm** they lived on, often replacing or supplementing surnames.  
> - In **Norway**, a man might be called "Ole Storlien" after the farm, even if unrelated to previous residents.  
> - In **the Netherlands**, farms like “De Veenhof” or “Klein Westeinde” became identity anchors; children or workers living there might be recorded under the farm name in local records.  
> This creates a **quasi-clan** identity centered on a *location* rather than a bloodline or kinship — blending elements of family, estate, and group affiliation.

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

### `g8:enumset-TORIGIN`

Specifies **how** a `TEMPLATE` or `STICKY` was originally created or derived.  
This describes the **construction method** — whether automated, copied, inferred, or transcribed.  
It is not the same as the trust level, but is used to assess credibility and compatibility.  

Multiple values may be listed if applicable (e.g. `1 TORIGIN REVERSENG, INCOMPLETE`).

| Trust | Icon | Tag           | Description |
|-------|------|----------------|-------------|
| 🟢    | 📄  | `ORIGDOC`      | Created directly from a physical or digital document that is **available, cited, and traceable in this GEDCOM file**. `CITA` structure must point to a `SOUR` in this GEDCOM. |
| 🟢    | ✍️  | `TRANSCRIBED`  | Manually transcribed from a known document. Can apply to individual facts or full documents. Must include a `CITA` structure pointing to a `SOUR` in this GEDCOM. |
| 🟡    | 📥  | `IMPORTED`     | Fully structured record or subtree was **mechanically loaded** from a GEDCOM 8-compatible source or system. |
| 🟡    | 🧬  | `MERGED`       | Created by combining overlapping records from multiple sources into a unified record. Often applies to families, clusters, or trees. |
| 🟡    | 🛠️  | `REVERSENG`    | Reverse-engineered manually or semi-automatically from legacy data (notes, citations, or prior GEDCOM), poorly structured, or incompatible data (e.g. GEDCOM 5.x). |
| 🟡    | 🪶  | `INCOMPLETE`   | Known to be partial or fragmentary, with gaps or missing fields. Can be added alongside any other tag to indicate incompleteness. |
| 🟠    | 🧩  | `COPIEDFRAG`   | Manually copied or extracted from another public tree, online profile, or website — **without verifying original sources**. Applies to selected facts or small clusters. |
| 🟠    | ℹ️  | `INDIFAM`      | **Reverse engineered** from **1 (one)** `INDI` or **1 (one)** `FAM` record from a file containing GEDCOM version 7.x or below. This is to be used in case a file is reverse engineered, and certain data from the older file has no proper connection (source-citation) to any `SOUR`ce. In that case that data from this 1 `INDI` or this 1 `FAM` will be put together in a temp-`TEMPLATE` and 1 (one) accompanying temp-`STICKY` until a `TAG` inside it, can later be properly connected to an existing `SOUR`. Then that data will be taken out, `TAG` by `TAG`, and put in the correct `STICKY`. This process continues until all data from that temp-`STICKY` marked with `INDIFAM` is processed, and the `STICKY` is "empty". After that the temp-`STICKY` and the temp-`TEMPLATE` that it belongs to, can be deleted. This ensures no data is lost from older files. |   
| 🟠    | ℹ️  | `INDIFAM`      | Reverse-engineered from a single `INDI` or `FAM` record in a pre-GEDCOM 8 file **without a valid `SOUR` link**. Data is stored in a temporary `TEMPLATE` and `STICKY` until each `TAG` is linked to a verified source. |
| 🔴    | 🎲  | `GUESSED`      | Constructed by logic, guesswork, deduction or inference without supporting documentation. |
| 🔴    | ❓  | `UNKNOWN`      | No record of how this data was created or obtained. Method is unclear or lost. |

---

**Special notes:**

- **`INDIFAM` handling process:**  
  When reverse-engineering a pre-GEDCOM 8 file, some data from an `INDI` or `FAM` record may have no proper source-citation link.  
  In such cases, all unlinked data from **one** `INDI` or **one** `FAM` is placed into a temporary `TEMPLATE` and **one** accompanying temporary `STICKY`, both marked with `TORIGIN INDIFAM`.  
  Over time, each `TAG` is linked to a verified `SOUR`. As each `TAG` is moved to its correct `STICKY`, it is removed from the temporary one.  
  When the temporary `STICKY` is empty, both it and its `TEMPLATE` are deleted.  
  This ensures that no unlinked data from older files is lost during migration while clearly flagging it as lacking verified sources at the time of import.  
- **If a `TEMPLATE` does not have a proper `SOUR` connected from inside this GEDCOM itself, `TORIGIN` cannot be `ORIGDOC`or `TRANSCRIBED`.**

---

Applies to:
- `TEMPLATE` records
- `STICKY` records

Used by:
- quality-assessment tools
- compatibility checks
- documentation and interface hints

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
