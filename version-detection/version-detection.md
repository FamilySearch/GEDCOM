# GEDCOM Version Detection

GEDCOM, an acronym standing for Genealogical Data Communication, is a format for exchanging genealogical data
in plain text files.  Such data is typically transported as a file (whether via removable storage or via a
protocol such as HTTP).  Since its origin in 1984, there have been many versions of the format, including
versions adding support for character sets including UTF-8 and UTF-16.  However, each version has had its
own specification document without regard for backwards compatibility.

This led to the need to detect which version was used when given an arbitrary GEDCOM file, to understand how
to parse the data.  The GEDCOM format itself does include a version identifier in the content, so that
a parser can detect the correct version and parse the file accordingly.  This document specifies a version
detection algorithm and provides references to the more specific format specifications.

## Commonalities

Every GEDCOM file, regardless of version, is a text file that conforms to the following general structure:

- The document is organized as a sequence of **lines** separated by ASCII line terminators (U+000A, U+000D, or both). Blank lines are ignored.
- Each line contains several components, separated by spaces (U+0020):
  1. A required **level**, which is a non-negative integer encoded using ASCII digits.
    - The first line's level is 0.
    - Each other line's level is between 0 and 1 + *x* inclusive, where *x* is the level of the immediately preceding line.
  2. An optional **identifier**, which begins and ends with a COMMERCIAL AT (U+0040 `@`) and contains no internal line terminators or COMMERCIAL ATs.
  3. A required **tag**, which is a string of one or more printable ASCII characters (U+0021 through U+007E), excluding the COMMERCIAL AT (U+0040 `@`).
  4. An optional **value**, which is a string of zero or more characters; all characters are permitted except ASCII line terminators (U+000A and U+000D).
- Each line represents a structure. Any line with level *x* > 0 represents a substructure of the structure represented by the nearest preceding line with level *x* − 1.

Beyond these commonalities, each GEDCOM version differs in details and is described by its own specification.
Version specifications typically describe both the meaning of various structures
and provide additional serialization details, including whether blank lines are allowed, whether multiple spaces can be used to separate line components, limits on tag, identifier, and value lengths and characters, etc.


## Version detection

For succinctness, we use the following notation: `ABC`.`DEF`.`GHI` means "a structure with tag `GHI` that is a substructure of a structure with tag `DEF` that is a substructure of a structure with tag `ABC` which is the first structure in the document."

If there is a structure `HEAD`.`GEDC`.`VERS`
then the specification describing the GEDCOM version in the file is determined by the longest matching prefix of the value of that structure from the following table:

