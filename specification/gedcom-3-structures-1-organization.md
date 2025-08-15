# Genealogical structures {#gedcom-structures}

This chapter describes a set of structure types for exchanging family-based lineage-linked genealogical information.
Lineage-linked data pertains to individuals linked in family relationships across multiple generations.

The genealogical structures defined in this chapter are based on the general framework of the container format and data types defined in Chapters 1 and 2.

Historically, these genealogical structures were used as the only form approved for exchanging data with Ancestral File, TempleReady and other Family History resource files.
Those systems were all replaced between 1999 and 2019, and [GEDCOM-X](https://gedcomx.org) was introduced as the new syntax for communication with their replacements.
FamilySearch GEDCOM 7.0 and GEDCOM-X have similar expressive power,
but as of 2021 GEDCOM is more common for exchanging single-researcher files between applications
and GEDCOM-X is more common for transferring bulk data and communication directly between applications.

The basic description of the genealogical structures' organization is presented in the following 3 major sections:

* "[Structure Organization]" describes records and other nested structures.
* "[Structure Meaning]" provides a definition of each structure by its tag.
* "[Enumeration Values]"  provides a definition of each enumeration value by its containing structure.

## A Metasyntax for Structure Organization

The structures, with their payloads and substructures,
are represented using a custom metasyntax.
The intent of this metasyntax is to resemble the line encoding of allowable structures. In the metasyntax:

- Options are placed between brackets `[` and `]` and have choices separated by pipes `|`.
- Named sets of rules are indicated with a name followed by `:=`.
- Level markers are used to indicate substructure relationships.
    - `0` means "must be a record".
    - `n` means "level inherited from rule instantiation".
    - `+1`, `+2`, etc., indicate nesting within nearest preceding structure with lesser level.
- Four cardinality markers are used: `{0:1}`, `{1:1}`, `{0:M}`, and `{1:M}`.
    - `{0:` means "optional" -- the structure may be omitted
    - `{1:` means "required" -- at least 1 must appear
    - `:M}` means "any number" -- 1 or more structures may appear.
        Unless otherwise specified, the first is the most-preferred value.
        If an application needs to display just 1 of several `NAME`s, `BIRT`s, etc, they should show the first such structure unless more specific selection criteria are available.
    - `:1}` means "singular" -- at most 1 may appear; a second must not be present.
    
    Systems interested in violating the cardinality rules should instead create [extension structures](#extensions) with different cardinality.
- Rule instantiation is indicated by the rule name in double angle-brackets (such as `<<`rule name`>>`) and a cardinality marker.
    
    The cardinality markers of rule instantiations and their referenced line templates are combined such that the resulting cardinality
    is required only if both combined cardinalities are required
    and singular only if both combined cardinalities are singular.
    
    <div class="example">
    The definition of the `FAM` record has the line

    ````gedstruct
      +1 <<CREATION_DATE>>                     {0:1}
    ````
    
    and the `CREATION_DATE` rule begins

    ````gedstruct
    n CREA                                     {1:1}  g7:CREA
    ````
    
    Thus, a `FAM` record has an optional singular `CREA` substructure
    (such as cardinality `{0:1}`).
    </div>
    
- Line templates have several parts:
    - An optional cross-reference template `@XREF:`tag`@`, meaning this structure may be pointed to by other structures.
        
        Structures that are not pointed to by other structures need not have a [cross-reference identifier](#lines) even if their line template has a cross-reference template.
    - The standard tag for this structure.
    - An optional payload descriptor; if present this is 1 of the following:
        
        - `@<XREF:`tag`>@` means a pointer to a structure with this cross-reference template; `@VOID@` is also permitted.
        - `<`data type`>` means a non-pointer payload, as described in [Data types](#datatypes). If the data type allows the empty string, the payload may be omitted.
        - `[`text`|<NULL>]` means the payload is optional but if present must be the given text.
        
        If there is a payload descriptor, a payload that matches the payload is required of the described structure unless the descriptor says the payload is optional.

        If there is no payload descriptor, the described structure must not have a payload.
        
    - A cardinality marker.
    - The URI of this structure type.
        
        Pseudo-structures do not have a URI.

- Within the metasyntax, the order in which substructures are presented within a structure and the order in which choices are presented within an option set are not significant unless otherwise specified in the text next to the metasyntax block.

The context of a structure's superstructure may be necessary in addition to the structure's standard tag to fully determine its structure type.
To refer to a structure in the context of its superstructure,
tags are written with intervening periods.
For example, `GEDC`.`VERS` refers to a structure with tag `VERS`
and a superstructure with tag `GEDC`.


## Structure Organization

### Document

#### Dataset := {-}

```gedstruct
0 <<HEADER>>                               {1:1}
0 <<RECORD>>                               {0:M}
0 TRLR                                     {1:1}  g7:TRLR
```

The order of these is significant:
the `HEADER` must come first and `TRLR` must be last,
with any `RECORD`s in between.

#### `RECORD` :=

```gedstruct
[
n <<ASSET_RECORD>>                         {1:1}
|
n <<FAMILY_RECORD>>                        {1:1}
|
n <<GROUP_RECORD>>                         {1:1}
|
n <<INDIVIDUAL_RECORD>>                    {1:1}
|
n <<MULTIMEDIA_RECORD>>                    {1:1}
|
n <<PROOF_RECORD>>                         {1:1}
|
n <<REPOSITORY_RECORD>>                    {1:1}
|
n <<SHARED_NOTE_RECORD>>                   {1:1}
|
n <<SOURCE_RECORD>>                        {1:1}
|
n <<STICKY_RECORD>>                        {1:1}
|
n <<SUBMITTER_RECORD>>                     {1:1}
|
n <<TEMPLATE_RECORD>>                      {1:1}
]
```

***
$\color{Coral}\large{\textbf{Gedcom 8:}}$

>- **This Draft-PR is written to allow the new structures to go *alongside* GEDCOM 7.X, and because of that in this GEDCOM 8 specification, lines are added in GEDCOM 7 parts, to be able to allow that.**
>- **If the GEDCOM group would decide to add this PR, but make it a new start, without old GEDCOM 7.x constructions inside it, a few parts of this draft have to be changed to remove some of the old structures and records of current GEDCOM 7.x.**
***

#### `HEADER` :=

```gedstruct
n HEAD                                     {1:1}  g7:HEAD
  +1 GEDC                                  {1:1}  g7:GEDC
     +2 VERS <Special>                     {1:1}  g7:GEDC-VERS
  +1 SCHMA                                 {0:1}  g7:SCHMA
     +2 TAG <Special>                      {0:M}  g7:TAG
  +1 SOUR <Special>                        {1:1}  g7:HEAD-SOUR
     +2 VERS <Special>                     {1:1}  g7:VERS
     +2 NAME <Text>                        {1:1}  g7:NAME
     +2 CORP <Text>                        {1:1}  g7:CORP
        +3 <<ADDRESS_STRUCTURE>>           {0:1}
        +3 PHON <Special>                  {0:M}  g7:PHON
        +3 EMAIL <Special>                 {1:M}  g7:EMAIL
        +3 FAX <Special>                   {0:M}  g7:FAX
        +3 WWW <Special>                   {1:M}  g7:WWW
     +2 DATA <Text>                        {0:1}  g7:HEAD-SOUR-DATA
        +3 DATE <DateExact>                {0:1}  g7:DATE-exact
           +4 TIME <Time>                  {0:1}  g7:TIME
        +3 COPR <Text>                     {0:1}  g7:COPR
  +1 DEST <Special>                        {0:1}  g7:DEST
  +1 DATE <DateExact>                      {1:1}  g7:HEAD-DATE
     +2 TIME <Time>                        {1:1}  g7:TIME
  +1 SUBM @<XREF:SUBM>@                    {1:1}  g7:SUBM
  +1 COPR <Text>                           {0:1}  g7:COPR
  +1 LANG <Language>                       {0:1}  g7:HEAD-LANG
  +1 PLAC                                  {0:1}  g7:HEAD-PLAC
     +2 FORM <List:Text>                   {1:1}  g7:HEAD-PLAC-FORM
  +1 <<NOTE_STRUCTURE>>                    {1:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

The header pseudo-structure provides metadata about the entire dataset.
A few substructures of note:

- `GEDC` identifies the specification that this document conforms to.
    It is recommended that `GEDC` be the first substructure of the header.
- `SCHMA` gives the meaning of extension tags; see [Extensions](#extensions) for more details.
- `SOUR` describes the originating software.
    - `CORP` describes the corporation creating the software.
    - `HEAD`.`SOUR`.`DATA` describes a larger database this data is extracted from.
- `LANG` and `PLAC` give a default value for the rest of the document.

$\color{Coral}\large{\textbf{Gedcom 8 changes:}}$

>**Some cardinality markers are changed:**
>- `SOUR`, the program used to create this GEDCOM, should at a minimum give certain information, so users and other software can track the origin of a specific GEDCOM.
>- `VERS`, `NAME`, `CORP`, `EMAIL` and `WWW`, are the minimal info about the software this GEDCOM was created by, that should be present in a header.
>- `NOTE`: As more programs now allow users to have some kind of "general info notes" for a specific GEDCOM, the cardinality of `NOTE_STRUCTURE` is changed to {1:M}. That way users can add general information about how they're working or what they need to look at later, and much more, into the header. Now if a header is a bit "out of space" with a lot of added notes, we could also say that the header is only allowed to have 1  maybe 2 inline `NOTE`s and the rest should be links to `SNOTES`.  
By allowing more `NOTE`s, we also give software the ability to describe when a conversion was performed, and from which GEDCOM version to which new version, it can mention the original filename if that was changed by the conversion, and other things.
>- `DATE` and `TIME`, The datetime this GEDCOM file was created, is now also mandatory.
>- `SUBM`, Submitter is now also mandatory.
>- `CREA` and `CHAN`, added these too, as the header was the only record that did not have these. Because a conversion form 1 GEDCOM version to another, also changes info in the header. (replacing the name of the software for instance)  

>**Further for GEDCOM 8:**
>- All records that have a `<<CHANGE_DATE>>` and a `<<CREATION_DATE>>`, now have the cardinality markers for those set to **{1:1}**.
>- As now the `TEMPLATE` is the only place a `SOURCE_CITATION` is used (by the `CITA` structure), at all other places the `SOURCE_CITATION` was used, some lines have been added (`GEDC` and `VERS` from the header) to try to make sure it cannot be used in GEDCOM 8.  
That way evidence exists on **1 (ONE)** place only: **Inside the `TEMPLATE`**


### Records

#### `ASSET_RECORD` :=

An `ASSET` represents a **physical, living, symbolic, financial, or digital entity** that exists independently but interacts with individuals, groups, and events in genealogical records.

Examples include **heirlooms, land parcels, animals, tools, artworks, digital objects, and persistent conditions such as hereditary diseases**. `ASSET`'s serve as reusable entities that acquire meaning through participation in `TEMPLATE` events via linked `STICKY` records.

```gedstruct
n @XREF:ASSET@ ASSET                       {1:1}  g8:record-ASSET
  +1 TYPE <Enum>                           {1:1}  g8:ENTITY-TYPE
    +2 SUBTYPE                             {1:1}  g8:ENTITY-SUBTYPE
    +2 PHRASE <Text>                       {0:1}  g8:PHRASE
  +1 TITL <Text>                           {0:1}  g8:TITL
    +2 PHRASE <Text>                       {0:1}  g8:PHRASE
  +1 TORIGIN <Enum>                        {1:1}  g8:TORIGIN
  +1 QUAY <Enum>                           {0:1}  g7:QUAY
  +1 SUBM @<XREF:SUBM>@                    {1:M}  g8:SUBM
    +2 <<NOTE_STRUCTURE>>                  {0:M}
  +1 NAME <<NAME_STRUCTURE>>               {0:1}  g8:INDI-NAME 
  +1 DATE <DateValue>                      {1:1}  g8:DATE-value
  +1 <<ADDRPLUS_STRUCTURE>>                {0:1}  g8:ADDRPLUS
  +1 <<SHARED_PLACE_STRUCTURE>>            {0:1}  g8:SPLAC
  +1 SUBM @<XREF:SUBM>@                    {1:M}  g8:SUBM
    +2 <<NOTE_STRUCTURE>>                  {0:M}
  +1 HISTORY                               {1:1}
    +2 STICKY @<XREF:STICKY>@              {1:M}  g8:STICKY
      +3 RESN <List:Enum>                  {0:1}  g8:RESN
      +3 SUBM @<XREF:SUBM>@                {1:M}  g7:SUBM
        +4 PHRASE <Text>                   {0:1}  g7:PHRASE
      +3 PROOF @<XREF:PROOF>@              {0:M}  g8:PROOF
        +4 OUTCOME <Enum>                  {1:1}  g8:OUTCOME
  +1 RESN <List:Enum>                      {0:1}  g8:RESN
  +1 <<FLEX_STRUCTURE>>                    {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

**💬 Field Notes:**
- The `TYPE` value must be chosen from the enumset `g8:enumset-ENTITY-TYPE`.
  - ⚠️ Do not use `PERSON` as an ASSET type. People are always represented via `@INDI@` records and linked there using `STICKY`s.
  -  For `PROOF` and `OUTCOME`, see the explanation with the `PROOF`-record.
  - All other `ENTITY` types (e.g., `CREATURES`, `PROPERTY`, `JEWELRY`) are valid.
- `TYPE`, `SUBTYPE`, and `PHRASE`, are defined the same as for `STICKY`. They go together on 1 line.

:::example
  - For a horse: 
  ```gedcom
  1 TYPE CREATURES, HORSE, "Breeder: Meadow Stud, Christopher Chenery"
  ```
  So `TYPE`, `SUBTYPE` and `PHRASE` are on 1 line.
:::
  
- `TITLE` and `NAME`: These are used to "name/describe" the `ASSET`. In case of an animal the `NAME` can be used, in case of for instance a painting, the `TITLE` can be used. `NAME` follows the new GEDCOM8 `NAME`format.<br>**At least 1 of the 2 must be present!**  
:::example
  - For a horse: Secretariat  (Meadow Stud, Virginia, USA, owned by Penny Chenery).
  ```gedcom
  1 NAME
  2 TYPE BIRTH 
  2 FORM Secretariat
  2 PART Secretariat
  3 TYPE GIVN
  1 NAME
  2 FORM Big Red
  2 PART Big Red
  3 TYPE NICK
  ```
  - For a painting: `TITLE "Oil painting of Castle King Windemere"`
:::

- `TORIGIN`, Defines how an `ASSET` was originally entered, generated or reconstructed. This helps distinguish freshly structured entries from those generated or inferred from legacy data. It clarifies the **origin and trust context** of each entry — whether manually entered, system-generated, or reverse-engineered — supporting gradual adoption of the new model and better transparency in data lineage.

- `QUAY`, defines the quality of this whole `ASSET`. Together with `TORIGON`.

- `DATE` A date associated with the asset's "founding", or first documentation.
- `SUBM`and `NOTE_STRUCTURE` same as for STICKY.
- `ADDRPLUS_STRUCTURE`: Can be used for the address and other addressing information that might be present for this `ASSET`.
- `<<SHARED_PLACE_STRUCTURE>>`: if the `ASSET` is a real property (so a non-movable object), like land or a building, it can have an `SPLAC` describing that place. 
- `HISTORY`: in this section a list of `STICKY`'s is mentioned that were present, or have a `ROLE`, in a `TEMPLATE`. The `HISTORY` section can have many `STICKY`s, coming from many `TEMPLATE`s.
- `STICKY`s should be sorted chronologically by their internal `DATE`.
- `RESN` This is meant to have a restriction on just this 1 `STICKY` when needed, or on this whole `ASSET`.
- `FLEX_STRUCTURE`, this is used for information in the `ASSET` that has no GEDCOM tag, and that should be saved, and later represented, to a user. For instance:
  - Condition of the `ASSET` (“Mint,” “Restored,” “Damaged in 1942”)
  - Other possibilities: Inscription or mark, or restoration details, cultural symbolic use (“Used in family weddings,” “Sacred object,” “Tribal spear”).

- All other structures are defined the same as for GEDCOM7.

:::example:   
**Land inherited from a Will Template**
```gedcom
0 @A0002@ ASSET
1 TYPE LAND, FIELD
1 TITL "Hilltop Pasture"
1 TORIGIN ORIGDOC
1 QUAY 3
1 SUBM @B001@
1 DATE Mar 10 1871            /* First known presence in documents of this Field */
1 SPLAC @SP0021@              /* Norfolk, England: location of the field */
1 HISTORY
2 STICKY @ST1022@             /* Mar 10 1871: Owned by Edward Hamilton */
2 STICKY @ST1123@             /* Jul 12 1882: Recieved by George Hamilton, as HEIR of Edward */
1 NOTE "The field includes a riverbank."
1 OBJ @O003@                  /* Map of the field */
1 CREA 2025-05-01
1 CHAN 2025-07-04
```
:::

#### `FAMILY_RECORD` :=

```gedstruct
n @XREF:FAM@ FAM                           {1:1}  g7:record-FAM
  +1 RESN <List:Enum>                      {0:1}  g7:RESN
  +1 <<FAMILY_ATTRIBUTE_STRUCTURE>>        {0:M}
  +1 <<FAMILY_EVENT_STRUCTURE>>            {0:M}
  +1 <<NON_EVENT_STRUCTURE>>               {0:M}
  +1 HUSB @<XREF:INDI>@                    {0:1}  g7:FAM-HUSB
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 WIFE @<XREF:INDI>@                    {0:1}  g7:FAM-WIFE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 CHIL @<XREF:INDI>@                    {0:M}  g7:CHIL
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<ASSOCIATION_STRUCTURE>>             {0:M}
  +1 SUBM @<XREF:SUBM>@                    {0:M}  g7:SUBM
  +1 <<LDS_SPOUSE_SEALING>>                {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {1:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The `FAM` record was originally structured to represent families where a male `HUSB` (husband or father) and female `WIFE` (wife or mother) produce `CHIL` (children).
The `FAM` record may also be used for cultural parallels to this,
including nuclear families, marriage, cohabitation, fostering, adoption, and so on, regardless of the gender of the partners.
Sex, gender, titles, and roles of partners should not be inferred based on the partner that the `HUSB` or `WIFE` structure points to.

$\color{Coral}\large{\textbf{Gedcom 8 changes:}}$

>- In GEDCOM 8 the `FAM` record is no longer used. As the `TEMPLATE` now represents a kind of "mini" tree, describing the relations between all persons and objects inside it.  
>- Software is free to use an internal FAM construction, but in a GEDCOM 8 file itself, it is no longer needed or supported.  


The individuals pointed to by the `HUSB` and `WIFE` are collectively referred to as "partners", "parents" or "spouses".

Some displays may be unable to display more than 2 partners.
Displays may use `HUSB` and `WIFE` as layout hints,
for example, by consistently displaying the `HUSB` on the same side of the `WIFE` in a tree view.
Family structures with more than 2 partners
may either use several `FAM` records
or use `ASSOCIATION_STRUCTURE`s to indicate additional partners.

:::note
The `FAM` record will be revised in a future version to more fully express the diversity of human family relationships.
:::

The order of the `CHIL` (children) pointers within a `FAM` (family) structure should be chronological by birth;
this is an exception to the usual "most preferred value first" rule.
A `CHIL` with a `voidPtr` indicates a placeholder for an unknown child in this birth order.

If a `FAM` record uses `HUSB` or `WIFE` to point to an `INDI` record,
the `INDI` record must use `FAMS` to point to the `FAM` record.
If a `FAM` record uses `CHIL` to point to an `INDI` record,
the `INDI` record must use a `FAMC` to point to the `FAM` record.

An `INDI` record should not have multiple `FAMS` substructures pointing to the same `FAM`.

A `FAM` record should not have multiple `CHIL` substructures pointing to the same `INDI`; doing so implies a nonsensical birth order.
An `INDI` record may have multiple `FAMC` substructures pointing to the same `FAM`, but doing so is not recommended.

#### `GROUP_RECORD` :=

This structure allows GEDCOM 8 to model social affiliations that span beyond family ties and record the source of such affiliations with precision.

```gedstruct
n @XREF:GROUP@ GROUP                       {1:1}  g8:record-GROUP
  +1 TYPE <Enum>                           {1:1}  g8:GROUP-TYPE
    +2 PHRASE <Text>                       {0:1}  g8:PHRASE
  +1 RESN <List:Enum>                      {0:1}  g8:RESN
  +1 TITL <Text>                           {0:1}  g8:TITL
    +2 PHRASE <Text>                       {0:1}  g8:PHRASE
  +1 TORIGIN <Enum>                        {1:1}  g8:TORIGIN
  +1 QUAY <Enum>                           {0:1}  g7:QUAY
  +1 SUBM @<XREF:SUBM>@                    {1:M}  g8:SUBM
    +2 <<NOTE_STRUCTURE>>                  {0:M}
  +1 NAME <<PERSONAL_NAME_STRUCTURE>>      {0:M}  g8:INDI-NAME
  +1 <<ADDRPLUS_STRUCTURE>>                {0:1}  g8:ADDRPLUS
  +1 <<SHARED_PLACE_STRUCTURE>>            {0:1}  g8:SPLAC
  +1 DATE <DateValue>                      {1:1}  g8:DATE-value
  +1 <<FLEX_STRUCTURE>>                    {0:M}
  +1 MEMBERS                               {1:1}
    +2 STICKY @<XREF:STICKY>@              {1:M}  g8:STICKY
      +3 SUBM @<XREF:SUBM>@                {1:1}  g7:SUBM
        +4 PHRASE <Text>                   {0:1}  g7:PHRASE
      +3 RESN <List:Enum>                  {0:1}  g8:RESN
      +3 PROOF @<XREF:PROOF>@              {0:M}  g8:PROOF
        +4 OUTCOME <Enum>                  {1:1}  g8:OUTCOME
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

- `GROUP` Defines a named social, cultural, or ancestral unit, such as a clan, caste, guild, farm, religious order, a sports team etc.
- `TYPE` The category of the group being represented. Must be chosen from `g8:enumset-GROUP-TYPE`.
- `PHRASE` A human-readable description of the group, only required when `TYPE` is `OTHER`, but allowed in all other cases. `PHRASE` must go on the same line as `TYPE`, separated from it by ", ".
- `RESN` Optional restriction notice for access or visibility (e.g., privacy settings).
- `TITL` A short title or label for the group, such as "The Blacksmiths' Guild".

- `TORIGIN`, Defines how an `GROUP` was originally entered, generated or reconstructed. This helps distinguish freshly structured entries from those generated or inferred from legacy data. It clarifies the **origin and trust context** of each entry — whether manually entered, system-generated, or reverse-engineered — supporting gradual adoption of the new model and better transparency in data lineage.

- `QUAY`, defines the quality of this whole `GROUP`. Together with `TORIGIN`.

- `NAME` One or more names used to refer to this group; e.g., "Clan MacGregor", including name parts. It follows the new GEDCOM8 `NAME` format. With this its possible to trace lastnames coming from a `GROUP`.
>**At least 1 of `NAME` and `TITL` must be present**.
- `ADDRPLUS_STRUCTURE`: Can be used for the address and other addressing information that might be present for this `GROUP`.
  - In case of a `CLAN`or `TRIBE` etc. it might only be a WWW adress where info about this `GROUP` can be found.
- `SHARED_PLACE_STRUCTURE` The group's place of origin, base, or primary region of activity. It follows the new GEDCOM8 `SPLAC` format.
- `DATE` A date associated with the group's founding, first documentation, or formal recognition. (Can also be a Date period)
- `FLEX_STRUCTURE`, this is used for information in the `GROUP` that has no GEDCOM tag, and that should be saved, and later represented, to a user. For instance:
  - Motto or slogan: “Semper Fidelis,” “Strength in Unity”
  - Origin story: Brief legend or founding tale
  - Symbol or crest: Heraldry, emblems, tribal markings
  - Legal registration: Chamber of commerce or civil registration info

- `SUBM` At least one submitter who contributed information about this group. The default `SUBM` is the same as the `SUBM` from the `HEAD`.
- `MEMBERS` A container for listing individual membership events in the group. `STICKY`s are sorted on `NAME` first and on `DATE` second.
-  For `PROOF` and `OUTCOME`, see the explanation with the `PROOF`-record.
- `STICKY` References to STICKY records that reflect an individual’s connection to the group. These `STICKY`s should include the `ROLE`/Event of the person within the group, such as `MEMBER` or `LEADER` or `JOINED`. <br>If a `GROUP` has for instance 3 members and each member has 3 `STICKY`s inside the `MEMBERS` tag, the `STICKY`s will be grouped by member name first, and by `DATE` from inside the `STICKY` second. So like this: Ben, 1864, 1870, 1877, John, 1645, 1646, 1675, William, 1860, 1870, 1899, Peter, 1630.
- `RESN` This is meant to have a restriction on just this 1 `STICKY` when needed.
- `QUAY` This is to be able to qualify the connection of this `STICKY` on this specific place.
- `IDENTIFIER_STRUCTURE` External or internal identifiers for this group, such as catalog or archive numbers.
- `NOTE_STRUCTURE` Additional notes about the group.
- `MULTIMEDIA_LINK` Links to images or other media associated with the group.
- `CHANGE_DATE` The date this group record was last modified.
- `CREATION_DATE` The date this group record was originally created.

#### Example: Clan Membership

This example illustrates the use of a `GROUP` record to represent a clan, and a corresponding `STICKY` record to indicate a person's membership in that clan at a specific point in time.

- The `GROUP` record uses `TYPE CLAN` and includes a structured `NAME`, an `SPLAC` for geographical association, a `DATE` for historical context, and a `TITL` to clarify the group's nature. `TITL` is the official `GROUP`s "name".
- The `INDI` record defines John Mackay with a properly structured `NAME`.
- The `STICKY` record links the individual and the group, marking John as a `CLAN MEMBER` in the year 1820.
- A `TEMPLATE` reference is included to indicate the source document where this membership was recorded (e.g., "1820 court rolls").
- The `NOTE` in the `STICKY` provides additional human-readable context.

A `STICKY` that connects an `INDI` to a `GROUP` represents a known relationship at a specific point in time, not necessarily the full duration of membership.


The following shows:
- John Mackay is a member of the Mackay clan.
- The clan itself is linked to as `GROUP` in the `STICKY`.
- The relationship is time-stamped and contextualized using `STICKY`.

You may also define roles like `CHIEFTAIN`, `ELDER`, `SPOKESPERSON`, or others using `ROLE` or `SUBTYPE` if culturally relevant.


```gedcom
0 @G0007@ GROUP /* Clan Mackay */
1 TYPE CLAN
1 TITL Scottish Highland Clan
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 NAME
2 FORM Clan Mackay
2 PART Mackay
3 TYPE GROUP
2 PART Clan
3 TYPE OTHER, Clan
1 SPLAC @SP037@               /* Sutherland, Scotland *
1 DATE 1600
1 MEMBERS
2 STICKY @ST0008@             /* John Mackay, 1820 */
~ ~ ~

0 @I0003@ INDI                /* John Mackay */
1 NAME
2 FORM John Mackay
2 PART John
3 TYPE GIVN
2 PART Mackay
3 TYPE SURN
1 ROLES
2 STICKY @ST0008@             /* John Mackay mentioned as a clan member */
~ ~ ~

0 @ST0008@ STICKY             /* Clan member John Mackay */
1 TYPE PERSON
1 TITL Clan member John Mackay
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 TEMPLATE @T0123@            /* 1820 court rolls define John as member */
1 GROUP @G0007@               /* Associated group for John */
1 ROLE MEMBER
1 NAME
2 FORM John Mackay
2 PART John
3 TYPE GIVN
2 PART Mackay
3 TYPE SURN
1 DATE 1820
1 SEX M
1 SPLAC @SP066@               /* Melvich, Scotland */
1 OCCU Crofter and Piper
1 NOTE "John Mackay identified as a clan member in 1820 court rolls."
~ ~ ~
```
#### Tip: Best Practice: Defining Group Membership Periods
- If no date is provided, the STICKY is treated as undated — indicating only that the relationship existed at some unspecified time.

To express **entry** or **exit** dates, or just **membership** more precisely, use one of the following:

- Use a `DATE RANGE` for a known membership:
```gedcom
1 STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 TEMPLATE @T0123@            /* 1820 court rolls */
1 GROUP @G123@                /* Associated group for John */
1 Name
1 FORM John Mackay            /* this is meant to be the full GEDCOM 8 NAME structure */
1 ROLE MEMBER
1 DATE FROM 1810 TO 1830      /* Membership over some years, no specific entry and exit date */
~ ~ ~
```
- Use separate STICKYs for joining and leaving:

```gedcom
1 STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 TEMPLATE @T0456@            /* 1810 guild admission register */
1 GROUP @G0007@               /* Associated group for John */
1 Name
1 FORM John Mackay            /* this is meant to be the full GEDCOM 8 NAME structure */
1 ROLE JOINED                 /* ROLE JOINED means John entered the Clan */
1 DATE 1810
~ ~ ~

1 STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 TEMPLATE @T0111@            /* 1830 community council minutes */
1 GROUP @G0098@               /* Associated group for John */
1 Name
2 FORM John Mackay
2 PART John
3 TYPE GIVN
2 PART Mackay
3 TYPE LOCATION
1 ROLE LEFT                   /* ROLE LEFT means John exited the Clan */
1 DATE 1830
~ ~ ~
```

If the exact role is known (e.g., `INITIATED`, `EXPELLED`, `HONOREE`), define this in the ROLE field and include a `DATE`.

If no date is provided, the `STICKY` is treated as undated — indicating only that the relationship existed at some unspecified time.

:::

#### Example: Norwegian Farm Name Group
:::example
```gedcom
0 @G0024@ GROUP
1 TYPE FARM                   /* groups all farm members of this farm over time */
1 TITL Lien Farm Group
1 PHRASE Historic residence unit in Valdres, Norway
1 SUBM @B001@
1 NAME
2 FORM Lien
2 PART Lien
3 TYPE LOCATION
1 NOTE Residents of this farm traditionally adopted 'Lien' as a surname.
1 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 DATE 1700
1 MEMBERS
2 STICKY @ST0091@             /* Ola Lien */
~ ~ ~

0 @ST0091@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0073@
1 GROUP @G0024@               /* Lien Farm, Valdres, Norway */
1 DATE 01 JAN 1832
1 ROLE MAIN, LEADER, RESIDENT
1 AGE 39
1 OCCU Farmer
1 NOTE Head of household residing at Lien Farm.
1 NOTE Ola Lien appears in farm census of 1832.
~ ~ ~
```
:::


#### `INDIVIDUAL_RECORD` :=

```gedstruct
n @XREF:INDI@ INDI                         {1:1}  g7:record-INDI
  +1 RESN <List:Enum>                      {0:1}  g7:RESN
  +1 <<PERSONAL_NAME_STRUCTURE>>           {0:M}
  +1 SEX <Enum>                            {0:1}  g7:SEX
  +1 <<INDIVIDUAL_ATTRIBUTE_STRUCTURE>>    {0:M}
  +1 <<INDIVIDUAL_EVENT_STRUCTURE>>        {0:M}
  +1 <<NON_EVENT_STRUCTURE>>               {0:M}
  +1 <<LDS_INDIVIDUAL_ORDINANCE>>          {0:M}
  +1 FAMC @<XREF:FAM>@                     {0:M}  g7:INDI-FAMC
     +2 PEDI <Enum>                        {0:1}  g7:PEDI
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
     +2 STAT <Enum>                        {0:1}  g7:FAMC-STAT
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
     +2 <<NOTE_STRUCTURE>>                 {0:M}
  +1 FAMS @<XREF:FAM>@                     {0:M}  g7:FAMS
     +2 <<NOTE_STRUCTURE>>                 {0:M}
  +1 ROLES                                 {0:1}
    +2 STICKY @<XREF:STICKY>@              {1:M}  g8:STICKY
      +3 RESN <List:Enum>                  {0:1}  g8:RESN
      +3 SUBM @<XREF:SUBM>@                {1:M}  g7:SUBM
        +4 PHRASE <Text>                   {0:1}  g7:PHRASE
      +3 PROOF @<XREF:PROOF>@              {0:M}  g8:PROOF
        +4 OUTCOME <Enum>                  {1:1}  g8:OUTCOME
  +1 ASSETS                                {0:1}
    +2 STICKY @<XREF:STICKY>@              {1:M}  g8:STICKY
      +3 RESN <List:Enum>                  {0:1}  g8:RESN
      +3 SUBM @<XREF:SUBM>@                {1:M}  g7:SUBM
        +4 PHRASE <Text>                   {0:1}  g7:PHRASE
      +3 PROOF @<XREF:PROOF>@              {0:M}  g8:PROOF
        +4 OUTCOME <Enum>                  {1:1}  g8:OUTCOME
  +1 SUBM @<XREF:SUBM>@                    {0:M}  g7:SUBM
  +1 ALIA @<XREF:INDI>@                    {0:M}  g7:ALIA
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 ANCI @<XREF:SUBM>@                    {0:M}  g7:ANCI
  +1 DESI @<XREF:SUBM>@                    {0:M}  g7:DESI
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 GEDC                                  {0:1}  g8:GEDC
    +2 VERS <Special>                      {1:1}  g8:GEDC-VERS
      +3 <<SOURCE_CITATION>>               {1:M}
      +3 <<ASSOCIATION_STRUCTURE>>         {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

The individual record is a compilation of facts or hypothesized facts about an individual.
These facts may come from multiple sources.
Source citations and notes allow documentation of the source where each of the facts were discovered.

$\color{Coral}\large{\textbf{GEDCOM 8 changes (to make it go alongside GEDCOM 7):}}$

>- `SOURCE_CITATION` and `<<ASSOCIATION_STRUCTURE>>` are now *behind* the same GEDCOM version tag as in the Header.  
> Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` or `<<ASSOCIATION_STRUCTURE>>` are allowed at this place.   
> This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and all associations of everything that belongs to it. (inside the `STICKY`s)  
>- `FAMC` and `FAMS` no longer exist in GEDCOM 8 `INDI`s. As their role is taken over by the `TEMPLATE` itself.  
>- If an `INDI` has no `ROLES` or `ASSETS` section, it is understood as a GEDCOM 7 `INDI`, where `FAMC` and `FAMS` are possible inside the `INDI`.

$\color{Coral}\large{\textbf{NEW GEDCOM 8 part of INDI record}}$

>- `ROLES`, in this section a list of `STICKY`'s is mentioned that were present, or have a `ROLE`, in a `TEMPLATE`, and contain evidenced information belonging to this `INDI`. The `ROLES` section can have many `STICKY`s, coming from many `TEMPLATE`s.
>- `STICKY`, The `STICKY` record identifies 1 single person from a `TEMPLATE` record. It describes **all information of this 1 single person** as found in that `TEMPLATE`.
>- `SUBM`, the user who added this `STICKY` in the `ROLES` section.
>- `PHRASE`, short description explaining the reason this `STICKY` was added by this user.
>- `PROOF`, **Experimental Link** to the `PROOF` record, from which result this `STICKY` was added. More `PROOF` records are possible for each `STICKY` as those `PROOF` records may deal with different questions for one and the same `STICKY`.
>- `OUTCOME`, credibility of this information. (See the `PROOF` record itself.)
>- `ASSETS`, in this section a list of asset `STICKY`'s is mentioned, that are connected to this `INDI`, as described in the `TEMPLATE` this `STICKY` belongs to.


A single individual may have facts distributed across multiple individual records, connected by `ALIA` (alias, in the computing sense not the pseudonym sense) pointers.
See `ALIA` for more details.

Individual records are linked to Family records by use of bi-directional pointers.
Details about those links are stored as substructures of the pointers in the individual record.

Other associations or relationships are represented by the `ASSO` (association) tag.
The person's relation or associate is the person being pointed to.
The association or relationship is stated by the value on the subordinate `ROLE` line.

:::example
The following example refers to 2 individuals, `@I1@` and `@I2@`,
where `@I2@` is a godparent of `@I1@`:

```gedcom
0 @I1@ INDI
1 ASSO @I2@
2 ROLE GODP
```
:::
***
$\color{Coral}\large{\textbf{GEDCOM 8 "replacement" for `ASSO`}}$

>With GEDCOM 8 that would be:

>:::example

>The following example refers to 2 individuals, `@I004@` and `@I005@`, where `@I004@` is a godparent of `@I005@`:

```gedcom
0 @I004@ INDI
1 ROLES 
2 STICKY @ST0152@             /* GODPARENT role inside the STICKY */
```
>- The `ROLE` of  `I004` is **inside** the `STICKY` now, its the `ROLE` this `INDI (I004)` had, for the `MAIN` person `(I005)` mentioned in the `TEMPLATE` this `STICKY (ST0152)` belongs to. So that makes it absolutely clear who is who in this connection.  
>- Further: **ALL** events this `INDI` has been part of, are now also in the `ROLES` section, sorted on their `DATE`.
>- And more: Because parents have been "present" (dead or still alive) at the `BIRT` or from a `MARR` or `ADOP` event of their children, their `ROLE` in those events is also mentioned here. That means **all** children are now kind of present under 1 of their parents (Biological, godparent, or adopting parent). And a long outstanding wish of users, to be able to see **each and every child** of someone, can now be realised easily from this list.  

:::
***

Events stored as facts within an `INDI` record may also have `FAMC` or `ASSO` tags to indicate families and individuals that participated in those events.
For example,
a `FAMC` pointer subordinate to an adoption event indicates a relationship to family by adoption;
biological parents can be shown by a `FAMC` pointer subordinate to the birth event;
the eulogist at a funeral can be shown by an `ASSO` pointer subordinate to the burial event;
and so on. A subordinate `FAMC` pointer is allowed to refer to a family where the individual
does not appear as a child.



#### `MULTIMEDIA_RECORD` :=

```gedstruct
n @XREF:OBJE@ OBJE                         {1:1}  g7:record-OBJE
  +1 RESN <List:Enum>                      {0:1}  g7:RESN
  +1 FILE <FilePath>                       {1:M}  g7:FILE
     +2 FORM <MediaType>                   {1:1}  g7:FORM
        +3 MEDI <Enum>                     {0:1}  g7:MEDI
           +4 PHRASE <Text>                {0:1}  g7:PHRASE
     +2 TITL <Text>                        {0:1}  g7:TITL
     +2 TRAN <FilePath>                    {0:M}  g7:FILE-TRAN
        +3 FORM <MediaType>                {1:1}  g7:FORM
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 GEDC                                  {0:1}  g8:GEDC
    +2 VERS <Special>                      {1:1}  g8:GEDC-VERS
      +3 <<SOURCE_CITATION>>               {1:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

The multimedia record refers to 1 or more external digital files, and may provide some additional information about the files and the media they encode.

The file reference can occur more than once to group multiple files together. Grouped files should each pertain to the same context. For example, a sound clip and a photo both of the same event might be grouped in a single `OBJE`.

The change and creation dates should be for the `OBJE` record itself,
not the underlying files.


$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- `SOURCE_CITATION` is now *behind* the same GEDCOM version tag as in the Header.  
Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` is allowed at this place.   
This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and everything that belongs to it. (inside the `STICKY`s)  


***
$\color{Fuchsia}\large{\textbf{The following PROOF record is experimental:}}$

#### `PROOF_RECORD` :=

**📜 PROOF_RECORD (experimental)**

The `PROOF` record is an **experimental and optional structure** designed to support **reasoning, weighing, and justification** when evaluating competing `STICKY` records for use in an `INDI` , `GROUP` or `ASSET` role.

>- This structure is currently **an unfinished and provisional concept**.  
>- It is **not in active use** in the provided examples and may change or be removed in a future version.
>- Enums belonging to this structure are also defined here, so in case this `PROOF` record will/must be removed, everything is on one place.

**Purpose**  

The `PROOF` record is meant to:
- Pose a specific genealogical **QUESTION** (e.g., “Which marriage event best matches William Smith?”)
- List **CANDIDATES** (STICKY references) being considered
- Provide **ARGUMENTS** and **OUTCOME** ratings _per candidate_
- Optionally identify a `TOPSTICKY` — the `STICKY` the user considers most accurate

```gedcom
PROOF_RECORD := 
n @<XREF:PROOF>@ PROOF                     {1:1}  g8:record-PROOF
  +1 TYPE <Enum>                           {1:1}  g8:PROOF-TYPE
  +1 QUESTION <Text>                       {1:1}  g8:QUESTION
  +1 CANDIDATES                            {1:1}  g8:CANDIDATES
    +2 STICKY @<XREF:STICKY>@              {1:M}  g8:CANDIDATE-STICKY
      +3 ARGUMENT <Text>                   {0:M}  g8:ARGUMENT
      +3 OUTCOME <Enum>                    {0:1}  g8:OUTCOME
  +1 TOPSTICKY @<XREF:STICKY>@             {0:1}  g8:TOPSTICKY
  +1 OUTCOME <Enum>                        {0:1}  g8:OUTCOME
  +1 DATE <Date>                           {0:1}  g7:DATE
  +1 SUBM @<XREF:SUBM>@                    {0:1}  g7:SUBM
  +1 <<FLEX_STRUCTURE>>                    {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

**Example Use**  
A researcher is trying to decide which of two marriage `STICKY` records belongs to a particular `INDI`. They compare `STICKY`s, write arguments, and select the most convincing one.

**Tag Descriptions**
- `TYPE`: `PROOF_TYPE`: Category of the evaluation (e.g., `BIRTH`, `MARRIAGE`, `IDENTITY`) see `g8:PROOF-TYPE`
- `QUESTION`: The plain-language question being answered, as filled in by a user. (or maybe by software)
- `CANDIDATES`: Set of `STICKY` records under consideration. The set could either be given by a user, or software could assist a user in proposing candidate `STICKY`s. As each `STICKY` is tied to 1 `TEMPLATE` the `SOUR` belonging to this `STICKY` can always be reached from that `TEMPLATE`.
- `ARGUMENT`: Explanatory reasoning from the user in favor of this `STICKY` being correct; may be repeated. Can contain `CONT` as with a `NOTE`.
- `TOPSTICKY`: The chosen `STICKY` (if one is determined). Can only hold the ID of 1 of the `STICKY`s in the `CANDIDATES` list.
- `OUTCOME`: Confidence level of this `ARGUMENT` for the selected `STICKY`, from the enumtable `g8:OUTCOME`
- `DATE`: Optional date when reasoning was formalized
- `SUBM`: Optional submitter reference responsible for the reasoning.
- `<<MULTIMEDIA_LINK>>`, link to an `OBJE` for this `PROOF`-record. There is **NO** link to a `SOURCE_CITATION` as that only belongs in the `TEMPLATE`.  

> 🧠 *`ARGUMENT` appears before `OUTCOME` so that evaluators first encounter the reasoning before seeing the resulting confidence level — reinforcing transparent thinking over blind scoring.*

#### `g8:enumset-OUTCOME`

| Value       | Description      |
|-------------|------------------|
| `DISPUTED`  | Explicitly contested; arguments exist on both sides                |
| `SELECTED`  | This is the top candidate (same as the STICKY used in `TOPSTICKY`) |
| `STRONG`    | Strongly supported by argument(s); high confidence                 |
| `UNDECIDED` | Unclear or insufficient info to make a judgment                    |
| `WEAK`      | Weak support; included for completeness or contrast                |
| `OTHER`     | Used with `PHRASE` for special or ambiguous evaluations            |

**Evaluating OUTCOME:**  

The `OUTCOME` tag represents the status or perceived quality of a candidate argument.

While no formal scoring system is imposed, users may consider:

- **Source Type**: Primary evidence (e.g., original documents) is generally more persuasive than derivative summaries.
- **Consistency**: Are multiple sources or arguments aligned?
- **Directness**: Does the evidence relate directly to the claim or is it circumstantial?
- **Clarity and Logic**: Is the reasoning clearly expressed and logically sound?
- **Bias**: Could the evidence or its interpretation be skewed?
- **Currency**: How recent is the evidence?

These factors may influence whether an argument is marked `STRONG`, `DISPUTED`, or otherwise.

Note: These are advisory only — there is no enforced ranking system.

#### `g8:enumset-PROOFTYPE`  
Defines the kind of question this PROOF record is trying to resolve. Each value describes a specific genealogical topic under investigation.  

| ENUM          | Description    |
|---------------|----------------|
| `BIRTHDATE`   | Determining the date of a person’s birth                                    |
| `BIRTHPLACE`  | Determining the place of a person’s birth                                   |
| `CHILDREN`    | Evaluating whether someone is a child of the person                         |
| `DEATHDATE`   | Determining the date of death                                               |
| `DEATHPLACE`  | Determining the place of death                                              |
| `GENDER`      | Establishing or confirming the person’s sex/gender                          |
| `IDENTIFIER`  | Determining whether two records refer to the same individual                |
| `IMMIGRATION` | Determining the date/place of immigration or emigration                     |
| `MARRIAGE`    | Confirming that a marriage took place (spouse identity, location, timeframe)|
| `MARRIAGEDATE`| Determining the exact or likely date of a marriage                          |
| `NAME`        | Resolving questions around full name, alternate spellings, or nicknames     |
| `OCCUPATION`  | Confirming a person’s job or profession                                     |
| `PARENTS`     | Confirming who the person's parents are                                     |
| `RELIGION`    | Confirming religious affiliation or denomination                            |
| `RESIDENCE`   | Confirming a person’s key location during a time period                     |
| `OTHER`       | Other question not listed above; use with `PHRASE` to describe the topic    |

The `PROOF`-TYPE enum describes the focus of a specific proof record — the *question* under evaluation. This may involve choosing between competing `STICKY` entries (e.g., two birth records), or validating a single assertion.

Typical examples include `BIRTHDATE`, `NAME`, or `PARENTS` — but users may also define their own focus via the `OTHER` + `PHRASE` combination.

Note: Some record plausibility issues (e.g., implausible lifespans) are not ideal for `PROOF`-type records unless competing candidate data exists.

:::example  

**💍 Example: PROOF Record — Which Marriage Belongs to Margaret Puddlewharf?**

```gedcom
0 @P0201@ PROOF
1 TYPE MARRIAGE
1 QUESTION What is the correct marriage event for Margaret Puddlewharf of Devon?
1 CANDIDATES
2 STICKY @ST2011@  /* 1879 marriage to Henry Bibble at Exeter Cathedral */
3 ARGUMENT The 1879 Exeter record lists Margaret as 24 years old, matches known birthdate.
3 OUTCOME SELECTED
2 STICKY @ST2012@  /* 1881 marriage to Charles Flingham in Barnstaple */
3 ARGUMENT The 1881 Barnstaple entry lists a Margaret Puddlewharf, age 30, but no parents.
3 OUTCOME WEAK
2 STICKY @ST2013@  /* Undated mention of marriage in cousin’s letter */
3 ARGUMENT Letter mentions a 'Margaret marrying a tall man from Barnstaple' but is undated.
3 OUTCOME DISPUTED
1 TOPSTICKY @ST2011@
1 DATE 29 JUL 2025
1 SUBM @B001@
1 NOTE Concluded by age match and parental details listed in the 1879 parish register.
```
:::

**📍In the INDI block (snippet only):**  

```gedcom
1 ROLES
2 STICKY @ST2011@ /* 1879 marriage to Henry Bibble at Exeter Cathedral */
3 SUBM @B001@
3 PROOF @P0201@
4 OUTCOME SELECTED
2 STICKY @ST2012@  /* 1881 marriage to Charles Flingham in Barnstaple */
3 SUBM @B001@
3 PROOF @P0201@
4 OUTCOME WEAK
2 STICKY @ST2013@  /* Undated mention of marriage in cousin’s letter */
3 SUBM @B001@
3 PROOF @P0201@
4 OUTCOME DISPUTED
```




#### `REPOSITORY_RECORD` :=

```gedstruct
n @XREF:REPO@ REPO                         {1:1}  g7:record-REPO
  +1 NAME <Text>                           {1:1}  g7:NAME
  +1 <<ADDRESS_STRUCTURE>>                 {0:1}
  +1 PHON <Special>                        {0:M}  g7:PHON
  +1 EMAIL <Special>                       {0:M}  g7:EMAIL
  +1 FAX <Special>                         {0:M}  g7:FAX
  +1 WWW <Special>                         {0:M}  g7:WWW
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

The repository record provides information about an institution or person that has a collection of sources.
Informal repositories include the owner of an unpublished work or of a rare published source, or a keeper of personal collections.
An example would be the owner of a family Bible containing unpublished family genealogical entries.

Layered repositories, such as an archive containing copies of a subset of records from another archive or archives that have moved or been bought by other archives, are not modeled in this version of the specification.
It is expected they will be added in a later version.
Until such time, it is recommended that the repository record store current contact information, if known.


#### `SHARED_NOTE_RECORD` :=

```gedstruct
n @XREF:SNOTE@ SNOTE <Text>                {1:1}  g7:record-SNOTE
  +1 MIME <MediaType>                      {0:1}  g7:MIME
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TRAN <Text>                           {0:M}  g7:NOTE-TRAN
     +2 MIME <MediaType>                   {0:1}  g7:MIME
     +2 LANG <Language>                    {0:1}  g7:LANG
  +1 GEDC                                  {0:1}  g8:GEDC
    +2 VERS <Special>                      {1:1}  g8:GEDC-VERS
      +3 <<SOURCE_CITATION>>               {1:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

A catch-all location for information that does not fully fit within other structures.
It may include research notes, additional context, alternative interpretations, reasoning, and so forth.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- `SOURCE_CITATION` is now *behind* the same GEDCOM version tag as in the Header.  
Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` is allowed at this place.   
This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and everything that belongs to it. (inside the `STICKY`s)  


A shared note record may be pointed to by multiple other structures. Shared notes should only be used if editing the note in one place should edit it in all other places
or if the note itself requires an `IDENTIFIER_STRUCTURE`.
If each instance of the note may be edited separately and no identifier is needed, a `NOTE` should be used instead.

Each [`SNOTE`.`TRAN`](#NOTE-TRAN) must have either a `MIME` or `LANG` substructure or both.

:::example
The origin of a name might be a reasonable shared note, while the reason a particular person was given that name may make more sense as a non-shared note.

```gedcom
0 @GORDON@ SNOTE "Gordon" is a traditional Scottish surname.
1 CONT It became a given name in honor of Charles George Gordon.
0 @I1@ INDI
1 NAME Gordon /Jones/
2 NOTE Named after the astronaut Gordon Cooper
2 SNOTE @GORDON@
```
:::

:::note
The ability to have multiple structures share a single note using pointers was introduced in version 5.0 in 1991.
However, as of 2021 relatively few applications have a user interface that presents shared notes as such to users. It is recommended that `SNOTE` be avoided when `NOTE` will suffice.
:::

A `SHARED_NOTE_RECORD` may contain a pointer to a `SOURCE_RECORD` and vice versa. Applications must not create datasets where these mutual pointers form a cycle. Applications should also ensure they can handle invalid files with such cycles in a safe manner.


#### `SOURCE_RECORD` :=

```gedstruct
n @XREF:SOUR@ SOUR                         {1:1}  g7:record-SOUR
  +1 DATA                                  {0:1}  g7:DATA
     +2 EVEN <List:Enum>                   {0:M}  g7:DATA-EVEN
        +3 DATE <DatePeriod>               {0:1}  g7:DATA-EVEN-DATE
           +4 PHRASE <Text>                {0:1}  g7:PHRASE
        +3 <<PLACE_STRUCTURE>>             {0:1}
     +2 AGNC <Text>                        {0:1}  g7:AGNC
     +2 <<NOTE_STRUCTURE>>                 {0:M}
  +1 AUTH <Text>                           {0:1}  g7:AUTH
  +1 TITL <Text>                           {0:1}  g7:TITL
  +1 ABBR <Text>                           {0:1}  g7:ABBR
  +1 PUBL <Text>                           {0:1}  g7:PUBL
  +1 TEXT <Text>                           {0:1}  g7:TEXT
     +2 MIME <MediaType>                   {0:1}  g7:MIME
     +2 LANG <Language>                    {0:1}  g7:LANG
  +1 <<SOURCE_REPOSITORY_CITATION>>        {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

A source record describes an entire source.
A source may also point to `REPO`s to describe repositories or archives where the source document may be found.
The part of a source relevant to a specific fact, such as a specific page or entry, is indicated in a `SOURCE_CITATION` that points to the source record.

:::note
This sourcing model is known to be insufficient for some use cases and may be refined in a future version of this specification.
:::

A `SOURCE_RECORD` may contain a pointer to a `SHARED_NOTE_RECORD` and vice versa. Applications must not create datasets where these mutual pointers form a cycle. Applications should also ensure they can handle invalid files with such cycles in a safe manner.

#### `STICKY_RECORD` :=

The `STICKY` record identifies 1 single entity from a `TEMPLATE` record. It describes all information of this 1 single entity as found on that `TEMPLATE`. So 1 `TEMPLATE` can own many `STICKY`'s.
The same `STICKY` might be linked to many different `INDI`'s, or other records.  
It is possible for a GEDCOM 8 file to have `STICKY`s that are **not yet linked into an `INDI`s `ROLES` section**, That can happen when a user decides not all `STICKY`s from 1 `TEMPLATE` are important enough to have their own `INDI`.  
For instance non related persons in a Census.

```gedcom
n @XREF:STICKY@ STICKY                          {1:1}  g8:record-STICKY
  +1 TYPE <Enum>                                {1:1}  g8:ENTITY-TYPE
    +2 SUBTYPE <Enum>                           {1:1}  g8:ENTITY-SUBTYPE
    +2 PHRASE <Text>                            {0:1}  g8:PHRASE
  +1 TITLE <Text>                               {0:1}  g8:TITLE
    +2 PHRASE <Text>                            {0:1}  g8:PHRASE
  +1 SUBM @<XREF:SUBM>@                         {1:M}  g8:SUBM
    +2 <<NOTE_STRUCTURE>>                       {0:M}
  +1 TEMPLATE @<XREF:TEMPLATE>@                 {1:1}  g8:TEMPLATE
  +1 TORIGIN <Enum>                             {1:1}  g8:TORIGIN
  +1 QUAY <Enum>                                {0:1}  g7:QUAY
  +1 DATE <DateValue>                           {1:1}  g8:DATE-value
  +1 <<SHARED_PLACE_STRUCTURE>>                 {0:1}  g8:SPLAC
  +1 MAINROLE <Enum>                            {0:0}  g8:STICKY-MAINROLE
    +2 ROLE <Enum>                              {1:M}  g8:STICKY-ROLE
  +1 GROUP @<XREF:GROUP>@                       {0:M}  g8:GROUP
  +1 ASSET @<XREF:ASSET>@                       {0:M}  g8:ASSET
  +1 RESN <List:Enum>                           {0:1}  g8:RESN
  +1 TDABOVI <Special>                          {0:1}  g8:TDABOVI
  +1 <<PERSONAL_NAME_STRUCTURE>>                {0:M}  g8:INDI-NAME
  +1 PEDI <Enum>                                {0:1}  g7:PEDI
  +1 SEX <Enum>                                 {0:1}  g8:SEX
  +1 <<FLEX_STRUCTURE>>                         {0:M}
  +1 <<LDS_INDIVIDUAL_ORDINANCE>>               {0:1}
  +1 <<LDS_SPOUSE_SEALING>>                     {0:1}
  +1 <<FAMILY_EVENT_STRUCTURE>>                 {0:1}
  +1 <<INDIVIDUAL_EVENT_STRUCTURE>>             {0:1}
  +1 <<INDIVIDUAL_ATTRIBUTE_STRUCTURE>>         {0:M}
  +1 <<MULTIMEDIA_LINK>>                        {0:M}
  +1 LANG <Language>                            {0:M}  g8:SUBM-LANG
  +1 <<IDENTIFIER_STRUCTURE>>                   {0:M}
  +1 <<NOTE_STRUCTURE>>                         {0:M}
  +1 <<CHANGE_DATE>>                            {1:1}
  +1 <<CREATION_DATE>>                          {1:1}
```
- The TYPE value must be chosen from the unified enumset `g8:enumset-ENTITY-TYPE`.
  - This list includes `PERSON`, which is valid only in `STICKY`'s that reference an `INDI`.
  - All other `ASSET` types (e.g., `ARTWORK`, `ESTATE`, `PROPERTY`) can be used, regardless of the referenced record type.
- `SUBTYPE` is required and further narrows the kind of `STICKY` object (depends on `TYPE`).
   - Most `STICKY`s are of `TYPE` `PERSON` and dont need a `SUBTYPE`, as for a `PERSON` most of the time there is a `ROLE` and `SUBROLE` to further define the `PERSON`.<br>Incase of annotated events, `SUBTYPE` for a person is needed to be able to define the secondary "event" of this `STICKY`.<br>Example: a censustype event where for 1 or more persons there are annotated "events" written in the margin, like *"moved to London feb 89"*. 
   - When `TYPE` and `SUBTYPE` both are present, they are written on 1 and the same line for readability, with ", " separating them.
- `PHRASE` This is optonal, **except** for `TYPE` `OTHER`, in that case there **must** be a `PHRASE`; `PHRASE`must be written on the same line as `TYPE`, separated from the `TYPE` contents by ", ". As follows:
  - `1 TYPE OTHER, "spoon with inscription"`
  - or `1 TYPE ARTWORK, PAINTING, "Oil painting of Castle King Windemere"`

- `TITLE`, only for an `ENTITY` type `STICKY`: this is the **official title** of this `STICKY` in case it is an item that has a Title, like a painting, a testreport, a book, etc. In case the `STICKY` is about an official document, the `TITLE` is the official title of the document, and `PHRASE` can be a further description. See **Example 08: Naturalization and Passport**
- `TITL.PHRASE` this can be a further description or subtitle.

- `SUBM` lists the contributor(s) of this STICKY entry.  
  - The first listed submitter is considered primary, and is the same `SUBM` as used in the `HEAD` of the GEDCOM file.
  - Additional submitters may represent later changes or annotations.
  - Use `NOTE` for detailed explanation of edits if needed.

- `TORIGIN`, Defines how a `TEMPLATE` or `STICKY` was originally entered, generated or reconstructed. This helps distinguish freshly structured entries from those generated or inferred from legacy data. It clarifies the **origin and trust context** of each entry — whether manually entered, system-generated, or reverse-engineered — supporting gradual adoption of the new model and better transparency in data lineage.

- `QUAY`, defines the quality of this whole `STICKY`. Together with `TORIGIN`.

- `<<INDIVIDUAL_ATTRIBUTE_STRUCTURE>>`, same as in GEDCOM7, but **without the event part**.
- `<<FAMILY_EVENT_STRUCTURE>>`, `<<INDIVIDUAL_EVENT_STRUCTURE>>`, `<<LDS_SPOUSE_SEALING>>` and `<<LDS_INDIVIDUAL_ORDINANCE>>`, same as in GEDCOM7, but **without the event part**.
  - This structure describes the event the linked `TEMPLATE` is about, with the GEDCOM7 tags that excist for the event **in this specific context**.
  - If the `TEMPLATE` describes an event, for which there is no official GEDCOM tag, it will use the general `EVEN`tag, as follows:<br>`1 EVEN TYPE, SUBTYPE`<br>where `TYPE` and `SUBTYPE` are the same as the event type and subtype of this `TEMPLATE`. So for instance:<br>`1 EVEN DEATH, DISAPPEARED`<br>Doing it this way helps software to understand the event as it comes from the same enum table as is used for the main `TYPE` and `SUBTYPE` for the `TEMPLATE` itself.

- `MAINROLE` defines the contextual function of the participants in this `TEMPLATE`. It is defined as {0:0}
because:
  - It is only present to give the user a smaller list of subroles to choose from. The main `ROLE` itself is not mentioned.
  - There is 1 exeption to that: It is required if `TYPE=PERSON` and this `STICKY` describes an annotated event.
- `ROLE`:  
  - It refines the participant’s position in that role, such as `MAIN`, `FATHER`, `MEMBER`, `CHILD`, etc.
  - `ROLE`s are mentioned on the same line as `ROLE`, separated from each other by ", ".
  - The first `ROLE` is separated from `ROLE` by 1 space.
  - There can be more subroles, like for instance `ROLE MAIN, BRIDE` or `ROLE FATHER, BRIDE, PRIEST` (Father of the bride, who also is the priest in the ceremony) 
- `GROUP`, if present, it points to the `GROUP` this `STICKY` has a connection with. The connection is described in the `TEMPLATE` this `STICKY` belongs to.
- `ASSET`, only for non-`PERSON` `STICKY`'s, if present, points to the `ASSET` describing the "lifecycle" of this `ASSET`.
  - **Not all `ASSET`s will have, or need to have, their own `ASSET`record. Only those a user finds important enough.**

> The following applies to `GROUP` and `ASSET`: if a `STICKY` is about a person related to a certain `GROUP` or the `STICKY` describes an entity for which an `ASSET` already excists, or needs to be created, this `STICKY` must have a `GROUP` or `ASSET` link on this place inside the `STICKY`. And if necessary the corresponding `GROUP`- or `ASSET`- record must be created.

- `TEMPLATE`, pointer to the `TEMPLATE` instance this `STICKY` was derived from (so the `TEMPLATE` in which `ROLES` section this `STICKY` is mentioned.)
  - The `TEMPLATE` pointer is technically deducible from the `STICKY`'s internal ID or generation context, but is required in the export for:
    - human readability
    - easy tracing of origin
    - consistent parsing across tools

- `DATE` The same `DATE` as in the `TEMPLATE` this record refers to (e.g. the date of the marriage, baptism, will) – It defines the date of the described entity's role or involvement. This supports chronological sorting of `STICKY`'s in an `INDI`, `GROUP` or `ASSET`.

- `TDABOVI` This is only valid if the `TEMPLATE` this `STICKY` belongs to, contains secondary events that together form a mini-tree. (also see the `TDECUJUS` description with the `TEMPLATE` itself.)  
  - **Example: a family bible with a handwritten part**, that describes many people of a family in a tree-like way.  
  In that case, it is **the D'Aboville number of this `STICKY`'s person** in the mini-tree inside this `TEMPLATE`. 

- `PERSONAL_NAME_STRUCTURE`, this is the Name of the person, or asset in this `STICKY`.
  - It follows the new GEDCOM8 Name structure!
- `FLEX_STRUCTURE`, this is used for information in the `STICKY` that has no GEDCOM tag, and that should be saved, and later represented, to a user. For instance:
  - Signature information: "signed with a mark", or "Signature illegible".
  - Comments written in the margin: "Clerk wrote: 'mother possibly misnamed'".
  - Witness behaviour: "Witness appeared intoxicated"

- `INDIVIDUAL_ATTRIBUTE_STRUCTURE`, partly the same as for `INDI`
  -  It only describes facts and attributes known about the STICKY object **in this specific context**.
  -  It **doesnt have the `EVENT_DETAIL` structure** inside. As the `TEMPLATE` itself describes the **event** or **situation**.
  - For instance it describes `BURI` with a `TYPE` and an `AGE` and nothing more. As the event itself, is already described in the `TEMPLATE` this `STICKY` comes from / belongs to.
- `SEX`, `LANG`, `MULTIMEDIA_LINK`, and `IDENTIFIER_STRUCTURE` are standard GEDCOM7 elements.  
  -  These are used as defined in GEDCOM7 unless otherwise noted.
---

#### IMPORTANT!
- The `STICKY` only contains data that is directly or indirectly found in or on the `TEMPLATE`**it is part of!** So if, in older records, hardly any other information is present, the `STICKY` might not contain much more than eventdate, name, and `ROLE`'s. But more modern records might have a lot of information about people for instance, `NAME`, `AGE` and or `BIRT`, `RESI` and or `ADDR`, `OCCU`, `RELI`, marriage status like "widow", and more.<br>Each of those go in their corresponding `TAG` in the `STICKY`.
- Each `STICKY` is an unseparable part of only 1 `TEMPLATE`.
- Each new `TEMPLATE` gets its own `STICKY`'s! A `STICKY` can not be reused for another `TEMPLATE` as it only "belongs" to 1 !
- 1 and the same `STICKY` **can be connected to more records**, as it can be part of for instance an `INDI` but at the same time it can also be part of a `GROUP` (as a `GROUP` member).<br>In case the `STICKY` for instance is a child, it can be linked in its own `INDI`, but also in the `INDI`'s of both its Father and Mother, as they have the parent role on a birth certificate.
>  - **This means the `FAM` record is no longer used in GEDCOM 8**.
- `ADOP` and `PEDI`: If the `TEMPLATE` is about an adoption, the `TEMPLATE`, as wel as the `STICKY` of the child, have `ADOP` inside it, followed by `PEDI` with the type of "pedigree". In case of an adoption it will be `1 PEDI ADOPTED`, in case of a sealing it will be `1 PEDI SEALING` etcetera. 

#### SPECIAL CASES:

`ROLE`'s inside a `STICKY` have a very important function. They define the `ROLE` or `ROLE`'s the `STICKY`-entity has in the `TEMPLATE` it belongs to.  
Now it is also mentioned that `ROLE`'s are separated from eachother by a ", ". When 2 `ROLE`'s are directly after one another, and those `ROLE`'s are family related, we pronounce the "," as: **"of the"**, see below. 

- `ROLE MAIN`: This role denotes the main entity, or entities, of the `TEMPLATE`. It is a necessary role, to be able to define family related connections. For instance:
  - `ROLE MAIN, BRIDE` This defines that this `STICKY` is the bride (a main person) in a marriage. But as often her father, mother and maybe brothers and sisters and other family members are present, we need `MAIN` as a reference point. So we can say:
  - `ROLE MOTHER, BRIDE` which is the mother **of the** bride. And we can also have:
  - `ROLE FATHER, BRIDE, PRIEST`. Here we have a father **of the** bride, who also is the `PRIEST` in the ceremony. For this last one we could also fill in an `OCCU PRIEST` for the father, as that can be concluded from his role.
  - If a `STICKY` for instance is the birth of a child, and his parents are part of a group, like a `FARM`, the `ROLE`'s for the child become `1 ROLE MAIN, CHILD, MEMBER`, as the child in that case automatically becomes a member too, because of his parents. Further, in that case, the childs `STICKY` gets a pointer to the `GROUP` its parents belong to.


- There is no rule/limit on the `ROLE`'s we can combine (although it must be reasonably readable and understandable!), so for instance we can have:
  - `ROLE MAIN, BRIDE` and in that same `TEMPLATE` we have another `ROLE MAIN, BRIDE`, that gives us a couple with 2 woman.
  - But as we now might get problems **defining their relatives** we must do it like this:
    - `ROLE MAIN, BRIDE1` and another `ROLE MAIN, BRIDE2`. So we put a number behind each `BRIDE`, to be able to correctly define their relatives. That way we can say: `ROLE, MOTHER, BRIDE2` and we have the mother **of the** bride number 2. That saves us the trouble of being forced to put names inside a `ROLE` tag otherwise, as we dont want to do that.
- As we also have the role `PARTNER` which is a person of whom we do not now the sex we can define:
  - `ROLE MAIN, BRIDE` together with `ROLE MAIN, PARTNER`. Now we have a relationship where one of the 2 does not want to be called man or woman, and in case both dont want to be called that we can also have:
  - `ROLE MAIN, PARTNER1` and `ROLE MAIN, PARTNER2`. (Again with a number to be able to distinguish between them)

- We can even go one step further and have a relation that has the 3 following roles:
  - `ROLE MAIN, BRIDE1` and a `ROLE MAIN, BRIDE2` together with this one: `ROLE MAIN, GROOM`. Now we have a polyamorous relationship.

- We must make sure, that in case we have more `ROLE`'s in 1 tag, they follow each other in a logical sequence! So **dont write** `ROLE FATHER, PRIEST, BRIDE` but in stead write `ROLE FATHER, BRIDE, PRIEST` (father of the bride who is also the priest) or `ROLE PRIEST, FATHER, BRIDE` (the priest, who is also father of the bride).

- Another `ROLE` that might need to be numbered is `HEIR`, as there can be more `HEIR`'s in 1 will. So we might see for that `TEMPLATE`: `ROLE HEIR1` , `ROLE HEIR2` etc.

#### Role numbering:
All `ROLE`'s that appear more than once in 1 `TEMPLATE` and can cause confusion because other persons might have a `ROLE` **that denotes a relationship** to them, are numbered to prevent confusion:
- Example 1 a will with 3 HEIRS, they will be numbered like this inside the `ROLE` section in the respective `STICKY`s: `HEIR1`, `HEIR2` and `HEIR3`.
- Example 2 a marriage with 2 brides: the `ROLE` in their `STICKY`s will be: `BRIDE1`and `BRIDE2`, so other family members can be related to the correct Bride. (`ROLE FATHER, BRIDE1` or `ROLE FRIEND, BRIDE2`)
- Example 3 a Census, where each family member has the `ROLE` `RESIDENT`, here numbering is not necessary as there is no `ROLE` that "relates" to `RESIDENT`.

#### Examples

:::example
#### STICKY Example 1 – Groom in a Marriage Certificate

This is a full example of a STICKY_RECORD, based on a marriage certificate. It shows the groom as the subject, including personal name, role, and details derived from the certificate's template.

**Explanation:**

- This `STICKY` refers to **Pieter van Dijk**, the groom, age 21, he is a baker.
- His data is taken only from template @T0123@, (dated 1855-06-14) which corresponds to a marriage certificate from Amsterdam.
- His occupation, residence, and birth are included in this `STICKY` **because they appear on the document**.
- `ROLE` is `GROOM`, with `MAIN` to indicate he's a main subject.
- This `STICKY` is **only filled** with information that is present **on the `TEMPLATE`** it derives from. 
- This record can now be linked inside an `INDI` record for Pieter, contributing to his `INDI`-timeline, based on this one source.

```gedcom
0 @ST345@ STICKY              /* Pieter van Dijk */
1 TYPE PERSON
1 SUBM @B001@                 /* Original submitter (same as in the HEAD of the GEDCOM) */
1 TEMPLATE @T0123@            /* The original marriage certificate template this STICKY belongs to */
1 TORIGIN ORIGDOC             /* Directly derived from an original document */ 
1 QUAY 3
1 DATE 1855-06-14             /* The date of that template, so the marriage registration date */
1 ROLE MAIN, GROOM            /* He is 1 of the 2 MAIN persons, and he is the GROOM */
1 NAME                        /* In latest NAME format of GEDCOM8 */
2 TYPE GENERAL
1 FORM Pieter van Dijk
2 PART Pieter
3 TYPE GIVN
2 PART PIET
3 TYPE VARIANT
2 PART van                    /* PART is particle, e.g. Dutch "van", "van de", or "uijt den" — or French "de", Italian "di" */
3 TYPE PART
2 PART DIJK
3 TYPE SURN
1 SEX M
1 MARR                        /* Information of the marriage itself */
2 TYPE CIVIL
2 DATE 1855-06-14
2 SPLAC @SP063@               /* Amsterdam, Noord-Holland, Netherlands */
1 AGE 21
1 BIRT
2 DATE ABT 1834               /* Estimated birth date from age */
2 SPLAC @SP628@               /* Leiden, Zuid-Holland, Netherlands */
1 OCCU Baker
1 RESI
2 DATE ABT 1855
2 SPLAC @SP063@               /* Amsterdam, Noord-Holland, Netherlands */
1 NOTE This STICKY only reflects the data for the groom as recorded in this civil marriage record.
1 CITA
~ ~ ~
1 CREA 01 MAY 2025
1 CHAN 03 MAY 2025
```
:::

### STICKY Example 2 – Militaire Willems-Orde Medal ("ASSET" STICKY) 

This `STICKY` describes a medal as an `ASSET`, specifically the Militaire Willems-Orde (4e klasse), awarded in 1831 after the Ten Day Campaign. The 2 `FLEX` entries capture the registry number and a Dutch-language archival description.
For these 2 values there is no official GEDCOM tag, but this way they can still be entered, and shown to the user.  
This `STICKY` is an `ASSET` so it has **No `ROLE`'s**  
The `TEMPLATE` this `STICKY` belongs to, has a `TRANSFER` statement, that describes the "move" for the medal from the organization that cxxx the medal, to the new owner: Willem Johan de Vries, as in the `STICKY` in  example 3.

```gedcom
0 @ST998@ STICKY
1 TYPE MILITARY, MEDALS, "Ridder vierde klasse in de Militaire Willems-Orde, uitgereikt na Tiendaagse Veldtocht"
1 TITL Militaire Willems-Orde – 4e klasse
1 SUBM @B001@                 /* Submitter of this record (likely from archival source) */
1 TEMPLATE @T456@             /* This could be a military honors record or award list */
1 TORIGIN ORIGDOC             /* Directly derived from an original document */ 
1 QUAY 3
1 DATE 1831-09-15             /* Actual date of the award ceremony or registration */
1 SPLAC @SP942@               /* 's-Gravenhage, Zuid-Holland, Netherlands */
1 FLEX REGNUMBER
2 CONTENTS MW-1831-00456      /* This is the registration nr of this medal */
2 PHRASE "Registratie nummer" /* This is the exact text as it is found on the record itself */
3 LANG nl
1 FLEX NOTE
2 CONTENTS "Ridderorde toegekend voor moed en beleid tijdens de Tiendaagse Veldtocht"
2 PHRASE "Beschrijving van de medaille"
3 LANG nl
~ ~ ~
1 CREA 05 MAY 2025
1 CHAN 06 MAY 2025
```
### STICKY Example 3 – recipient of the medal in `@ST998@` (previous example)

- This `STICKY` describes the recipient of the medal in `@ST998@`, in the previous example.
- The `FLEX` encodes the rank specifically at the time of the award.
- `PHRASE` shows the field as seen in the source register.
- "Militair register van onderscheiding" = "Military Register of Awards"
- The actual Transfer of the medal to Willem, is done on the `TEMPLATE` itself by means of a `TRANSFER` structure.

```gedcom
0 @ST999@ STICKY
1 TYPE PERSON                 /* `PERSON` only has a `SUBTYPE` for secondary events */
1 TITL "Militair register van onderscheiding, 1831"
1 SUBM @B001@
1 TEMPLATE @T456@             /* Same template as the medal itself, STICKY @ST998@ */
1 TORIGIN ORIGDOC             /* Directly derived from an original document */ 
1 QUAY 3
1 DATE 1831-09-15             /* Date on the source document */
1 ROLE MAIN, RECIPIENT        /* RECIPIENT of the medal */
1 NAME
2 TYPE GENERAL
2 FORM Willem Johan de Vries
2 PART Willem Johan
3 TYPE GIVN
2 PART de
3 TYPE PART
2 PART Vries
3 TYPE SURN
1 NAME
2 TYPE INFORMAL
2 FORM WIM
2 PART WIM
3 TYPE ROEPNAAM
1 SEX M
1 OCCU Kapitein der Infanterie   /* Captain of Infantry */
1 BIRT
2 DATE 1795
2 SPLAC @SP937@               /* Utrecht, Utrecht, Netherlands */
1 DEAT
2 DATE 1847
2 SPLAC @SP534@               /* Maastricht, Limburg, Netherlands */
1 FLEX DESCRIPT
2 CONTENTS "Kapitein der Infanterie"
2 PHRASE "Rang bij onderscheiding"  /* Rank by distinction */
3 LANG nl
1 FLEX NOTE
2 CONTENTS "Willem Johan de Vries ontving de Militaire Willems-Orde (vierde klasse) voor zijn moed tijdens de Tiendaagse Veldtocht."
2 PHRASE reden van onderscheiden.
3 LANG nl
1 CITA
~ ~ ~
1 CREA 05 MAY 2025
1 CHAN 06 MAY 2025
```

#### `SUBMITTER_RECORD` :=

```gedstruct
n @XREF:SUBM@ SUBM                         {1:1}  g7:record-SUBM
  +1 NAME <Text>                           {1:1}  g7:NAME
  +1 <<ADDRESS_STRUCTURE>>                 {0:1}
  +1 PHON <Special>                        {0:M}  g7:PHON
  +1 EMAIL <Special>                       {0:M}  g7:EMAIL
  +1 FAX <Special>                         {0:M}  g7:FAX
  +1 WWW <Special>                         {0:M}  g7:WWW
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 LANG <Language>                       {0:M}  g7:SUBM-LANG
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

The submitter record identifies an individual or organization that contributed information contained in the dataset.
All records in the document are assumed to be contributed by the
submitter referenced in the `HEAD`,
unless a `SUBM` structure inside a specific record points at a different submitter record.

#### `TEMPLATE_RECORD` :=

The `TEMPLATE` record identifies **1 single event**  or situation from a `SOUR`. It describes all information of this 1 single event/situation as found in that `SOUR`. So if a `SOUR` is a churchbook, the `TEMPLATE` defines 1 birth, or 1 marriage etcetera. 

The main information of the `TEMPLATE` is in fact the same as what in GEDCOM V7 was called "SOURCE_CITATION". But the information that in V7 was inside the transcription, so just a "booklike" 1 on 1 transcription of the event/fact data itself, including all the people present at that event or having some relation to the situation, including all information found about those persons / assets, all that is now also put in a `STICKY` of its own.  
1 `STICKY` for each person or asset involved. And each `STICKY` describing the `ROLE`('s) that person or `ASSET` had in this 1 event.  

---
> **Linking to a `TEMPLATE`:** The **only place** a link to a `TEMPLATE` is allowed is from **inside a `STICKY`**. Each `STICKY` **always** links back to the `TEMPLATE` it belongs to and is part of.
---  

#### 📌 Guidelines for Choosing the `MAIN` Person(s) in a TEMPLATE

The `MAIN` person or persons of a `TEMPLATE` represent the primary individual(s) the document is *about*. This may differ from the person who created or signed the record. The goal is to clearly reflect **who is central to the event** described in the `TEMPLATE`.

---

**🔁 NOTE:** `MAIN` is added in the `ROLE` field **inside** each `STICKY`, *not* in the `TEMPLATE` structure itself. This tells software and humans **who the document is about**, without duplicating data in the TEMPLATE header.

---

#### ✅ Common Examples (Straightforward)
| Event Type           | `MAIN` Person(s)                                   |
|----------------------|----------------------------------------------------|
| Birth                | The child being born                               |
| Marriage             | The couple getting married                         |
| Tombstone            | All persons named on the stone                     |
| Family Bible         | The "de cujus" (person the tree starts from) and partner |

#### ⚠️ Tricky Cases (Could be Misunderstood)
| Document Type              | `MAIN` Person(s) Explanation |
|----------------------------|------------------------------|
| **Census household**       | Head of household only — others are included as family but not `MAIN` |
| **Will / Probate**         | The deceased (decedent, testator). Heirs and executors are not `MAIN` |
| **Pension Application**    | The applicant (e.g., widow); not the deceased spouse |
| **Court Case**             | The defendant (person accused or sued); witnesses/judges not `MAIN` |
| **Affidavit / Declaration**| The person making the sworn statement |
| **Naturalization**         | The person becoming a citizen |
| **School Enrollment**      | The student (not the guardian who signs) |
| **Marriage License Application** | The couple applying; witnesses and officials are not `MAIN` |
| **Medical Report**         | The patient |
| **Ship Manifest**          | The immigrant listed (typically head of family or individual traveler) |
| **DNA Test Report**        | The individual whose DNA is being tested or interpreted |

> 👤 Use `MAIN` only for persons who are central to the event or document's **evidentiary focus**.

So a `TEMPLATE` consists of information from:
- `EVENT_DETAIL` as a `TEMPLATE` describes the event (or events, see below). **But without** the `ASSOCIATION_STRUCTURE` of the `EVENT_DETAIL`, as that is now described by the `ROLE`'s in each `STICKY`.
- `SOURCE_CITATION` All information from that is now inside a `CITA_STRUCTURE`. Except the event itself, as that is now taken over by the whole `TEMPLATE`.
- 1 or more `STICKY`s, each describing 1 person or `ASSET` and its `ROLE` in the event.

```gedstruct
n @XREF:TEMPLATE@ TEMPLATE                 {1:1}  g8:record-TEMPLATE
  +1 TYPE  <Enum>                          {1:1}  g8:EVENT-TYPE
    +2 SUBTYPE  <Enum>                     {1:1}  g8:EVENT-SUBTYPE
    +2 PHRASE <Text>                       {0:1}  g8:PHRASE
  +1 TITLE <Text>                          {1:1}  g8:TITLE
    +2 PHRASE <Text>                       {0:1}  g8:PHRASE
  +1 SUBM @<XREF:SUBM>@                    {1:M}  g8:SUBM 
    +1 <<NOTE_STRUCTURE>>                  {0:M}
  +1 RESN <List:Enum>                      {0:1}  g8:RESN
  +1 TORIGIN <Enum>                        {1:1}  g8:TORIGIN
  +1 QUAY <Enum>                           {0:1}  g7:QUAY
  +1 DATE <DateValue>                      {1:1}  g8:DATE-value 
    +2 TIME <Time>                         {0:1}  g8:TIME
    +2 PHRASE <Text>                       {0:1}  g8:PHRASE
  +1 <<SHARED_PLACE_STRUCTURE>>            {1:M}  g8:SPLAC
  +1 <<LDS_INDIVIDUAL_ORDINANCE>>          {0:1}
  +1 <<LDS_SPOUSE_SEALING>>                {0:1}
  +1 <<FAMILY_EVENT_STRUCTURE>>            {0:1}
  +1 <<INDIVIDUAL_EVENT_STRUCTURE>>        {0:1}
  +1 AGNC <Text>                           {0:1}  g7:AGNC
  +1 RELI <Text>                           {0:1}  g7:RELI
  +1 CAUS <Text>                           {0:1}  g7:CAUS
  +1 PEDI <Enum>                           {0:1}  g7:PEDI
  +1 SDATE <DateValue>                     {0:1}  g7:SDATE
    +2 TIME <Time>                         {0:1}  g7:TIME
    +2 PHRASE <Text>                       {0:1}  g7:PHRASE
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 ROLES                                 {1:1}  g8:ROLES
    +2 STICKY @<XREF:STICKY>@              {1:M}  g8:STICKY
      +3 RESN <List:Enum>                  {0:1}  g8:RESN
  +1 TDECUJUS @<XREF:STICKY>@              {0:1}  g8:TDECUJUS
  +1 <<TRANSFER_STRUCTURE                  {0:M}
  +1 <<FLEX_STRUCTURE>>                    {0:M}
  +1 <<ADDRPLUS_STRUCTURE>>                {0:1}  g8:ADDRPLUS
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CITA_STRUCTURE>>                    {1:1}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

:::example  
##### example of a `TRANSFER`: 

Suppose there is a Will, with a deceased, a witness, an heir, and a piece of land, that Will will have:
- 1 `STICKY` for the deceased, with roles: `MAIN, DECEASED, GRANTOR` or officially `MAIN, DECEDENT, GRANTOR`. He transfers ownership of the piece of land.
- 1 person `STICKY` for the witness, with Role: `WITNESS`
- 1 person `STICKY` for the heir, with role: `HEIR, SON`, if he is also the son of the deceased.
- 1 `STICKY` for the land, with Sticky type: `ESTATE, PARCEL` or `LAND, FIELD` or `PROPERTY, FARM`, depending on the situation. 
- a `TRANSFER` structure in the `TEMPLATE` itself, that shows the piece of land goes from the `GRANTOR` (the deceased) to the `GRANTEE` (the heir).  
:::

So a template can be the origin of many STICKY's. Each of those `STICKY`'s might/can be linked to many different `INDI`'s, or other records.

- `TYPE` and `SUBTYPE`. These 2 belong together. Eacht `TYPE` can have 1 or more `SUBTYPES`. They are written on the same line starting with the choosen `TYPE` value. For instance `TYPE PERSON` for a `STICKY` that describes a person, or `TYPE ESTATE, LAND` for a piece of land in for instance a will. 
  - `PHRASE` can be used to further specify. It is always part of the `TYPE`-line.
- `TITLE` this is the **official title** of this certificat, as know by an authority. So not "John Doe Birth Certificate" but:
  -	"Standard Dutch Birth Certificate (1811-1870)"
  - "Catholic Church Marriage Record (19th Century)"
- `TITL.PHRASE` this can be the unofficial "name" of this certificate like: "John Doe Birth Certificate"

- `TORIGIN`, Defines how a `TEMPLATE` or `STICKY` was originally entered, generated or reconstructed. This helps distinguish freshly structured entries from those generated or inferred from legacy data. It clarifies the **origin and trust context** of each entry — whether manually entered, system-generated, or reverse-engineered — supporting gradual adoption of the new model and better transparency in data lineage.

- `QUAY`, defines the quality of this whole `TEMPLATE`. Together with `TORIGON`.

- `DATE` and `<<SHARED_PLACE_STRUCTURE>>`, they describe the date and place of this `TEMPLATE`. This is not necessarely the same as the date and place of the event. For instance a `BIRT` happens a few days earlier, than the actual filing of the birth record itself.

- `<<FAMILY_EVENT_STRUCTURE>>`, `<<INDIVIDUAL_EVENT_STRUCTURE>>`, `<<LDS_SPOUSE_SEALING>>` and `<<LDS_INDIVIDUAL_ORDINANCE>>`, 1 of these must be present in a `TEMPLATE`:
  - These structures describes the event this `TEMPLATE` is about, with the GEDCOM7 tags that excist for the event **in this specific context**.
  - Only 1 of these 4 can, and must be present.
  - If the `TEMPLATE` describes an event, **for which there is no official GEDCOM tag**, it will use the general `EVEN` tag, as follows:<br>`1 EVEN TYPE, SUBTYPE, PHRASE`<br>where `TYPE`, `SUBTYPE`, and `PHRASE` are the same as the event type and subtype of this `TEMPLATE`. So for instance:<br>`1 EVEN DEATH, DISAPPEARED`<br>Doing it this way helps software to understand the event as it comes from the same enum table as is used for the main `TYPE` and `SUBTYPE` for the `TEMPLATE` itself.
  - The Event of the `TEMPLATE` goes to all person `STICKY`s that have `MAIN`in their `ROLE`. So for `BIRT` its only the child, for a marriage its the `BRIDE` and the `GROOM`, but for a `CENSUS` its all persons who are on the Census. Other persons and assets in the `TEMPLATE` dont get the event, as they were there, but didnot play a `MAIN` `ROLE`. And if they need the event, they can find it through the `TEMPLATE` pointer that is in each `STICKY`.
  - If a `TEMPLATE` is of type `SECONDARY`, the `TEMPLATE` itself has an event, but the persons in the `TEMPLATE` have not.

- `ROLES`: in this section a list of `STICKY`'s is mentioned that are present, or have a `ROLE`, in the event of this `TEMPLATE`. Each `STICKY` can only be mentioned inside the `ROLES` section of 1 `TEMPLATE`, as it is only part of, and in fact, belongs to, **that** `TEMPLATE`. But that same `STICKY` **can** be mentioned in other records, like the person it belongs to, or the `GROUP` it belongs to.

- `TDECUJUS`, Only used if the `TEMPLATE`, contains secondary events that together form a mini-tree.  
**Example: a family bible with a handwritten part**, that describes many people of a family in a tree-like way.  
Normally those people and the events described, would all have their own `TEMPLATE`. As they all would have their own separate official document. But in this case the Bible is the `TEMPLATE` and **the "events" are only annotated inside the Bible's pages**.  
As in that case the normal `ROLE` system, that defines the connection people have relative to each other in the family, is not possible, as there might be many generations in that annotated part. And `ROLES` are defined for relations of 1, at most, 2 generations apart.  
  - So in this special case, for the annotated people **inside this `TEMPLATE`**, we use the d'Aboville numbering system.
  - And **the eldest person in that annotated tree is the De Cujus**.  
  - Further numbering is done inside the `STICKY`'s belonging to this special `TEMPLATE`, starting from the De Cujus.
  - The **`TDECUJUS`** points to the `STICKY` that is **the eldest person** in this annotated part of the `TEMPLATE`.  

  The name `TDECUJUS` starts with a **T** to denote it belongs inside a `TEMPLATE` so if there would ever be a DeCujus necessary in GEDCOM, `DECUJUS` can be used. Same for `TDABOVI`.

- `TRANSFER_STRUCTURE`, this is used to be able to denote if an asset `STICKY` is "moving" on or in this `TEMPLATE`. Example:
  - In case of an asset `STICKY`, for a piece of land on a will `TEMPLATE`, it defines from whom to whom this `ASSET` is transferered
  - If 1 asset goes to more `HEIR`s, the `SHARE` of the `TRANSFER` is used to define the share of each `HEIR`.
- `FLEX_STRUCTURE`, this is used for information on the `TEMPLATE` that has no GEDCOM tag, and that should be saved, and later represented, to a user. For instance:
  - The addres of an agency that is the issuer of the official form, but that can not be saved and/or represented in current GEDCOM.
  - Other possibilities: Filing location name, Local form number, Reason for record, Document state, Consent or approval line.
  - Document condition: "Torn, corner missing".

- `ADDRPLUS_STRUCTURE`, If necessary the complete addressing information of the Organization that issued the `TEMPLATE`, in case the `TEMPLATE` describes a document issued by that specific Organisation.<br>For instancce a Will certificate issued by a notary office. Or an adoption certificat issued by a court.

- `SOUR`, this is seen as the origin for this `TEMPLATE`. Now as a `SOUR` in itself can point to more `TEMPLATE`'s (example: church book with many birth records) it is allowed for a `SOUR` to be linked to in other **`TEMPLATE`'s**. But a `SOUR` is only linked to from inside 1 or more `TEMPLATES` never from any other place in the GEDCOM file.
- `RESN` (below `STICKY`, this is meant to have a restriction on just this 1 `STICKY` when needed.
- By default the first `SUBM` wil point to the submitter as referenced in the `HEAD`,
unless there are 1 or more extra `SUBM`'s in this `TEMPLATE` structure. In that case each of these extra `SUBM`'s points to the submitter who changed this `TEMPLATE` record. That way changes can be tracked. The `NOTE_STRUCTURE` of a `SUBM` can be used to describe those changes.

---

#### IMPORTANT!
- `ADOP` and `PEDI`: If the `TEMPLATE` is about an adoption, the `TEMPLATE`, as wel as the `STICKY` of the child, have `ADOP` inside it, followed by `PEDI` with the type of "pedigree". In case of an adoption it will be `1 PEDI ADOPTED`, in case of a sealing it will be `1 PEDI SEALING` etcetera. 


#### TEMPLATE example
::example

This `TEMPLATE` describes a marriage event (`MARR`) involving several people.
- `MARR` has a `DATE` and an `SPLAC`, following the GEDCOM 7 convention.
- **However**, the event description that would normally go *under* the `MARR` tag now appears directly under the `TEMPLATE` itself.  This change is necessary because a `TEMPLATE` can now represent far more events than GEDCOM 7 allowed. And all those events can now be handled the same way.

- If a `TEMPLAYE` describes an event, that has no GEDCOM8 tag, use the general `EVEN` in its place, with `DATE` and `SPLAC` *under* it.

```gedcom
0 @T0042@ TEMPLATE
1 TYPE MARRIAGE, CIVIL        /* Eventtype marriage, is MARR tag */
1 TITL Wedding Certificate Springfield
2 PHRASE Wedding "Certificate"
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 MARR                        /* Family Event */
2 DATE 18 JUN 1954            /* Marriage date */
2 SPLAC @SP006@               /* Place of marriage - London */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE, not necessarily the MARR date */
1 SPLAC @SP006@               /* Place of this event - London */
1 ROLES
2 STICKY @ST0142@             /* MAIN, BRIDE */
2 STICKY @ST0143@             /* MAIN, GROOM */
2 STICKY @ST0241@             /* FATHER, BRIDE Father of the Bride */
2 STICKY @ST0242@             /* MOTHER, GROOM, Mother of the Groom */
2 STICKY @ST0341@             /* UNCLE, BRIDE, Uncle of the Bride */
2 STICKY @ST0342@             /* FRIEND, GROOM, Friend of the Groom */
2 STICKY @ST0441@             /* OFFICIANT of the Marriage */
1 PAGE 5                      /* Pagenumber this certificat is found in the source */
1 DATA 
1 CREA 22 JUL 2025
1 CHAN 22 JUL 2025
```
::: 

#### "Missing" information, compared to GEDCOM V7's Source-Citation:

- `EVEN` The Event-tag, is now kind of "substituted" by `TYPE`and `SUBTYPE`of the `TEMPLATE` itself. Together with the tag for the event, mentioned in the `STICKY`s the tag belongs to.
- `ROLE` now moved inside a `STICKY` as each person or asset present at the event or situation, can have its own `ROLE` or even more roles, like a `FATHER` who is also a `WITNESS` in a marriage. So `ASSO` is no longer needed.
- Non mentioned tags, have the same meaning as in GEDCOM 7, as they originally came from the `EVENT_DETAIL` or the `SOURCE_CITATION` in GEDCOM7.

#### Handling Annotated (Secondary) Events in Templates

A `TEMPLATE` normally describes a **single event** or action, drawn from one real-world document or genealogical artifact. Its `TYPE` defines the main event it represents (e.g., `CENSUS`, `BAPTISM`, `MARRIAGE`) and determines the structure and roles within.

However, some documents, for instance a Census, also include **additional notes or annotations** about **secondary events**. These are not the primary focus of the Census document but may record occurrences such as:

- The **birth** of a child during the time of residence (`CENSUS`)
- The **death** of a household member (added later to the census form)
- A **move or departure** noted in a margin, sometimes with a new address

These secondary facts do **not** alter the `TYPE` of the `TEMPLATE`, which remains bound to the main document’s function. And they are not the **primary event** of the document (which remains a `CENSUS`), but they are real, meaningful notes that deserve structured representation.

So they justify the creation of **additional `STICKY`s**, each of which may describe the side-event involving a person already mentioned in another `STICKY` in this `TEMPLATE`.

Rather than redefining the `TEMPLATE.TYPE`, we handle these as **additional STICKYs** tied to the same template. These `STICKY`s describe **side events**, and have specially designated `STICKY`-subtypes that reflect their **marginal nature** — typically annotations or supplemental facts, described in the `STICKY`-type itself like:

:::examples:
```
1 TYPE PERSON, AN_BIRTH
1 TYPE PERSON, AN_DEATH
1 TYPE PERSON, AN_LEAVE
```
:::

The `TYPE` is still `PERSON`, but the subtype makes it clear this is an *annotation event* — a derived fact extracted from a margin, note, or supplement, not the main event. This method:

- Keeps `TEMPLATE.TYPE` singular and correct
- Allows side events to be described without muddling the main structure
- Ensures clarity and integrity for users and software

This approach allows multiple STICKYs per person in the same TEMPLATE:

- One for their **main role** (e.g., household member)
- One or more for **annotated roles** or **side events**

These additional STICKYs remain linked to the same TEMPLATE.  
This preserves:

- Structural clarity (one TEMPLATE, multiple participant views)
- Contextual integrity (the STICKY documents what the template says)

The prefix `AN_` (for “annotation”) distinguishes these subtypes as **secondary**, and signals that their data was derived from **side/marginal notes, comments or supplemental markings**, not from the main event.

### Substructures

#### `ADDRESS_STRUCTURE` :=

```gedstruct
n ADDR <Special>                           {1:1}  g7:ADDR
  +1 ADR1 <Special>                        {0:1}  g7:ADR1
  +1 ADR2 <Special>                        {0:1}  g7:ADR2
  +1 ADR3 <Special>                        {0:1}  g7:ADR3
  +1 CITY <Special>                        {0:1}  g7:CITY
  +1 STAE <Special>                        {0:1}  g7:STAE
  +1 POST <Special>                        {0:1}  g7:POST
  +1 CTRY <Special>                        {0:1}  g7:CTRY
```

A specific building, plot, or location.
The payload is the full formatted address as it would appear on a mailing label, including appropriate line breaks (encoded using `CONT` tags).
The expected order of address components varies by region; the address should be organized as expected by the addressed region.

Optionally, additional substructures such as `STAE` and `CTRY` are provided to be used by systems that have structured their addresses for indexing and sorting. If the substructures and `ADDR` payload disagree, the `ADDR` payload shall be taken as correct.
Because the regionally-correct order and formatting of address components cannot be determined from the substructures alone, the `ADDR` payload is required, even if its content appears to be redundant with the substructures.

:::deprecation
`ADR1` and `ADR2` were introduced in version 5.5 (1996)
and `ADR3` in version 5.5.1 (1999),
defined as "The first/second/third line of an address."
Some applications interpreted ADR1 as "the first line of the *street* address",
but most took the spec as-written and treated it as a straight copy of a line of text already available in the `ADDR` payload.

Duplicating information bloats files and introduces the potential for self-contradiction.
`ADR1`, `ADR2`, and `ADR3` should not be added to new files.
:::

#### `ADDRPLUS_STRUCTURE` :=

An extended address structure containing all relevant information for modern contact records, including physical and digital addresses.  
It is introduced to be able to describe addresses, especially on `TEMPLATE`'s, that are not addresses belonging to a person, but, for example, to the institution that issued the `TEMPLATE` itself.

```gedstruct
n ADDRPLUS <Text>                          {1:1}
  +1 <<ADDRESS_STRUCTURE>>                 {0:1}
  +1 PHON <Special>                        {0:M}  g7:PHON
    +2 TITL <Text>                         {1:1}  g7:TITL
  +1 EMAIL <Special>                       {0:M}  g7:EMAIL
    +2 TITL <Text>                         {1:1}  g7:TITL
  +1 FAX <Special>                         {0:M}  g7:FAX
    +2 TITL <Text>                         {1:1}  g7:TITL
  +1 WWW <Special>                         {0:M}  g7:WWW
    +2 TITL <Text>                         {1:1}  g7:TITL
  +1 AGNC <Text>                           {0:1}  g7:AGNC
  +1 NOTE_STRUCTURE                        {0:M}  g8:NOTE
  ```

- The top-level `ADDRPLUS` payload provides a description of what the contact block represents — for example:  
“Contact information of: Genetic Information Research Institute (GIRI)”.
- `PHON`, `EMAIL`, `FAX`, and `WWW` follow GEDCOM 7 usage and formatting.
- `TITL` provides a descriptive label for the contact item, such as a person, role, or institution name.
- There needs to be at least 1 correct line of contact information present in this structure!

:::example  
Example: Contact information with titles per entry

```gedcom
1 ADDRPLUS Contact information of: Genetic Information Research Institute (GIRI)
2 ADDR 2020 Alameda de las Pulgas
3 CITY San Mateo
3 STAE CA
3 POST 94403
3 CTRY USA
2 PHON +1-650-212-2220
3 TITL Main research line
2 PHON +1-650-212-2221
3 TITL Fax line for document intake
2 EMAIL contact@girinst.org
3 TITL General correspondence
2 EMAIL submissions@girinst.org
3 TITL Sequence data submission desk
2 WWW https://www.girinst.org
3 TITL Official research website
2 AGNC GIRI – Public communications desk
```
:::

#### `ARRAY_STRUCTURE` :=

```gedstruct
n ARRAY                                    {1:1}  g8:ARRAY
  +1 CONT <ArrayValue>                     {1:M}  g8:type-Array2col
```

The `ARRAY_STRUCTURE` element is used to encode a structured sequence of related data points — typically pairs like marker and allele values for DNA — in a list format. 

It is designed to support structured genetic data such as DNA segment or marker match tables in a way that is both human-readable and machine-parseable. 

In GEDCOM 8, `ARRAY_STRUCTURE` uses the `TupleList` data type, where each entry is stored as a tuple on its own `CONT` line. It allows the data to be embedded directly in the record while retaining strict formatting requirements.

> ⚠️ The first line with the tag `ARRAY` **may include a GEDCOM comment** to clarify the array content.  
> However, **no inline comments are permitted inside `CONT` lines** — they must strictly conform to the `TupleList` format.

:::example  
```gedcom
1 ARRAY                       /* Example of DNA test output in tuples */
2 CONT (rs123456, A)
2 CONT (rs234567, T)
2 CONT (rs345678, G)
2 CONT (rs456789, C)
2 CONT (rs567890, T)
2 CONT (rs987654, G)
2 CONT (rs999020, T)
```  
:::


#### `ASSOCIATION_STRUCTURE` :=

```gedstruct
n ASSO @<XREF:INDI>@                       {1:1}  g7:ASSO
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
  +1 ROLE <Enum>                           {1:1}  g7:ROLE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {1:M}
```

An individual associated with the subject of the superstructure.
The nature of the association is indicated in the `ROLE` substructure.

A `voidPtr` and `PHRASE` can be used to describe associations to people not referenced by any `INDI` record.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- The `ASSOCIATION_STRUCTURE` is now no longer needed in GEDCOM 8. All associations are now represented by `ROLE`s in the `STICKY`'s  that belong to a `TEMPLATE`.


:::example
The following indicates that "Mr Stockdale" was the individual's teacher
and that individual `@I2@` was the clergy officiating at their baptism.

```gedcom
0 @I1@ INDI
1 ASSO @VOID@
2 PHRASE Mr Stockdale
2 ROLE OTHER
3 PHRASE Teacher
1 BAPM
2 DATE 1930
2 ASSO @I2@
3 ROLE CLERGY
```
:::

#### `CITA_STRUCTURE` :=

```gedstruct
n CITA                                     {1:1}  g8:CITA
  +1 SOUR @<XREF:SOUR>@                    {1:1}  g7:SOUR
  +1 PAGE <Text>                           {0:1}  g7:PAGE
  +1 DATA                                  {0:1}  g7:SOUR-DATA
    +2 <<DATE_VALUE>>                      {0:1}
    +2 TEXT <Text>                         {0:M}  g7:TEXT
      +3 MIME <MediaType>                  {0:1}  g7:MIME
      +3 LANG <Language>                   {0:1}  g7:LANG
  +1 AUTHOR <Text>                         {0:1}
  +1 TITL <Text>                           {0:1}
  +1 DATES                                 {0:1}
    +2 CREATED <DateValue>                 {0:1}
    +2 PUBLISHED <DateValue>               {0:1}
    +2 ACCESSED <DateValue>                {0:1}
    +2 RECORDED <DateValue>                {0:1}
  +1 REPOSITORY <Text>                     {0:1}
  +1 TEXTDISPLAY <Text>                    {0:1}
  +1 TRANSCRIPT <Text>                     {0:1}
  +1 FORMAT                                {0:1}
    +2 TYPE <MediaType>                    {1:1}
  +1 URL <Url>                             {0:1}
  +1 LANGUAGE <Language>                   {0:1}
  +1 RECORDID <Text>                       {0:1}
  +1 VOLUME <Text>                         {0:1}
  +1 CHAPTER <Text>                        {0:1}
  +1 SUBCHAPTER <Text>                     {0:1}
  +1 ITEMTYPE <Enum>                       {0:1}
  +1 CONTAINER <Text>                      {0:1}
  +1 SHORTTITLE <Text>                     {0:1}
  +1 WWWLINK <Special>                     {0:M} g7:WWW
    +2 VALUE <Url>                         {1:1}
  +1 QUAY <Enum>                           {0:1}  g7:QUAY
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

This structure is only used *inside* the `TEMPLATE` but is taken out for clarity.  
It is a replacement for the `SOURCE_CITATION` and contains all tags that went in there, **except the tag `EVEN`** and its underlying tags.  
As the information in that `EVEN` tag is taken over by the whole `TEMPLATE` itself.  

> The definition and tags might change as the current **GEDCOM Source Citation Committee** is also working on changes for Citation Structures. **But until then, these are the proposed tags**.  

This structure indicates that the pointed-to source record supports the claims made in the superstructure (`TEMPLATE`). Substructures provide additional information about how that source applies to the subject of the citation’s superstructure.  
Every `CITA_STRUCTURE` **must point to a `SOURCE_RECORD`**. No `voidPtr` is allowed.

Non-mentioned tags have the same meaning as in GEDCOM 7.  

- `SOUR`, a pointer to the formal `@SOUR@` record containing general source metadata. Required. Same as `SOUR` in GEDCOM 7.
  - Examples:
  - if `SOUR` itself is a churchbook containing all Marriages over a certain period of time in a certain church in a certain place. In that case the `CITA` record points to and describes only 1 of the marriages as further described in this `TEMPLATE`.

- `PAGE`, `g7:PAGE`, specific location in the source being cited (e.g., page number, folio, volume entry). Equivalent to `PAGES` in Zotero, and `RECORDDETAIL` in EE. `PAGE` can have comma-separated parts like:<br> `PAGE Film: 1234567, Frame: 344, Line: 28`<br>  (See with **Structure Types**)

- `DATA`, a substructure holding extracted or quoted information from the cited source.  
  This block reflects the *relevant portion* of the source record, often a snippet, sentence, or transcription tied to the citation.  
  Mirrors `g7:SOUR-DATA`.  
  Common in platforms that attach literal source content.  
  Not to be confused with `TRANSCRIPT`, which is often a full verbatim copy.  

  - `TEXT`, the actual content or snippet from the source being cited.  
  May be a direct quote, a paraphrase, or other extracted content.  
  Corresponds to `g7:TEXT`.  
  Multiple `TEXT` lines may be used for multi-part or multi-language citations.  

    - `MIME`, the `<MediaType>` of the specific `TEXT` content.  
  Indicates the format of the quoted or extracted material, such as `text/plain`, `text/html`, or `application/pdf`.  
  Corresponds to `g7:MIME`.  
  Useful in distinguishing machine-readable data from narrative.  

    - `LANG`, the language of the associated `TEXT` block.  
  Uses standard language codes (e.g., `en`, `de`, `nl`).  
  Corresponds to `g7:LANG`.  
  Enables multi-language citations, each with proper attribution.  

- `AUTHOR`, the creator of the content being cited — person, church, agency, or organization. Known as `CREATOR` in Zotero and CSL, and `AUTHOR` in EE/CMOS.

- `TITL`, the full title of the work or document (e.g., book name, registry volume, article). Called `TITLE` in EE, Zotero, CSL, and GEDCOM.

- `DATES`, container for date-related metadata about the source.

  - `CREATED`, date the source was originally written or generated. Matches `DATE` in EE, `CREATION DATE` in citation managers.

  - `PUBLISHED`, when the source was made public or officially distributed. Used by Zotero, CSL, EE.

  - `ACCESSED`, when the researcher accessed or retrieved the source. Matches `ACCESSDATE` in Zotero and `ACCESSED` in CMOS.

  - `RECORDED`, date the entry was logged into the source (e.g., baptism entered into a parish register). Not widely used outside GEDCOM contexts.

- `REPOSITORY`, the archive, website, or institution holding the source. Matches `ARCHIVE` in Zotero, `REPO` in GEDCOM, and `REPOSITORY` in EE.

- `TEXTDISPLAY`, a formatted citation string suitable for output, display, or printing. Equivalent to `CITATIONTEXT` in EE, and `VALUE` in GEDCOM-X citations.

- `TRANSCRIPT`, exact 1:1 copy of the text as it appears in the source. Equivalent to `TEXT` in GEDCOM, `QUOTE` in Zotero, and `TRANSCRIPT` in Gramps.

- `FORMAT`, container for media-type information about the cited source.

  - `TYPE`, the file/media format (e.g., `text/plain`, `image/jpeg`). Equivalent to `FORM` in GEDCOM 7.

- `URL`, the direct link to a web-hosted version of the source, if available. Equivalent to `URL` in GEDCOM-X and Zotero.

- `LANGUAGE`, the language code of the source content (`en`, `nl`, `fr`, etc.). In Zotero this field is called `language` (lowercase).

- `RECORDID`, an external or archival ID for the item, used by systems like FamilySearch, Ancestry, and in Family Historian exports.

- `VOLUME`, the volume number or title within a multi-volume work or record group. Equivalent to `VOLUME` in Zotero and `RECORDDETAIL` in EE.

- `CHAPTER`, a major subdivision within a source (e.g., book chapter, registry section). Not always used in citation managers, but valid structurally.

- `SUBCHAPTER`, an optional subdivision within a `CHAPTER`. For deep-structured sources like law books, archives, or nested records.

- `ITEMTYPE`, a controlled classification for the source (e.g., `Book`, `Letter`, `Church Register`). Matches `ITEMTYPE` in Zotero and `TYPE` in GEDCOM-X.

- `CONTAINER`, the name of the larger holding work (e.g., journal title, series name). Equivalent to `PUBLICATIONTITLE` in Zotero, `CONTAINER-TITLE` in CSL.

- `SHORTTITLE`, abbreviated title used internally or in compact lists. Matches `SHORTTITLE` in Zotero.

- `WWWLINK`, a pointer to a specific web-hosted version or instance of the cited source.  
  Used when the same source exists in multiple hosted locations (e.g., FamilySearch, Ancestry, Archive.org).  
  Not the same as `URL`, which is a general field; `WWWLINK` allows for multiple variants.  
  Each `WWWLINK` must contain a `VALUE` line holding a valid URL.  
  - `VALUE`, the actual URL link to that external record.

- `QUAY`, a quality estimate for the certainty and reliability of the cited source, from the perspective of the compiler.  
  Inherited from GEDCOM 7 (p.83).  
  Values range from 0 (unreliable) to 3 (highly reliable).  
  This value does not reflect the credibility of the event itself, only the strength of the citation.  

- `<<MULTIMEDIA_LINK>>`, pointer to scanned images or supporting documents. Same mechanism as GEDCOM 7.

- `<<NOTE_STRUCTURE>>`, optional notes about this citation. For comments that don’t belong in structured fields.

#### `CHANGE_DATE` :=

```gedstruct
n CHAN                                     {1:1}  g7:CHAN
  +1 DATE <DateExact>                      {1:1}  g7:DATE-exact
     +2 TIME <Time>                        {0:1}  g7:TIME
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

The date of the most recent modification of the superstructure, optionally with notes about that modification.

The `NOTE` substructure may describe previous changes as well as the most recent, although only the most recent change is described by the `DATE` substructure.

#### `CREATION_DATE` :=

```gedstruct
n CREA                                     {1:1}  g7:CREA
  +1 DATE <DateExact>                      {1:1}  g7:DATE-exact
     +2 TIME <Time>                        {0:1}  g7:TIME
```

The date of the initial creation of the superstructure.
Because this refers to the initial creation, it should not be modified after the structure is created.

#### `DATE_VALUE` :=

```gedstruct
n DATE <DateValue>                         {1:1}  g7:DATE
  +1 TIME <Time>                           {0:1}  g7:TIME
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
```

A date, optionally with a time and/or a phrase.
If there is a `TIME`, it asserts that the event happened at a specific time on a single day.
`TIME` should not be used with `DatePeriod` but may be used with other date types.

:::note
There is currently no provision for approximate times or time phrases.
Time phrases are expected to be added in version 7.1.
:::

#### `EVENT_DETAIL` :=

```gedstruct
n <<DATE_VALUE>>                           {0:1}
n <<PLACE_STRUCTURE>>                      {0:1}
n <<ADDRESS_STRUCTURE>>                    {0:1}
n PHON <Special>                           {0:M}  g7:PHON
n EMAIL <Special>                          {0:M}  g7:EMAIL
n FAX <Special>                            {0:M}  g7:FAX
n WWW <Special>                            {0:M}  g7:WWW
n AGNC <Text>                              {0:1}  g7:AGNC
n RELI <Text>                              {0:1}  g7:RELI
n CAUS <Text>                              {0:1}  g7:CAUS
n RESN <List:Enum>                         {0:1}  g7:RESN
n SDATE <DateValue>                        {0:1}  g7:SDATE
  +1 TIME <Time>                           {0:1}  g7:TIME
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
n <<NOTE_STRUCTURE>>                       {0:M}
n QUAY <Enum>                              {0:1}  g7:QUAY
n GEDC                                     {0:1}  g8:GEDC
  +1 VERS <Special>                        {1:1}  g8:GEDC-VERS
    +2 <<SOURCE_CITATION>>                 {1:M}
    +2 <<ASSOCIATION_STRUCTURE>>           {0:M}
n <<MULTIMEDIA_LINK>>                      {0:M}
n UID <Special>                            {0:M}  g7:UID
```

Substructures that may be shared by most individual and family events and attributes.

Note that many of these substructures are limited to 1 per event.
Conflicting event information should be represented by placing them in separate event structures (with appropriate source citations) rather than by placing them under the same enclosing event.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- `SOURCE_CITATION` and the `ASSOCIATION_STRUCTURE` are now *behind* the same GEDCOM version tag as in the Header.  
>Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` or the `ASSOCIATION_STRUCTURE` are allowed at this place.   
>    - This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and all `ROLE`s and everything that belongs to it. (inside the `STICKY`s)  
>    - Because of that **it is no longer allowed** for any of these 4 structures to point to a `SOURCE_CITATION` **from enywhere** inside the structure itself!
>- `QUAY` is added to have a possibility to define the credibility of each event.  
>- ✨ When this PR will be implemented, **it is possible another method will be chosen** to make sure `SOURCE_CITATION`  and `ASSOCIATION_STRUCTURE` can no longer be used as they were in GEDCOM 7 !


#### `FAMILY_ATTRIBUTE_STRUCTURE` :=

```gedstruct
[
n NCHI <Integer>                           {1:1}  g7:FAM-NCHI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n RESI <Text>                              {1:1}  g7:FAM-RESI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n FACT <Text>                              {1:1}  g7:FAM-FACT
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
]
```

Family attributes; see [Family Attributes](#family-attributes) for descriptions of each family attribute type.

:::note
Family attribute structures vary as follows:

- `FAM`.`NCHI` has an [Integer](#integer) payload; others have [Text](#text) payloads
- `FAM`.`FACT` requires `TYPE`; it's optional for others
:::


#### `FAMILY_EVENT_DETAIL` :=

```gedstruct
n HUSB                                     {0:1}  g7:HUSB
  +1 AGE <Age>                             {1:1}  g7:AGE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
n WIFE                                     {0:1}  g7:WIFE
  +1 AGE <Age>                             {1:1}  g7:AGE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
n <<EVENT_DETAIL>>                         {0:1}
```

Substructures shared by most family events and attributes.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

> **Important**
>- In GEDCOM 8 the `FAMILY_EVENT_DETAIL` is no longer allowed to have the `HUSB` and/or `WIFE` tags, just the `<<EVENT_DETAIL>>`.  


#### `FAMILY_EVENT_STRUCTURE` :=

```` {.gedstruct .long}
[
n ANUL [Y|<NULL>]                          {1:1}  g7:ANUL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n CENS [Y|<NULL>]                          {1:1}  g7:FAM-CENS
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n DIV [Y|<NULL>]                           {1:1}  g7:DIV
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n DIVF [Y|<NULL>]                          {1:1}  g7:DIVF
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n ENGA [Y|<NULL>]                          {1:1}  g7:ENGA
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARB [Y|<NULL>]                          {1:1}  g7:MARB
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARC [Y|<NULL>]                          {1:1}  g7:MARC
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARL [Y|<NULL>]                          {1:1}  g7:MARL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARR [Y|<NULL>]                          {1:1}  g7:MARR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARS [Y|<NULL>]                          {1:1}  g7:MARS
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n EVEN <Text>                              {1:1}  g7:FAM-EVEN
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
]
````

Family events; see [Family Events](#family-events) for descriptions of each family event type.

An event structure may be used to discuss an event even if the event is not known to have occurred.
See [Events] for a discussion of how `DATE`, `PLAC`, and the optional `Y` payload indicate whether the structure is asserting the event occurred.
See the `NON_EVENT_STRUCTURE` for how to state an event did not occur.

:::note
Family event structures vary as follows:

- `FAM`.`EVEN` has a [Text](#text) payload; others may have a `Y` payload
- `FAM`.`EVEN` requires `TYPE`; it's optional for others
:::

#### `FLEX_STRUCTURE` :=

```gedstruct
n FLEX <Text>                         {1:1}  g8:FLEX
  +1 TYPE <Text>                      {1:M}  g8:FLEX-TYPE
  +1 PHRASE <Text>                  {1:1}  g8:PHRASE
    +2 LANG <Language>              {0:1}  g7:LANG
  +1 CONTENTS <Text>                  {1:1}  g8:CONTENTS
  +1 RESN <List:Enum>                 {0:1}  g8:RESN
  +1 <<NOTE_STRUCTURE>>               {0:1}
```

A `FLEX` structure allows flexible encoding of additional typed values within records, that are specific to a document, template, or local practice. It supports structured value recording even when the type is not part of standard GEDCOM fields.

- `FLEX` can only be used inside `TEMPLATE`, `STICKY`, `ASSET`, `PROOF` or `GROUP`. 

It consists of a `FLEX` tag followed by one or more subordinate lines that define its meaning.

By using `FLEX`, a lot of the maybe dozens and more widespread `_SILLYTAG`'s, can be changed into user readable information, while the software processing it, can deal with it, without having to know the real meaning, or its definition or otherwise. If a `FLEX` later will have to be replaced by an offcial GEDCOM tag, because that `FLEX` is so widespread and often used, it deserves its own tag, its likely that software can do that, without much user assistance. (By comparing the `PHRASE` of the FLEX, with the `_SILLYTAG`'s tagname.)

- The `TYPE` line declares one or more types describing the structure of the `CONTENTS`. If multiple types are given, they must be separated by a comma and a space. The `TYPE`'s appear on the same line as `FLEX`, separated from `FLEX` by 1 space.
- The `CONTENTS` line contains the value, matching the declared `TYPE`. In certain case this line can be followed by `2 CONT some text`, in case the `FLEX` type is a `NOTE`-type enum.
- The `PHRASE` line must be present and must **exactly match** the label of the field on the original document or template. This ensures that software can display or print human-readable information even if it does not interpret the `TYPE` or `CONTENTS`. The `PHRASE` line appears directly after the `CONTENTS`line.

 - `LANG`, defines the language of the `PHRASE`.
- `NOTE` can be used for special remarks about this specific `FLEX`.
- `RESN`, with this the user can decide if the information of this `FLEX` should be presented in the outputs.

##### Rules:

- `TYPE` values must be valid entries from the `FLEX-TYPE` enumeration. For readability they must be put directly behind the `FLEX`tag, separated from it by 1 space, like this: `FLEX DECIMAL, CURR, USD`. So the `TYPE`tag itself does not show. And, for instance with `CURR`, the chosen currency value itself, also goes on that same line. Same for `UNIT`.
- The only allowed combination of `TYPE`s as for now is with `CURR` or `UNIT` behind `AMOUNT`, `DECIMAL`, or `INTEGER`.
- Parsers must treat the contents as an ordered list.
- Use of `TEXT` as a `TYPE` is allowed only if no more precise type is applicable. For instance, do **not** use `TEXT` to represent `"1944-06-06"` or `"12500.00"`; use `DATE` and `DECIMAL`, respectively.
- The `PHRASE` must reflect the **exact label used on the source document** to help users recognize the field's meaning.
  - **This allows software to:**
    - display fields using user-recognizable labels,
    - disambiguate similar fields (e.g., two different monetary amounts),
    - and support output of human-readable versions even without interpreting the underlying `TYPE`/`CONTENTS`.

$\color{Coral}\large{\textbf{Important! GEDCOM 8 changes:}}$


>**In this PR `FLEX` has been given a restriction:**
>- It can only be used inside `TEMPLATE`, `STICKY`, `ASSET`, or `GROUP`.  
>This way it does not interfere with current GEDCOM7.  

>**If this PR would be accepted, it is always possible to extend the use of `FLEX` to other places in GEDCOM.**


##### Example 1: Single typed value

```gedstruct
1 FLEX DATE
2 PHRASE "Date of Transfer"
2 CONTENTS 1944-06-06
```
In this case "Date of Transfer" does NOT have its own GEDCOM tag, so a `FLEX` is used instead.

##### Example 2: Combined typed value (decimal amount with currency)

```gedstruct
1 FLEX DECIMAL, CURR, USD
2 PHRASE "Property Value."
2 CONTENTS 12500.00
2 NOTE "Transferred to widow"
```
Value of the property on a will.

##### Example 3: Typed field in a STICKY from an inheritance template

```gedstruct
0 @ST0043@ STICKY
1 TYPE FINANCE, ACCOUNTS "Inheritance Share: Savings Account at Miami Credit Union"
2 PHRASE "Savings Account at Miami Credit Union"
1 ROLE ASSET
1 FLEX DECIMAL, CURR, USD
2 PHRASE "Savings"            /* Text as on the original certificat */
2 CONTENTS 12500.00
1 NOTE "Savings inherited by Anna Harrison from George Harrison."
```

#### `IDENTIFIER_STRUCTURE` :=

```gedstruct
[
n REFN <Special>                           {1:1}  g7:REFN
  +1 TYPE <Text>                           {0:1}  g7:TYPE
|
n UID <Special>                            {1:1}  g7:UID
|
n EXID <Special>                           {1:1}  g7:EXID
  +1 TYPE <Special>                        {0:1}  g7:EXID-TYPE
]
```

:::deprecation
Having an `EXID` without an `EXID`.`TYPE` substructure is deprecated.
The meaning of an `EXID` depends on its `EXID`.`TYPE`.
The cardinality of `EXID`.`TYPE` will be changed to `{1:1}` in version 8.0.
:::

Each of these provides an identifier for a structure or its subject,
and each is different in purpose:

- `REFN` is a user-generated identifier for a structure.

- `UID` is a globally-unique identifier for a structure.

- `EXID` is an identifier maintained by an external authority that applies to the subject of the structure.


#### `INDIVIDUAL_ATTRIBUTE_STRUCTURE` :=

```` {.gedstruct .long}
[
n CAST <Text>                              {1:1}  g7:CAST
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n DSCR <Text>                              {1:1}  g7:DSCR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n EDUC <Text>                              {1:1}  g7:EDUC
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n IDNO <Special>                           {1:1}  g7:IDNO
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NATI <Text>                              {1:1}  g7:NATI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NCHI <Integer>                           {1:1}  g7:INDI-NCHI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NMR <Integer>                            {1:1}  g7:NMR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n OCCU <Text>                              {1:1}  g7:OCCU
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n PROP <Text>                              {1:1}  g7:PROP
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n RELI <Text>                              {1:1}  g7:INDI-RELI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n RESI <Text>                              {1:1}  g7:INDI-RESI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n SSN <Special>                            {1:1}  g7:SSN
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n TITL <Text>                              {1:1}  g7:INDI-TITL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n FACT <Text>                              {1:1}  g7:INDI-FACT
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
]
````

Individual attributes; see [Individual Attributes](#individual-attributes) for descriptions of each individual attribute type..

:::note
Individual attribute structures vary as follows:

- `INDI`.`NCHI` and `NMR` have [Integer](#text) payloads; `IDNO` and `SSN` have [Special](#special) payloads; others have [Text](#text) payloads
- `INDI`.`FACT` and `IDNO` require `TYPE`; it's optional for others
:::

#### `INDIVIDUAL_EVENT_DETAIL` :=

```gedstruct
n <<EVENT_DETAIL>>                         {1:1}
n AGE <Age>                                {0:1}  g7:AGE
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
```

Substructures shared by most individual events and attributes.

#### `INDIVIDUAL_EVENT_STRUCTURE` :=

```` {.gedstruct .long}
[
n ADOP [Y|<NULL>]                          {1:1}  g7:ADOP
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:ADOP-FAMC
     +2 ADOP <Enum>                        {0:1}  g7:FAMC-ADOP
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
|
n BAPM [Y|<NULL>]                          {1:1}  g7:BAPM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BARM [Y|<NULL>]                          {1:1}  g7:BARM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BASM [Y|<NULL>]                          {1:1}  g7:BASM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BIRT [Y|<NULL>]                          {1:1}  g7:BIRT
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:FAMC
|
n BLES [Y|<NULL>]                          {1:1}  g7:BLES
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n BURI [Y|<NULL>]                          {1:1}  g7:BURI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CENS [Y|<NULL>]                          {1:1}  g7:INDI-CENS
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CHR [Y|<NULL>]                           {1:1}  g7:CHR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:FAMC
|
n CHRA [Y|<NULL>]                          {1:1}  g7:CHRA
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CONF [Y|<NULL>]                          {1:1}  g7:CONF
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n CREM [Y|<NULL>]                          {1:1}  g7:CREM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n DEAT [Y|<NULL>]                          {1:1}  g7:DEAT
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n EMIG [Y|<NULL>]                          {1:1}  g7:EMIG
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n FCOM [Y|<NULL>]                          {1:1}  g7:FCOM
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n GRAD [Y|<NULL>]                          {1:1}  g7:GRAD
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n IMMI [Y|<NULL>]                          {1:1}  g7:IMMI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n NATU [Y|<NULL>]                          {1:1}  g7:NATU
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n ORDN [Y|<NULL>]                          {1:1}  g7:ORDN
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n PROB [Y|<NULL>]                          {1:1}  g7:PROB
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n RETI [Y|<NULL>]                          {1:1}  g7:RETI
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n WILL [Y|<NULL>]                          {1:1}  g7:WILL
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
|
n EVEN <Text>                              {1:1}  g7:INDI-EVEN
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
]
````

Individual events; see [Individual Events](#individual-events) for descriptions of each individual event type.

An event structure may be used to discuss an event even if the event is not known to have occurred.
See [Events] for a discussion of how `DATE`, `PLAC`, and the optional `Y` payload indicate whether the structure is asserting the event occurred.
See the `NON_EVENT_STRUCTURE` for how to state an event did not occur.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>**Important**
>- `CHRC`, `BIRT` and `ADOP` in GEDCOM 8, are no longer allowed to have a `FAMC` link.



:::note
Individual event structures vary as follows:

- `INDI`.`EVEN` has a [Text](#text) payload; others may have a `Y` payload
- `INDI`.`EVEN` requires `TYPE`; it's optional for others
- `BIRT` and `CHR` may have a `FAMC` with no substructures; `ADOP` may have a `FAMC` with an optional `ADOP` substructure; others may not have a `FAMC` substructure
:::



#### `LDS_INDIVIDUAL_ORDINANCE` :=

```gedstruct
[
n BAPL                                     {1:1}  g7:BAPL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n CONL                                     {1:1}  g7:CONL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n ENDL                                     {1:1}  g7:ENDL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n INIL                                     {1:1}  g7:INIL
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
|
n SLGC                                     {1:1}  g7:SLGC
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
  +1 FAMC @<XREF:FAM>@                     {1:1}  g7:FAMC
]
```

Ordinances performed by members of The Church of Jesus Christ of Latter-day Saints; see [Latter-day Saint Ordinances] for descriptions of each ordinance type.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>**Important**
> - In GEDCOM 8 `SLGC` no longer has a `FAMC` link.


#### `LDS_ORDINANCE_DETAIL` :=

```gedstruct
n <<DATE_VALUE>>                         {0:1}
n TEMP <Text>                            {0:1}  g7:TEMP
n <<PLACE_STRUCTURE>>                    {0:1}
n STAT <Enum>                            {0:1}  g7:ord-STAT
  +1 DATE <DateExact>                    {1:1}  g7:DATE-exact
     +2 TIME <Time>                      {0:1}  g7:TIME
n <<NOTE_STRUCTURE>>                     {0:M}
  +1 GEDC                                {0:1}  g8:GEDC
    +2 VERS <Special>                    {1:1}  g8:GEDC-VERS
      +3 <<SOURCE_CITATION>>             {1:M}
```

Dates for these ordinances should be in the default (`GREGORIAN`) calendar and be 1830 or later.
These ordinances can be performed posthumously by proxy, and the date may reflect that posthumous date.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- `SOURCE_CITATION` is now *behind* the same GEDCOM version tag as in the Header.  
Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` is allowed at this place.   
This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and everything that belongs to it. (inside the `STICKY`s)  


#### `LDS_SPOUSE_SEALING` :=

```gedstruct
n SLGS                                     {1:1}  g7:SLGS
  +1 <<LDS_ORDINANCE_DETAIL>>              {0:1}
```

Ordinances performed by members of The Church of Jesus Christ of Latter-day Saints; see [Latter-day Saint Ordinances] for descriptions of each ordinance type.

#### `MULTIMEDIA_LINK` :=
```gedstruct
n OBJE @<XREF:OBJE>@                       {1:1}  g7:OBJE
  +1 CROP                                  {0:1}  g7:CROP
     +2 TOP <Integer>                      {0:1}  g7:TOP
     +2 LEFT <Integer>                     {0:1}  g7:LEFT
     +2 HEIGHT <Integer>                   {0:1}  g7:HEIGHT
     +2 WIDTH <Integer>                    {0:1}  g7:WIDTH
  +1 TITL <Text>                           {0:1}  g7:TITL
```

Links the superstructure to the `MULTIMEDIA_RECORD` with the given pointer.

The optional `CROP` substructure indicates that a subregion of an image represents or applies to the superstructure.

The optional `TITL` substructure supersedes any `OBJE.FILE.TITL` substructures included in the `MULTIMEDIA_RECORD`.

#### `NON_EVENT_STRUCTURE` :=

```gedstruct
n NO <Enum>                                {1:1}  g7:NO
  +1 DATE <DatePeriod>                     {0:1}  g7:NO-DATE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 GEDC                                  {0:1}  g8:GEDC
    +2 VERS <Special>                      {1:1}  g8:GEDC-VERS
      +3 <<SOURCE_CITATION>>               {1:M}
```

Indicates that a specific type of event, given in the payload, did not happen within a given date period
(or never happened if there is no `DATE` substructure).

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- `SOURCE_CITATION` is now *behind* the same GEDCOM version tag as in the Header.  
Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` is allowed at this place.   
This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and everything that belongs to it. (inside the `STICKY`s)  


Substructures may provide discussion about the non-occurrence of the event
but must not limit the meaning of what did not occur.
No substructure other than `DATE` may restrict the breadth of that negative assertion.

:::example
`1 NO MARR`{.gedcom} means "no marriage occurred"
:::

:::example
```gedcom
1 NO MARR
2 DATE TO 24 MAR 1880
```
means "no marriage had occurred as of March 24^th^, 1880"
:::

#### `NOTE_STRUCTURE` :=

```gedstruct
[
n NOTE <Text>                              {1:1}  g7:NOTE
  +1 MIME <MediaType>                      {0:1}  g7:MIME
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TRAN <Text>                           {0:M}  g7:NOTE-TRAN
     +2 MIME <MediaType>                   {0:1}  g7:MIME
     +2 LANG <Language>                    {0:1}  g7:LANG
  +1 GEDC                                  {0:1}  g8:GEDC
    +2 VERS <Special>                      {1:1}  g8:GEDC-VERS
      +3 <<SOURCE_CITATION>>               {1:M}
|
n SNOTE @<XREF:SNOTE>@                     {1:1}  g7:SNOTE
]
```

A catch-all location for information that does not fully fit within other structures.
It may include research notes, additional context, alternative interpretations, reasoning, and so forth.

Each `NOTE`.`TRAN` must have either a `MIME` or `LANG` substructure, and may have both.

See `SHARED_NOTE_RECORD` for advice on choosing between `NOTE` and `SNOTE`.

A `NOTE_STRUCTURE` can contain a `SOURCE_CITATION`, which in turn can contain a `NOTE_STRUCTURE`, allowing potentially unbounded nesting of structures. Because each dataset is finite, this nesting is also guaranteed to be finite.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- `SOURCE_CITATION` is now *behind* the same GEDCOM version tag as in the Header.  
Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` is allowed at this place.   
This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and everything that belongs to it. (inside the `STICKY`s)  



#### `PERSONAL_NAME_PIECES` :=

```gedstruct
n NPFX <Text>                              {0:M}  g7:NPFX
n GIVN <Text>                              {0:M}  g7:GIVN
n NICK <Text>                              {0:M}  g7:NICK
n SPFX <Text>                              {0:M}  g7:SPFX
n SURN <Text>                              {0:M}  g7:SURN
n NSFX <Text>                              {0:M}  g7:NSFX
```

Optional isolated name parts; see `PERSONAL_NAME_STRUCTURE` for more details.

:::example
"Lt. Cmndr. Joseph Allen jr.” might be presented as

```gedcom
1 NAME Lt. Cmndr. Joseph /Allen/ jr.
2 NPFX Lt. Cmndr.
2 GIVN Joseph
2 SURN Allen
2 NSFX jr.
```
:::

This specification does not define how the meaning of multiple parts with the same tag differs from the meaning of a single part with a concatenated larger payload.
However, some applications allow the user to chose whether to combine or split name parts, meaning the tag quantity should be treated as expressing at least a user preference.
Even when multiple `SURN` tags are used, the `PersonalName` data type identifies a single surname substring between its slashes.

#### `PERSONAL_NAME_STRUCTURE` :=

```gedstruct
n NAME <PersonalName>                      {1:1}  g7:INDI-NAME
  +1 TYPE <Enum>                           {0:1}  g7:NAME-TYPE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<PERSONAL_NAME_PIECES>>              {0:1}
  +1 TRAN <PersonalName>                   {0:M}  g7:NAME-TRAN
     +2 LANG <Language>                    {1:1}  g7:LANG
     +2 <<PERSONAL_NAME_PIECES>>           {0:1}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 GEDC                                  {0:1}  g8:GEDC
    +2 VERS <Special>                      {1:1}  g8:GEDC-VERS
      +3 <<SOURCE_CITATION>>               {1:M}
```

Names of individuals are represented in the manner the name is normally spoken, with the family name, surname, or nearest cultural parallel thereunto separated by slashes (U+002F `/`). Based on the dynamic nature or unknown compositions of naming conventions, it is difficult to provide a more detailed name piece structure to handle every case. The `PERSONAL_NAME_PIECES` are provided optionally for systems that cannot operate effectively with less structured information. The Personal Name payload shall be seen as the primary name representation, with name pieces as optional auxiliary information; in particular it is recommended that all name parts in `PERSONAL_NAME_PIECES` appear within the `PersonalName` payload in some form, possibly adjusted for gender-specific suffixes or the like.
It is permitted for the payload to contain information not present in any name piece substructure.

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>- `SOURCE_CITATION` is now *behind* the same GEDCOM version tag as in the Header.  
Only when the GEDCOM version of the file is a lower version than GEDCOM 8, a `SOURCE_CITATION` is allowed at this place.   
This is done because GEDCOM 8 uses a `TEMPLATE` to fully describe the `SOURCE_CITATION` and everything that belongs to it. (inside the `STICKY`s)  


The name may be translated or transliterated into different languages or scripts using the `TRAN` substructure.
It is recommended, but not required, that if the name pieces are used, the same pieces are used in each translation and transliteration.

A `TYPE` is used to specify the particular variation that this name is.
For example; it could indicate that this name is a name taken at immigration or that it could be an ‘also known as’ name.
See `g7:enumset-NAME-TYPE` for more details.

:::note
Alternative approaches to representing names are being considered for future versions of this specification.
:::

#### `PLACE_STRUCTURE` :=

```gedstruct
n PLAC <List:Text>                         {1:1}  g7:PLAC
  +1 FORM <List:Text>                      {0:1}  g7:PLAC-FORM
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TRAN <List:Text>                      {0:M}  g7:PLAC-TRAN
     +2 LANG <Language>                    {1:1}  g7:LANG
  +1 MAP                                   {0:1}  g7:MAP
     +2 LATI <Special>                     {1:1}  g7:LATI
     +2 LONG <Special>                     {1:1}  g7:LONG
  +1 EXID <Special>                        {0:M}  g7:EXID
     +2 TYPE <Special>                     {0:1}  g7:EXID-TYPE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

:::deprecation
Having an `EXID` without an `EXID`.`TYPE` substructure is deprecated.
The meaning of an `EXID` depends on its `EXID`.`TYPE`.
The cardinality of `EXID`.`TYPE` will be changed to `{1:1}` in version 8.0.
:::


A place, which can be represented in several ways:

- The payload contains a comma-separated list of region names,
    ordered from smallest to largest.
    The specific meaning of each element is given by the `FORM` substructure,
    or in the `HEAD`.`PLAC`.`FORM` if there is no `FORM` substructure.
    If neither `FORM` exists, the meaning of the elements are not defined in this specification beyond being names of jurisdictions of some kind, ordered from smallest to largest.

    Elements should be left blank if they are unknown, do not apply to the location, or are too specific for the region in question.

    <div class="example">
    A record describing births throughout Oneida county could be recorded as

    ````gedcom
    0 @S1@ SOUR
    1 DATA
    2 EVEN BIRT
    3 PLAC , Oneida, Idaho, USA
    4 FORM City, County, State, Country
    ````
    </div>

- The payload may be translated or transliterated into different languages or scripts using the `TRAN` substructure.
    It should use the same `FORM` as the payload.

- Global coordinates may be presented in the `MAP` substructure

:::note
This specification does not support places where a region name contains a comma. An alternative system for representing locations is likely to be added in a later version.
:::



#### `SOURCE_CITATION` :=

```gedstruct
n SOUR @<XREF:SOUR>@                       {1:1}  g7:SOUR
  +1 PAGE <Text>                           {0:1}  g7:PAGE
  +1 DATA                                  {0:1}  g7:SOUR-DATA
     +2 <<DATE_VALUE>>                     {0:1}
     +2 TEXT <Text>                        {0:M}  g7:TEXT
        +3 MIME <MediaType>                {0:1}  g7:MIME
        +3 LANG <Language>                 {0:1}  g7:LANG
  +1 EVEN <Enum>                           {0:1}  g7:SOUR-EVEN
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
     +2 ROLE <Enum>                        {0:1}  g7:ROLE
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
  +1 QUAY <Enum>                           {0:1}  g7:QUAY
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

$\color{Coral}\large{\textbf{GEDCOM 8 changes:}}$

>**IMPORTANT**
>  
> The `SOURCE_CITATION` in GEDCOM 8 is now "replaced" by the `CITA_STRUCTURE`, as in GEDCOM 8 everything from a document is now described in a `TEMPLATE`, of which the `CITA_STRUCTURE` is a part. So the important parts of the original `SOURCE_CITATION` are now in the `CITA_STRUCTURE`, and other parts, like the event, are now described in the `TEMPLATE` itself.  
> More information can be found with the `CITA_STRUCTURE` and the `TEMPLATE`.

A citation indicating that the pointed-to source record supports the claims made in the superstructure.
Substructures provide additional information about how that source applies to the subject of the citation's superstructure:

- `PAGE`: where in the source the relevant material can be found.
- `DATA`: the relevant data from the source.
- `EVEN`: what event the relevant material was recording.
- `QUAY`: an estimation of the reliability of the source in regard to these claims.
- `MULTIMEDIA_LINK`: digital copies of the cited part of the source

It is recommended that every `SOURCE_CITATION` point to a `SOURCE_RECORD`.
However, a `voidPtr` can be used with the citation text in a `PAGE` substructure.
The `PAGE` is defined to express a "specific location within the information referenced;"
with a `voidPtr` there is no information referenced, so the `PAGE` may describe the entire source.

A `SOURCE_CITATION` can contain a `NOTE_STRUCTURE`, which in turn can contain a `SOURCE_CITATION`, allowing potentially unbounded nesting of structures. Because each dataset is finite, this nesting is also guaranteed to be finite.


#### `SOURCE_REPOSITORY_CITATION` :=

```gedstruct
n REPO @<XREF:REPO>@                       {1:1}  g7:REPO
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 CALN <Special>                        {0:M}  g7:CALN
     +2 MEDI <Enum>                        {0:1}  g7:MEDI
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
```

This structure is used within a source record to point to a name and address record of the holder of the source document.
Formal and informal repository name and addresses are stored in the
`REPOSITORY_RECORD`.
More formal repositories, such as the Family History Library, should show a call number of the source at that repository.
The call number of that source should be recorded using a `CALN` substructure.

#### `TRANSFER_STRUCTURE` :=

A `TRANSFER_STRUCTURE` describes the transfer of a `STICKY`-record from an origin to a destination.
- The entity is pointing to an `ASSET STICKY` that "moves" from an original owner to a new owner, hence on a will, selling contract or otherwise. Example: a house that is given to an heir on a will, or a horse that is sold to a new owner via a purchase contract.
- a `TRANSFER` structure can only be used inside a `TEMPLATE` record.

```gedstruct
n TRANSFER @<XREF:STICKY>@                 {1:1}
  +1 GRANTOR @<XREF:STICKY>@               {1:1}  g8:STICKY
  +1 GRANTEE @<XREF:STICKY>@               {1:M}  g8:STICKY
    +2 SHARE <PercentLiteral>              {0:1}
  +1 <<NOTE_STRUCTURE>>                    {0:1}
```

- `TRANSFER`: the referenced `STICKY` is the `ASSET` that "moves" from 1 owner to another owner.
  - `GRANTOR`, must be a valid `pointer` to a person `STICKY`, who is the original owner of the asset in this `TRANSFER`. Grantor can be the deceased in a will, but also the seller or giver of something.
  - `GRANTEE` describes 1 or more person `STICKY`'s representing those who recieved (a share of) the `ASSET`.
  - all `pointers` in this `TRANSFER` structure must point to `STICKY`'s in the same `TEMPLATE` as the `TRANSFER` structure itself.
  - `SHARE`, the part of the `ASSET` as a percent value, that this `GRANTEE` recieves.



