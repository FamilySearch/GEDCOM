## Structure Meaning

### Events

As a general rule, events are things that happen on a specific date.
Use the `dateRange` form to indicate that an event took place at some time between 2 dates.
In most cases, a `DatePeriod` is inappropriate for an event; if the subject of your recording occurred over a period of time, then it is probably not an event, but rather an attribute.

Event structures can be used to record notes about an event without asserting the event actually occurred.
An event structure asserts the event did occur if any of the following are true:

- There is a `DATE` substructure

    <div class="example">

    ````gedcom
    1 DEAT
    2 DATE 2 OCT 1937
    ````
    
    </div>
    
    <div class="note">

    Version 5.4 (1995) introduced the "event did occur" meaning of event.`DATE`, so it is now well-established in applications and files.
    However, it is common for users to enter a date range with no end without intending to indicate that the event occurred.
    For example, pre 7.0 files sometimes used
    
    ````gedcom
    1 NATU
    2 DATE AFT 1800
    ````
    
    to mean what 7.0 encodes as
    
    ````gedcom
    1 NOT NATU
    2 DATE TO 1800
    ````
    
    without intending to imply that `NATU` ever did actually occur.
    Because this is a "sometimes used" rather than a "formally means" situation,
    it is likely that data using 5.x "after meaning not before" *de facto* pattern will be transferred as-is into 7.0 and persist in files for the foreseeable future.

    </div>

- There is a `PLAC` substructure
    
    <div class="example">

    ````gedcom
    1 DEAT
    2 PLAC Cove, Cache, Utah
    ````

    </div>

- The event has a payload.
    A special payload `Y` can be used with some event types to indicate that the event is known to have occurred without providing any additional information about it.
    
    <div class="example">
    
    ````gedcom
    1 DEAT Y
    ````
    
    </div>

If none of the above are true, the structure should be seen as a place for inconclusive research notes about the possibility of the event.
An assertion that an event did not occur should be encoded using the `NO` structure.

#### Individual Events

