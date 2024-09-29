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
n <<FAMILY_RECORD>>                        {1:1}
|
n <<INDIVIDUAL_RECORD>>                    {1:1}
|
n <<MULTIMEDIA_RECORD>>                    {1:1}
|
n <<REPOSITORY_RECORD>>                    {1:1}
|
n <<SHARED_NOTE_RECORD>>                   {1:1}
|
n <<SOURCE_RECORD>>                        {1:1}
|
n <<SPLAC_RECORD>>                         {1:1}
|
n <<SUBMITTER_RECORD>>                     {1:1}
]
```

#### `HEADER` :=

```gedstruct
n HEAD                                     {1:1}  g7:HEAD
  +1 GEDC                                  {1:1}  g7:GEDC
     +2 VERS <Special>                     {1:1}  g7:GEDC-VERS
  +1 SCHMA                                 {0:1}  g7:SCHMA
     +2 TAG <Special>                      {0:M}  g7:TAG
  +1 SOUR <Special>                        {0:1}  g7:HEAD-SOUR
     +2 VERS <Special>                     {0:1}  g7:VERS
     +2 NAME <Text>                        {0:1}  g7:NAME
     +2 CORP <Text>                        {0:1}  g7:CORP
        +3 <<ADDRESS_STRUCTURE>>           {0:1}
        +3 PHON <Special>                  {0:M}  g7:PHON
        +3 EMAIL <Special>                 {0:M}  g7:EMAIL
        +3 FAX <Special>                   {0:M}  g7:FAX
        +3 WWW <Special>                   {0:M}  g7:WWW
     +2 DATA <Text>                        {0:1}  g7:HEAD-SOUR-DATA
        +3 DATE <DateExact>                {0:1}  g7:DATE-exact
           +4 TIME <Time>                  {0:1}  g7:TIME
        +3 COPR <Text>                     {0:1}  g7:COPR
  +1 DEST <Special>                        {0:1}  g7:DEST
  +1 DATE <DateExact>                      {0:1}  g7:HEAD-DATE
     +2 TIME <Time>                        {0:1}  g7:TIME
  +1 SUBM @<XREF:SUBM>@                    {0:1}  g7:SUBM
  +1 COPR <Text>                           {0:1}  g7:COPR
  +1 LANG <Language>                       {0:1}  g7:HEAD-LANG
  +1 PLAC                                  {1:1}  g7:HEAD-PLAC
     +2 FORM <List:Text>                   {1:1}  g7:HEAD-PLAC-FORM
  +1 <<NOTE_STRUCTURE>>                    {0:1}
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

