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

## Charset Detection

To locate the version in the content, the character set must first be determined.  
A GEDCOM file starts with the character "0" in some character set, possibly prefixed by a
Byte Order Mark (BOM) indicating the character set.

Thus, charset detection can be done by reading the first two characters of the file, and using the table below:

Initial bytes | Charset
------------- | -------
0xFF 0xFE     | [UTF-16LE](https://www.rfc-editor.org/info/rfc2781) (with BOM)
0x30 0x00     | [UTF-16LE](https://www.rfc-editor.org/info/rfc2781) (without BOM)
0xFE 0xFF     | [UTF-16BE](https://www.rfc-editor.org/info/rfc2781) (with BOM)
0x00 0x30     | [UTF-16BE](https://www.rfc-editor.org/info/rfc2781) (without BOM)
0xEF 0xBB     | [UTF-8](https://www.rfc-editor.org/info/rfc3629) (with BOM 0xEF 0xBB 0xBF)
Otherwise     | [UTF-8](https://www.rfc-editor.org/info/rfc3629) (without BOM)

## Version Detection

To detect the GEDCOM file version, perform the steps below, using the charset determined
above.  If the end of the file is reached before
all steps can be successfully completed, the file is not a valid GEDCOM file.

1. Read until "1 GEDC" is detected.

2. Read until "2 VERS " (including the trailing space) is detected.

3. Read a string of characters up to, but not including, a carriage return (U+000D) or line feed (U+000A).  The resulting string is the version identifier.

4. Look up the string in the table below:

String  | Reference
------- | ---------
"3.0"   | [GENEALOGICAL DATA COMMUNICATION (GEDCOM), Release 3.0](https://web.archive.org/web/20200705155231/https://chronoplexsoftware.com/gedcomvalidator/gedcom/gedcom-3.0.pdf)
"4.0"   | [THE GEDCOM STANDARD, Release 4.0](https://web.archive.org/web/20200705182809/https://chronoplexsoftware.com/gedcomvalidator/gedcom/gedcom-4.0.pdf)
"5.0"   | [THE GEDCOM STANDARD, DRAFT Release 5.0](https://web.archive.org/web/20200705085334/https://chronoplexsoftware.com/gedcomvalidator/gedcom/gedcom-5.0.pdf)
"5.3"   | [THE GEDCOM STANDARD, DRAFT Release 5.3](https://web.archive.org/web/20100722012217/http://ftp.aset.psu.edu/genealogy/gedcom55/gedstand.t82)
"5.4"   | [THE GEDCOM STANDARD, DRAFT Release 5.4](http://www.lege.com/gedcom54.html)
"5.5"   | [THE GEDCOM STANDARD, Release 5.5](https://gedcom.io/specifications/ged55.pdf) 
"5.5.1" | [THE GEDCOM STANDARD, Release 5.5.1](https://gedcom.io/specifications/ged551.pdf)
"5.5.5" | [THE GEDCOM 5.5.5 Specification with Annotations](https://www.gedcom.org/specs/GEDCOM555.zip)
"5.6"   | [THE GEDCOM SPECIFICATION, DRAFT Release 5.6](http://www.daubnet.com/ftp/gedcom-56-english.pdf)
"7.0"   | [The FamilySearch GEDCOM Specification, 7.0.3](https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf)

5. Parse the entire payload according to the indicated specification.

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
  the charset information is transported inside the payload.  However, should version negotiation be needed,
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
