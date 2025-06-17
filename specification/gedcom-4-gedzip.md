# The FamilySearch GEDZIP file format {#gedzip}

It is often useful to transmit a dataset together with a set of external files.
The FamilySearch GEDZIP 7.0 file format is provided for this purpose.
Version 7.0 was the first version of GEDZIP released; the version number of a GEDZIP file is the same as the version number of the dataset it contains.

A GEDZIP file is a zip archive, as defined by [the .ZIP File Format Specification](http://www.pkware.com/appnote)
and standardized by [ISO/IEC 21320-1:2015](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=60101).

Each GEDZIP file contains the following entries:

- An entry with name `gedcom.ged` containing a data stream.

- An entry for each *local file* `g7:type-FilePath` payload in `gedcom.ged`, with the same zip *file name* as the payload.
    If there is a local file named `gedcom.ged`, it must be renamed to a new unused filename with the same extension prior to constructing the GEDZIP.

All file names inside a GEDZIP are case-sensitive UTF-8. Whereas a `g7:type-FilePath` [payload](#file-path)
must percent-escape characters in the file name that cannot appear literally in a URI reference or valid URL string, zip *file names*
are not percent-escaped.

Many other zip-based file formats (such as jar, epub, docx, GEDCOM-X) assign special meaning to the zip directory `META-INF` and the zip file names `MANIFEST.MF` and `META-INF/MANIFEST.MF`. These have no special meaning in GEDZIP and it is recommended that they not be used in a GEDZIP file, both to avoid confusing systems that look inside zip archives to determine their file type, and to leave open the possibility of their addition in a future version of this specification.

When saved as a file, a GEDZIP should use the filename extension `.gdz`.

Zip archives can encrypt their contained files' contents, with multiple encryption algorithms supported by the zip archive specification.
Encrypted GEDZIP files are a portable way to encrypt FamilySearch GEDCOM data.
Only contained file contents are encrypted by zip's encryption: the names and sizes of its contained files are not encrypted.
Encrypting the entire gdz file with an external encryption scheme can encrypt file names and sizes, but requires an external method for communicating the encryption scheme chosen.

:::note
A few details about the zip archive format are useful to fully understand GEDZIP:

- An archive can contain 1 or more files.
- Files within an archive can be added, removed, or updated individually without needing to re-process the rest of the archive. Libraries such as [libzip](https://libzip.org) allow applications to operate directly on the zip archive as if it were a normal directory tree.
- What the zip specification calls a "file name" is actually a local path and may contain directories.
- Directory separators are `/` internally and are converted to the appropriate form by the zip processing tool during zipping and unzipping. Because of this, unzipping a GEDZIP in any local directory results in all GEDZIP file paths working as-is for the resulting `gedcom.ged` without the need for any additional processing.
:::