### New for 7.1: 
- `PLAC` now is {1:1} so obligatory.
- `FORM` now has `g7:HEAD-PLAC-FORM71` which is defined as follows:  
The `<List:Text> ` always consists of the following string of jurisdictions (smallest to largest:  
  **`LOCATION, ZIPCODE, VILLAGE, CITY, CODEINSEE, DISTRICT, PROVINCE, COUNTY, STATE, COUNTRY, SEA, EARTH`**  
  These are in fact the original jurisdictions from GEDCOM7 with a few added. With this list, older GEDCOM files can be converted, by comparing their `PLAC.FORM's` with this list.  
  When GEDCOM files have other jurisdictions, which they often have, the jurisdiction in this list, that comes closest has to be taken. After that it can be further subdivided into the jurisdiction found in the original file that is converted, by adding the **GOV** number as explained for the TAG `GOVTYP` in the `PERIOD_STRUCTURE`.  
  **See the examples for how this will look and has to be done** as it is possible to also add descriptive text, to make it more visible for users.

:::  
Example:
- In the original file the jurisdiction is "Kingdom", then the one coming closest is "COUNTRY", and we add the GOV number 31 to denote it is a kingdom.
- In the original file the jurisdiction is cemetary, then we use the general (smallest) `LOCATION` from the above list, and we add the GOV number 89 to make it a cemetary.  
:::  

### Records

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
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The `FAM` record was originally structured to represent families where a male `HUSB` (husband or father) and female `WIFE` (wife or mother) produce `CHIL` (children).
The `FAM` record may also be used for cultural parallels to this,
including nuclear families, marriage, cohabitation, fostering, adoption, and so on, regardless of the gender of the partners.
Sex, gender, titles, and roles of partners should not be inferred based on the partner that the `HUSB` or `WIFE` structure points to.

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
  +1 SUBM @<XREF:SUBM>@                    {0:M}  g7:SUBM
  +1 <<ASSOCIATION_STRUCTURE>>             {0:M}
  +1 ALIA @<XREF:INDI>@                    {0:M}  g7:ALIA
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 ANCI @<XREF:SUBM>@                    {0:M}  g7:ANCI
  +1 DESI @<XREF:SUBM>@                    {0:M}  g7:DESI
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<MULTIMEDIA_LINK>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The individual record is a compilation of facts or hypothesized facts about an individual.
These facts may come from multiple sources.
Source citations and notes allow documentation of the source where each of the facts were discovered.

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
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The multimedia record refers to 1 or more external digital files, and may provide some additional information about the files and the media they encode.

The file reference can occur more than once to group multiple files together. Grouped files should each pertain to the same context. For example, a sound clip and a photo both of the same event might be grouped in a single `OBJE`.

The change and creation dates should be for the `OBJE` record itself,
not the underlying files.



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
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
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
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<IDENTIFIER_STRUCTURE>>              {0:M}
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

A catch-all location for information that does not fully fit within other structures.
It may include research notes, additional context, alternative interpretations, reasoning, and so forth.

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


#### `SHARED_PLACE_RECORD` :=

```gedstruct
n @XREF:SPLAC@ SPLAC <Text>                {1:1}  g71:record-SPLAC
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TYPE <Text>                           {1:1}  g71:SPLAC-TYPE 
    +2 HREL <HIERARCHICAL_RELATIONSHIP>    {1:1}  g71:SPLAC-HREL
      +3 GOVTYP  <GOVID_OF_TYPE>           {0:1}
        +4 TEXT                            {0:1}  g71:SPLAC-TEXT  
  +1 <<PERIOD_STRUCTURE>>                  {1:M}
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
  +1 <<CHANGE_DATE>>                       {1:1}
  +1 <<CREATION_DATE>>                     {1:1}
```

A descriptor of a single place, location, or jurisdiction.
This record describes a location where an event occurred, including its name, geographical position, and historical parent jurisdictions across various timeframes. Each timeframe (`PERIOD`) is detailed with its corresponding administrative hierarchy, reflecting the changes in jurisdiction, boundaries, names or geopolitical status over time. The record allows for the capture of information relevant to the specific date of an event.  

As the `SPLAC`Record now will contain a lot of information, coming from (possibly) many users, it might be a good idea to allow the adding of **`SUBM`** on some places (as is already done now for the `TYPE`of the `PERIOD`structure) That way information can be traced back.

The `PERIOD_STRUCTURE`consists of the folowing parts:
- **The `<TEXT>` payload** of the `SPLAC`, is the **default name** of the location, that will be used for this `SPLAC`. For instance in a "Treeview", or user-output, or when a user searches for a place to enter for an event. The only time a user should see another name, is when he/she (partly) typed one of the Names, inside a `PERIOD` of this place.  

:::  
Example: When, for a certain date of an event, a user types "Amster" the program might show him "Amsterdam", but when he types "Amstelle", the program will show him "Amstelledamme" as that was the name of Amsterdam around 1275, and valid on the date of the event the user is entering.  
**In both cases** the user gets **the same SPLAC**. This way there is less clutter in the GEDCOM, and there are less entrypoints to maintain.  
:::

- **LANG** only defines the language of the TEXT payload (which is the default NAME of this `SPLAC`).  
If an `SPLAC` has more Names with Translations for those Names, they must all be inside the `PERIOD_STRUCTURE`(s).  
This way, "links" from **inside other SPLAC's, or from events**, always have 1 entry point for whatever information might be inside any `PERIOD` of this `SPLAC`.
As the `PERIOD's` inside an `SPLAC` always have a DATE-period, a program can determine, coming from an event on a certain Date (or in a certain timeframe), which `PERIOD` of the `SPLAC` it should pick its information from.  

- **TYPE** The `TYPE` of the `SPLAC`. This is meant to be the types that now are in the`PLAC` or `PLAC.FORM` of GEDCOM7, so in fact **the original jurisdictions**. These jurisdictions are now defined in the enumset `SPLAC-TYPE`.  
`TYPE`can be combined with the subtags `HREL`, `GOVTYP`and `TEXT` that follow it. (see **"TYPE, HREL, GOVTYP and TEXT"** for an explanation.)

- **HREL**  A `TYPE` that is the `HIERARCHICAL_RELATIONSHIP` of the `SPLAC`.  
This type describes the structured relationships between entities, where one holds a position of authority or influence over another. This includes political, administrative, religious, geographical, cultural, or other hierarchical associations, such as between nations, regions, organizations, or social groups.  
So the relationship of an `SPLAC`can be: political (administrative), religious, geographical or cultural. See `g71:SPLAC-HREL`.  
`HREL`can be combined with the subtags `TYPE`, `GOVTYP`and `TEXT` that are near it. (see **"TYPE, HREL, GOVTYP and TEXT"** for an explanation.) `HREL` is defined directly after `TYPE` because both have an {1:1}, so both are obligatory and should always be present.

- **GOVTYP** (which is a `TYPE`) Defined in GEDCOM_L as: {Size=1:3} In GEDCOM_L it is called `<GOVID_OF_TYPE>` and it is defined there as follows:  
An integer positive number as defined in the GOV system. The definition in the GOV system http://gov.genealogy.net/type/list is binding for the interpretation of this line and allows an interpretation of the superior line 1 TYPE for all languages stored in the GOV system. The multilingual RDF file with the definitions of the object types of the GOV system is also available for this purpose https://gov.genealogy.net/types.owl .  
The enumeration: `g71:SPLAC-TYPE` only defines a subset of the GEDCOM_L `<GOVID_OF_TYPE>` list, namely those that are the most common jurisdictions in GEDCOM7. To use the other `<GOVID_OF_TYPE>` values, they have to be put behind the general `g71:SPLAC-TYPE` **"LOCATION"**, to further specify `LOCATION`. This way all numbers from the around 280 GOV numbers can be used.  
We strongly encourage to always have a `GOVTYP` too. (See the above mentioned list)
  
Also see the examples in the example chapter.  
`GOVTYP`can be combined with the subtags `HREL`, `TYPE`and `TEXT` that are above and below. (see **"TYPE, HREL, GOVTYP and TEXT"** for an explanation.)

- **TEXT** (`g71:SPLAC-TEXT`) Optional. This is either the written "Name" of the **GOVTYP**, or a free user text. If it is present it must always be put at the end of the line, separated from it by a comma. (see **"TYPE, HREL, GOVTYP and TEXT"** for a definition and explanation.)

- **TYPE, HREL, GOVTYP and TEXT**, which are in fact 4 separate lines, have to be combined to 1 line, for better readability. Combining is only possible when the first 3 lines both are a **`"TYPE"`** as in this case, followed by a `TEXT`of type `g71:SPLAC-TEXT`.

:::Example:  
**`  1 TYPE COUNTRY, 7, POLI, Federal State`**  
This means it is the `SPLAC-TYPE` **COUNTRY**, combined with the `<GOVID_OF_TYPE>` **7, which is Federal state**, and this `SPLAC` is in an political hierarchy.  
Each parameter is separated from the previous one by a comma. The explaining text of the number is put at the end of the line.  

**`  1 TYPE PROVINCE, 6, RELI, Diocese`**  
This means it is the `SPLAC-TYPE` **PROVINCE**, combined with the `<GOVID_OF_TYPE>` **6, which is a Diocese** and this `SPLAC` is in a religious hierarchy.  
:::

- **`<<PERIOD_STRUCTURE>>`** This reflects the historical changes in governance, boundaries, or place names in a certain timeframe.


**The first `PERIOD` inside an `SPLAC`**, always serves as the default `PERIOD`. Information from this `PERIOD` has to be used if another `PERIOD` in this same `SPLAC` lacks that information.  
Also if a user enters a place that has no `SPLAC` yet, that `SPLAC` will get a default `PERIOD` with a DATE period filled in **From 0** (as Dates cannot be empty)

:::Example:  
**the Places location(s)**. If inside a `PERIOD` where there is no other location given (meaning for this period the place has not "moved", according to the first `PERIOD`), the program should use the Location given in the first (default) `PERIOD`. But if there IS a location inside a `PERIOD` (meaning the SPLAC has "moved" to another location inside this period of time), that location is valid for that period. So a program can pick the correct location depending on **the date ( or dateframe) of the event pointing to this SPLAC**.  

**The Place Name(s)**. If inside a `PERIOD` no other Name(s) are mentioned, the Name as it is specified in the first `PERIOD` is valid. But if there **IS** a name inside a `PERIOD`, that name is valid for that period. So a program can pick the correct Name depending on the date (or dateframe) of the event pointing to this `SPLAC`.  
Same for other information inside `PERIOD's`.  
See also the extended examples in the examples chapter.  
:::

#### `PLACENAME_STRUCTURE` :=

**As there is no more `PLACE_STRUCTURE` with `FORM` as in GEDCOM7, we might need to define `<PlaceName>` in chapter 2, same as **"PersonalName"** is defined in GEDCOM7 now.** Because `<PlaceName>` can have other elements than `PERSONALName.` 

```gedstruct
n NAME <PlaceName>                         {1:1}  g7:INDI-NAME
  +1 TRAN <PlaceName>                      {0:M}  g7:NAME-TRAN
     +2 LANG <Language>                    {1:1}  g7:LANG
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
```

-  **NAME** The name(s) of the SPLAC in this `PERIOD`.  

-  **TRAN** The Tran structure used to translate the name in this `PERIOD`.  

:::Example  
The following example shows the Dutch Province **"Friesland"**, as it is called in 2 different ways:  
- It is officially called **"Friesland"** as default name, in Dutch (nl).  
- After a certain date it is **officially** called **"Friesland"** AND **"Fryslân"**,  with 2 translations, but Frisian people will also call it **"It Heitelân"**, with 2 translations.

The default name:
```gedcom
  1 NAME Friesland
    2 LANG nl
```

In another time period:
```
  1 NAME Friesland
    2 LANG nl
  1 TRAN Fryslân 
    2 LANG fy
  1 NAME It Heitelân          (The Homeland)
    2 LANG fy
  1 TRAN Het Vaderland        
    2 LANG nl
```
:::

As the `PLACENAME_STRUCTURE` will often have names that might have been valid in older times, the structure also has a `NOTE_STRUCTURE` and a `SOURCE_STRUCTURE` to make it possible to add extra information about the names.

#### PLACE_LOCATION_STRUCTURE :=
This structure is meant to contain all means of locating a certain `SPLAC`
```gedstruct
n MAP                                      {0:1}  g7:MAP
  +1 LATI <Special>                        {1:1}  g7:LATI
  +1 LONG <Special>                        {1:1}  g7:LONG
  +1 RADIUS <Decimal>                      {0:1}  g71:RADIUS
n <<ADDRESS_STRUCTURE>>                    {0:1}
n EXID <Special>                           {0:M}  g7:EXID
  +1 TYPE <Special>                        {0:1}  g7:EXID-TYPE
n GOVIDN <GOV_IDENTIFIER>                  {0:1}  
n MAID <MAIDENHEAD_LOCATOR>                {0:1} 
n ZIPCD <POSTAL_CODE>                      {0:1} 
  +1 DATE <DATE_VALUE>                     {0:1} 
  +1 <<SOURCE_CITATION>>                   {0:M} 
n <<NOTE_STRUCTURE>>                       {0:M}
n <<SOURCE_CITATION>>                      {0:M}
```
:::deprecation Having an `EXID` without an `EXID.TYPE` substructure is deprecated. The meaning of an `EXID` depends on its `EXID.TYPE`. The cardinality of `EXID.TYPE` will be changed to `{1:1}` in version 8.0. :::

Location information about a place.

- **`RADIUS`** is added to have the possibility of defining an area, not just a location, in case the exact location is not known. It can be presented in Kilometers or in Meters. `RADIUS`, as presented here inside the `MAP`, is not supposed to be very large, as that does not give an accurate location.

:::  
Examples:

```gedcom
  +1 MAP
    +2 LATI xxx
    +2 LONG xxx
    +2 RADIUS 2 KM

  .....
  +1 MAP
    +2 LATI xxx
    +2 LONG xxx
    +2 RADIUS 1.75 KM

  .....
  +1 MAP
    +2 LATI xxx
    +2 LONG xxx
    +2 RADIUS 400 M
```
:::  

- **`<<ADDRESS_STRUCTURE>>`** This needs more discussion. In fact the GEDCOM-L's address structure might be a good start, but in here it is just mentioned as a possibility, as it is not clear yet how the address should look.

- **`GOVIDN`** Defined as **`<GOV_IDENTIFIER>`** in GEDCOM_L as: := {Size=1:14} The official GOV1 Id. ID of the object in the Historical Place Register / Historic Gazetteer (GOV), see http://wiki-de.genealogy.net/GOV. The GOV-ID, for example, has the form **CREGENJO52HG** for **"Cremlingen"**. A list of the GOV-ID is available via the MiniGOV files (download via http://wiki-de.genealogy.net/GOV/Mini-GOV ) or online via the web service of the GOV system http://wiki-de.genealogy.net/GOV/Webservice . 

- **`MAID`** Defined as **`<MAIDENHEAD_LOCATOR>`** in GEDCOM_L as: := {Size=1:8} The maidenhead code. (For Maidenhead code see: (https://www.egloff.eu/qralocator/)  
The Maidenhead Locator System (a.k.a. QTH Locator and IARU Locator) is a geocode system used by amateur radio operators to succinctly describe their geographic coordinates, which replaced the deprecated QRA locator.

- **`ZIPCD`** Defined as **`<POSTAL_CODE>`** in GEDCOM_L as: := {Size=1:10} The official ZIP code, called **`ADDRESS_POSTAL_CODE`** in GEDCOM7.  
It is changed into **{0:1}** in this specification.

#### `SOURCE_RECORD` :=

```gedstruct
n @XREF:SOUR@ SOUR                         {1:1}  g7:record-SOUR
  +1 DATA                                  {0:1}  g7:DATA
     +2 EVEN <List:Enum>                   {0:M}  g7:DATA-EVEN
        +3 DATE <DatePeriod>               {0:1}  g7:DATA-EVEN-DATE
           +4 PHRASE <Text>                {0:1}  g7:PHRASE
        +3 <<PLACE_REFERENCE>>             {0:1}
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
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

A source record describes an entire source.
A source may also point to `REPO`s to describe repositories or archives where the source document may be found.
The part of a source relevant to a specific fact, such as a specific page or entry, is indicated in a `SOURCE_CITATION` that points to the source record.

:::note
This sourcing model is known to be insufficient for some use cases and may be refined in a future version of this specification.
:::

A `SOURCE_RECORD` may contain a pointer to a `SHARED_NOTE_RECORD` and vice versa. Applications must not create datasets where these mutual pointers form a cycle. Applications should also ensure they can handle invalid files with such cycles in a safe manner.

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
  +1 <<CHANGE_DATE>>                       {0:1}
  +1 <<CREATION_DATE>>                     {0:1}
```

The submitter record identifies an individual or organization that contributed information contained in the dataset.
All records in the document are assumed to be contributed by the
submitter referenced in the `HEAD`,
unless a `SUBM` structure inside a specific record points at a different submitter record.

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


#### `ASSOCIATION_STRUCTURE` :=

```gedstruct
n ASSO @<XREF:INDI>@                       {1:1}  g7:ASSO
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
  +1 ROLE <Enum>                           {1:1}  g7:ROLE
     +2 PHRASE <Text>                      {0:1}  g7:PHRASE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
  +1 <<SOURCE_CITATION>>                   {0:M}
```

An individual associated with the subject of the superstructure.
The nature of the association is indicated in the `ROLE` substructure.

A `voidPtr` and `PHRASE` can be used to describe associations to people not referenced by any `INDI` record.

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
n <<PLACE_REFERENCE>>                      {0:1}
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
n <<ASSOCIATION_STRUCTURE>>                {0:M}
n <<NOTE_STRUCTURE>>                       {0:M}
n <<SOURCE_CITATION>>                      {0:M}
n <<MULTIMEDIA_LINK>>                      {0:M}
n UID <Special>                            {0:M}  g7:UID
```

Substructures that may be shared by most individual and family events and attributes.

Note that many of these substructures are limited to 1 per event.
Conflicting event information should be represented by placing them in separate event structures (with appropriate source citations) rather than by placing them under the same enclosing event.

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

#### `LDS_ORDINANCE_DETAIL` :=

```gedstruct
n <<DATE_VALUE>>                         {0:1}
n TEMP <Text>                            {0:1}  g7:TEMP
n <<PLACE_REFERENCE>>                    {0:1}
n STAT <Enum>                            {0:1}  g7:ord-STAT
  +1 DATE <DateExact>                    {1:1}  g7:DATE-exact
     +2 TIME <Time>                      {0:1}  g7:TIME
n <<NOTE_STRUCTURE>>                     {0:M}
n <<SOURCE_CITATION>>                    {0:M}
```

Dates for these ordinances should be in the default (`GREGORIAN`) calendar and be 1830 or later.
These ordinances can be performed posthumously by proxy, and the date may reflect that posthumous date.

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
  +1 <<SOURCE_CITATION>>                   {0:M}
```

Indicates that a specific type of event, given in the payload, did not happen within a given date period
(or never happened if there is no `DATE` substructure).

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
  +1 <<SOURCE_CITATION>>                   {0:M}
|
n SNOTE @<XREF:SNOTE>@                     {1:1}  g7:SNOTE
]
```

A catch-all location for information that does not fully fit within other structures.
It may include research notes, additional context, alternative interpretations, reasoning, and so forth.

Each `NOTE`.`TRAN` must have either a `MIME` or `LANG` substructure, and may have both.

See `SHARED_NOTE_RECORD` for advice on choosing between `NOTE` and `SNOTE`.

A `NOTE_STRUCTURE` can contain a `SOURCE_CITATION`, which in turn can contain a `NOTE_STRUCTURE`, allowing potentially unbounded nesting of structures. Because each dataset is finite, this nesting is also guaranteed to be finite.



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
  +1 <<SOURCE_CITATION>>                   {0:M}
```

Names of individuals are represented in the manner the name is normally spoken, with the family name, surname, or nearest cultural parallel thereunto separated by slashes (U+002F `/`). Based on the dynamic nature or unknown compositions of naming conventions, it is difficult to provide a more detailed name piece structure to handle every case. The `PERSONAL_NAME_PIECES` are provided optionally for systems that cannot operate effectively with less structured information. The Personal Name payload shall be seen as the primary name representation, with name pieces as optional auxiliary information; in particular it is recommended that all name parts in `PERSONAL_NAME_PIECES` appear within the `PersonalName` payload in some form, possibly adjusted for gender-specific suffixes or the like.
It is permitted for the payload to contain information not present in any name piece substructure.

The name may be translated or transliterated into different languages or scripts using the `TRAN` substructure.
It is recommended, but not required, that if the name pieces are used, the same pieces are used in each translation and transliteration.

A `TYPE` is used to specify the particular variation that this name is.
For example; it could indicate that this name is a name taken at immigration or that it could be an ‘also known as’ name.
See `g7:enumset-NAME-TYPE` for more details.

:::note
Alternative approaches to representing names are being considered for future versions of this specification.
:::

#### `PLACE_DETAILS` :=

```gedstruct
n MAP                                      {0:1}  g7:MAP
  +1 LATI <Special>                        {1:1}  g7:LATI
  +1 LONG <Special>                        {1:1}  g7:LONG
n EXID <Special>                           {0:M}  g7:EXID
  +1 TYPE <Special>                        {0:1}  g7:EXID-TYPE
n <<NOTE_STRUCTURE>>                       {0:M}
```

:::deprecation
Having an `EXID` without an `EXID`.`TYPE` substructure is deprecated.
The meaning of an `EXID` depends on its `EXID`.`TYPE`.
The cardinality of `EXID`.`TYPE` will be changed to `{1:1}` in version 8.0.
:::

Information about a place (either `PLAC` or `SPLAC`).

#### `PLACE_REFERENCE` :=

```gedstruct
[
n <<PLACE_STRUCTURE>>               {1:1}
|
n <<SHARED_PLACE_STRUCTURE>>        {1:1}
]
```

Place structures have been part of GEDCOM since its earliest version,
but have difficulty distinguishing information about a place itself from information about a reference to that place
and cannot store information about larger jurisdictions that a given referenced place is included within.
Shared place structures should be used instead unless backwards compatibility with old GEDCOM versions is required.

#### `PLACE_STRUCTURE` :=

```gedstruct
[
n PLAC <List:Text>                         {1:1}  g7:PLAC
  +1 FORM <List:Text>                      {0:1}  g7:PLAC-FORM
  +1 LANG <Language>                       {0:1}  g7:LANG
  +1 TRAN <List:Text>                      {0:M}  g7:PLAC-TRAN
     +2 LANG <Language>                    {1:1}  g7:LANG
  +1 <<PLACE_DETAILS>>
|
n <<SHARED_PLACE_STRUCTURE>>               {1:1}
]
```

A way of representing a place without using the several records involved in the more-expressive `SHARED_PLACE_RECORD` alternative.

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

:::note
`PLAC` does not support places where a single place's name contains a comma. If commas are desired, use `SPLAC` instead of `PLAC`.
:::

A `PLAC`.`NOTE` could in principle be about the place generally or about the connection between the place and its superstructure. The `PLAC`-to-`SPLAC` conversion outlined under `SHARED_PLACE_RECORD` assumes the latter meaning.

`PLAC` does not support recording any information except names of jurisdictions other than the most specific jurisdiction in the hierarchy.

See `SHARED_PLACE_RECORD` for how to convert between `PLAC` and `SPLAC`.


#### `SHARED_PLACE_STRUCTURE` :=

```gedstruct
n SPLAC @<XREF:SPLAC>@                     {1:1}  g71:SPLAC
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
  +1 <<NOTE_STRUCTURE>>                    {0:M}
```

An assertion that something took place in or is part of some place.

it is a pointer (link) to a **`SHARED_PLACE_RECORD`**, this pointer is placed in a `SOURCE_RECORD`, an `LDS_ORDINANCE_DETAIL` or in an `EVENT_DETAIL`, to assign a Place for, or to, an event. 

- **`TYPE`** The Hierarchical relationship to the parent **`SPLAC`**. Defined in GEDCOM-L as: := [POLI|RELI|GEOG|CULT] Used to differentiate political (administrative), religious, geographical or cultural associations. For the superior location object the details of its type are defined by the <TYPE_OF_LOCATION> in its record. 

The `NOTE_STRUCTURE`s here are about the connection between the topic of the superstructure and the pointed-to place.
Notes about the place itself should be placed inside the pointed-to `SHARED_PLACE_RECORD`.

A `voidPtr` and `PHRASE` can be used to describe places not referenced by any `SPLAC` record, but so can a `PLAC` structure. Using a `voidPtr` with `SPLAC` is not recommended.

:::example
The following both indicate that a birth happened "at home" with no additional details on where that was. The second version is preferred; the first should not be used.

```gedcom  
0 @I1@ INDI
  1 BIRT
    2 SPLAC @SP321@
      3 PHRASE at home
      3 NOTE This link points to a general "At Home" structure.

0 @SP321@ SPLAC at home
  1 LANG en
  1 TYPE LOCATION, , 17, Building
  1 PERIOD 
    2 TYPE SOURCE 
  1 NOTE some more explanation here about "at home" itself.            
  1 CREA
    2 DATE 22 JUL 2022
      3 TIME 20:56:25
  1 CHAN
    2 DATE 24 SEP 2024
      3 TIME 15:25:18
```
The **`TYPE`** of this **`SPLAC`** is **`LOCATION`**, the general **`SPLAC`** type that is further specified with the **`GOVTYP`** location type 17, from the GOV list, which denotes a building of unknown further description. For the "empty comma", see the explanation of `TYPE`at the `SHARED_PLACE` RECORD. 
The **`PERIOD`** has no payload, denoting it is usable from old days till present. For that reason there is also no **`DATE`**.  
There is no Location mentioned either, as there is no further description of "at home" given.  
This **`SPLAC`** does not point to a parent **`SPLAC`**, but a user could make it point to **`EARTH`** if he wishes.  
:::

See `SHARED_PLACE_RECORD` for how to convert between `PLAC` and `SPLAC`.

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