Tag | Name<br/>URI | Description
--- | ---- | -----------
`ADOP` | adoption<br/>`g7:ADOP` | Creation of a legally approved child-parent relationship that does not exist biologically.
`BAPM` | baptism<br/>`g7:BAPM` | Baptism, performed in infancy or later. (See also [`BAPL`](#latter-day-saint-ordinances) and `CHR`.)
`BARM` | Bar Mitzvah<br/>`g7:BARM` | The ceremonial event held when a Jewish boy reaches age 13.
`BASM` | Bas Mitzvah<br/>`g7:BASM` | The ceremonial event held when a Jewish girl reaches age 13, also known as "Bat Mitzvah."
`BIRT` | birth<br/>`g7:BIRT` | Entering into life.
`BLES` | blessing<br/>`g7:BLES` | Bestowing divine care or intercession. Sometimes given in connection with a naming ceremony.
`BURI` | depositing remains<br/>`g7:BURI` | Depositing the mortal remains of a deceased person.
`CENS` | census<br/>`g7:INDI-CENS` | Periodic count of the population for a designated locality, such as a national or state census.
`CHR` | christening<br/>`g7:CHR` | Baptism or naming events for a child.
`CHRA` | adult christening<br/>`g7:CHRA` | Baptism or naming events for an adult person.
`CONF` | confirmation<br/>`g7:CONF` | Conferring full church membership.
`CREM` | cremation<br/>`g7:CREM` | The act of reducing a dead body to ashes by fire.
`DEAT` | death<br/>`g7:DEAT` | Mortal life terminates.
`EMIG` | emigration<br/>`g7:EMIG` | Leaving one's homeland with the intent of residing elsewhere.
`FCOM` | first communion<br/>`g7:FCOM` | The first act of sharing in the Lord's supper as part of church worship.
`GRAD` | graduation<br/>`g7:GRAD` | Awarding educational diplomas or degrees to individuals.
`IMMI` | immigration<br/>`g7:IMMI` | Entering into a new locality with the intent of residing there.
`NATU` | naturalization<br/>`g7:NATU` | Obtaining citizenship.
`ORDN` | ordination<br/>`g7:ORDN` | Receiving authority to act in religious matters.
`PROB` | probate<br/>`g7:PROB` | Judicial determination of the validity of a will. It may indicate several related court activities over several dates.
`RETI` | retirement<br/>`g7:RETI` | Exiting an occupational relationship with an employer after a qualifying time period.
`WILL` | will<br/>`g7:WILL` | A legal document treated as an event, by which a person disposes of his or her estate. It takes effect after death. The event date is the date the will was signed while the person was alive. (See also `PROB`)

In addition, `INDI`.`EVEN` is a structure for a generic individual event. It must have a `TYPE` substructure to define what kind of event is being provided.

#### Family Events

Tag | Name<br/>URI | Description
--- | ---- | -----------
`ANUL` | annulment<br/>`g7:ANUL` | Declaring a marriage void from the beginning (never existed).
`CENS` | census<br/>`g7:FAM-CENS` | Periodic count of the population for a designated locality, such as a national or state census.
`DIV` | divorce<br/>`g7:DIV` | Dissolving a marriage through civil action.
`DIVF` | divorce filed<br/>`g7:DIVF` | Filing for a divorce by a spouse.
`ENGA` | engagement<br/>`g7:ENGA` | Recording or announcing an agreement between 2 people to become married.
`MARB` | marriage bann<br/>`g7:MARB` | Official public notice given that 2 people intend to marry.
`MARC` | marriage contract<br/>`g7:MARC` | Recording a formal agreement of marriage, including the prenuptial agreement in which marriage partners reach agreement about the property rights of 1 or both, securing property to their children.
`MARL` | marriage license<br/>`g7:MARL` | Obtaining a legal license to marry.
`MARR` | marriage<br/>`g7:MARR` | A legal, common-law, or customary event such as a wedding or marriage ceremony that joins 2 partners to create or extend a family unit.
`MARS` | marriage settlement<br/>`g7:MARS` | Creating an agreement between 2 people contemplating marriage, at which time they agree to release or modify property rights that would otherwise arise from the marriage.

In addition, `FAM`.`EVEN` is a structure for a generic family event. It must have a `TYPE` substructure to define what kind of event is being provided.


### Attributes

Unlike events, the presence of an attribute is sufficient to assert the attribute applied to the individual, regardless of the attribute's substructures and payload.

#### Individual Attributes

Tag | Name<br/>URI | Description
--- | ---- | -----------
`CAST` | caste<br/>`g7:CAST` | The name of an individual's rank or status in society which is sometimes based on racial or religious differences, or differences in wealth, inherited rank, profession, or occupation.
`DSCR` | physical description<br/>`g7:DSCR` | The physical characteristics of a person.
`EDUC` | education<br/>`g7:EDUC` | Indicator of a level of education attained.
`IDNO` | identifying number<br/>`g7:IDNO` | A number or other string assigned to identify a person within some significant external system. It must have a `TYPE` substructure to define what kind of identification number is being provided.
`NATI` | nationality<br/>`g7:NATI` | An individual's national heritage or origin, or other folk, house, kindred, lineage, or tribal interest.
`NCHI` | number of children<br/>`g7:INDI-NCHI` | The number of children that this person is known to be the parent of (all marriages).
`NMR` | number of marriages<br/>`g7:NMR` | The number of times this person has participated in a family as a spouse or parent.
`OCCU` | occupation<br/>`g7:OCCU` | The type of work or profession of an individual.
`PROP` | property<br/>`g7:PROP` | Pertaining to possessions such as real estate or other property of interest.
`RELI` | religion<br/>`g7:INDI-RELI` | A religious denomination to which a person is affiliated or for which a record applies.
`RESI` | residence<br/>`g7:INDI-RESI` | An address or place of residence where an individual resided.
`SSN` | social security number<br/>`g7:SSN` | A number assigned by the United States Social Security Administration, used for tax identification purposes. It is a type of `IDNO`.
`TITL` | title<br/>`g7:INDI-TITL` | A formal designation used by an individual in connection with positions of royalty or other social status, such as Grand Duke.

In addition, `INDI`.`FACT` is a structure for a generic individual attribute. It must have a `TYPE` substructure to define what kind of attribute is being provided.

#### Family Attributes

Tag | Name<br/>URI | Description
----|--------------|-----------------
`NCHI` | number of children<br/>`g7:FAM-NCHI` | The number of children that belong to this family.
`RESI` | residence<br/>`g7:FAM-RESI` | An address or place of residence where a family resided.

In addition, `FAM`.`FACT` is a structure for a generic family attribute. It must have a `TYPE` substructure to define what kind of attribute is being provided.

### Latter-day Saint Ordinances

The structures describing ordinances performed by The Church of Jesus Christ of Latter-day Saints are unlike regular events in that they might either be performed during life or by proxy on the behalf of a deceased individual.

Proxy ordinances on behalf of deceased persons were once requested and officially recorded using an earlier version of GEDCOM.
This is no longer the case, but when it was the case the following principles held:

- `PLAC` was used only for ordinances that were performed by the recipient in life.
- `TEMP` was used with all `ENDL`, `SLGC`, and `SLGS`, but only with posthumous proxy `BAPL` and `CONL`.


Tag | Name<br/>URI | Description
----|------|-----------------
`BAPL` | baptism<br/>`g7:BAPL` | The event of baptism performed at age 8 or later by priesthood authority of The Church of Jesus Christ of Latter-day Saints. (See also [`BAPM`](#individual-events))
`CONL` | confirmation<br/>`g7:CONL` | The religious event by which a person receives membership in The Church of Jesus Christ of Latter-day Saints. (See also [`CONF`](#individual-events))
`INIL` | initiatory<br/>`g7:INIL` | A religious event where an initiatory ordinance for an individual was performed by priesthood authority in a temple of The Church of Jesus Christ of Latter-day Saints.
`ENDL` | endowment<br/>`g7:ENDL` | A religious event where an endowment ordinance for an individual was performed by priesthood authority in a temple of The Church of Jesus Christ of Latter-day Saints.
`SLGC` | sealing child<br/>`g7:SLGC` | A religious event pertaining to the sealing of a child to his or her parents in a temple ceremony of The Church of Jesus Christ of Latter-day Saints.
`SLGS` | sealing spouse<br/>`g7:SLGS` | A religious event pertaining to the sealing of a husband and wife in a temple ceremony of The Church of Jesus Christ of Latter-day Saints. (See also [`MARR`](#family-events))



### Structure types

Structure types are listed in this section alphabetically by tag.
When the same tag is used for different structure types in different contexts, they may be distinguished by their URI.

#### `ABBR` (Abbreviation) `g7:ABBR`

A short name of a title, description, or name used for sorting, filing, and retrieving records.

#### `ADDR` (Address) `g7:ADDR`

The location of, or most relevant to, the subject of the superstructure.
See `ADDRESS_STRUCTURE` for more details.

#### `ADOP` (Adoption) `g7:ADOP`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `ADOP` (Adoption) `g7:FAMC-ADOP`

An enumerated value from set `g7:enumset-ADOP` indicating which parent(s) in the family adopted this individual.

#### `ADR1` (Address Line 1) `g7:ADR1`

The first line of the address, used for indexing.
This structure's payload should be a single line of text equal to the first line of the corresponding `ADDR`.
See `ADDRESS_STRUCTURE` for more details.

:::deprecation
`ADR1` should not be added to new files; see `ADDRESS_STRUCTURE` for more details.
:::

#### `ADR2` (Address Line 2) `g7:ADR2`

The second line of the address, used for indexing.
This structure's payload should be a single line of text equal to the second line of the corresponding `ADDR`.
See `ADDRESS_STRUCTURE` for more details.

:::deprecation
`ADR2` should not be added to new files; see `ADDRESS_STRUCTURE` for more details.
:::

#### `ADR3` (Address Line 3) `g7:ADR3`

The third line of the address, used for indexing.
This structure's payload should be a single line of text equal to the third line of the corresponding `ADDR`.
See `ADDRESS_STRUCTURE` for more details.

:::deprecation
`ADR3` should not be added to new files; see `ADDRESS_STRUCTURE` for more details.
:::

#### `AGE` (Age at event) `g7:AGE`

The age of the individual at the time an event occurred. It is recommended that this be an age from a cited source document.

#### `AGNC` (Responsible agency) `g7:AGNC`

The organization, institution, corporation, person, or other entity that has responsibility for the associated context.
Examples are an employer of a person of an associated occupation, or a church that administered rites or events, or an organization responsible for creating or archiving records.

#### `ALIA` (Alias) `g7:ALIA`

A single individual may have facts distributed across multiple individual records, connected by `ALIA` pointers
(named after "alias" in the computing sense, not the pseudonym sense).

An `ALIA` pointer should not point to the superstructure of the `ALIA`.

:::note
This specification does not define how to connect `INDI` records with `ALIA`.
Some systems organize `ALIA` pointers to create a tree structure, with the root `INDI` record containing the composite view of all facts in the leaf `INDI` records.
Others distribute events and attributes between `INDI` records mutually linked by symmetric pairs of `ALIA` pointers.

`ALIA` is known to be used for different purposes by different users.
Some users use `ALIA` for uncertain connections, tentatively linking records prior to confirming identities and merging them into a single record;
other users create one `INDI` for each single-source view of an individual, linked together with `ALIA` and never merged into a single record;
other uses of `ALIA` may also exist.
Applications should avoid assuming a particular usage was intended without user confirmation.

A future version of this specification may adjust the definition of `ALIA`.
:::

#### `ANCI` (Ancestor interest) `g7:ANCI`

Indicates an interest in additional research for ancestors of this individual.
(See also `DESI`).

#### `ANUL` (Annulment) `g7:ANUL`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `ASSO` (Associates) `g7:ASSO`

A pointer to an associated individual.
See `ASSOCIATION_STRUCTURE` for more details.

#### `AUTH` (Author) `g7:AUTH`

The person, agency, or entity who created the record. For a published work, this could be the author, compiler, transcriber, abstractor, or editor. For an unpublished source, this may be an individual, a government agency, church organization, or private organization.

#### `BAPL` (Baptism, Latter-Day Saint) `g7:BAPL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `BAPM` (Baptism) `g7:BAPM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BARM` (Bar Mitzvah) `g7:BARM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BASM` (Bas Mitzvah) `g7:BASM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BIRT` (Birth) `g7:BIRT`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `KIND` (Birth Kind) `g7.1:BIRT-KIND`

An enumerated value from set `g7.1:enumset-BIRT-KIND` indicating the type of birth.

There is some conceptual overlap between `BIRT`.`TYPE` and `BIRT`.`KIND`:

- `BIRT`.`TYPE` is preferred for general-purpose human-readable information elaborating on the birth type.
- `BIRT`.`KIND` is preferred for information that informs some programmatic behaviors
    (such as creating a list of persons who were ever alive)
    or to support automated translation into multiple languages.

#### `BLES` (Blessing) `g7:BLES`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BURI` (Depositing remains) `g7:BURI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

Although defined as any depositing of remains since it was introduced in the first version of GEDCOM, this tag is a shortened form of the English word "burial" and has been interpreted to mean "depositing of remains by burial" by some applications and users.
In the absence of a clarifying `TYPE` substructure it is likely, but not guaranteed, that a `BURI` structure refers to a burial rather than another form of depositing remains.

#### `CALN` (Call number) `g7:CALN`

An identification or reference description used to file and retrieve items from the holdings of a repository.
Despite the word "number" in the name, may contain any character, not just digits.

#### `CAST` (Caste)  `g7:CAST`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `CAUS` (Cause) `g7:CAUS`

The reasons which precipitated an event.
It is often used subordinate to a death event to show cause of death, such as might be listed on a death certificate.

#### `CENS` (Census)  `g7:FAM-CENS`

An [Family Event](#family-events).

#### `CENS` (Census)  `g7:INDI-CENS`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CHAN` (Change) `g7:CHAN`

The most recent change to the superstructure.
This is metadata about the structure itself, not data about its subject.
See `CHANGE_DATE` for more details.

#### `CHIL` (Child) `g7:CHIL`

The child in a family, whether biological, adopted, foster, sealed, or other relationship.

#### `CHRA` (Christening, adult)  `g7:CHRA`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CHR` (Christening)  `g7:CHR`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CITY` (City) `g7:CITY`

The name of the city used in the address.
See `ADDRESS_STRUCTURE` for more details.

#### `CONF` (Confirmation)  `g7:CONF`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CONL` (Confirmation, Latter-Day Saint) `g7:CONL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `CONT` (Continued) `g7:CONT`

A pseudo-structure to indicate a line break.
The `CONT` tag is generated during serialization and is never present in parsed datasets.
See [Lines](#lines) for more details.

#### `COPR` (Copyright) `g7:COPR`

A copyright statement, as appropriate for the copyright laws applicable to this data.

#### `CORP` (Corporate name) `g7:CORP`

The name of the business, corporation, or person that produced or commissioned the product.

#### `CREA` (Creation) `g7:CREA`

The initial creation of the superstructure.
This is metadata about the structure itself, not data about its subject.
See `CREATION_DATE` for more details.

#### `CREM` (Cremation)  `g7:CREM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CROP` (Crop) `g7:CROP`

A subregion of an image to display.
It is only valid when the superstructure links to a `MULTIMEDIA_RECORD` with at least
1 `FILE` substructure that refers to an external file with a defined pixel unit.

`LEFT` and `TOP` indicate the top-left corner of the region to display.
`WIDTH` and `HEIGHT` indicate how many pixels wide and tall the region to display is.
If omitted, `LEFT` and `TOP` each default to 0;
`WIDTH` defaults to the image width minus `LEFT`;
and `HEIGHT` defaults to the image height minus `TOP`.

If the superstructure links to a `MULTIMEDIA_RECORD` that includes multiple `FILE`
substructures, the `CROP` applies to the first `FILE` to which it can apply,
namely the first external file with a defined pixel unit.

It is recommended that `CROP` be used only with a single-FILE `MULTIMEDIA_RECORD`.

The following are errors:

- `LEFT` or `LEFT` + `WIDTH` exceed the image width.
- `TOP` or `TOP` + `HEIGHT` exceed the image height.
- `CROP` applied to a non-image or image without a defined pixel unit.


#### `CTRY` (Country) `g7:CTRY`

The name of the country that pertains to the associated address.
See `ADDRESS_STRUCTURE` for more details.

#### `DATA` (Data) `g7:DATA`

A structure with no payload used to distinguish a description of something from metadata about it.
For example, `SOUR` and its other substructures describe a source itself,
while `SOUR`.`DATA` describes the content of the source.

#### `DATA` (Data) `g7:SOUR-DATA`

See `g7:DATA`.

#### `DATA` (Data) `g7:HEAD-SOUR-DATA`

The database, electronic data source, or digital repository from which this dataset was exported.
The payload is the name of the database, electronic data source, or digital repository,
with substructures providing additional details about it (not about the export).

#### `DATE` (Date) `g7:DATE`

The principal date of the subject of the superstructure.
The payload is a `DateValue`.

When the superstructure is an event, the principal date indicates when the event took place.

When the superstructure is an attribute, the principal date indicates when the attribute was observed, asserted, or applied.
A date period might put bounds on the attributes applicability, but other date forms assume that the attribute may have also applied on other dates too.

When the superstructure is a `g7:SOUR-DATA`, the principal date indicates when the data was entered into the source; or, for a source like a website that changes over time, a date on which the source contained the data.

See `DATE_VALUE` for more details.

#### `DATE` (Date) `g7:DATE-exact`

The principal date of the subject of the superstructure.
The payload is a `DateExact`.

#### `DATE` (Date) `g7:HEAD-DATE`

The `DateExact` that this document was created.

#### `DATE` (Date) `g7:NO-DATE`

The `DatePeriod` during which the event did not occur or the attribute did not apply.

#### `DATE` (Date) `g7:DATA-EVEN-DATE`

The `DatePeriod` covered by the entire source; the period during which this source recorded events.

#### `DEAT` (Death) `g7:DEAT`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `DESI` (Descendant Interest) `g7:DESI`

Indicates an interest in research to identify additional descendants of this individual.
See also `ANCI`.

#### `DEST` (Destination) `g7:DEST`

An identifier for the system expected to receive this document.
See `HEAD`.`SOUR` for guidance on choosing identifiers.

#### `DIVF` (Divorce filing) `g7:DIVF`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `DIV` (Divorce) `g7:DIV`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `DSCR` (Description) `g7:DSCR`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `EDUC` (Education) `g7:EDUC`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `EMAIL` (Email) `g7:EMAIL`

An electronic mail address, as defined by any relevant standard
such as [RFC 3696](https://www.rfc-editor.org/info/rfc3696), [RFC 5321](https://www.rfc-editor.org/info/rfc5321), or [RFC 5322](https://www.rfc-editor.org/info/rfc5322).

If an invalid email address is present upon import, it should be preserved as-is on export.

:::note
The version 5.5.1 specification contained a typo where this tag was sometimes written `EMAI` and sometimes written `EMAIL`. `EMAIL` should be used in version 7.0 and later.
:::

#### `EMIG` (Emigration) `g7:EMIG`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `ENDL` (Endowment, Latter-Day Saint) `g7:ENDL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `ENGA` (Engagement) `g7:ENGA`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `EVEN` (Event) `g7:FAM-EVEN`

See `g7:INDI-EVEN`.

#### `EVEN` (Event) `g7:INDI-EVEN`

An event: a noteworthy happening related to an individual or family.
If a specific event type exists, it should be used instead of a generic `EVEN` structure.
Each `EVEN` must be classified by a subordinate use of the `TYPE` tag
and may be further described in the structure's payload.

:::example
A person that signed a lease for land dated October 2, 1837 and a lease for mining equipment dated November 4, 1837 would be written as:

```gedcom
0 @I1@ INDI
1 EVEN
2 TYPE Land Lease
2 DATE 2 OCT 1837
1 EVEN Mining equipment
2 TYPE Equipment Lease
2 DATE 4 NOV 1837
```
:::

#### `EVEN` (Event) `g7:DATA-EVEN`

A list of enumerated values from set `g7:enumset-EVENATTR` indicating the types of events that were recorded in a particular source.
Each event type is separated by a comma and space.
For example, a parish register of births, deaths, and marriages would be `BIRT, DEAT, MARR`.

#### `EVEN` (Event) `g7:SOUR-EVEN`

An enumerated value from set `g7:enumset-EVENATTR` indicating the type of event or attribute which was responsible for the source entry being recorded.
For example, if the entry was created to record a birth of a child, then the type would be `BIRT` regardless of the assertions made from that record, such as the mother's name or mother's birth date.

#### `EXID` (External Identifier) `g7:EXID`

An identifier for the subject of the superstructure.
The identifier is maintained by some external authority;
the authority owning the identifier is provided in the TYPE substructure; see `EXID`.`TYPE` for more details.

Depending on the maintaining authority, an `EXID` may be a unique identifier for the subject, an identifier for 1 of several views of the subject, or an identifier for the externally-maintained copy of the same information as is contained in this structure. However, unlike `UID` and `REFN`, `EXID` does not identify a structure; structures with the same `EXID` may have originated independently rather than by edits from the same starting point.

`EXID` identifiers are expected to be unique. Once assigned, an `EXID` identifier should never be re-used for any other purpose.

#### `FAM` (Family record) `g7:record-FAM`

See `FAMILY_RECORD`

:::note
The common case is that each couple has one `FAM` record,
but that is not always the case.

A couple that separates and then gets together again
can be represented either as a single `FAM` with multiple events (`MARR`, `DIV`, etc.)
or as a separate `FAM` for each time together.
Some user interfaces may display these two in different ways
and the two admit different semantics in sourcing.
A single `FAM` with two `MARR` with distinct dates might also represent uncertainty about dates
and a pair of `FAM` with same spouses might also be the result of merging multiple files.

Implementers should support both representations,
and should choose between them based on user input or other context beyond that provided in the datasets themselves.
:::

#### `FACT` (Fact) `g7:FAM-FACT`

See `g7:INDI-FACT`.

#### `FACT` (Fact) `g7:INDI-FACT`

A noteworthy attribute or fact concerning an individual or family.
If a specific attribute type exists, it should be used instead of a generic `FACT` structure.
Each `FACT` must be classified by a subordinate use of the `TYPE` tag
and may be further described in the structure's payload.

:::example
If the attribute being defined was 1 of the person's skills, such as woodworking, the `FACT` tag would have the value of "Woodworking", followed by a subordinate `TYPE` tag with the value "Skills".

```gedcom
0 @I1@ INDI
1 FACT Woodworking
2 TYPE Skills
```
:::

#### `FAMC` (Family child) `g7:INDI-FAMC`

The family in which an individual appears as a child.
It is also used with a `g7:FAMC-STAT` substructure to show individuals who are not children of the family.
See `FAMILY_RECORD` for more details.

#### `FAMC` (Family child) `g7:FAMC`

The family with which this individual event is associated.

#### `FAMC` (Family child) `g7:ADOP-FAMC`

The individual or couple that adopted this individual.

Adoption by an individual, rather than a couple, may be represented either by pointing to a `FAM` where that individual is a `HUSB` or `WIFE` and using a `g7:FAMC-ADOP` substructure to indicate which 1 performed the adoption; or by using a `FAM` where the adopting individual is the only `HUSB`/`WIFE`.

#### `FAMS` (Family spouse) `g7:FAMS`

The family in which an individual appears as a partner.
See `FAMILY_RECORD` for more details.

#### `FAX` (Facsimile) `g7:FAX`

A fax telephone number appropriate for sending data facsimiles.
See `PHON` for additional comments on telephone numbers.

#### `FCOM` (First communion) `g7:FCOM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `FILE` (File reference) `g7:FILE`

A reference to an external file.
See the [File Path datatype](#file-path) for more details.

#### `FORM` (Format) `g7:FORM`

The [media type](#media-type) of the file referenced by the superstructure.

#### `FORM` (Format) `g7:PLAC-FORM`

A comma-separated list of jurisdictional titles,
which has the same number of elements and in the same order as the `PLAC` structure.
As with `PLAC`, this shall be ordered from lowest to highest jurisdiction.

:::example
The following represents Baltimore, a city that is not within a county.

```gedcom
2 PLAC Baltimore, , Maryland, USA
3 FORM City, County, State, Country
```
:::

#### `FORM` (Format) `g7:HEAD-PLAC-FORM`

Any `PLAC` with no [`FORM`](#PLAC-FORM) shall be treated as if it has this [`FORM`](#PLAC-FORM).

#### `GEDC` (GEDCOM) `g7:GEDC`

A container for information about the entire document.

It is recommended that applications write `GEDC` with its required substructure `g7:GEDC-VERS` as the first substructure of `HEAD`.

#### `GIVN` (Given name) `g7:GIVN`

A given or earned name used for official identification of a person.

#### `GRAD` (Graduation) `g7:GRAD`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `HEAD` (Header) `g7:HEAD`

A pseudo-structure for storing metadata about the document.
See [The Header and Trailer](#the-header) for more details.

#### `HEIGHT` (Height in pixels) `g7:HEIGHT`

How many pixels to display vertically for the image.
See `CROP` for more details.

:::note
`HEIGHT` is a number of pixels.
The correct tag for the height of an individual is the `DSCR` attribute.

:::example
```gedcom
0 @I45@ INDI
1 DSCR brown eyes, 5ft 10in, 198 pounds
```
:::
:::

#### `HUSB` (Husband) `g7:HUSB`

A structure for storing information related to one partner in the context of a `FAMILY_EVENT`;
in particular,
the partner referenced in the `g7:FAM-HUSB` substructure
of the `g7:record-FAM` superstructure of the `FAMILY_EVENT`.

:::example
The following indicates that individual `@I1@` was 32 years old at the time of the marriage, without indicating an age for individual `@I2@`.

```gedcom
0 @F1@ FAM
1 HUSB @I1@
1 WIFE @I2@
1 MARR
2 HUSB
3 AGE 32y
```
:::

#### `HUSB` (Husband) `g7:FAM-HUSB`

This is a partner in a `FAM` record.
See `FAMILY_RECORD` for more details.

#### `IDNO` (Identification number) `g7:IDNO`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `IMMI` (Immigration) `g7:IMMI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `INDI` (Individual) `g7.1:record-INDI`

See `INDIVIDUAL_RECORD`.

#### `INIL` (Initiatory, Latter-Day Saint) `g7:INIL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.  Previously, GEDCOM versions 3.0 through 5.3 called this `WAC`; it was not part of 5.4 through 5.5.1.
FamilySearch GEDCOM 7.0 reintroduced it with the name `INIL` for consistency with `BAPL`, `CONL`, and `ENDL`.

#### `LANG` (Language) `g7:LANG`

The primary human language of the superstructure.
The primary language in which the `Text`-typed payloads of the superstructure and its substructures appear.

The payload of the `LANG` structure is a language tag, as defined by [BCP 47](https://www.rfc-editor.org/info/bcp47).
A [registry of component subtags](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) is maintained publicly by the IANA.

In the absence of a `LANG` structure, the language is assumed to be unspecified;
that may also be recorded explicitly with language tag `und` (meaning "undetermined").
See `g7:HEAD-LANG` for information about applying language-specific algorithms to text in an unspecified language.

If the text is primarily in one language with a few parts in a different language,
it is recommended that a language tag identifying the primary language be used.
If no one language is primary, the language tag `mul` (meaning "multiple") may be used,
but most language-specific algorithms will treat `mul` the same way they do `und`.

:::note
Conversations are ongoing about adding part-of-payload language tagging in a future version of the specification
to provide more fidelity for multilingual text.
:::

If the text is not in any human language and should not be treated as lingual content,
the language tag `zxx` (meaning "no linguistic content" or "not applicable") may be used.
An example of `zxx` text might be a diagram approximated using characters for their shape, not their meaning.

:::note
This specification does not permit `LANG` in every place where human language text might appear.
Conversations are ongoing about adding it in more places in a future version of the specification.
Using the current specification, additional language tagging can be accomplished using a [documented extension tag](#extension-tags)
by including the following in the header:

```gedcom
1 SCHEMA
2 TAG _LANG https://gedcom.io/terms/v7/LANG
```

and using the extension tag like so:

```gedcom
2 DATE 31 AUG 2018
3 PHRASE 2018年8月31日
4 _LANG cmn
```
:::


#### `LANG` (Language) `g7:HEAD-LANG`

A default language which may be used to interpret any `Text`-typed payloads that lack a specific language tag from a `g7:LANG` structure.
An application may choose to use a different default based on its knowledge of the language preferences of the user.

The payload of the `LANG` structure is a language tag, as defined by [BCP 47](https://www.rfc-editor.org/info/bcp47).

:::note
Some algorithms on text are language-specific.
Examples include sorting sequences, name comparison and phonetic name matching algorithms, spell-checking, computer-synthesized speech, Braille transcription, and language translation.
When the language of the text is given through a `g7:LANG`, that should be used.
When `g7:LANG` is not available, `g7:HEAD-LANG` provides the file creator's suggested default language.
For some language-specific algorithms, the user's preferred language may be a more appropriate default than the file's default language.
User language preferences can be found in a variety of platform-specific places, such as the default language from operating system settings, user locales, Input Method Editors (IMEs), etc.
:::


#### `LANG` (Language) `g7:SUBM-LANG`

A language the subject of that record understands.

The payload of the `LANG` structure is a language tag, as defined by [BCP 47](https://www.rfc-editor.org/info/bcp47).

#### `LATI` (Latitude) `g7:LATI`

A latitudinal coordinate.

#### `LEFT` (Left crop width) `g7:LEFT`

Left is a number of pixels to not display from the left side of the image.
See `CROP` for more details.

#### `LONG` (Longitude) `g7:LONG`

A longitudinal coordinate.

#### `MAP` (Map) `g7:MAP`

A representative point for a location,
as defined by `LATI` and `LONG` substructures.

Note that `MAP`  provides
neither a notion of accuracy
(for example, the `MAP` for a birth event may be some distance from the point where the birth occurred)
nor a notion of region size
(for example, the `MAP` for a place "Belarus" may be anywhere within that nation's 200,000 square kilometer area).

#### `MARB` (Marriage banns) `g7:MARB`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARC` (Marriage contract) `g7:MARC`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARL` (Marriage license) `g7:MARL`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARR` (Marriage) `g7:MARR`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MARS` (Marriage settlement) `g7:MARS`

A [Family Event](#family-events).
See also `FAMILY_EVENT_STRUCTURE`.

#### `MEDI` (Medium) `g7:MEDI`

An enumerated value from set `g7:enumset-MEDI` providing information about the media or the medium in which information is stored.

When `MEDI` is a substructure of a `g7:CALN`, it is recommended that its payload describes the medium directly found at that call number rather than a medium from which it was derived.

:::example
Consider an asset in a repository that is a digital scan of a book of compiled newspapers;
for this asset, the `CALN`.`MEDI` is recommended to be `ELECTRONIC` rather than `BOOK` or `NEWSPAPER`.
:::

When `MEDI` is a substructure of a `g7:FORM`, it is recommended that its payload describes the medium from which it was derived.

:::example
Consider a digital photo in a multimedia record;
for this asset, the `FORM`.`MEDI` is recommended to be `PHOTO` rather than `ELECTRONIC`.
:::

#### `MIME` (Media type) `g7:MIME`

Indicates the [media type](#media-type) of the payload of the superstructure.

As of version 7.1, three media types are supported by this structure:

- `text/plain` shall be presented to the user as-is, preserving all spacing, line breaks, and so forth.

- `text/html` uses HTML tags to provide presentation information.
    Applications should support at least the following:
    
    - `p` and `br` elements for paragraphing and line breaks.
    - `b`, `i`, `u`, and `s` elements for bold, italic, underlined, and strike-through text (or corresponding display in other locales; see [HTML §4.5](https://html.spec.whatwg.org/multipage/text-level-semantics.html) for more).
    - `sup` and `sub` elements for super- and sub-script.
    - The 3 XML entities that appear in text: `&amp;`, `&lt;` `&gt;`.
        Note that `&quote;` and `&apos;` are only needed in attributes.
        Other entities should be represented as their respective Unicode characters instead.
    
    Supporting more of HTML is encouraged.
    Unsupported tags should be ignored during display.

    <div class="note">
    Applications are welcome to support more XML entities or HTML character references in their user interface.
    However, exporting must only use the core XML entities, translating any other entities into their corresponding Unicode characters.
    </div>

    <div class="note">
    Applications are welcome to support additional HTML elements,
    but they should ensure that content is meaningful if those extra elements are ignored and only their content text is displayed.
    </div>

    If needed, `text/html` can be converted to `text/plain` using the following steps:

    1. Replace any sequence of 1 or more spaces, tabs, and line breaks with a single space
    2. Case-insensitively replace each `<p`...`>`, `</p`...`>`, and `<br`...`>` with a line break
    3. Remove all other `<`...`>` tags
    4. Replace each `&lt;` with `<` and `&gt;` with `>`
    5. Replace each `&amp;` with `&`

- `text/markdown` employs a plain text format for creating structured documents, and is designed
    to be fairly understandable by users even if only displayed as plain text.
    Applications should support the elements specified by [CommonMark](https://commonmark.org).

    For example:

    <div class="example">

    ````gedcom
    1 NOTE # 1940 US Census for New York, New York
    2 CONT __Individuals located at this address__
    2 CONT * John **Doe** (age 35)
    2 CONT * Sally (age 32)
    2 CONT * Junior (age 3)
    2 CONT * Betty (age 1)
    2 MIME text/markdown
    ````
    
    </div>

    <div class="note">
    Applications are welcome to support additional Markdown elements,
    but they should ensure that content is meaningful if those extra elements are only displayed as plain text.
    </div>

:::note
Other `text` media types not discussed above are also permitted, though not recommended.
If present, they are considered extensions.  Such extensions do not require an
[extension tag](#extensions) because the definition of `g7:MIME` is sufficient
to cover this kind of extension.
:::

:::note
Media types are also used by external files, as described under `FORM`. External file media types are not limited to `text` types.
:::

#### `NAME` (Name) `g7:NAME`

The name of the superstructure's subject, represented as a simple string.

#### `NAME` (Name) `g7:INDI-NAME`

A `PERSONAL_NAME_STRUCTURE` with parts, translations, sources, and so forth.

#### `NATI` (Nationality) `g7:NATI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `NATU` (Naturalization) `g7:NATU`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `NCHI` (Number of children) `g7:FAM-NCHI`

A [Family Attribute](#family-attributes).
See also `FAMILY_ATTRIBUTE_STRUCTURE`.

#### `NCHI` (Number of children) `g7:INDI-NCHI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `NICK` (Nickname) `g7:NICK`

A descriptive or familiar name that is used instead of, or in addition to, one’s official or legal name.

:::note
The label "nickname" and description text of this structure were introduced with version 5.5 in 1996, but are understood differently by different users.
Some use `NICK` only for names that would be inappropriate in formal settings.
Some use it for pseudonyms regardless of where they are used.
Some use it for any variant of a name that is not the one used on legal documents.
Because all of these uses, and likely others as well, are common in existing data, no further clarification of the meaning of the `NICK` structure is possible without contradicting some existing data.
:::

#### `NMR` (Number of marriages) `g7:NMR`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `NO` (Did not happen) `g7:NO`

An enumerated value from set `g7:enumset-EVEN` identifying an event type which did not occur to the superstructure's subject.
A specific payload `NO XYZ` should only appear where `XYZ` would be legal.

See `NON_EVENT_STRUCTURE` for more details.

#### `NOTE` (Note) `g7:NOTE`

A `NOTE_STRUCTURE`, containing additional information provided by the submitter for understanding the enclosing data.

When a substructure of `HEAD`, it should describe the contents of the document in terms of "ancestors or descendants of" so that the person receiving the data knows what genealogical information the document contains.

#### `NPFX` (Name prefix) `g7:NPFX`

Text that appears on a name line before the given and surname parts of a name.

#### `NSFX` (Name suffix) `g7:NSFX`

Text which appears on a name line after or behind the given and surname parts of a name.

#### `OBJE` (Object) `g7:OBJE`

See `MULTIMEDIA_LINK`.

#### `OBJE` (Object) `g7:record-OBJE`

See `MULTIMEDIA_RECORD`.

#### `OCCU` (Occupation) `g7:OCCU`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `ORDN` (Ordination) `g7:ORDN`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `PAGE` (Page) `g7:PAGE`

A specific location within the information referenced. For a published work, this could include the volume of a multi-volume work and the page number or numbers. For a periodical, it could include volume, issue, and page numbers. For a newspaper, it could include a date, page number, and column number. For an unpublished source or microfilmed works, this could be a film or sheet number, page number, or frame number. A census record might have an enumerating district, page number, line number, dwelling number, and family number.

It is recommended that the data in this field be formatted comma-separated with label: value pairs

:::example
```gedcom
2 SOUR @S1@
3 PAGE Film: 1234567, Frame: 344, Line: 28
```
:::

If the superstructure's pointer is `@VOID@`
then there is no information referenced
and the `PAGE` may describe the entire source.

:::example
```gedcom
1 DSCR Tall enough his head touched the ceiling
2 SOUR @VOID@
3 PAGE His grand-daughter Lydia told me this in 1980
```
:::

#### `PEDI` (Pedigree) `g7:PEDI`

An enumerated value from set `g7:enumset-PEDI` indicating the type of child-to-family relationship represented by the superstructure.

#### `PHON` (Phone) `g7:PHON`

A telephone number.
Telephone numbers have many regional variations and can contain non-digit characters.
Users should be encouraged to use internationalized telephone numbers rather than local versions.
As a starting point for this recommendation, there are international standards that use a "'+'" shorthand for the international prefix (for example, in place of "011" in the US or "00" in the UK).
Examples are `+1 (555) 555-1234` (US) or `+44 20 1234 1234` (UK).

See ITU standards [E.123](https://www.itu.int/rec/T-REC-E.123) and [E.164](https://www.itu.int/rec/T-REC-E.164) for more information.

#### `PHRASE` (Phrase) `g7:PHRASE`

Textual information that cannot be expressed in the superstructure due to the limitations of its data type.
A `PHRASE` may restate information contained in the superstructure, but doing so is not recommended unless it is needed for clarity.

:::example
A date interpreted from the phrase "The Feast of St John" might be

````gedcom
2 DATE 24 JUN 1852
3 PHRASE During the feast of St John
````
:::

:::example
A record using `1648/9` to indicate a change in new year might become

````gedcom
2 DATE 30 JAN 1649
3 PHRASE 30th of January, 1648/9
````
:::

:::example
A record using `1648/9` to indicate uncertainty in the year might become

````gedcom
2 DATE BET 1648 AND 1649
3 PHRASE 1648/9
````
:::

:::example
A record using `Q1 1867` to indicate an event occurred sometime within the first quarter of 1867 might become

````gedcom
2 DATE BET 1 JAN 1867 AND 31 MAR 1867
3 PHRASE Q1 1867
````
:::

:::example
A record defining the Maid of Honor in a marriage might become

````gedcom
1 MARR
2 ASSO @I2@
3 ROLE OTHER
4 PHRASE Maid of Honor
````
:::

:::example
A name given to a foundling orphan might be

````gedcom
1 NAME Mary //
2 GIVN Mary
2 TYPE OTHER
3 PHRASE given by orphanage
````
:::

:::example
A record specifying a writer's "pen name" (a type of professional name) might become

````gedcom
1 NAME Mark /Twain/
2 TYPE PROFESSIONAL
3 PHRASE Pen
````
:::


#### `PLAC` (Place) `g7:PLAC`

The principal place in which the superstructure's subject occurred,
represented as a [List] of jurisdictional entities in a sequence from the lowest to the highest jurisdiction,
where "jurisdiction" includes units in a political, ecclesiastical, and geographical hierarchies
and may include units of any size, such as a continent, "at sea", or a specific building, farm, or cemetery.
As with other lists, the jurisdictions are separated by commas.
Any jurisdiction's name that is missing is still accounted for by an empty string in the list.

The type of each jurisdiction is given in the `PLAC`.`FORM` substructure, if present,
or in the `HEAD`.`PLAC`.`FORM` structure.
If neither is present, the jurisdictional types are unspecified
beyond the lowest-to-highest order noted above.

#### `PLAC` (Place) `g7:HEAD-PLAC`

This is a placeholder for providing a default `PLAC`.`FORM`, and must not have a payload.

#### `POST` (Postal code) `g7:POST`

A code used by a postal service to identify an area to facilitate mail handling.
See `ADDRESS_STRUCTURE` for more details.

#### `PROB` (Probate) `g7:PROB`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `PROP` (Property) `g7:PROP`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `PUBL` (Publication) `g7:PUBL`

When and where the record was created. For published works, this includes information such as the city of publication, name of the publisher, and year of publication.

For an unpublished work, it includes the date the record was created and the place where it was created, such as the county and state of residence of a person making a declaration for a pension or the city and state of residence of the writer of a letter.

#### `QUAY` (Quality of data) `g7:QUAY`

An enumerated value from set `g7:enumset-QUAY` indicating the credibility of a piece of information, based on its supporting evidence.
Some systems use this feature to rank multiple conflicting opinions for display of most likely information first.
It is not intended to eliminate the receivers' need to evaluate the evidence for themselves.

#### `REFN` (Reference) `g7:REFN`

A user-defined number or text that the submitter uses to identify the superstructure.
For instance, it may be a record number within the submitter's automated or manual system, or it may be a page and position number on a pedigree chart.

This is metadata about the structure itself, not data about its subject.
Multiple structures describing different aspects of the same subject must not have the same `REFN` value.

#### `RELI` (Religion) `g7:RELI`

A religious denomination associated with the event or attribute described by the superstructure.

#### `RELI` (Religion) `g7:INDI-RELI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `RESN` (Restriction) `g7:RESN`

A [List] of enumerated values from set `g7:enumset-RESN` signifying access to information may be denied or otherwise restricted.

The `RESN` structure is provided to assist software in filtering data that should not be exported or otherwise used in a particular context. It is recommended that tools provide an interface to allow users to filter data on export
such that certain `RESN` structure payload entries result in the `RESN` structure and its superstructure being removed from the export.
Such removal must abide by some constraints: see [Removing data](#removing-data) for more details.

This is metadata about the structure itself, not data about its subject.

#### `REPO` (Repository) `g7:REPO`

See `SOURCE_REPOSITORY_CITATION`.

#### `REPO` (Repository) `g7.1:record-REPO`

See `REPOSITORY_RECORD`.

#### `RESI` (Residence) `g7:FAM-RESI`

A [Family Attribute](#family-attributes).
See also `FAMILY_ATTRIBUTE_STRUCTURE`.

See `g7:INDI-RESI` for comments on the use of payload strings in `RESI` structures.


#### `RESI` (Residence) `g7:INDI-RESI`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

Where possible, the residence should be identified in `PLAC` and/or `ADDR` substructures of the `RESI` structure. The payload text should not duplicate `PLAC` or `ADDR` information, but may be used for residence information that cannot be expressed by those structures.

:::example
The following two examples show situations where a `RESI` payload may be appropriate:

```gedcom
1 RESI living with an aunt
2 DATE ABT MAR 1894
```

```gedcom
1 RESI in a mobile caravan
2 PLAC , , Austro-Hungarian Empire
3 FORM City, County, Country
```
:::


#### `RETI` (Retirement) `g7:RETI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `ROLE` (Role) `g7:ROLE`

An enumerated value from set `g7:enumset-ROLE` indicating what role this person played in an event or person's life.

:::example
The following indicates a child's birth record as the source of the mother's name:

```gedcom
0 @I1@ INDI
1 NAME Mary //
2 SOUR @S1@
3 EVEN BIRT
4 ROLE MOTH
```
:::

:::example
The following indicates that a person's best friend was a witness at their baptism:

```gedcom
0 @I2@ INDI
1 ASSO @I3@
2 ROLE FRIEND
3 PHRASE best friend
1 BAPM
2 ASSO @I3@
3 ROLE WITN
```
:::

#### `SCHMA` (Extension schema) `g7:SCHMA`

A container for storing meta-information about the extension tags used in this document.
See [Extensions](#extensions) for more details.

#### `SDATE` (Sort date) `g7:SDATE`

A date to be used as a sorting hint.
It is intended for use when the actual date is unknown, but the display order may be dependent on date.

If both a `DATE` and `SDATE` are present in the same structure,
the `SDATE` should be used for sorting and positioning
while the `DATE` should be displayed as the date of the structure.

`SDATE` and its substructures (including `PHRASE`, `TIME`, and any extension structures) should be used only as sorting hints, not to convey historical meaning.

It is recommended to use a payload that matches `[[day D] month D] year [D epoch]`.
Other DateValue forms may have unreliable effects on sorting. Including a month and
day is encouraged to help different applications sort dates the same way, as the
relative ordering of dates with different levels of precision is not well defined.

#### `SEX` (Sex) `g7:SEX`

An enumerated value from set `g7:enumset-SEX` that indicates the sex of the individual at birth.

#### `SLGC` (Sealing, child) `g7:SLGC`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `SLGS` (Sealing, spouse) `g7:SLGS`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_SPOUSE_SEALING`.

#### `SNOTE` (Shared note) `g7:SNOTE`

A pointer to a note that is shared by multiple structures.
See `NOTE_STRUCTURE` for more details.

#### `SNOTE` (Shared note) `g7.1:record-SNOTE`

A note that is shared by multiple structures.
See `SHARED_NOTE_RECORD` for more details.

#### `SOUR` (Source) `g7:SOUR`

A description of the relevant part of a source to support the superstructure's data.
See `SOURCE_CITATION` for more details.

#### `SOUR` (Source) `g7.1:record-SOUR`

A description of an entire source.
See `SOURCE_RECORD` for more details.

#### `SOUR` (Source) `g7:HEAD-SOUR`

An identifier for the product producing this dataset.
A registration process for these identifiers existed for a time, but no longer does.
If an existing identifier is known, it should be used.
Otherwise, a URI owned by the product should be used instead.

#### `SPFX` (Surname prefix) `g7:SPFX`

A name piece used as a non-indexing pre-part of a surname.

#### `SSN` (Social security number) `g7:SSN`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `STAE` (State) `g7:STAE`

A geographical division of a larger jurisdictional area, such as a state within the United States of America.
See `ADDRESS_STRUCTURE` for more details.

#### `STAT` (Status) `g7:ord-STAT`

An enumerated value from set `g7:enumset-ord-STAT` assessing of the state or condition of an ordinance.

#### `STAT` (Status) `g7:FAMC-STAT`

An enumerated value from set `g7:enumset-FAMC-STAT` assessing of the state or condition of a researcher's belief in a family connection.

#### `SUBM` (Submitter) `g7:SUBM`

A contributor of information in the substructure.
This is metadata about the structure itself, not data about its subject.

#### `SUBM` (Submitter) `g7.1:record-SUBM`

A description of a contributor of information to the document.
See `SUBMITTER_RECORD` for more details.

#### `SURN` (Surname) `g7:SURN`

A family name passed on or used by members of a family.

#### `TAG` (Extension tag) `g7:TAG`

Information relating to a single extension tag as used in this document.
See [Extensions](#extensions) for more details.

#### `TEMP` (Temple) `g7:TEMP`

The name of a temple of The Church of Jesus Christ of Latter-day Saints.
Previous versions recommended using a set of abbreviations for temple names, but the list of abbreviations is no longer published by the Church and using abbreviations is no longer recommended.

#### `TEXT` (Text from Source) `g7:TEXT`

A verbatim copy of any description contained within the source.
This indicates notes or text that are actually contained in the source document, not the submitter's opinion about the source.
This should be, from the evidence point of view, "what the original record keeper said" as opposed to the researcher's interpretation.

#### `TIME` (Time) `g7:TIME`

A `Time` value in a 24-hour clock format.

#### `TITL` (Title) `g7:TITL`

The title, formal or informal, of the superstructure.

A published work, such as a book, might have a title plus the title of the series of which the book is a part. A magazine article would have a title plus the title of the magazine that published the article.

For an unpublished work, including most digital files, titles should be descriptive and appropriate to the work.

:::example

<p></p>

* The `TITL` of a letter might include the date, the sender, and the receiver.
* The `TITL` of a transaction between a buyer and seller might have their names and the transaction date.
* The `TITL` of a family Bible containing genealogical information might have past and present owners and a physical description of the book.
* The `TITL` of a personal interview would cite the informant and interviewer.

:::

Some sources may have a citation text that cannot readily be represented using the `SOURCE_RECORD` substructures `AUTH`, `PUBL`, `REPO`, and so on.
In such cases, the entire citation text may be presented as the payload of the `SOUR`.`TITL`.

#### `TITL` (Title) `g7:INDI-TITL`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `TOP` (Top crop width) `g7:TOP`

A number of pixels to not display from the top side of the image.
See `CROP` for more details.


#### `TRAN` (Translation)

A representation of the superstructure's data in a different format.

In some situations it is desirable to provide the same semantic content in multiple formats.
Where this is desirable, a `TRAN` substructure is used,
where the specific format is given in its language tag substructure, media type substructure, or both.

Different `TRAN` structures are used in different contexts to fully capture the structure of the information being presented in multiple formats.
In all cases, a `TRAN` structure's payload and substructures should provide only information also contained in the `TRAN` structures' superstructure, but provide it in a new language, script, or media type.

Each `TRAN` substructure must have either a language tag or a media type or both.
Each `TRAN` structure must differ from its superstructure
and from every other `TRAN` substructure of its superstructure
in either its language tag or its media type or both.

#### `TRAN` (Translation) `g7:NAME-TRAN`

A type of `TRAN` substructure specific to [Personal Names](#personal-name).
Each `NAME`.`TRAN` must have a `LANG` substructure.
See also `INDI`.`NAME`.

:::example
The following presents a name in Mandarin, transliterated using Pinyin

```gedcom
1 NAME /孔/德庸
2 GIVN 德庸
2 SURN 孔
2 TRAN /Kǒng/ Déyōng
3 GIVN Déyōng
3 SURN Kǒng
3 LANG zh-pinyin
```
:::

#### `TRAN` (Translation) `g7:PLAC-TRAN`

A type of `TRAN` substructure specific to places.
Each `PLAC`.`TRAN` must have a `LANG` substructure.
See also `PLAC`.

:::example
The following presents a place
in Japanese
with a romaji transliteration
and English translation

```gedcom
2 PLAC 千代田, 東京, 日本
3 FORM 区, 都, 国
3 LANG ja
3 TRAN Chiyoda, Tokyo, Nihon
4 LANG ja-Latn
3 TRAN Chiyoda, Tokyo, Japan
4 LANG en
```
:::


#### `TRAN` (Translation) `g7:NOTE-TRAN`

A type of `TRAN` for unstructured human-readable text,
such as is found in `NOTE` and `SNOTE` payloads.
Each `g7:NOTE-TRAN` must have either a `LANG` substructure or a `MIME` substructure or both.
If either is missing, it is assumed to have the same value as the superstructure.
See also `NOTE` and `SNOTE`.

:::example
The following presents the same note in HTML-format English;
in plain-text with the same language as the superstructure (English);
and in Spanish with the same media type as the superstructure (HTML).

```gedcom
1 NAME Arete /Hernandez/
2 NOTE Named after Arete from <i>The Odyssey</i>
3 LANG en
3 MIME text/html
3 TRAN Named after Arete from "The Odyssey"
4 MIME text/plain
3 TRAN Nombrada en honor a Arete de <i>La Odisea</i>
4 LANG es
```
:::

It is recommended that text given in `text/html`
should only be translated into `text/plain`
if the resulting text is different from the text created by the HTML-to-text conversion process defined in `g7:MIME`.

#### `TRAN` (Translation) `g7:FILE-TRAN`

A type of `TRAN` for external media files.
Each `g7:NOTE-TRAN` must have a `FORM` substructure.
See also `FILE` and the [File Path datatype](#file-path).

:::example
If an mp3 audio file
has been transcoded as an ogg file
and a timestamped transcript has been extracted as a WebVTT file,
the resulting set of files might be presented as follows:

```gedcom
0 @EX@ OBJE
1 FILE media/original.mp3
2 FORM audio/mp3
2 TRAN media/derived.oga
3 FORM audio/ogg
2 TRAN media/transcript.vtt
3 FORM text/vtt
```
:::

Note that `FILE`.`TRAN` refers to translation to a different digital format,
not to translation to a different human language.
Files that differ in the human language of their content
should each be given their own `FILE` structure.


#### `TRLR` (Trailer) `g7:TRLR`

A pseudo-structure marking the end of a dataset.
See [The Header and Trailer](#the-header) for more details.

#### `TYPE` (Type) `g7:TYPE`

A descriptive word or phrase used to further classify the superstructure.

When both a `NOTE` and free-text `TYPE` are permitted as substructures of the same structure,
the displaying systems should always display the `TYPE` value
when they display the data from the associated structure;
`NOTE` will typically be visible only in a detailed view.

`TYPE` must be used whenever the generic `EVEN`, `FACT` and `IDNO` tags are used.
It may also be used for any other event or attribute.

Using the subordinate `TYPE` classification method provides a further classification of the superstructure but does not change its basic meaning.

:::example
A `ORDN` with a `TYPE` could clarify what kind of ordination was performed:

```gedcom
0 @I1@ INDI
1 ORDN
2 TYPE Bishop
```

This classifies the entry as an ordination as a bishop, which is still a ordination event. The event could be further clarified with `RELI`, `DATE`, and other substructures.

Other descriptor values might include, for example,

- "Stillborn" as a qualifier to `BIRT` (birth)
- "Civil" as a qualifier to `MARR` (marriage)
- "College" as a qualifier to `GRAD` (graduation)
- "Oral" as a qualifier to `WILL`

See also `FACT` and `EVEN` for additional examples.
:::

#### `TYPE` (Type) `g7:NAME-TYPE`

An enumerated value from set `g7:enumset-NAME-TYPE` indicating the type of the name.

#### `TYPE` (Type) `g7:EXID-TYPE`

The authority issuing the `EXID`, represented as a URI.
It is recommended that this be a URL.

If the authority maintains stable URLs for each identifier it issues,
it is recommended that the `TYPE` payload be selected such that appending the `EXID` payload to it yields that URL.
However, this is not required and a different URI for the set of issued identifiers may be used instead.

Registered URIs are listed in the [exid-types registry](https://github.com/FamilySearch/GEDCOM-registries/tree/main/uri/exid-types), where fields are defined using the [YAML file format](https://gedcom.io/terms/format).

Additional type URIs can be registered by filing a
[GitHub pull request](https://github.com/FamilySearch/GEDCOM-registries/pulls).

#### `UID` (Unique Identifier) `g7:UID`

A globally-unique identifier of the superstructure,
to be preserved across edits.
If a globally-unique identifier for the record already exists, it should be used without modification, not even whitespace or letter case normalization.
It is recommended that new globally unique identifiers be created and formatted using the UUID
production specified in [RFC 9562](https://www.rfc-editor.org/info/rfc9562) Section 4.

This is metadata about the structure itself, not data about its subject.
Multiple structures describing different aspects of the same subject would have different `UID` values.

Because the `UID` identifies a structure, it can facilitate inter-tool collaboration
by distinguishing between a structure being edited and a new structure being created.
If an application allows structures to be edited in a way that completely changes their meaning
(e.g., changing all the contents of an `INDI` record to have it describe a completely different person)
then any `UID`s should also be changed.

:::note
Some systems used a 16-byte UUID with a custom 2-byte checksum for a total of 18 bytes:

- checksum byte 1 =
  (sum of (byte~*i*~) for *i* 1 through 16) mod 256
- checksum byte 2 =
  (sum of ((16 − *i*) × (byte~*i*~)) for *i* 1 through 16) mod 256

Use of checksums for UIDs is discouraged except in cases where error-prone input is expected and an appropriate action to take in case of an error is known.
:::

#### `VERS` (Version) `g7:VERS`

An identifier that represents the version level assigned to the associated product.
It is defined and changed by the creators of the product.

#### `VERS` (Version) `g7:GEDC-VERS`

The version number of the official specification that this document's data conforms to.
This must include the major and minor version (for example, "`7.0`");
it may include the patch as well (for example, "`7.0.1`"), but doing so is not required.
See [A Guide to Version Numbers] for more details about version numbers.

#### `WIDTH` (Width in pixels) `g7:WIDTH`

How many pixels to display horizontally for the image.
See `CROP` for more details.

#### `WIFE` (Wife) `g7:WIFE`

A structure for storing information related to one partner in the context of a `FAMILY_EVENT`;
in particular,
the partner referenced in the `g7:FAM-WIFE` substructure
of the `g7:record-FAM` superstructure of the `FAMILY_EVENT`.

:::example
The following indicates that individual `@I2@` was 32 years old at the time of the marriage, without indicating an age for individual `@I1@`.

```gedcom
0 @F1@ FAM
1 HUSB @I1@
1 WIFE @I2@
1 MARR
2 WIFE
3 AGE 32y
```
:::

#### `WIFE` (Wife) `g7:FAM-WIFE`

A partner in a `FAM` record.
See `FAMILY_RECORD` for more details.

#### `WILL` (Will) `g7:WILL`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `WWW` (Web address) `g7:WWW`

A URL or other locator for a World Wide Web page of the subject of the superstructure,
as defined by any relevant standard
such as [whatwg/url](https://url.spec.whatwg.org/),
[RFC 3986](https://www.rfc-editor.org/info/rfc3986),
[RFC 3987](https://www.rfc-editor.org/info/rfc3987),
and so forth.

Like other substructures, the `WWW` structure provides details about the subject of its superstructure.
For example, a `MARR`.`WWW` is a world wide web page of the marriage event,
not the personal website of the couple or an entry in an online database serving as a source documenting the marriage.
However, the meaning of `WWW` was only implicit when it was introduced in version 5.5.1
and many files were created that use `WWW` to store a more tangentially-related web address,
so applications are recommended to interpret the `WWW` structure's meaning cautiously.

If an invalid or no longer existing web address is present upon import, it should be preserved as-is on export.

