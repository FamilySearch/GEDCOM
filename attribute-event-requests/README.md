# Proposed new Family and Individual Attributes and Events

The documents in this folder track various proposed additions to the set of Family Attributes, Family Events, Individual Attributes, and Individual Events in FamilySearch GEDCOM 7.

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
2. A table of the major proposals in the document.
3. A section for each proposal that is not yet in the specification, with evidence of the three criteria above

To propose, support, or oppose the addition of a new structure type to a future version of FamilySearch GEDCOM 7, please submit a **pull request** editing the appropriate document. If you are not comfortable submitting a pull request, an **issue** or **discussion** can be used instead.

## Guide on the table

Each proposal should have one row in the table, with five cells:

1. **G7 Tag** is set only once present in the specification. The special value "\*" is used to indicate attributes or events that are present in a different way, such 

2. **v7.x** is set only once present in the specification

3. **Name** is a proposed short English name (suitable for use in a label). If the concept is uncommon in English-speaking cultures, the name may be that used in the language of a culture where it is common, transliterated into the Latin script as needed.

4. **URIs** is the concept's identifiers from other specifications, such as GEDCOM-X, FamilySearch API, etc. If several, the markdown should have them on one line separated by line break tags, like this:

    ````
    | | | Example | `http://example.com/uri1`<br/>`http://example.com/uri2` | |
    ````

5. **Notes** about other ways this information is encoded in FamilySearch GEDCOM 7 (other than as an event or attribute)

When an event or attribute type that is part of GEDCOM is present in a family history system that does not use GEDCOM, it is appropriate to include it in the table to make the relationship to GEDCOM explicit.

## Guide on the per-proposal sections

Open with the same header as a **Name** field in the table, preceded by two hashtags, like `## Example`

Have the following subsections:

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