Prefix | Reference
----------- | ---------
"`7.0`"     | [The FamilySearch GEDCOM Specification, 7.0.3](https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf)
"`5.6`"     | [THE GEDCOM SPECIFICATION, DRAFT Release 5.6](https://gedcom.io/specifications/Gedcom5.6.pdf)
"`5.5.1`"   | [THE GEDCOM STANDARD, Release 5.5.1](https://gedcom.io/specifications/ged551.pdf)
"`5.5`"     | [THE GEDCOM STANDARD, Release 5.5](https://gedcom.io/specifications/ged55.pdf) 
"`5.4`"     | [THE GEDCOM STANDARD, DRAFT Release 5.4](https://gedcom.io/specifications/Gedcom5.4.pdf)
"`5.3`"     | [THE GEDCOM STANDARD, DRAFT Release 5.3](https://chronoplexsoftware.com/gedcomvalidator/gedcom/gedcom-5.3.pdf)
"`5.0`"     | [THE GEDCOM STANDARD, DRAFT Release 5.0](https://gedcom.io/specifications/Gedcom5.0.pdf)
"`4`"       | [THE GEDCOM STANDARD, Release 4.0](https://gedcom.io/specifications/Gedcom4.0.pdf)
Otherwise   | [GENEALOGICAL DATA COMMUNICATION (GEDCOM), Release 3.0](https://gedcom.io/specifications/Gedcom3.0.pdf)

If there is no structure `HEAD`.`GEDC`.`VERS` but there is a structure `HEAD`.`SYST` then the specification describing the GEDCOM version in the file is [PAF GEDCOM Specifications](https://armidalesoftware.com/GEDCOM/PAF-GEDCOM-Specifications.pdf) section 4.

If there is neither `HEAD`.`GEDC`.`VERS` nor `HEAD`.`SYST` then the specification describing the GEDCOM version in the file is [GENEALOGICAL DATA COMMUNICATION (GEDCOM), Release 3.0](https://gedcom.io/specifications/Gedcom3.0.pdf).

### Extensions and non-standard versions

Various third-party extensions to and variants of the standard GEDCOM versions have been published. These may be detected as follows:

Specification | Detection                         | Notes
--------------|-----------------------------------|----------------------------
[GEDCOM Event-Oriented Form](http://bartonstreet.com/deadends/EventGEDCOMDraft1.0.pdf) | `HEAD`.`GEDC`.`FROM`.`FORM` with value "`EVENT`" | Based on *THE GEDCOM STANDARD, DRAFT Release 5.3*, but not compatible with it.
[THE GEDCOM 5.5.5 Specification with Annotations](https://www.gedcom.org/specs/GEDCOM555.zip) | `HEAD`.`GEDC`.`VERS` with value "`5.5.5`" | Based on *THE GEDCOM STANDARD, Release 5.5.1* with only a few changes, mostly banning certain data that is permitted in that standard.
[GEDCOM 5.5EL](http://wiki-de.genealogy.net/Gedcom_5.5EL) | `HEAD`.`GEDC`.`VERS` with value "`5.5 EL`" | A strict superset of *THE GEDCOM STANDARD, Release 5.5*.
(none known) | `HEAD`.`GEDC`.`VERS` with value "`5.5.1 EL`" | Makes the same changes to *THE GEDCOM STANDARD, Release 5.5.1* that *GEDCOM 5.5EL* makes to *THE GEDCOM STANDARD, Release 5.5*.
(none known) | The first structure has tag "`HEADER`" | A variant of another GEDCOM version (detected using the value of `HEADER`.`GEDCOM`.`VERSION`, or *THE GEDCOM STANDARD, DRAFT Release 5.3* if that structure does not exist) where all tags have been replaced by the longer names for the tags found in the appendix of the specification of that version which lists tag names and meanings.



## IANA Media Type Registration

This section defines the "text/gedcom" media type for use with protocols such as HTTP or email, to identify content
as being a GEDCOM file.  The Internet Assigned Numbers Authority (IANA) maintains the
[registry of assigned media types](https://www.iana.org/assignments/media-types/media-types.xhtml).

The following registration for "text/gedcom" is specified using the template defined in
[RFC 4288](https://www.rfc-editor.org/rfc/rfc4288).

**Name**: text/gedcom

**Parameters**:

* **charset**: As specified in [RFC 2046, section 4.1.2](https://www.rfc-editor.org/rfc/rfc2046.html#section-4.1.2).
  The parameter is not used when payload is present because the charset information is transported inside
  the payload.  However, should charset negotiation be needed, and no Accept-Charset header or equivalent
  is supported, it may be used in a media range used in a request, such as in an Accept header.

  Many earlier versions of GEDCOM specified an "ANSEL" character set, which does not have an assignment in 
  the [IANA Character Sets registry](https://www.iana.org/assignments/character-sets/character-sets.xhtml)
  and so cannot be used by either the charset parameter or Accept-Charset.  Since UTF-16 support was added
  in 1993, UTF-8 has been supported in GEDCOM since 1999, and the latest version of GEDCOM only supports UTF-8,
  it is not expected that ANSEL would need to be requested.

* **version**: The GEDCOM specification version.  The parameter is not used when payload is present because
  the version information is transported inside the payload.  However, should version negotiation be needed,
  it may be used in a media range used in a request, such as in an Accept header.

**Encoding considerations**: Text in a specified character set.

**Security considerations**:
Can contain directives to read files on the local hard drive and send GET requests to HTTP and HTTPS URLs.
No active content, no file modification directives, no information-sharing directives.
Commonly used to store genealogical information, which may include personal and sensitive information as well
as information commonly used to create security questions. This information is not encrypted or otherwise
protected by GEDCOM itself; hence, it falls on the software and persons managing the files to ensure they are
kept confidential if they contain such information.

**Interoperability considerations**: The GEDCOM version is encoded in the content, and an algorithm is provided
for detecting the version.

**Application usage**: GEDCOM is used by family history and related applications, including family trees,
one-place and one-name studies, and historical analysis of interrelated individuals.

**Fragment Identifier**: not used

**Restrictions on Use**: none

**Provisional Registration**: This media type is intended to be permanent.

**Magic numbers**: One of the following sequences of bytes should be present at the start of the file:
* 9 octets: EF BB BF 30 20 48 45 41 44
* 8 octets: 30 20 48 45 41 44
* 14 octets: FF FE 30 00 20 00 48 00 45 00 41 00 44 00
* 12 octets: 30 00 20 00 48 00 45 00 41 00 44 00
* 14 octets: FE FF 00 30 00 20 00 48 00 45 00 41 00 44
* 12 octets: 00 30 00 20 00 48 00 45 00 41 00 44

**File Extension**: .ged

**Mac OS File Type Code**: none

**Intended Use**: Common

Used for exchanging and storage of computerized genealogical data. Primary use is for inter-operable software products to assist genealogists, historians, and other researchers. Secondary use is as a long-term storage format for preserving genealogical information.
