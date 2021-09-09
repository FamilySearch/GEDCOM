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

All GEDCOM versions are text files that conform to the following general structure:

- The document is organized as a sequence of **lines** separated by ASCII line terminators (U+000A, U+000D, or both)
- Each line contains several components, separated by spaces (U+0020):
  1. A required **level**, which is a non-negative integer encoded using ASCII digits.
    The first level is always 0.
    Each line's level is between 0 and 1 + the preceding line's level, inclusive.
  2. An optional **identifier**, which begins and ends with a COMMERCIAL AT (U+0040 `@`) and contains no internal line terminators or COMMERCIAL ATs. No two lines share the same identifier.
  3. A required **tag**, which is a string of one or more ASCII digits (U+0030 through U+0039 `9`-`0`), letters (U+0041 through U+005A `A`–`Z` and U+0061 through U+007A `a`–`z`), and underscores (U+005F `_`).
  4. An optional **value**, which may contain any non-line terminator character.
- Each line represents a structure.
- Any line with level *x* > 0 represents a substructure of the nearest preceding line with level *x* − 1.

Beyond these commonalities, each GEDCOM version differs in details and is described by its own specification.
Version specifications typically describe both the meaning of various structures
and provide additional serialization details, including whether blank lines are allowed, whether multiple spaces can be used to separate line components, limits on tag and identifier length and characters, etc.

## Character Width and Byte Order Detection

To efficiently locate the version in the content, one can first determine the character width and byte order
used in the file.  (The version detection algorithm can be done without this by trying all three possibilities
separately.)

A GEDCOM file starts with the character "0" in some character set, possibly prefixed by a
Byte Order Mark (BOM) indicating the character set.  The actual character set, however, does not matter
as version detection only requires knowing the character width and byte order.

Thus, the character width and byte order can be determined by reading the first two characters of the file,
and using the table below:

Initial bytes (hex) | Width | Order
------------------- | ----- | -------------
FF FE               | 2     | LE (Little-endian)
30 00               | 2     | LE (Little-endian)
FE FF               | 2     | BE (Big-endian)
00 30               | 2     | BE (Big-endian)
Otherwise           | 1     | (N/A)

## Version Detection

To detect the GEDCOM file version, perform the steps below, using the character width and byte order determined
above.  If the end of the file is reached before
all steps can be successfully completed, the file is not a valid GEDCOM file.

1. Read until one of the following byte sequences is detected ("1 GEDC"):

Width | Order | Byte sequence to look for           | Explanation
----- | ----- | ----------------------------------- | ------------
2     | LE    | 49 00 20 00 47 00 45 00 44 00 43 00 | "1 GEDC"
2     | BE    | 00 49 00 20 00 47 00 45 00 44 00 43 | "1 GEDC"
1     | (N/A) | 49 20 47 45 44 43                   | "1 GEDC"
1     | (N/A) | 49 20 53 59 53 54                   | "1 SYST"

2. If one of the first three rows above is matched, continue to step 3.  If instead the last line above ("1 SYST") is
   matched, skip to step 7 using the following specification:

* [PAF GEDCOM Specifications](https://armidalesoftware.com/GEDCOM/PAF-GEDCOM-Specifications.pdf) section 4

3. Continue reading bytes until the following byte sequence is detected ("2 VERS "):

Width | Order | Byte sequence to look for
----- | ----- | --------------------
2     | LE    | 32 00 20 00 56 00 45 00 52 00 53 00 20 00
2     | BE    | 00 32 00 20 00 56 00 45 00 52 00 53 00 20
1     | (N/A) | 32 20 56 45 52 53 20

4. Read the next 5 * Width bytes.

5. Convert the bytes read to a 5-byte sequence by dropping all 00 bytes. That is, using 1-based indices:

Width | Order | Transform
----- | ----- | ---------
2     | LE    | Keep bytes 1, 3, 5, 7, 9
2     | BE    | Keep bytes 2, 4, 6, 8, 10
1     | (N/A) | Keep bytes 1, 2, 3, 4, 5

6. Do a longest match using the table of GEDCOM versions below:

Byte sequence  | Explanation | Reference
-------------- | ----------- | ---------
37 2E 30       | "7.0"       | [The FamilySearch GEDCOM Specification, 7.0.3](https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf)
35 2E 36       | "5.6"       | [THE GEDCOM SPECIFICATION, DRAFT Release 5.6](https://gedcom.io/specifications/Gedcom5.6.pdf)
35 2E 35 2E 31 | "5.5.1"     | [THE GEDCOM STANDARD, Release 5.5.1](https://gedcom.io/specifications/ged551.pdf)
35 2E 35       | "5.5"       | [THE GEDCOM STANDARD, Release 5.5](https://gedcom.io/specifications/ged55.pdf) 
35 2E 34       | "5.4"       | [THE GEDCOM STANDARD, DRAFT Release 5.4](https://gedcom.io/specifications/Gedcom5.4.pdf)
35 2E 33       | "5.3"       | [THE GEDCOM STANDARD, DRAFT Release 5.3](https://chronoplexsoftware.com/gedcomvalidator/gedcom/gedcom-5.3.pdf)
35 2E 30       | "5.0"       | [THE GEDCOM STANDARD, DRAFT Release 5.0](https://gedcom.io/specifications/Gedcom5.0.pdf)
34             | "4.0", "4+" | [THE GEDCOM STANDARD, Release 4.0](https://gedcom.io/specifications/Gedcom4.0.pdf)
Otherwise      |             | [GENEALOGICAL DATA COMMUNICATION (GEDCOM), Release 3.0](https://gedcom.io/specifications/Gedcom3.0.pdf)

In addition, there are known to be files in the wild that use an unofficial format.  Some implementations may
wish to detect the following byte sequence as well which might conform to the specification below:

Byte sequence  | Explanation | Reference
-------------- | ----------- | ---------
35 2E 35 2E 35 | "5.5.5"     | [THE GEDCOM 5.5.5 Specification with Annotations](https://www.gedcom.org/specs/GEDCOM555.zip)

7. Parse the entire payload according to the indicated specification.

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
