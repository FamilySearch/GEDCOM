# Version 7.0.2

- Clarify that inside a document stating "`2 VERS 7.0`" is sufficient but "`2 VERS 7.0.1`" is permitted

    Previously the document only said "the version number of the official specification that this document's data conforms to" which was ambiguous and could be interpreted in several ways.
    The major number is needed to define the interpretation of present tags and the minor to define the set of tags included.
    The patch number has no impact on the data itself, but may be included if desired.
    
- Update links to IETF documents to conform to recommendations from [RFC 7322](https://www.rfc-editor.org/rfc/rfc7322#section-4.8.6.2)

- Correct a few typos

# Version 7.0.1

- Corrected a mistake in the contributors section

# Version 7.0.0

As a major release and the first update to the specification in 20 years, there a many changes in this version.

This version is the first version to use [semantic versioning](https://semver.org/).
7 was chosen as the new major version number because 1 through 6 were each used previously, some for released standards and others for abandoned drafts.

## New Expressivity

These features add new semantic power to FamilySearch GEDCOM, allowing 7 to represent concepts 5 could not represent

- The `NO` tag allows making negative assertions

- Media can now be combined with a FamilySearch GEDCOM file in a GEDZIP file

- Media can now link to the Internet as well as to local files

- Notes may now use a subset of HTML for basic rich-text markup

- All dates can now have date phrases, including date ranges and periods

- All dates can now have associated times

- Ages and all enumerated values (formerly called "controlled line_value choices") can now have additional user-text values and clarifying phrases

- Names and place names may now have multiple translations and transliterations, not just the few permitted by 5.5.1's `FONE` and `ROMN` tags

- Identifiers `RIN`, `RFN`, and `AFN` have been combined into a new `EXID`, which can now also be used to link to external databases and websites

- `ASSO` is now permitted under events as well as individuals and families

- `CREA`tion dates can now be recorded (along with the existing `CHAN`ge dates)

- New enumerated values were added, including 
    - `SEX X` for intersex persons
    - Eight new `ROLE`: `CLERGY`, `FRIEND`, `GODP`, `NGHBR`, `OFFICIATOR`, `PARENT`, `WITN`
    - a new `NAME`.`TYPE`: `PROFESSIONAL`
    - `OTHER` with user-defined text to all enumerated values that lacked that before

- Ages may now be expressed in weeks, as well as years, months, and days; former age terms (CHILD, INFANT, and STILLBORN) have been moved to the new `PHRASE` structure

- `FAM`.`FACT` can be used to express general family attributes

- Time may now either be in local time or in UTC

- Some common extensions are now standard:
    - `SDATE` is a sort-by date
    - `UID` is a globally-unique identifier for a record or event
    - `INIL` is the "initiatory" ordinance of The Church of Jesus Christ of Latter-Day Saints
    - `ASSO` now covers previous more-versatile `_ASSO` usage

- Pointer-payload structures may now use the special pointer `@VOID@` to indicate that there is no record for it to point to in this document. This can be used to flag what has been omitted or in combination with a `PHRASE` or `NOTE` to describe what would be pointed to informally.

- Inline `NOTE`s may now have `SOUR`ces.

- Places may now have `EXID`, enabling referencing external place authorities.

## New flexibility

- The following are now optional, not required: `HEAD`.`SOUR`, `HEAD`.`SUBM`, `FILE`.`FORM`

- All text payloads may contain line breaks via the `CONT` tag

- `PHON`, `EMAIL`, `FAX`, and `WWW` no longer require an `ADDR`

## New Compatibility

Earlier versions of GEDCOM predated language tags, media types, and Unicode became international standards. This version adopts those standards over GEDCOM's previous solutions for these purposes:

- `LANG` payloads are now language tags, as defined in [IETF BCP 47](https://tools.ietf.org/html/bcp47) with [tag parts](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) registered by the IANA.

- `ROMN` and `FONE` are now merged into `TRAN`, which also uses IETF BCP 47

- Media types are now [IANA Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)

- [UTF-8](https://www.unicode.org/versions/latest/) is now the only permitted character encoding

- Permitted characters are now defined and align with other formats like [XML](https://www.w3.org/TR/xml11/#NT-RestrictedChar)

- All structure types and enumerated values now have a defined IRI, for greater compatibility with GEDCOM-X and various linked-data and RDF-related standards.

## New Extensibility

- Every standard tag now has a single "default" meaning, even if it also has additional meanings in other contexts. Tags conforming to this default meaning can now be used by extensions as substructures of structures with extention tags.

- Extension tags remain in a backwards-compatible way, but should additionally be paired with a URI to avoid name collisions and provide documentation.

## Refactoring

- All length limits (on lines, payloads, and records) are removed.
    The 99-level limit has been removed.
    The `CONC` tag, which was only present to work around line length limits, has been removed.

- All `{0:3}` cardinalities have been replaced with `{0:M}` instead

- Free-text `ASSO`.`RELA` has been replaced by enumerated value `ASSO`.`ROLE`; former semantics are available through the `OTHER` enumerated value and associated `PHRASE` tag

- The case and permitted characters of tags, cross-reference identifiers, and enumerated values are now standardized

- Date escapes are now date keywords

- `@@` is only used if `@` is the first character of a text-valued payload.

- Obsolete tags `SUBN`, `HEAD`.`FILE`, `HEAD`.`CHAR`, `HEAD`.`GEDC`.`FORM`, and `CHAN`.`NOTE`.`SOUR` have been removed

- Age phrases are now only phrases, not long-hand terms for specific age ranges

- Previously registered values (APPROVED_SYSTEM_ID, RECEIVING_SYSTEM_NAME, etc) are kept as-is if present; new ones are URIs instead of having a separate registration process

- `RESI` may have a payload, just as all other attributes may

- `CROP` is now allowed under image-valued `OBJE` to indicate a region of interest within an image

- Temple codes are no longer in use, and have been replaced with temple names.

- The different kinds of notes in GEDCOM 5.5.1 (unsourced, sourced, and shared) have been simplified into just two and given separate tags (`NOTE`, and `SNOTE`) and clarifying text

## Ambiguities resolved

Various ambiguities were identified in version 5.5.1: some due to poor wording, some due to seemingly-conflicting information being presented in different places, and some due to certain cases not being mentioned at all. The following ambiguities have been resolved in 7.0:

- Use of white-space in lines, line values, ages, and dates is now defined.

- Dual-year dates were used with widely different semantics and have been replaced by more flexibility in date phrases.

- `SEX` is now unambiguously biological sex at birth; all other related concepts (gender identity, sexual preference, sex reassignment, etc) are time-varying attributes and to be stored in an individual attribute instead

    Note that new tags were not introduced for gender-related attributes. It is not yet clear what the correct set of attribute types should be given the evolving and regionally-specific understanding of these concepts. The generic `FACT` is recommended for these concepts instead. 

- The meaning of `HUSB` and `WIFE` structures in `FAM`ily units without a single husband and wife is now defined.
    
    Note that these tags were not converted to `SPOU` in the 7.0 release because of existing age-at-event structures that depend upon them and the bundled nature of relationship assertions present in a single `FAM` record. A reworking of relationship structures is contemplated for a future release.

- `NOTE`, `SOUR`, and `OBJE` no longer have a "can be record or structure, you pick" design ambiguity

- The various bespoke grammars used in the spec have been replaced with just two: ABNF for payload- and line-level syntax, and a clarified version of the example-like nesting grammar used since version 5.

- All examples in the spec now follow the spec.

- All text suggesting "but some people don't follow the spec, so you should also..." has been removed, including
    - no longer suggest exceptions to the "preferred first" rule
    - no longer suggest exceptions to the whitespace rules

- Byte-order mark is recommended, but not required

- Single-digits years are allowed.

- Correct various inaccuracies in the descriptions of non-Gregorian calendars.

- `CONT` may have an empty payload.

- `CONT` cannot be reordered to follow substructures.

- Empty payloads and missing payloads are considered equivalent

- Removed self-contradictions in spec, including
    - The tag is `EMAIL`, not `EMAI`
    - `ASSO` can only point to `INDI`, not to `SUBM`

- Name pieces are not comma separated.


## Specification refactoring

- Significant reordering of presentation generally

- Terminology updated to match modern usage, including

    - "GEDCOM transmission" is now "dataset"
    - "line value" is now "payload", and unambiguously refers to full payload after un-escaping `@@` and merging on `CONT`
    - terms "structure", "substructure", "superstructure", "record" are now better defined and more consistently used
    - clean separation between the conceptual idea of a structure and the syntactic idea of a line

- Escapes (which last had special semantic meaning in 5.3) have been removed

- Each structure is described once, not in two or three places as was done in version 5.5.1. Where possible, 5.5.1 wording was preserved.

- References to future use of colons and exclamation marks in cross-reference identifiers removed; cross-reference identifiers instead limited to the upper-case ASCII alphanumerics.

- Called out specific use cases, including

    - The universal "preferred first" rule does apply to picking profile pictures and display names.
    - `ALIA` is for pointers, not for `NAME`s with `TYPE AKA`
    


# Version 5.5.1

This version predates semantic versioning and despite the number is a major, not patch, release

## Modifications in Version 5.5.1

- Editorial corrections.

- Added **continuation tags** to the **header** copyright tags (see <<HEADER>>, page 23.)

- Added **email**, **fax**, and **web page** addresses to the **address** structure (see <<ADDRESS_STRUCTURE>>, page 31.)

- Added a **status** tag to the **child to family link** (see <<CHILD_TO_FAMILY_LINK>>, page 31.)

- Added a **restriction** notice tag to the **family record** to allow a source database to indicate why data may not have been supplied in the transmission. (see <<FAMILY_RECORD>>, page 24.) Also added a restriction notice tag to the <<EVENT_DETAIL>> structure page 32 to allow an event to be flagged so that it can be treated in special ways such as not to be printed on reports. 

- Added additional subordinate structure to the **personal name structure** (see <<PERSONAL_NAME_STRUCTURE>>, page 38.) These changes are in preparation for handling more varied cultures as we move into the unicode character set environment.

- Added subordinate map coordinates and other additional changes to the **place structure** (see <<PLACE_STRUCTURE>>, page 38.) These changes are in preparation for handling more varied cultures as we move into the unicode character set environment and to allow recording of map coordinates to places such as burial cites.

- Added a subordinate affiliated **religion** tag to the **event detail** substructure (see <<EVENT_DETAIL>>, page 32.)

- Added a generic **FACT** tag to the individual attribute structure. Previously, the generic EVEN tag was used. The FACT was added to give a semantic difference between generic events and generic facts or characteristics (see <<INDIVIDUAL_ATTRIBUTE_STRUCTURE>>, page 33.)

- **Removed** the option for **encoding embedded multimedia** objects. A file reference to a multimedia file and its subordinate format and media types were added to the multimedia record. Multiple file references can now be used to group related multimedia objects. This changed the multimedia link by placing the FORM tag subordinate to the FILE tag rather than at the same level. The BLOB tag was eliminated. See FILE tag and its subordinate FORM tag used in the <<MULTIMEDIA_RECORD>> page 26 and the <<MULTIMEDIA_LINK>> page 37.

- The following tags were added:

    |           |                               |
    |-----------|-------------------------------|
    | **EMAIL** | electronic mailing address |
    | **FAX**   | FAX address |
    | **FACT**  | A fact or characteristic. |
    | **FONE**  | Phonetic variation of a text. |
    | **ROMN**  | Romanized variation of a text. |
    | **WWW**   | Web Home page address. |
    | **MAP**   | Pertaining to maps. |
    | **LATI**  | value of a latitudinal coordinate pertaining to the place of an event |
    | **LONG**  | value of a longitudinal coordinate pertaining to the place of an event. |
    
- The following tag was removed:
    
    BLOB

# Version 5.5

This version predates semantic versioning and despite the number is a major, not minor, release. It skipped a number, as version 5.4 was only a discussion draft and was not released for implementation.

## Modification in Version 5.5. as a result of the 5.4 (draft) review 

- Added tags for storing detailed address pieces under the address structure.

- Added nickname and surname prefix name pieces to the personal name structure.

- Added subordinate source citation to the note structure.

- Changed the encoding rules and the structure for including embedded multimedia objects.

- Added a RIN tag to the record structures. The RIN tag is a record identification assigned to the record by the source software. Its intended use is to allow for automated access to that record upon receipt of return transactions or other reconciliation processes.

- The meaning of a GEDCOM tag without a value on its line depends on its subordinate context for any assertions intended by the researcher. For example, In an event structure, a subordinate DATE and/or PLACe value imply that an event happened. However, a subordinate NOTE or SOURce context by themselves do not imply that the event took place. For a researcher to indicate that an event took place without knowing a date or a place requires that a Y(es) value be added to the event tag line. Using this convention protects GEDCOM processors which may remove (prune) lines that have no value and also no subordinate lines. A N(o) value must not be used on an event tag line to assert that the event never happened. This requires the definition of a different tag.

- Returned the calendar escape sequence to support alternate calendars.

- The definition of the date value was refined to include many of the potential ways in which a person may define an imprecise date in a free form text field. Systems which guide users through a date statement should not result in such a precise way of stating an imprecise date. For example, if software was to estimate a marriage date based on an algorithm involving the birth date of the couple's first child, hardly needs to say "EST ABT 1881".

- The following tags were added:
    
    ADR1, ADR2, CITY, NICK, POST, SPFX

## Changes introduced or Modified in Draft Version 5.4

Some changes introduced in GEDCOM draft version 5.4 are not compatible with earlier 5.x draft forms. Some concepts have been removed with the intent to address them in a future release of GEDCOM. The following features are either new or different:

- The use of the SCHEMA has been eliminated. Although the schema concept is valid and essential to the growth of GEDCOM, it is too complex and premature to be implemented successfully into current products. Implementing it too early could cause developers to spend a great deal of resources programming something that would be outdated very quickly. Object definition languages are likely to contribute to meeting these needs.

- The EVENT_RECORD context has been deleted. This context was intended to support the evidence record concept in the Lineage-Linked GEDCOM Form, which ended up being more complicated than first supposed. Understanding the difference between the role of a source record and the role of a so-called evidence record requires further study.

- Non-standard tags (see <NEW_TAG>, page 50) can be used within a GEDCOM transmission, provided that the first character is an underscore (for example \_NUTAG). Non-standard tags should be used only when structured information cannot be represented using existing context. Using a Note field is a more universal way of transmitting genealogical data that does not fit into the standard GEDCOM structure.

- The SOURCE_RECORD structure was simplified into five basic sections: data or classification, author, title, publication facts, and repository. The data or classification section contains facts about the data represented by this source and is used to analyze the collection of sources that the researcher used. The author, title, publication facts, and repository sections provide free-form text blocks that inform subsequent researchers how to access the source data that the original researcher used.

- The <<SOURCE_CITATION>> structure is placed subordinate to the fact being cited. It is generally best if the source citation contains only information specific to the fact being cited and then points to the more general description of the source, defined in a SOURCE_RECORD. This reduces redundancy, provides a way of controlling the GEDCOM record size, and more closely represents the normalized data model. Systems that represent sources using the AUTHor, TITLe, PUBLication, and REPOsitory descriptions can and should always pass this information in GEDCOM using the SOURce record pointed to by the <<SOURCE_CITATION>>. Systems that do not represent source information in these categories should provide the following information as unstructured text using the tags, TITL, AUTH, PUBL, and REPO, respectively, within the text: 

    - A descriptive title of the source
    - Who created the work
    - When and where was it created
    - Where can it be obtained or viewed

- Some attributes of individuals such as their EDUCation, OCCUpation, RESIdence, or nobility TITLe need to be described using a date and place. Therefore, the structure to describe the attributes was formatted to be the same as for describing events. That is, these attributes are further defined using a date, place, and other values used to describe events. (See <<INDIVIDUAL_EVENT_STRUCTURE>>, page 31.)

- The LDS ordinance structure was extended to include the place of a living LDS ordinance. The TYPE tag line was changed to a STATus tag line. This allows statements such as BIC, canceled, Infant, and so forth to be removed from the date line and be added here under the STATus tag. (See <LDS_(ordinance)_DATE_STATUS>, page 45, 46) where (ordinance) represents any of the following: BAPTISM, ENDOWMENT, CHILD_SEALING, or SPOUSE_SEALING.

- Previous GEDCOM 5.x versions overloaded the FAMC pointer structure with subordinate events which connected individual events and an associated family. An adoption event, for example, was shown subordinate to the FAMC pointer to indicate which was the adoptive family. The sealing of child to parent event (SLGC) was also shown in this manner. GEDCOM 5.4 recognizes that these are events and should be at the same level as the other individual events. To show the associated family, a subordinate FAMC pointer is placed subordinate to the appropriate event. (See <<INDIVIDUAL_EVENT_STRUCTURE>> page 31 and LDS_INDIVIDUAL_ORDINANCE at page 32.)

- The date modifier (int) was added to the date format to indicate that the associated date phrase has been interpreted and the interpretation follows the int prefix in the date field. The date phrase is also included in the date value enclosed in parentheses. (See <DATE_APPROXIMATED>, page 40.)

- The <AGE_AT_EVENT> primitive definition now includes the key words STILLBORN, INFANT, and CHILD. These words should be interpreted as being an approximate age at an event. (See <AGE_AT_EVENT>, page 37.)

- The family event context in the FAMily record now allows the ages of both the husband and wife at the time of the event to be shown. (See FAM_RECORD page 24)

- The <<PERSONAL_NAME_STRUCTURE>> structure now allows name pieces to be specifically identified as subordinate parts of the name line. Most products will not use subordinate name pieces. A nickname can now be included on the name line by enclosing it in double quotation marks. Note: Systems using the subordinate name parts must still provide the name structure formed in the same way specified for <NAME_PERSONAL> (see page 48.)

- A submission record was added to GEDCOM to enable the sending system to transmit information which will enable the receiving system to more appropriately process the GEDCOM data. The format currently designed for the submission record was created specifically for TempleReady™ system and for GEDCOM files being downloaded from Ancestral File™. (See SUBMISSION_RECORD, page 27.)

- A RESTRICTION (RESN) tag and a <RESTRICTION_NOTICE> primitive were added to the INDIVIDUAL_RECORD context. This allows some records in Ancestral File to be marked for privacy (indicating some personal information is not included) and some records to be marked as locked (indicating that Ancestral File will not make changes to the record without authorization from an assigned record steward).

- The following tags are no longer used in the Lineage-Linked Form:
    
    ARVL, BROT, BUYR, CEME, CNTC, CPLR, DEFM, DPRT, EDTR, FIDE, FILM, GODP, HDOH, HEIR, HFAT, HMOT, INFT, INDX, INTV, ISA, ISSU, ITEM, LABL, LCCN, LGTE, MBR, NAMS, NAMR, OFFI, ORIG, OWNR, PERI, PORT, PWIF, PUBR, RECO, SELR, SEQU, SERS, SIBL, SIGN, SIST, SITE, TXPY, XLTR, WFAT, WITN, WMOT, AUDIO, IMAGE, PHOTO, SCHEMA, VIDEO

- The following tags were added:
    
    BLOB, CTRY, CREM, FCOM, GIVN, NPFX, NSFX, OBJE, PEDI, RELA, RESI, RESN, SUBN, SURN, STAT


# Version 5.3

This version predates semantic versioning and despite the number is a major, not patch, release.
It was the first version to receive widespread adoption and the oldest version for which files may be readily found online.

