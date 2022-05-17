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
        - `<`datatype`>` means a non-pointer payload, as described in [Data types](#datatypes). If the datatype allows the empty string, the payload may be omitted.
        - `[`text`|<NULL>]` means the payload is optional but if present must be the given text.
        
        If there is a payload descriptor, a payload that matches the payload is required of the described structure unless the descriptor says the payload is optional.

        If there is no payload descriptor, the described structure must not have a payload.
        
    - A cardinality marker.
    - The URI of this structure type.
        
        Pseudo-structures do not have a URI.

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
0 TRLR                                     {1:1} 
```

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
n <<SUBMITTER_RECORD>>                     {1:1}
]
```

#### `HEADER` :=

```gedstruct
n HEAD                                     {1:1} 
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
  +1 PLAC                                  {0:1}  g7:HEAD-PLAC
     +2 FORM <List:Text>                   {1:1}  g7:HEAD-PLAC-FORM
  +1 <<NOTE_STRUCTURE>>                    {0:1}
```

The header pseudo-structure provides metadata about the entire dataset.
A few substructures of note:

- `GEDC` identifies the specification that this document conforms to.
- `SCHMA` gives the meaning of extension tags; see [Extensions](#extensions) for more.
- `SOUR` describes the originating software.
    - `CORP` describes the corporation creating the software.
    - `HEAD`.`SOUR`.`DATA` describes a larger database this data is extracted from.
- `LANG` and `PLAC` give a default value for the rest of the document.


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
See `ALIA` for more.

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
  +1 FILE <Special>                        {1:M}  g7:FILE
     +2 FORM <MediaType>                   {1:1}  g7:FORM
        +3 MEDI <Enum>                     {0:1}  g7:MEDI
           +4 PHRASE <Text>                {0:1}  g7:PHRASE
     +2 TITL <Text>                        {0:1}  g7:TITL
     +2 TRAN <Special>                     {0:M}  g7:FILE-TRAN
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

#### `EVENT_DETAIL` :=

```gedstruct
n DATE <DateValue>                         {0:1}  g7:DATE
  +1 TIME <Time>                           {0:1}  g7:TIME
  +1 PHRASE <Text>                         {0:1}  g7:PHRASE
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

Family attributes; see [Family Attributes](#family-attributes) for more.

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
n MARS [Y|<NULL>]                          {1:1}  g7:MARS
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n MARR [Y|<NULL>]                          {1:1}  g7:MARR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
|
n EVEN <Text>                              {1:1}  g7:FAM-EVEN
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<FAMILY_EVENT_DETAIL>>               {0:1}
]
````

Family events; see [Family Events](#family-events) for more.

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

Individual attributes; see [Individual Attributes](#individual-attributes) for more.

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
n ADOP [Y|<NULL>]                          {1:1}  g7:ADOP
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:ADOP-FAMC
     +2 ADOP <Enum>                        {0:1}  g7:FAMC-ADOP
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
|
n BIRT [Y|<NULL>]                          {1:1}  g7:BIRT
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:FAMC
|
n CHR [Y|<NULL>]                           {1:1}  g7:CHR
  +1 TYPE <Text>                           {0:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
  +1 FAMC @<XREF:FAM>@                     {0:1}  g7:FAMC
|
n EVEN <Text>                              {1:1}  g7:INDI-EVEN
  +1 TYPE <Text>                           {1:1}  g7:TYPE
  +1 <<INDIVIDUAL_EVENT_DETAIL>>           {0:1}
]
````

Individual events; see [Individual Events](#individual-events) for more.

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

Ordinances performed by members of The Church of Jesus Christ of Latter-day Saints; see [Latter-day Saint Ordinances] for more.

#### `LDS_ORDINANCE_DETAIL` :=

```gedstruct
n DATE <DateValue>                       {0:1}  g7:DATE
  +1 TIME <Time>                         {0:1}  g7:TIME
  +1 PHRASE <Text>                       {0:1}  g7:PHRASE
n TEMP <Text>                            {0:1}  g7:TEMP
n <<PLACE_STRUCTURE>>                    {0:1}
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

Ordinances performed by members of The Church of Jesus Christ of Latter-day Saints; see [Latter-day Saint Ordinances] for more.

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
  +1 TRAN <Text>                           {0:1}  g7:NOTE-TRAN
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

:::note
Although notes may be tagged with the language that they are written in, this specification does not provide a mechanism for distinguishing between notes with distinct content in distinct languages versus notes with the same content translated into distinct languages. It is expected that a future version of this specification will provide a mechanism for a single note to have multiple language translations.

The same is true for `MIME`: notes differing in `MIME` may contain the same content in a different format or contain distinct content, and this document provides no mechanism for distinguishing those cases.
:::

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

Optional isolated name parts; see `PERSONAL_NAME_STRUCTURE` for more.

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

Names of individuals are represented in the manner the name is normally spoken, with the family name, surname, or nearest cultural parallel thereunto separated by slashes (U+002F `/`). Based on the dynamic nature or unknown compositions of naming conventions, it is difficult to provide a more detailed name piece structure to handle every case. The `PERSONAL_NAME_PIECES` are provided optionally for systems that cannot operate effectively with less structured information. The Personal Name payload shall be seen as the primary name representation, with name pieces as optional auxiliary information.

The name may be translated or transliterated into different languages or scripts using the `TRAN` substructure.
It is recommended, but not required, that if the name pieces are used, the same pieces are used in each translation and transliteration.

A `TYPE` is used to specify the particular variation that this name is.
For example; it could indicate that this name is a name taken at immigration or that it could be an ‘also known as’ name.
See [the NAME.TYPE enumeration](#enum-TYPE) for more.

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
     +2 DATE <DateValue>                   {0:1}  g7:DATE
        +3 TIME <Time>                     {0:1}  g7:TIME
        +3 PHRASE <Text>                   {0:1}  g7:PHRASE
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
`BURI` | burial<br/>`g7:BURI` | Disposing of the mortal remains of a deceased person.
`CENS` | census<br/>`g7:INDI-CENS` | Periodic count of the population for a designated locality, such as a national or state census.
`CHR` | christening<br/>`g7:CHR` | Baptism or naming events for a child.
`CHRA` | adult christening<br/>`g7:CHRA` | Baptism or naming events for an adult person.
`CONF` | confirmation<br/>`g7:CONF` | Conferring full church membership.
`CREM` | cremation<br/>`g7:CREM` | Disposal of the remains of a person's body by fire.
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
`NATI` | nationality<br/>`g7:NATI` | The national heritage of an individual.
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

Strutures types are listed in this section alphabetically by tag.
When the same tag is used for different structure types in different contexts, they may be distinguished by their URI.

#### `ABBR` (Abbreviation) `g7:ABBR`

A short name of a title, description, or name used for sorting, filing, and retrieving records.

#### `ADDR` (Address) `g7:ADDR`

The location of, or most relevant to, the subject of the superstructure.
See `ADDRESS_STRUCTURE` for more.

#### `ADOP` (Adoption) `g7:ADOP`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `ADOP` (Adoption) `g7:FAMC-ADOP`

An [enumerated value](#enum-ADOP) indicating which parent(s) in the family adopted this individual.

#### `ADR1` (Address Line 1) `g7:ADR1`

The first line of the address, used for indexing.
This structure's payload should be a single line of text equal to the first line of the corresponding `ADDR`.
See `ADDRESS_STRUCTURE` for more.

#### `ADR2` (Address Line 2) `g7:ADR2`

The second line of the address, used for indexing.
This structure's payload should be a single line of text equal to the second line of the corresponding `ADDR`.
See `ADDRESS_STRUCTURE` for more.

#### `ADR3` (Address Line 3) `g7:ADR3`

The third line of the address, used for indexing.
This structure's payload should be a single line of text equal to the third line of the corresponding `ADDR`.
See `ADDRESS_STRUCTURE` for more.

#### `AGE` (Age at event) `g7:AGE`

The age of the individual at the time an event occurred, or the age listed in the document.

#### `AGNC` (Responsible agency) `g7:AGNC`

The organization, institution, corporation, person, or other entity that has responsibility for the associated context.
Examples are an employer of a person of an associated occupation, or a church that administered rites or events, or an organization responsible for creating or archiving records.

#### `ALIA` (Alias) `g7:ALIA`

A single individual may have facts distributed across multiple individual records, connected by `ALIA` pointers
(named after "alias" in the computing sense, not the pseudonym sense).

:::note
This specification does not define how to connect `INDI` records with `ALIA`.
Some systems organize `ALIA` pointers to create a tree structure, with the root `INDI` record containing the composite view of all facts in the leaf `INDI` records.
Others distribute events and attributes between `INDI` records mutually linked by symmetric pairs of `ALIA` pointers.
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
See `ASSOCIATION_STRUCTURE` for more.

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

#### `BLES` (Blessing) `g7:BLES`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `BURI` (Burial) `g7:BURI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

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
See `CHANGE_DATE` for more.

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
See `ADDRESS_STRUCTURE` for more.

#### `CONF` (Confirmation)  `g7:CONF`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `CONL` (Confirmation, Latter-Day Saint) `g7:CONL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `CONT` (Continued)

A pseudo-structure to indicate a line break.
See [Lines](#lines) for more.

#### `COPR` (Copyright) `g7:COPR`

A copyright statement, as appropriate for the copyright laws applicable to this data.

#### `CORP` (Corporate name) `g7:CORP`

The name of the business, corporation, or person that produced or commissioned the product.

#### `CREA` (Creation) `g7:CREA`

The initial creation of the superstructure.
This is metadata about the structure itself, not data about its subject.
See `CREATION_DATE` for more.

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
See `ADDRESS_STRUCTURE` for more.

#### `DATA` (Data) `g7:DATA`

A structure with no payload used to distinguish a description of something from metadata about it.
For example, `SOUR` and its other substructures describe a source itself,
while `SOUR`.`DATA` describes the content of the source.

#### `DATA` (Data) `g7:SOUR-DATA`

See `g7:DATA`.

#### `DATA` (Data) `g7:HEAD-SOUR-DATA`

The electronic data source or digital repository from which this dataset was exported.
The payload is the name of that source,
with substructures providing additional details about the source (not the export).

#### `DATE` (Date) `g7:DATE`

The principal date of the subject of the superstructure.
The payload is a `DateValue`.

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

#### `EDUC` (Description) `g7:EDUC`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `EMAIL` (Email) `g7:EMAIL`

An electronic mail address, as defined by any relevant standard
such as [RFC 3696](https://www.rfc-editor.org/info/rfc3696), [RFC 5321](https://www.rfc-editor.org/info/rfc5321), or [RFC 5322](https://www.rfc-editor.org/info/rfc5322).

If an invalid email address is present upon import, it should be preserved as-is on export.

:::note
The version 5.5.1 specification contained a typo where this tag was sometimes written `EMAI` and sometimes written `EMAIL`. `EMAIL` should be used in version 7.0 and later.
:::

#### `EMIG` (Description) `g7:EMIG`

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

A list of [enumerated values](#enum-EVEN) indicating the types of events that were recorded in a particular source.
Each event type is separated by a comma and space.
For example, a parish register of births, deaths, and marriages would be `BIRT, DEAT, MARR`.

#### `EVEN` (Event) `g7:SOUR-EVEN`

An [enumerated value](#enum-SOUR.EVEN) indicating the type of event or attribute which was responsible for the source entry being recorded.
For example, if the entry was created to record a birth of a child, then the type would be `BIRT` regardless of the assertions made from that record, such as the mother's name or mother's birth date.

#### `EXID` (External Identifier) `g7:EXID`

An identifier for the subject of the superstructure.
The identifier is maintained by some external authority;
the authority owning the identifier is provided in the TYPE substructure; see `EXID`.`TYPE` for more.

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
It is also used with a `STAT` substructure to show individuals who are not children of the family.
See `FAM` and `FAMC`.`STAT` for more.

#### `FAMC` (Family child) `g7:FAMC`

The family with which this individual event is associated.

#### `FAMC` (Family child) `g7:ADOP-FAMC`

The individual or couple that adopted this this individual.

Adoption by an individual, rather than a couple, may be represented either by pointing to a `FAM` where that individual is a `HUSB` or `WIFE` and using a `g7:FAMC-ADOP` substructure to indicate which 1 performed the adoption; or by using a `FAM` where the adopting individual is the only `HUSB`/`WIFE`.

#### `FAMS` (Family spouse) `g7:FAMS`

The family in which an individual appears as a partner.
See `FAM` for more.

#### `FAX` (Facsimile) `g7:FAX`

A fax telephone number appropriate for sending data facsimiles.
See `PHON` for more.

#### `FCOM` (First communion) `g7:FCOM`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `FILE` (File reference) `g7:FILE`

A reference to an external file.
Syntactically, the payload is a URI reference as defined by [RFC 3986](https://www.rfc-editor.org/info/rfc3986), or a valid URL string as defined by the [WHATWG URL specification](https://url.spec.whatwg.org/).
That is, it can be an absolute or relative URL, optionally with a fragment string.
However, only the following URL types are used:

- A URL with scheme `ftp`, `http`, or `https` refers to a **web-accessible file**.

- A URL with scheme `file` refers to a **machine-local file** as defined by [RFC 8089](https://www.rfc-editor.org/info/rfc8089). Machine-local files must not be used in [FamilySearch GEDZIP](#gedzip) nor when sharing datasets on the web or with unknown parties, but may be used for close collaboration between parties with known similar file structures.

- A URI reference with all of the following:
    - no scheme
    - not beginning with `/` (U+002F)
    - not containing any path segments equal to `..` (U+002E U+002E)
    - not containing a reverse solidus character (U+005C `\`) or `banned` character, either directly or in escaped form
    - no query or fragment
    
    refers to a **local file**. If the dataset is part of a [GEDZIP file](#gedzip), the URL of the local file is a zip archive filename; otherwise, the URL of a local file is resolved with *base* equal to the directory containing the dataset.
    
    It is recommended that local files use the directory prefix `media/`, but doing so is not required.

    For compatibility with [GEDZIP](#gedzip) and related formats, it is recommended that the following `FILE` payloads not be used:
    
    - `gedcom.ged`
    - `MANIFEST.MF`
    - any URL beginning `META-INF/`

The meaning of a `FILE` payload with any format not listed above is not defined by this version of the specification, but may be defined in a subsequent version.

#### `FORM` (Format) `g7:FORM`

The media type of the file referenced by the superstructure.
This should be a valid media type as defined by [BCP 13](https://www.rfc-editor.org/info/bcp13).
A [registry of media types](https://www.iana.org/assignments/media-types/media-types.xhtml) is maintained publicly by the IANA.

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

It is recommended that applications write `GEDC` with its required subrecord `VERS` as the first substructure of `HEAD`.

#### `GIVN` (Given name) `g7:GIVN`

A given or earned name used for official identification of a person.

#### `GRAD` (Graduation) `g7:GRAD`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `HEAD` (Header)

A pseudo-structure for storing metadata about the document.
See [The Header and Trailer](#the-header) for more.

#### `HEIGHT` (Height in pixels) `g7:HEIGHT`

How many pixels to display vertically for the image.
See `CROP` for more.

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

A container for information relevant to the subject of the superstructure
specific to the individual described by the associated `FAM`'s `HUSB` substructure.

#### `HUSB` (Husband) `g7:FAM-HUSB`

This is a partner in a `FAM` record.
See `FAMILY_RECORD` for more.

#### `IDNO` (Identification number) `g7:IDNO`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `IMMI` (Immigration) `g7:IMMI`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `INDI` (Individual) `g7:record-INDI`

See `INDIVIDUAL_RECORD`.

#### `INIL` (Initiatory, Latter-Day Saint) `g7:INIL`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

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
The payload is either `N` (for a coordinate north of the equator) or `S` (for a coordinate south of the equator) followed by a decimal number of degrees.
Minutes and seconds are not used and should be converted to fractional degrees prior to encoding.

:::example
18 degrees, 9 minutes, and 3.4 seconds North would be formatted as `N18.150944`.
:::

#### `LEFT` (Left crop width) `g7:LEFT`

Left is a number of pixels to not display from the left side of the image.
See `CROP` for more.

#### `LONG` (Longitude) `g7:LONG`

A longitudinal coordinate.
The payload is either `E` (for a coordinate east of the prime meridian) or `W` (for a coordinate west of the prime meridian) followed by a decimal number of degrees.
Minutes and seconds are not used and should be converted to fractional degrees prior to encoding.

:::example
168 degrees, 9 minutes, and 3.4 seconds East would be formatted as `E168.150944`.
:::

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

An [enumerated value](#enum-MEDI) providing information about the media or the medium in which information is stored.

#### `MIME` (Media type) `g7:MIME`

Indicates the media type of the payload of the superstructure,
as defined by [BCP 13](https://www.rfc-editor.org/info/bcp13).

As of version 7.0, only 2 media types are supported by this structure:

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
    Unsupported elements should be ignored during display.

:::note
Applications are welcome to support more XML entities or HTML character references in their user interface.
However, exporting must only use the core XML entities, translating any other entities into their corresponding Unicode characters.
:::

:::note
Applications are welcome to support additional HTML elements,
but they should ensure that content is meaningful if those extra elements are ignored and only their content text is displayed.
:::


:::note
Media types are also used by external files, as described under `FORM`. External file media types are not limited to `text/plain` and `text/html`.
:::

If needed, `text/html` can be converted to `text/plain` using the following steps:

1. Replace any sequence of 1 or more spaces, tabs, and line breaks with a single space
2. Case-insensitively replace each `<p`...`>`, `</p`...`>`, and `<br`...`>` with a line break
3. Remove all other `<`...`>` tags
4. Replace each `&lt;` with `<` and `&gt;` with `>`
4. Replace each `&amp;` with `&`

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

A descriptive or familiar name that is used instead of, or in addition to, one’s proper name.

#### `NMR` (Number of marriages) `g7:NMR`

An [Individual Attribute](#individual-attributes).
See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.

#### `NO` (Did not happen) `g7:NO`

An [enumerated value](#enum-NO) identifying an event type which did not occur to the superstructure's subject.
See `NON_EVENT_STRUCTURE` for more.

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

An [enumerated value](#enum-PEDI) indicating the type of child-to-family relationship represented by the superstructure.

#### `PHON` (Phone) `g7:PHON`

A telephone number.
Telephone numbers have many regional variations and can contain non-digit characters.
Users should be encouraged to use internationalized telephone numbers rather than local versions.
As a starting point for this recommendation, there are international standards that use a "'+'" shorthand for the international prefix (for example, in place of "011" in the US or "00" in the UK).
Examples are `+1 (555) 555-1234` (US) or `+44 20 1234 1234` (UK).

See ITU standards [E.123](https://www.itu.int/rec/T-REC-E.123) and [E.164](https://www.itu.int/rec/T-REC-E.164) for more information.

#### `PHRASE` (Phrase) `g7:PHRASE`

Textual information that cannot be expressed in the superstructure due to the limitations of its datatype.

:::example
A date interpreted from the phrase "The Feast of St John" might be

````gedcom
2 DATE 24 JUNE 1852
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


#### `PLAC` (Place) `g7:PLAC`

The principal place in which the superstructure's subject occurred,
represented as a [List] of jurisdictional entities in a sequence from the lowest to the highest jurisdiction.
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
See `ADDRESS_STRUCTURE` for more.

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

An [enumerated value](#enum-QUAY) indicating the credibility of a piece of information, based on its supporting evidence.
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

A [List] of [enumerated value](#enum-RESN)s signifying access to information may be denied or otherwise restricted.

The `RESN` structure is provided to assist software in filtering data that should not be exported or otherwise used in a particular context. It is recommended that tools provide an interface to allow users to filter data on export
such that certain `RESN` structure payload entries result in the `RESN` structure and its superstructure being removed from the export.
Such removal must abode by some constraints: see [Removing data](#removing-data) for more.

This is metadata about the structure itself, not data about its subject.

#### `REPO` (Repository) `g7:REPO`

See `SOURCE_REPOSITORY_CITATION`.

#### `REPO` (Repository) `g7:record-REPO`

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

An [enumerated value](#enum-ROLE) indicating what role this person played in an event or person's life.

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
See [Extensions](#extensions) for more.

#### `SDATE` (Sort date) `g7:SDATE`

A date to be used as a sorting hint.
It is intended for use when the actual date is unknown, but the display order may be dependent on date.

If both a `DATE` and `SDATE` are present in the same structure,
the `SDATE` should be used for sorting and positioning
while the `DATE` should be displayed as the date of the structure.

`SDATE` and its substructures (including `PHRASE`, `TIME`, and any extension structures) should be used only as sorting hints, not to convey historical meaning.

#### `SEX` (Sex) `g7:SEX`

An [enumerated value](#enum-SEX) that indicates the sex of the individual at birth.

#### `SLGC` (Sealing, child) `g7:SLGC`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_INDIVIDUAL_ORDINANCE`.

#### `SLGS` (Sealing, spouse) `g7:SLGS`

A [Latter-Day Saint Ordinance](#latter-day-saint-ordinances).
See also `LDS_SPOUSE_SEALING`.

#### `SNOTE` (Shared note) `g7:SNOTE`

A pointer to a note that is shared by multiple structures.
See `NOTE_STRUCTURE` for more.

#### `SNOTE` (Shared note) `g7:record-SNOTE`

A note that is shared by multiple structures.
See `SHARED_NOTE_RECORD` for more.

#### `SOUR` (Source) `g7:SOUR`

A description of the relevant part of a source to support the superstructure's data.
See `SOURCE_CITATION` for more.

#### `SOUR` (Source) `g7:record-SOUR`

A description of an entire source.
See `SOURCE_RECORD` for more.

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
See `ADDRESS_STRUCTURE` for more.

#### `STAT` (Status) `g7:ord-STAT`

An [enumerated value](#enum-Temple.STAT) assessing of the state or condition of an ordinance.

#### `STAT` (Status) `g7:FAMC-STAT`

An [enumerated value](#enum-FAMC.STAT) assessing of the state or condition of a researcher's belief in a family connection.

#### `SUBM` (Submitter) `g7:SUBM`

A contributor of information in the substructure.
This is metadata about the structure itself, not data about its subject.

#### `SUBM` (Submitter) `g7:record-SUBM`

A description of a contributor of information to the document.
See `SUBMITTER_RECORD` for more.

#### `SURN` (Surname) `g7:SURN`

A family name passed on or used by members of a family.

#### `TAG` (Extension tag) `g7:TAG`

Information relating to a single extension tag as used in this document.
See [Extensions](#extensions) for more.

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
See `CROP` for more.


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
with a romanji transliteration
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
See also `FILE`.

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


#### `TRLR` (Trailer)

A pseudo-structure marking the end of a dataset.
See [The Header and Trailer](#the-header) for more.

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

An [enumerated value](#enum-TYPE) indicating the type of the name.

#### `TYPE` (Type) `g7:EXID-TYPE`

The authority issuing the `EXID`, represented as a URI.
It is recommended that this be a URL.

If the authority maintains stable URLs for each identifier it issues,
it is recommended that the `TYPE` payload be selected such that appending the `EXID` payload to it yields that URL.
However, this is not required and a different URI for the set of issued identifiers may be used instead.

Registered URIs are listed in [exid-types.json](https://github.com/FamilySearch/GEDCOM/blob/main/exid-types.json), where fields include:
* "label": a short string suitable for display in a user interface.
* "type": The URI representing the authority issuing the `EXID`.
* "description": A description of the meaning of the `EXID`.
* "contact": A contact email address for the person or organization registering the URI.
* "change-controller": The name or contact information for the person or organization authorized to update the registration.
* "fragment": If present, indicates a short string that can be used as a label for a fragment identifier appended to the URI.  If absent, indicates that fragment identifiers are not used with the URI.
* "reference": A URL with more information about the meaning of the `EXID`. Such information should explain the uniqueness and expected durability of the identifier.

Additional type URIs can be registered by filing a
[GitHub pull request](https://github.com/FamilySearch/GEDCOM/pulls).

#### `UID` (Unique Identifier) `g7:UID`

A globally-unique identifier of the superstructure,
to be preserved across edits.
If a globally-unique identifier for the record already exists, it should be used without modification, not even whitespace or letter case normalization.
New globally unique identifiers should be created and formatted as described in [RFC 4122](https://www.rfc-editor.org/info/rfc4122).

This is metadata about the structure itself, not data about its subject.
Multiple structures describing different aspects of the same subject would have different `UID` values.

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
See [A Guide to Version Numbers] for more.

#### `WIDTH` (Width in pixels) `g7:WIDTH`

How many pixels to display horizontally for the image.
See `CROP` for more.

#### `WIFE` (Wife) `g7:WIFE`

A container for information relevant to the subject of the superstructure
specific to the individual described by the associated `FAM`'s `WIFE` substructure.

#### `WIFE` (Wife) `g7:FAM-WIFE`

A partner in a `FAM` record.
See `FAMILY_RECORD` for more.

#### `WILL` (Will) `g7:WILL`

An [Individual Event](#individual-events).
See also `INDIVIDUAL_EVENT_STRUCTURE`.

#### `WWW` (Web address) `g7:WWW`

A URL or other locator for a World Wide Web page,
as defined by any relevant standard
such as [whatwg/url](https://url.spec.whatwg.org/),
[RFC 3986](https://www.rfc-editor.org/info/rfc3986),
[RFC 3987](https://www.rfc-editor.org/info/rfc3987),
and so forth.

If an invalid or no longer existing web address is present upon import, it should be preserved as-is on export.




## Enumeration Values

Unless otherwise specified in the enumeration description in this section, each enumeration values defined in this section has a URI constructed by concatenating
`g7:enum-` to the enumeration value;
for example, the `HUSB` enumeration value has the URI `http://gedcom.io/terms/v7/enum-HUSB`.

### `FAMC`.`ADOP` {.unlisted .unnumbered #enum-ADOP}

| Value | Meaning |
| :---- | :------ |
| `HUSB` | Adopted by the `HUSB` of the `FAM` pointed to by `FAMC`.<br/>The URI of this value is `g7:enum-ADOP-HUSB` |
| `WIFE` | Adopted by the `WIFE` of the `FAM` pointed to by `FAMC`.<br/>The URI of this value is `g7:enum-ADOP-WIFE` |
| `BOTH` | Adopted by both `HUSB` and `WIFE` of the `FAM` pointed to by `FAMC` |

### `DATA`.`EVEN` {.unlisted .unnumbered #enum-EVEN}

A comma-separated list of event- and attribute-type tag names.
See [Events] and [Attributes].

### `SOUR`.`EVEN` {.unlisted .unnumbered #enum-SOUR.EVEN}

An event- or attribute-type tag name.
See [Events] and [Attributes].

### `MEDI` {.unlisted .unnumbered #enum-MEDI}

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

### `PEDI` {.unlisted .unnumbered #enum-PEDI}

| Value     | Meaning                                                   |
| :-------- | :-------------------------------------------------------- |
| `ADOPTED` | Adoptive parents                                          |
| `BIRTH`   | Family structure at time of birth                         |
| `FOSTER`  | The child was included in a foster or guardian family     |
| `SEALING` | The child was sealed to parents other than birth parents  |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |

:::note
It is known that some users have interpreted `BIRTH` to mean "genetic parent" and others to mean "social parent at time of birth", definition which differ many circumstances (infidelity, surrogacy, sperm donation, and so on). Hence, applications should refrain from asserting it has either meaning in imported data.
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

### `NO` {.unlisted .unnumbered #enum-NO}

A single event-type tag name, but not the generic `EVEN` tag.
See [Events].



### `QUAY` {.unlisted .unnumbered #enum-QUAY}

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

### `RESN` {.unlisted .unnumbered #enum-RESN}

| Value | Meaning                      |
| :---- | :--------------------------- |
| `CONFIDENTIAL` | This data was marked as confidential by the user. |
| `LOCKED` | Some systems may ignore changes to this data. |
| `PRIVACY` | This data is not to be shared outside of a trusted circle, generally because it contains information about living individuals. |

When a [List] of `RESN` enumeration values are present, all apply.

:::example
The line `1 RESN CONFIDENTIAL, LOCKED` means the superstructure's data is both considered confidential *and* read-only.
:::

### `ROLE` {.unlisted .unnumbered #enum-ROLE}

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

### `SEX` {.unlisted .unnumbered #enum-SEX}

| Value | Meaning                                     |
| ----- | :------------------------------------------ |
| `M`   | Male                                        |
| `F`   | Female                                      |
| `X`   | Does not fit the typical definition of only Male or only Female |
| `U`   | Cannot be determined from available sources |

This can describe an individual’s reproductive or sexual anatomy at birth.
Related concepts of gender identity or sexual preference
are not currently given their own tag. Cultural or personal gender preference may be indicated using the `FACT` tag.

### `FAMC`.`STAT` {.unlisted .unnumbered #enum-FAMC.STAT}

| Value | Meaning                        |
| ----- | :----------------------------- |
| `CHALLENGED` | Linking this child to this family is suspect, but the linkage has been neither proven nor disproven. |
| `DISPROVEN` | There has been a claim by some that this child belongs to this family, but the linkage has been disproven. |
| `PROVEN` | There has been a claim by some that this child does not belong to this family, but the linkage has been proven. |

:::note
The structures for representing the strength of and confidence in various claims are known to be inadequate and are likely to change in a future version of this specification.
:::

### (Latter-Day Saint Ordinance).`STAT` {.unlisted .unnumbered #enum-Temple.STAT}

These values were formerly used by The Church of Jesus Christ of Latter-day Saints for coordinating between temples and members.
They are no longer used in that way, meaning their interpretation is subject to individual user interpretation

| Value | Meaning                             |
| ----- | :---------------------------------- |
| `BIC` | Born in the covenant, receiving blessing of child to parent sealing. |
| `CANCELED` | Canceled and considered invalid. |
| `CHILD` | Died before 8 years old. |
| `COMPLETED` | Completed, but the date is not known. |
| `EXCLUDED` | Patron excluded this ordinance from being cleared in this submission. |
| `DNS` | This ordinance is not authorized. |
| `DNS_CAN` | This ordinance is not authorized, and the previous ordinance is cancelled. |
| `INFANT` | Died before less than 1 year old, baptism or endowment not required. |
| `PRE_1970` | Ordinance was likely completed because another ordinance for this person was converted from temple records of work completed before 1970. |
| `STILLBORN` | Stillborn, so ordinances not required. |
| `SUBMITTED` | Ordinance was previously submitted. |
| `UNCLEARED` | Data for clearing the ordinance request was insufficient. |

### `NAME`.`TYPE` {.unlisted .unnumbered #enum-TYPE}

| Value | Meaning                       |
| ----- | :---------------------------- |
| `AKA` | Also known as, alias, etc. |
| `BIRTH` | Name given at or near birth. |
| `IMMIGRANT` | Name assumed at the time of immigration. |
| `MAIDEN` | Maiden name, name before first marriage. |
| `MARRIED` | Married name, assumed as part of marriage. |
| `PROFESSIONAL` | Name used professionally (pen, screen, stage name). |
| `OTHER` | A value not listed here; should have a `PHRASE` substructure |
