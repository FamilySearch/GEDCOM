# Proposing new Family and Individual Attributes and Events

The documents in this folder track various proposed additions to the set of Family Attributes, Family Events, Individual Attributes, and Individual Events in FamilySearch GEDCOM 7.
It includes all current structures of those types for ease of reference.
It may include links to other systems or standards that use these structures in ways other than GEDCOM when such uses have been identified and contributed here.

There is an inherent tension between completeness (which would recommend including every event and attribute type we can define) and simplicity (which would recommend including only a few of the the most important options). In 2023. the GEDCOM Steering Committee identified the following criteria for a proposal to be added to the specification.

In general, events and attribute are accepted for inclusion once the following criteria are met:

1. **Valuable**: they are present in historical records and are either defining aspects of a person's life or otherwise important for informing research or creating life summaries

2. **Absent**: they are meaningfully distinct from, and not merely a more detailed subtype of, existing structure types

3. **Used**: multiple family history applications with active user bases either use it now or have expressed a desire to add it as soon as it is available in the standard

New events and attributes are added in minor versions (7.1, 7.2, etc.).
Old events and attributes can be deprecated at any time, but can only be removed in major versions (8.0, 9.0, etc.)
It may be that some of the event and attribute types in 7.0 were included because they were also in 5.5.1 and do not meet these criteria and may be removed in 8.0 or beyond.

# Directions for using the documents in this folder

Each of the other four documents in this folder are structured as follows:

1. A brief opening, pointing back to this document.
2. A table of the current and proposed structure types discussed in the document.
3. A section for those proposals for which additional information has been supplied.

To propose, support, or oppose the addition of a new structure type to a future version of FamilySearch GEDCOM 7, please submit a [pull request](https://github.com/FamilySearch/GEDCOM/pulls) editing the appropriate document. If you are not comfortable submitting a pull request, an [issue](https://github.com/FamilySearch/GEDCOM/issues) or [discussion](https://github.com/FamilySearch/GEDCOM/discussions) can be used instead.

If there is no document here for the type of structure you want to suggest, please use the [issues tracker](https://github.com/FamilySearch/GEDCOM/issues) instead.

## Guide on the table

Each proposal should have one row in the table, with four cells:

1. **G7 Tag** is set only once present in the specification.
    
    The special value "\*" is used to indicate attributes or events that are present in a different way, such as with a set of structures and payloads.

2. **Since** is set only once present in the specification, and identifies which version of GEDCOM first provided the structure.
    
    If the structure was provided in an earlier version of GEDCOM but removed before the current version, the *since* field is left blank.

3. **Name** is a short English name (suitable for use in a label) for the event or attribute type. If the concept is uncommon in English-speaking cultures, the name may be that used in the language of a culture where it is common, transliterated into the Latin script as needed.
    
    If there is a subsection for this structure in the details section, make this a hyperlink to it by
    
    - making a slug from the name by
        - lower-casing the name
        - replacing non-alphanumeric characters with hyphens
    - putting the name in brackets, then putting in parentheses a hash and the slug, like `[Name](#name)`

4. **Notes** clarifying the first three cells, such as explaining which structures are used if the tag was "\*" or noting a difference between name and meaning.

## Guide on the per-proposal sections

Open with the same header as a **Name** field in the table, preceded by two hashtags, like `## Example`

Structure types that are already part of the GEDCOM specification may contain just a list of ways the same structure is referenced in other (non-GEDCOM) formats and tools.
All other structure types should have the following subsections:

1. `### Description`

    A succinct but clear description such as might go in the specification if accepted.
    
    *In [specification X](https://example.com/specificationx.html> as* "The description used by specification X"

2. `### Value`

    Found in the following historical records:
    
    - A list of records that include it, such as
    - US Census, 1880 through 1940
    - Swedish grave markers, circa 1400
    
    Any additional explanation of value, such as how it is used to inform research or display information.
    
3. `### Absence`

    The most closely related structures are:
    
    - `TAG`: description of similarity and difference
    
    Related proposals include

    - Name: description of similarity and difference

4. `### Used`

    - *Application name* currently uses this in its user interface and internal file format, but removes it during GEDCOM export
    
    - *Application name* exports this with an `EVEN` tag with `TYPE whatever`

    - *Application name* exports this with an extension tag `_EX`, defined in <https://example.com/defining/EX.yaml>

