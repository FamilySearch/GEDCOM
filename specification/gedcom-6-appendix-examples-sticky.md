# Appendix B: GEDCOM Examples


## General Remarks

This appendix collects practical GEDCOM 8 examples to help users and developers see how the data structures can be applied in realistic (and sometimes lightly humorous) situations. Each example is tied to a specific `TEMPLATE` type and includes participants (via `STICKY`s), showing how GEDCOM 8 organizes complex, real-life, historical or genealogical data.

Use the index below to jump to an example that matches the kind of `TEMPLATE` you're working with.  
All examples follow the same pattern: a short explanation, followed by the full GEDCOM structure using fenced **gedcom** blocks for clarity.  

Click 🔝 to return here from any example.

### Things to remember:
- As the examples are really large, on some places the end part of a structure is removed, and replaced bij a line with **~ ~ ~**. So that means the examples can not be validated as correct GEDCOM 8. Some examples have complete records, they are recognizable by the end-lines `CREA` and `CHAN`.
- As `SPLAC` is now assigned to be implemented for GEDCOM 8, we use `SPLAC` here for places, and no longer the GEDCOM 7 `PLAC` tags.
- For the same reason as for `SPLAC`, Names are represented in the new GEDCOM 8 `NAME` format. But as a name like `John de Wit` can have many lines in the new format, here too the last lines of the new `NAME_STRUCTURE` are sometimes replaced by **~ ~ ~**.
- The examples make heavy use of the newly proposed Comment format that is also in this PR. So lines might look like:
  - `1 STICKY @ST0005@  /* here some explanatory comments */`
- As there are many examples for many different situations, below this **General Remarks** there is a link-list in a table, with short descriptions. That way a certain example is easier to find without scrolling.  

**Every example has a link back to the start of this page.**

---

## 📚 Examples Index

| 🧾 Example | 📂 TEMPLATE Type | 📌 What it Shows                                                  |
|-----------|------------------|-------------------------------------------------------------------|
| [💍 Example 01](#example-01) | MARRIAGE, CIVIL |  **💍 Example 01: Wedding Certificate with Family Necklace Transfer**<br>A marriage certificate that includes a non-monetary property transfer — in this case, a piece of jewelry given by the groom to the bride by a `TRANSFER`. (With `ASSET` and `FLEX`.)<br>Further, its `STICKY`s, hold **all information** that can be derived from a certain event, or `TEMPLATE`, so it shows the function of a `STICKY`is to replace part of the info of an `INDI`.<br>`MARR` tag now is in the couples `STICKY` records.   |
| [👧🏻 Example 02](#example-02) | CHILD, ADOPTION |  **👧🏻 Example 02: International Adoption Certificate**<br>International adoption certificate, issued in 1992, including adoptive parents (`ROLE ADOPTER`), adopted child (born elsewhere, `ROLE MAIN, CHILD, ADOPTEE`), and issuing authority.<br>`ADOP` and `PEDI` now in the `TEMPLATE` and in the childs `STICKY`. With BIRTH name and ADOPTED name. The adopted child is added to the `ROLES` section of **BOTH parents**.  |
| [🍼 Example 03](#example-03) | CHILD, BIRTH, Medical |  **🍼 Example 03: Medical Birth Certificate**<br>A birth certificate of a child born in a hospital. With father, mother, doctor and nurse `STICKY`'s. The child's `STICKY` has Weight, Length, and APGAR-score in `FLEX`. **The childs `STICKY` is also added to the `INDI` of both his parents !!** |
| [💍🧒 Example 04](#example-04) | MARRIAGE, CIVIL |  **💍🧒 Example 04: Wedding with step children from both sides**<br>A marriage where both partners each already have children who become each others step children after that marriage. Including connections to there `INDI`'s. **All children, their biological and stepchildren** are mentioned in the `ROLES`section of their parents.  |
| [🧮 Example 05](#example-05) | FAMILY, CENSUS |  **🧮 Example 05: Census with Annotated Events**<br>Census of a family: Father, Mother, Son, Daughter, Enumerator, Boarder. Includes **annotated "events"** (`AN_BIRTH`, and `AN_MOVE`) |
| [🎖️ Example 06](#example-06) | ASSET, MEDAL        | **🎖️ Example 06: Medal awarded to individual**<br>A medal (`ASSET`) given to a soldier, using `STICKY` links and `FLEX` fields. The `TEMPLATE` is of type `MILITARY, AWARD` and connects a tangible object (the medal itself) with the recipient using `STICKY` roles. |
| [🌿 Example 07](#example-07) | PROPERTY, GRANT | **🌿 Example 07: Land Grant Record**<br>This example models a royal land grant issued in 1811 to a private citizen as a reward for military service. It includes a structured `TRANSFER` with a defined `GRANTOR`, `GRANTEE`, and land parcel `ASSET`, as well as a properly detailed `CITA` section with archival metadata.|
| [🪪 Example 08](#example-08) | ORGANIZATION, COURT and<br>IDENTITY, PASSPORT | **🪪 Example 08: Naturalization and Passport**<br>**A `TEMPLATE` pair** modeling naturalization and passport issuance for Leopold Federwitz in early 1900s USA. Includes legal authority roles, asset `STICKY`s (Naturalization certificate and passport), and showcases how to store both under the `ASSETS` section of the `INDI`. The `TEMPLATE`s events are: `NATU` (official GEDCOM) and `EVEN IDENTITY, PASSPORT` (no official GEDCOM event present)|
| [⛪ Example 09](#example-09) | RELIGIOUS and BAPTISM | **⛪ Example 09: Adult baptism and Religious roles**<br>A combination of multi-role religious events: includes adult convert, clergy, ordination backstory, and baptism with an `ASSET` (baptism gown) use. It has: Adult conversion (Hans and Johannes); Infant baptism (Johannes); Ordination (Einar Voss); Clergy participation (Henrik Brodahl); Godparent and family witness roles (Marta, Karl); Religious assets (Baptism gown) |
| [📙 Example 10](#example-10) | SECONDARY, FAMILYBIBLE | **📙 Example 10: Family Bible**<br>A richly annotated family Bible (TYPE SECONDARY, FAMILYBIBLE) spanning 3 generations of the Eldridge family (1869–1936). Uses `AN_xxx` `STICKY` types to model secondary handwritten events (with `FLEX ANNOTATION`) like births, deaths, illnesses, and gifts. Includes the Bible's `ASSET`-record, a beloved butler and a midwife, and shows `TDABOVI` lineage, and emotional historical record-keeping in `FLEX`. Includes period photos. |
| [🧬 Example 11](#example-11) | IDENTITY, DNATEST | **🧬 Example 11: DNA Test Results – Match Comparison & Genotype Report**<br>A pair of `TEMPLATE`s modeling both a DNA match comparison report, using `FLEX` entries for shared segments and relationship estimates. And a direct genotype report. Includes `STICKY` for the match report (`ASSET`), uses `ADDRPLUS` for lab and test center contacts, and demonstrates `FLEX ARRAY` for tabular genotype values. Shared entities like individuals are reused across both reports. |
| [🛖 Example 12](#example-12) | RESIDENCE, FARM-OCCU | **🛖 Example 12: Norwegian Farm Membership**<br>This example demonstrates how to use a `GROUP` record to represent **a traditional Norwegian farm** in a historical context (Lien Farm Census, 1832, Valdres, Norway), and how to associate both family and non-family individuals with that group using `STICKY` roles like `LEADER`, `MEMBER`, `WORKER`, and `RESIDENT`. |
| [🏥 Example 13](#example-13) | MEDICAL, ADMISSION and DISCHARGE | **🏥 Example 13: Hospital Admission and Discharge Record**<br>Two `TEMPLATE`s modeling a patient's hospital stay in 1933 for acute appendicitis. An admission and a discharge `TEMPLATE`. Shows the hospital as an organization and roles like `PATIENT`, `PHYSICIAN`, and `SITE` (for the hospital itself), with `FLEX`, `SPLAC`, and a scanned source register. |
| [🛠️ Example 14](#example-14) | OCCUPATIONAL, EMPLOYMENT | **🛠️ Example 14: Mid Century Employment Transfer Order**<br>This `TEMPLATE` records the formal transfer of employee Gertrude Elmsbottom from the Leiden Branch to the Rotterdam HQ of Western Office Supplies Co. in 1954. Includes `STICKY` records for the employee, both originating and receiving workplaces, and the issuing officer. Demonstrates `EMPLOYER` roles for organizations, sequential `OCCU` facts for old and new positions, structured `FLEX DESCRIPT` for the new job title, and integration of `SOURCE` with scanned memo evidence. |
| [🧾 Example 15](#example-15) | DEATH, WILL | **🧾 Example 15: Legal Will Creation and Execution with Estate Transfers**<br>This dual-`TEMPLATE` example models the two-stage legal will process for Emil Rothenbühler: will creation (while alive) and will execution (after death). It includes `STICKY`s for the decedent across both stages, a notary, legal executor, multiple heirs, and detailed `TRANSFER` structures for assets. Also demonstrates `FLEX VALUE` for appraisal, `SHARE` for proportional distribution, and a realistic asset division process. Includes dedicated `STICKY` and `TRANSFER` for each asset to track inheritance lineage and value allocation. |
| [⚔️ Example 16](#example-16) | DEATH, WILL, Title | **⚔️ Example 16:  Historical Title and Nobility Inheritance**<br>This `TEMPLATE` models the inheritance of a noble title and estate following the death of a titled individual. Features include a `STICKY` for the title holder, an heir receiving both property and title, symbolic artifacts, and a ruling monarch confirming the transfer. Demonstrates `TITLE, Baron`, land size, annotations, and an `ASSET` history of previous holders. Includes a dedicated `STICKY` and `TRANSFER` for the title itself (`ROLE DIGNITY`), showing how titles can be modeled as independent assets with full lineage tracking.
| [🛡️ Example 17](#example-17) | GROUP, GUILD-MEM | **🛡️ Example 17: Guild Membership Certificate**<br>Guild admission certificate for John Smith in 1702 London, issued by the Worshipful Company of Blacksmiths in London, including the original oath and rights text<br>(“Be it knowne unto all men by these presentes…”),<br>modeled as both `TEMPLATE` event and asset `STICKY`. Includes structured membership details. |
[⚖️ Example 18](#example-18) | LEGAL, JUDGMENT | **⚖️ Example 18: Court Trial Record – Humorous Fictional Case**<br>Illustrates a fictional court trial modeled in GEDCOM 8, focusing on the use of `STICKY` roles in legal records. Includes `ROLE` types like `DEFENDANT`, `JUDGE`, `JURY FOREMAN`, and `WITNESS`, showing how to link individuals to a single `TEMPLATE`. Playfully absurd, but structurally correct. |
| [🪦 Example 19](#example-19) | MEMORIAL, GRAVESTONE | **🪦 Example 19: Gravestone with Named and Implied Persons**<br>Shows multiple individuals on a shared tombstone: two named (with roles `MAIN` and `WIDOW`) and two implied (`CHILD`, `GRANDCHILD`). Includes annotations, a Bible verse, estimated marriage date, and `QUAY` levels. `TEMPLATE` has `1 TORIGIN ORIGDOC, INCOMPLETE` |







[🔝 Back to top](#appendix-b-gedcom-examples)


---

<a name="example-01"></a>  
## 💍 Example 01: "Wedding Certificate with Family Necklace Transfer  

This example demonstrates a marriage certificate that includes a non-monetary property transfer — in this case, a piece of jewelry given by the groom to the bride by a `TRANSFER`. 

- It shows how **`ASSET`** types and **`FLEX`** entries can be used to capture contextual information about assets involved in life events.
- The `STICKY`'s in this example have a lot of Tags: like NAME, BIRT, MARR, OCCU, RELI and more. This clearly shows the function of a `STICKY`, it holds **all information** that can be derived from a certain event, or `TEMPLATE`.
- The `MARR` tag is only present in the `STICKY` of the bride and the groom, as it is their marriage. It is **not present** in the other `STICKY`s. They attend the marriage, but it is not theirs.

**💍 @T0042@ – Wedding Certificate with Family Necklace Transfer**
```gedcom
0 @T0042@ TEMPLATE
1 TYPE MARRIAGE, CIVIL
1 TITL Wedding Certificate Springfield
2 PHRASE Wedding "Certificate with Family Necklace Transfer"
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 SPLAC @SP0085@              /* Springfield, Illinois, USA */
1 MARR                        /* MARR tag is official tag for marriage */
2 DATE 18 JUN 1954            /* Date of marriage */
2 SPLAC @SP0521@              /* Springfield, Illinois, USA */
1 ROLES
2 STICKY @ST0142@             /* MAIN, BRIDE */
2 STICKY @ST0143@             /* MAIN, GROOM */
2 STICKY @ST0241@             /* FATHER, BRIDE Father of the Bride */
2 STICKY @ST0242@             /* MOTHER, GROOM, Mother of the Groom */
2 STICKY @ST0341@             /* UNCLE, BRIDE, Uncle of the Bride */
2 STICKY @ST0342@             /* FRIEND, GROOM, Friend of the Groom */
2 STICKY @ST0441@             /* OFFICIANT of the Marriage */
2 STICKY @ST0541@             /* JEWELRY, NECKLACE, Family Necklace */
1 TRANSFER @ST0541@           /* Transferred: JEWELRY, NECKLACE, Family Necklace */
1 GRANTOR @ST0241@            /* GRANTOR: FATHER, BRIDE  */
1 GRANTEE @ST0142@            /* GRANTEE: MAIN, BRIDE  */
1 CITA
2 SOUR @S0371@
2 PAGE 5
2 DATA
~  ~ ~
1 CREA 20 JUL 2025
1 CHAN 29 APR 2025
```
**👰‍♀️ @ST0142@ STICKY – Bride**
```gedcom
0 @ST0142@ STICKY
1 TYPE PERSON
1 TITL "Emily Johnson, bride"
1 SUBM @B001@
1 TEMPLATE @T0042@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 ROLE MAIN, BRIDE
1 NAME
2 FORM Emily Johnson
2 PART Emily
3 TYPE GIVN
2 PART Johnson
3 TYPE SURN
1 SEX F
1 BIRT
2 DATE 2 OCT 1930
2 SPLAC @SP0521@              /* Springfield, Illinois, USA */
1 MARR                        /* MARR tag now inside the STICKY of the bride !! */
2 DATE 18 JUN 1954
2 SPLAC @SP006@               /* Springfield */
1 RELI Protestant             /* relifion was only mentioned for the bride */
1 OCCU "Librarian (who secretly reshelves alphabet soup cans for fun)"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🤵 @ST0143@ STICKY – Groom**
```gedcom
0 @ST0143@ STICKY
1 TYPE PERSON
1 TITL "Robert Green, groom"
1 SUBM @B001@
1 TEMPLATE @T0042@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 ROLE MAIN, GROOM
1 NAME
2 FORM Robert Green
2 PART Robert
3 TYPE GIVN
2 PART Green
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 18 JAN 1929
2 SPLAC @SP006@               /* Edinburg */
1 MARR                        /* MARR tag now inside the STICKY of the groom !! */
2 DATE 18 JUN 1954
2 SPLAC @SP006@               /* Springfield */
1 RESI                        /* Address was only mentioned for the groom */
2 ADDR Mainstreet
3 CITY Springfield, ILL, USA
2 NOTE "Repair specialist, third class."
1 OCCU "Accordion repair technician (self-taught)"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**👨‍🦳 @ST0241@ STICKY – Father of the Bride**
```gedcom
0 @ST0241@ STICKY
1 TEMPLATE @T0042@
1 TITL "Harold Johnson, Father of the Bride"
1 SUBM @B001@
1 TYPE PERSON
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 ROLE FATHER, BRIDE
1 NAME
2 FORM Harold Johnson
2 PART Harold
3 TYPE GIVN
2 PART Johnson
3 TYPE SURN
1 SEX M
1 AGE 58
1 OCCU "Professional coffee reheater (retired)"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**👩‍🦳 @ST0242@ STICKY – Mother of the Groom**
```gedcom
0 @ST0242@ STICKY
1 TYPE PERSON
1 TITL "Margaret Green, Mother of the Groom"
1 SUBM @B001@
1 TEMPLATE @T0042@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 ROLE MOTHER, GROOM
1 NAME
2 FORM Margaret Green
2 PART Margaret
3 TYPE GIVN
2 PART Green
3 TYPE SURN
1 SEX F
1 AGE 60
1 OCCU "Former opera critic (known for falling asleep during Act II)"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**👨‍🦰 @ST0341@ STICKY – Uncle of the Bride**
```gedcom
0 @ST0341@ STICKY
1 TYPE PERSON
1 TITL "Temperance McKinley, Uncle of the Bride"
1 SUBM @B001@
1 TEMPLATE @T0042@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 ROLE UNCLE, BRIDE
1 NAME
2 FORM Temperance McKinley
2 PART Temperance
3 TYPE GIVN
2 PART McKinley
3 TYPE SURN
1 SEX M
1 AGE 55
1 OCCU "Inventor of the silent kazoo (never caught on)"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🧑‍🦱 @ST0342@ STICKY – Friend of the Groom**
```gedcom
0 @ST0342@ STICKY
1 TYPE PERSON
1 TITL "Jingle Bell, Friend of the Groom"
1 SUBM @B001@
1 TEMPLATE @T0042@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 ROLE FRIEND, GROOM
1 NAME
2 FORM Jingle Bell
2 PART Jingle
3 TYPE GIVN
2 PART Bell
3 TYPE SURN
1 SEX M
1 AGE 26
1 OCCU "Amateur philosopher (mostly at the pub)"
1 NOTE "Claims to be the best man, but no one asked him."
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🧑‍⚖️ @ST0441@ STICKY – Officiant**
```gedcom
0 @ST0441@ STICKY
1 TYPE PERSON
1 TITL "Mayor Winifred Spoon, Officiant"
1 SUBM @B001@
1 TEMPLATE @T0042@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 ROLE OFFICIANT
1 NAME
2 FORM Mayor Winifred Spoon
2 PART Winifred
3 TYPE GIVN
2 PART Spoon
3 TYPE SURN
1 SEX F
1 OCCU "Mayor and amateur wedding poet"
1 NOTE "Performed the ceremony in rhyme. No one asked for that either."
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**💍 @ST0541@ STICKY – Wedding Necklace (Transferred Gift)**
```gedcom
0 @ST0541@ STICKY
1 TYPE JEWELRY, NECKLACE "Victorian Silver Necklace with blue topaz"
1 TITL "Wedding Necklace"
1 SUBM @B001@
1 TEMPLATE @T0042@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954            /* Event date of this TEMPLATE */
1 FLEX DECIMAL, CURR, USD
2 PHRASE "Value of the item"
2 CONTENTS 185.00
1 FLEX DESCRIPT
2 PHRASE "Description:"
2 CONTENTS Victorian Silver Necklace with blue topaz
1 FLEX MATERIAL
2 PHRASE "Material it is made of"
2 CONTENTS Silver
1 NOTE "Passed down from Harold Johnson (father of the bride) to Emily Johnson on wedding day."
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```

[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-02"></a>  
## 👧🏻 Example 02: International Adoption Certificate  

This GEDCOM 8 example models an international adoption certificate, issued in 1992.  
It includes the adoptive parents, the adopted child (born in another country), and the issuing authority.  

The record captures the child's birth name and new adoptive name, the place of birth and adoption, and legal roles involved.
This example reuses:
- ROLE ADOPTIVE_PARENT, ROLE CHILD, ROLE ISSUER
- FLEX DESCRIPT
- NAME structure (as previously defined) With BIRTH name and ADOPTED name.
- TEMPLATE TYPE CHILD, ADOPTION
>- **`ADOP` is in the childs `STICKY` now**, and in the `TEMPLATE`, all info that used to go under the `ADOP` tag, now is in the `TEMPLATE` and the parents `STICKY`'s. 
>- The adopted child is also added **to the `INDI` of both adopting parents!!** 
>- **`PEDI`** is in the `TEMPLATE`. In this case it says the type of adoption is `ADOPTION`. But in case of an LDS sealing, the type of `PEDI` would be `SEALING`.

The adoption certificate is stored in the @S0047@ source record with a digital scan link.
    
**👧🏻 @T0045@ – International Adoption Certificate**
```gedcom
0 @T0047@ TEMPLATE
1 TYPE CHILD, ADOPTION, "Certificate of International Adoption"
1 TITL Certificate of International Adoption 1985
2 PHRASE "Adoption of Sofia Maria Petrova"
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 MAR 1992
1 SPLAC @SP0082@              /* The Hague, Netherlands */
1 ADOP                        /* This is an Adoption Event! */
2 DATE  12 MAR 1992
2 SPLAC @SP0082@              /* The Hague, Netherlands */
1 PEDI ADOPTED                /* Adoption of type Adopted */
1 FLEX DESCRIPT
2 PHRASE "Description"
2 CONTENTS "Sofia Petrova was formally adopted by Johan de Waal and Marijke van Oosterhout on 12 March 1992."
1 ROLES
2 STICKY @ST0146@             /* This "replaces" in fact her real birth certificate */
2 STICKY @ST0147@             /* MAIN, CHILD, ADOPTEE */
2 STICKY @ST0247@             /* FATHER, ADOPTER */
2 STICKY @ST0248@             /* MOTHER, ADOPTER */
2 STICKY @ST0347@             /* ORGANIZATION, ISSUER (Adoption Court) */
1 CITA
2 SOURCE @S0047@              /* Adoption Certificate */
2 TITL Certificate of International Adoption – Sofia Petrova
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🥈 @ST0146@ STICKY – Sofiya Mariya Stoyanova, real name at birth**
```gedcom
0 @ST0146@ STICKY             /* This "replaces/adds to" her real birth certificate */
1 TYPE PERSON, AN_BIRTH       /* Annotated, as this TEMPLATE is about adoption */
1 TEMPLATE @T0047@
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE MAIN, CHILD
1 NAME
2 TYPE BIRTH                  /* Name at birth, before adoption */
2 FORM Sofiya Mariya Stoyanova
2 PART Sofia
3 TYPE GIVN
2 PART Maria
3 TYPE GIVN
2 PART Petrova
3 TYPE SURN
1 SEX F
1 BIRT
2 DATE 5 MAY 1989
2 SPLAC @SP0042@              /* Plovdiv, Bulgaria */
1 FLEX DESCRIPT 
2 PHRASE "Original name at birth"
2 CONTENTS "Sofiya Mariya Stoyanova"
1 NOTE "Renamed after adoption and given Dutch citizenship."
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🥈 @ST0147@ STICKY – Sofia Maria Petrova, adopted child**
```gedcom
0 @ST0147@ STICKY
1 TYPE PERSON
1 TEMPLATE @T0047@
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE MAIN, CHILD, ADOPTEE
1 NAME
2 TYPE ADOPTED                /* Name after adoption */
2 FORM Sofia Maria Petrova
2 PART Sofia
3 TYPE GIVN
2 PART Maria
3 TYPE GIVN
2 PART Petrova
3 TYPE SURN
1 ADOP                        /* This child is adopted */
2 DATE  12 MAR 1992
2 SPLAC @SP0082@              /* The Hague, Netherlands */
1 PEDI ADOPTED                /* Adoption of type Adopted */
2 DATE  12 MAR 1992
2 SPLAC @SP0082@              /* The Hague, Netherlands */
1 SEX F
1 BIRT
2 DATE 5 MAY 1989
2 SPLAC @SP0042@              /* Plovdiv, Bulgaria */
1 FLEX DESCRIPT 
2 PHRASE "Original name at birth"
2 CONTENTS "Sofiya Mariya Stoyanova"
1 NOTE "Renamed after adoption and given Dutch citizenship."
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🥈 @ST0247@ STICKY – Johan de Waal, adopting father**
```gedcom
0 @ST0247@ STICKY
1 TYPE PERSON
1 TEMPLATE @T0047@
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE FATHER, ADOPTER
1 NAME
2 FORM Johan de Waal
2 PART Johan
3 TYPE GIVN
2 PART de Waal
3 TYPE SURN
1 SEX M
1 OCCU "Physics teacher and cheese enthusiast"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🥈 @ST0248@ STICKY – Marijke van Oosterhout, adopting mother**
```gedcom
0 @ST0248@ STICKY
1 TYPE PERSON
1 TEMPLATE @T0047@
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE MOTHER, ADOPTER
1 NAME
2 FORM Marijke van Oosterhout
2 PART Marijke
3 TYPE GIVN
2 PART van Oosterhout
3 TYPE SURN
1 SEX F
1 OCCU "Municipal librarian and puzzle queen"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**🥈 @ST0347@ STICKY – Hague District Family Court**
```gedcom
0 @ST0347@ STICKY
1 TYPE ORGANIZATION, ADOPTIONAGENCY, "Hague District Family Court"
1 TEMPLATE @T0047@
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE ISSUER
1 NAME
2 FORM Hague District Family Court
1 NOTE "Authorized under the 1993 Hague Adoption Convention"
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```
**👤 INDI @I501@ for Sofia Maria Petrova**
```gedcom
0 @I501@ INDI
1 NAME
2 FORM Sofia Maria Petrova
2 PART Sofia Maria
3 TYPE GIVN
2 PART Petrova
3 TYPE SURN
1 ROLES
2 STICKY @ST0146@             /* Sofiya, real name at birth (ALL info in the STICKY, No Longer in the INDI) */
2 STICKY @ST0147@             /* Sofia, adopted name (ALL info in the STICKY, No Longer in the INDI) */
1 CHAN 29 APR 2025
1 CHAN 29 APR 2025
```
**👤 INDI @I501@ for Marijke van Oosterhout**
```gedcom
0 @I502@ INDI                 /* The adopted child is ALSO added to the ROLES section of BOTH parents */
1 NAME
2 FORM Marijke van Oosterhout
~ ~ ~
1 ROLES
2 STICKY @ST0147@             /* Sofia Maria Petrova, adopted child */
1 CHAN 29 APR 2025
1 CHAN 29 APR 2025
```
**👤 INDI @I501@ for Johan de Waal**
```gedcom
0 @I503@ INDI                 /* The adopted child is ALSO added to the ROLES section of BOTH parents */
1 NAME
2 FORM Johan de Waal
~ ~ ~
1 ROLES
2 STICKY @ST0147@             /* Sofia Maria Petrova, adopted child */
1 CHAN 29 APR 2025
1 CHAN 29 APR 2025
```
**💾 SOURCE for Adoption Certificate**
```gedcom
0 @S0047@ SOUR
1 TITL Certificate of International Adoption – Sofia Petrova
1 AUTH Hague District Family Court
1 PUBL "Filed under case #INT-ADOP-92112"
1 ABBR "Adoption Certificate – Sofia"
1 DATA
2 EVEN ADOP
3 DATE 12 MAR 1992            /* Date of adoption */
4 PHRASE "Certificate of international adoption of child born in Bulgaria"
3 SPLAC @SP0008@              /* The Hague, Netherlands */
2 AGNC Hague District Family Court
~ ~ ~
1 OBJE @O0321@                /* Scan of original Hague certificate */
1 CHAN 29 APR 2025
1 CHAN 13 AUG 2025
```
**💾 OBJE Scan of Adoption Certificate**
```gedcom
0 OBJE @O0321@                /* Multimedia record with file link  */
1 FILE https://example.org/adoptions/petrova-1992.pdf
2 FORM application/pdf
2 TITL Scan of original Hague certificate
1 CREA 29 APR 2025
1 CHAN 29 APR 2025
```

[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-03"></a>  
## 🍼 Example 03: Medical Birth Certificate

This example has a birth certificate of a child born in a hospital.
- With father, mother, doctor and nurse `STICKY`'s.
- The child's `STICKY` has Weight, Length, and APGAR-score in `FLEX`. 
- The `TEMPLATE` has a lot of info in the `CITA` structure.
- The childs `STICKY` is also added to the `INDI` of both his parents !!

```gedcom
0 @T1020@ TEMPLATE
1 TYPE CHILD, BIRTH, Medical
1 TITL Medical Birth Certificate from St. Mary's Hospital, London
2 PHRASE Birth certificate of David Michael Johnson with medical details 
1 SUBM @B0003@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 5 MAY 1915             /* Date of the document */
1 SPLAC @SP042@               /* St. Mary's Hospital, London, England */
2 NOTE Hospital Birth Record
1 BIRT                        /* event this TEMPLATE is about */
2 DATE 5 MAY 1915
2 SPLAC @SP042@               /* St. Mary's Hospital, London, England */
1 ROLES
2 STICKY @ST9201@             /* MAIN, CHILD: Baby David Michael Johnson */
2 STICKY @ST9202@             /* MOTHER: Susan Johnson */
2 STICKY @ST9203@             /* FATHER: Michael Johnson */
2 STICKY @ST9204@             /* DOCTOR, WITNESS: Attending Physician: Dr. John Pricklebone */
2 STICKY @ST9205@             /* NURSE, WITNESS: Nurse Wiggle */
1 CITA
2 SOUR @S0444@                /* St. Mary's Hospital Birth Register */
2 PAGE Volume 12, Entry 449B
2 DATA
3 DATE 5 MAY 1915
3 TEXT “Infant David Michael Johnson born to Susan Johnson”
4 MIME text/plain
4 LANG en
2 AUTHOR St. Mary's Hospital
2 TITL Birth Register, 1910–1920
2 DATES
3 RECORDED 5 MAY 1915
2 TEXTDISPLAY “St. Mary's Hospital Birth Register, Vol 12, Entry 449B”
2 TRANSCRIPT “Infant David Michael Johnson born 5 May 1915 to Susan Johnson, attended by Dr. John Pricklebone and nurse Wiggle.”
2 FORMAT
3 TYPE image/jpeg
2 URL https://archive.londonhospitals.uk/stmarys/births/vol12-entry449B.jpg
2 LANGUAGE en
2 RECORDID NHS-BR-STMARYS-449B
2 CONTAINER Hospital Archives Division
2 ITEMTYPE Medical Birth Record
2 SHORTTITLE St. Mary's Births 1915
2 WWWLINK
3 VALUE https://nhs.uk/birthrecords/stmarys1915
2 QUAY 3
2 OBJE @O1020@               /* Scanned certificate image */
1 CREA 20 JUL 2025
1 CHAN 25 JUL 2025
```
**🧑🏼 @I0537@ INDI – David Michael Johnson**
```gedcom
0 @I0537@ INDI                /* David Michael Johnson, MAY 5 1915 */
1 NAME
2 FORM David Michael Johnson
~ ~ ~
1 SEX M
1 ROLES
2 STICKY @ST9201@             /* Birth with roles - MAIN, CHILD */
```
**👶 @ST9201@ STICKY – Baby David Michael Johnson**
```gedcom
0 STICKY @ST9201@             /* Many FLEXes for non GEDCOM information */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1020@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE MAIN, CHILD
1 NAME
2 FORM David Michael Johnson
~ ~ ~
1 BIRT
2 DATE 5 MAY 1915
2 SPLAC @0006@                /* St. Mary's Hospital, London, England */
1 DATE 5 MAY 1915
2 TIME 04:32                  /* Time of bearth */
1 FLEX DESCRIPT
2 PHRASE "Room/Ward of birth"
2 CONTENTS "Maternity Ward, Room 12B"
1 FLEX DECIMAL
2 PHRASE "Weight at Birth in kg"
2 CONTENTS 3.2
1 FLEX INTEGER
2 PHRASE "Length at Birth in cm"
2 CONTENTS 50
1 FLEX DESCRIPT
2 PHRASE "Type of Birth"
2 CONTENTS "Single"
1 FLEX DESCRIPT
2 PHRASE "Birth Complications"
2 CONTENTS "None"
1 FLEX INTEGER
2 PHRASE "APGAR Score at 1 Minute"
2 CONTENTS 9
1 FLEX INTEGER
2 PHRASE "APGAR Score at 5 Minutes"
2 CONTENTS 10
~ ~ ~
```
**👩🏻‍🦱 @ST9201@ STICKY – Mother Susan Johnson**
```gedcom
0 @ST9202@ STICKY             /* Mother Susan Johnson */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1020@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 AGE 32
1 OCCU Housewife
1 ROLE MOTHER
1 NAME
2 FORM Susan Johnson
~ ~ ~
```
**👨🏼‍🦰 @ST9201@ STICKY – Father Michael Johnson**
```gedcom
0 @ST9203@ STICKY             /* Father Michael Johnson */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1020@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 AGE 35
1 OCCU Farmer
1 ROLE FATHER
1 NAME
2 FORM Michael Johnson
~ ~ ~
```
**🧑🏼 @I0537@ INDI – David Michael Johnson**
```gedcom
0 @I0537@ INDI                /* David Michael Johnson, MAY 5 1915 */
1 NAME
2 FORM David Michael Johnson
~ ~ ~
1 SEX M
1 ROLES
2 STICKY @ST9201@             /* Birth with roles - MAIN, CHILD */
```
**👩🏻‍🦱🧑🏼 @I0537@ INDI – Mother Susan Johnson, baby David added to her ROLES section**
```gedcom
0 @I0538@ INDI                /* Mother Susan Johnson */
1 NAME
2 FORM David Michael Johnson
~ ~ ~
1 SEX M
1 ROLES
2 STICKY @ST9201@             /* Baby David Michael Johnson */
```
**👨🏼‍🦰 @I0537@ INDI – Father Michael Johnson, baby David added to her ROLES section**
```gedcom
0 @I0539@ INDI                /* Father Michael Johnson */
1 NAME
2 FORM David Michael Johnson
~ ~ ~
1 SEX M
1 ROLES
2 STICKY @ST9201@             /* Baby David Michael Johnson */
```
**🩺 @ST9201@ STICKY – Attending Physician: Dr. John Pricklebone**
```gedcom
0 @ST9204@ STICKY             /* Attending Physician */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1020@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE DOCTOR, WITNESS
1 NAME
2 FORM Dr. John Pricklebone
~ ~ ~
```
**👩‍⚕️ @ST9201@ STICKY – Nurse: Nurse Wiggle**
```gedcom
0 @ST9205@ STICKY             /* Nurse Witness */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1020@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE NURSE, WITNESS
1 NAME
2 FORM Nurse Wiggle
~ ~ ~
```
**📚 SOURCE block — St. Mary’s Hospital Birth Register**
```gedcom
0 @S0444@ SOUR
1 TITL Birth Register of St. Mary's Hospital, London (1910–1920)
1 AUTH St. Mary's Hospital
1 PUBL Hospital Archives Division, London NHS Trust
1 ABBR St. Mary's Birth Register
1 TEXT Original handwritten entries for births occurring at the hospital, Recorded by attending staff at time of birth
1 DATA
~ ~ ~
1 REPO @R0001@
2 CALN A32 756 nr3
3 MEDI ELECTRONIC
4 PHRASE Image/jpg
1 NOTE Register includes birth records with medical annotations and attending staff signatures.
```
**🖼️ OBJE block — Scanned certificate image**
```gedcom
0 @O1020@ OBJE
1 FILE https://archive.londonhospitals.uk/stmarys/births/vol12-entry449B.jpg
2 FORM image/jpeg
3 MEDI Image
2 TITL Scanned Birth Register Entry for David Michael Johnson, 5 MAY 1915
1 NOTE Digitized from St. Mary's Hospital Birth Register, volume 12.
```
**🏛️ REPO block — Hospital Archives**
```gedcom
0 @R0001@ REPO
1 NAME Hospital Archives Division, London NHS Trust
1 ADDR 221B Baker Street
2 CITY London
2 POST NW1 6XE
2 CTRY United Kingdom
1 EMAIL archives@londonhospitals.uk
1 WWW https://londonhospitals.uk/archives
```


[🔝 Back to top](#appendix-b-gedcom-examples)



---

<a name="example-04"></a>  
## 💍🧒 Example 04: Wedding with step children from both sides  

### 🧾 Example: A Dual Blended Family Marriage

This example models a remarriage where both spouses bring two children from prior relationships.  
Each child is marked as a `STEPCHILD` **to the new spouse**, and the marriage `TEMPLATE` shows all relevant relationships.

**Included in this example:**
- 1 `TEMPLATE`
- 7 `STICKYs` (bride, groom, 4 children, registrar)
- 7 `INDI` records

**Notes:**
- `INDI` records of the children list the `STICKY` they gain from this marriage (`TEMPLATE`),  
  but also include earlier `STICKYs` such as their births.
- The birth `STICKY` of each child connects them to their original birth parents.
- **Those earlier `TEMPLATE`s are not shown in this example**.
- Each child has a `ROLE` looking like this: `1 ROLE CHILD2, STEPCHILD, GROOM`. This `STICKY` will also be linked into the `ROLES` section of the child itself. Now looking at that `ROLE` from inside the `STICKY` in the `INDI` of the child, one could say this is the `GROOM` itself, but thats not possible, as the real `GROOM` of a marriage **always** has a `MAIN` in its `ROLE` line.<br>And this child has not! So the child is somehow related to the `GROOM`, **but is not the `GROOM` himself.**
-**All children own and stepchildren** are mentioned in the `ROLES`section of their parents.
- As the registrar of this marriage is only mentioned in a sidenote, and apparantly not officially on this cerificate, his `STICKY` is of type `PERSON, AN_MENTION`.

**📜 @T09901@ TEMPLATE – Marriage of Johanna van Loon & Willem de Zwart**
```gedcom
0 @T09901@ TEMPLATE
1 TYPE MARRIAGE, CIVIL
1 TITL Standard Dutch Marriage Certificate (1823-1890)
2 PHRASE "Marriage Certificat of Johanna van Loon and Willem de Zwart, JUNE 15 1888, Delft "
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 15 JUN 1888
1 SPLAC @SP006@               /* Delft Town Hall, Netherlands */
1 MARR                        /* MARR tag also in TEMPLATE */
2 DATE 15 JUN 1888
2 SPLAC @SP006@               /* Delft Town Hall, Netherlands */
1 ROLES
2 STICKY @ST1010@ /* ROLE MAIN, BRIDE — Johanna van Loon */
2 STICKY @ST1011@ /* ROLE MAIN, GROOM — Willem de Zwart */
2 STICKY @ST1012@ /* ROLE CHILD1, STEPCHILD, GROOM — Anna van Loon (bride’s daughter) */
2 STICKY @ST1013@ /* ROLE CHILD2, STEPCHILD, GROOM — Bastiaan van Loon (bride’s son) */
2 STICKY @ST1014@ /* ROLE CHILD3, STEPCHILD, BRIDE — Lisette de Zwart (groom’s daughter) */
2 STICKY @ST1015@ /* ROLE CHILD4, STEPCHILD, BRIDE — Marius de Zwart (groom’s son) */
2 STICKY @ST1016@ /* ROLE REGISTRAR — Bastiaan van den Akten */
1 FLEX ANNOTATION
2 PHRASE Note added later.
2 CONTENTS Amb. Burg.Stand is Bastiaan van den Akten
3 LANG nl
1 CITA
2 SOUR @S0373@
2 PAGE 5
2 DATA
~  ~ ~
1 NOTE "Marriage between Johanna and Willem. Both brought children from previous relationships."
```
**👩🏻 @ST1010@ STICKY – MAIN, BRIDE, Johanna van Loon**
```gedcom
0 @ST1010@ STICKY             /* MAIN, BRIDE, Johanna van Loon */
1 TYPE PERSON
1 TEMPLATE @T09901@
1 DATE 15 JUN 1888
1 SPLAC @SP006@               /* Delft Town Hall, Netherlands */
1 ROLE MAIN, BRIDE
1 NAME
2 FORM Johanna van Loon
~ ~ ~
1 AGE 38
1 SEX F
1 MARR                        /* MARR tag now in STICKY */
2 DATE 15 JUN 1888
2 SPLAC @SP006@               /* Delft Town Hall, Netherlands */
1 RESI
2 DATE BEF 1888               /* Residence at time of marriage */
2 SPLAC @SP042@               /* Delft, NH, Netherlands */
1 NOTE "Bride, widow with two children from earlier marriage."
```
**👨🏻 @ST1011@ STICKY – MAIN, GROOM, Willem de Zwart**
```gedcom
0 @ST1011@ STICKY             /* MAIN, GROOM, Willem de Zwart */
1 TYPE PERSON
1 TEMPLATE @T09901@
1 DATE 15 JUN 1888
1 ROLE MAIN, GROOM
1 NAME
2 FORM Willem de Zwart
~ ~ ~
1 AGE 40
1 MARR                        /* MARR tag now in STICKY */
2 DATE 15 JUN 1888
2 SPLAC @SP006@               /* Delft Town Hall, Netherlands */
1 RESI
2 DATE BEF 1888               /* Residence at time of marriage */
2 SPLAC @SP042@               /* Delft, NH, Netherlands */
1 NOTE "Groom, widower with two children from earlier marriage."
```
**🧒🏻 @ST1012@ STICKY – CHILD1, STEPCHILD, GROOM – Anna van Loon**
```gedcom
0 @ST1012@ STICKY             /* Anna van Loon - CHILD1, STEPCHILD, GROOM  */
1 TYPE PERSON
1 TEMPLATE @T09901@
1 DATE 15 JUN 1888
1 ROLE CHILD1, STEPCHILD, GROOM
1 NAME
2 FORM Anna van Loon
~ ~ ~
1 AGE 12
1 NOTE "Daughter of Johanna; became stepchild of Willem upon marriage."
```
**👦🏻 @ST1013@ STICKY – CHILD2, STEPCHILD, GROOM – Bastiaan van Loon**
```gedcom
0 @ST1013@ STICKY             /* Bastiaan van Loon - CHILD2, STEPCHILD, GROOM  */
1 TYPE PERSON
1 TEMPLATE @T09901@
1 DATE 15 JUN 1888
1 ROLE CHILD2, STEPCHILD, GROOM
1 NAME
2 FORM Bastiaan van Loon
1 AGE 9
1 NOTE "Son of Johanna; became stepchild of Willem upon marriage."
```
**👧🏻 @ST1014@ STICKY – CHILD3, STEPCHILD, BRIDE – Lisette de Zwart**
```gedcom
0 @ST1014@ STICKY             /* Lisette de Zwart - CHILD3, STEPCHILD, BRIDE  */
1 TYPE PERSON
1 TEMPLATE @T09901@
1 DATE 15 JUN 1888
1 ROLE CHILD3, STEPCHILD, BRIDE
1 NAME
2 FORM Lisette de Zwart
~ ~ ~
1 AGE 10
1 NOTE "Daughter of Willem; became stepchild of Johanna upon marriage."
```
**👦🏼 @ST1015@ STICKY – CHILD4, STEPCHILD, BRIDE – Marius de Zwart**
```gedcom
0 @ST1015@ STICKY             /* Marius de Zwart - CHILD4, STEPCHILD, BRIDE  */
1 TYPE PERSON
1 TEMPLATE @T09901@
1 DATE 15 JUN 1888
1 ROLE CHILD4, STEPCHILD, BRIDE
1 NAME
2 FORM Marius de Zwart
~ ~ ~
1 AGE 7
1 NOTE "Son of Willem; became stepchild of Johanna upon marriage."
```
**🧾 @ST1016@ STICKY – REGISTRAR – Bastiaan van den Akten**
```gedcom
0 @ST1016@ STICKY             /* REGISTRAR, Bastiaan van den Akten */
1 TYPE PERSON, AN_MENTION
1 TEMPLATE @T09901@
1 DATE 15 JUN 1888
1 ROLE REGISTRAR
1 NAME
2 FORM Bastiaan van den Akten
~ ~ ~
1 NOTE "Official registrar recording the marriage."
```
### INDI records for all people

**👩🏻‍🦰 @I1010@ INDI – Johanna van Loon**
```gedcom
0 @I1010@ INDI                /* Johanna van Loon, Bride, widow, kids: Anna and Bastiaan */
1 NAME
2 FORM Johanna van Loon
~ ~ ~
1 ROLES
1 STICKY @ST0800@             /* Marriage to her former husband */
1 STICKY @ST0953@             /* Birth of her own child: Anna van Loon */
1 STICKY @ST0999@             /* Birth of her own child: Bastiaan van Loon */
1 STICKY @ST1010@             /* Here she is: MAIN, BRIDE, when she marries Willem de Zwart */
1 STICKY @ST1014@             /* After marriage becomes stepmom of: Lisette de Zwart */
2 STICKY @ST1015@             /* After marriage becomes stepmom of: Marius de Zwart */
~ ~ ~
```
**👨🏻‍🦰 @I1011@ INDI – Willem de Zwart**
```gedcom
0 @I1011@ INDI                /* Willem de Zwart, Groom, widower, kids: Lisette and Marius */
1 NAME
2 FORM Willem de Zwart
~ ~ ~
1 ROLES
1 STICKY @ST0800@             /* Marriage to his former wife */
1 STICKY @ST0853@             /* Birth of his own child: Lisette de Zwart */
1 STICKY @ST0899@             /* Birth of his own child: Marius de Zwart */
1 STICKY @ST1011@             /* Here he is: MAIN, GROOM, when he marries Johanna van Loon */
1 STICKY @ST1012@             /* After marriage becomes stepdad of: Anna van Loon */
2 STICKY @ST1013@             /* After marriage becomes stepdad of: Bastiaan van Loon */
~ ~ ~
```
**👧🏻 @I1012@ INDI – Anna van Loon**
```gedcom
0 @I1012@ INDI                /* Anna van Loon, Johanna's daughter */
1 NAME
2 FORM Anna van Loon
~ ~ ~
1 ROLES
2 STICKY @ST0951@             /* Birth of Anna */
2 STICKY @ST1012@             /* CHILD1, STEPCHILD, GROOM, Anna van Loon */
~ ~ ~
```
**👦🏻 @I1013@ INDI – Bastiaan van Loon**
```gedcom
0 @I1013@ INDI                /* Bastiaan van Loon, Johanna's son */
1 NAME
2 FORM Bastiaan van Loon
~ ~ ~
1 ROLES
2 STICKY @ST0998@             /* Birth of Bastiaan */
2 STICKY @ST1013@             /* CHILD2, STEPCHILD, GROOM, Bastiaan van Loon */
~ ~ ~
```
**👧🏻 @I1014@ INDI – Lisette de Zwart**
```gedcom
0 @I1014@ INDI                /* Lisette de Zwart, Willem's daughter */
1 NAME
2 FORM Lisette de Zwart
~ ~ ~
1 ROLES
2 STICKY @ST0805@             /* Birth of Lisette */
2 STICKY @ST1014@             /* CHILD3, STEPCHILD, BRIDE, Lisette de Zwart */
~ ~ ~
```
**👦🏼 @I1015@ INDI – Marius de Zwart**
```gedcom
0 @I1015@ INDI                /* Marius de Zwart, Willem's son */
1 NAME
2 FORM Marius de Zwart
~ ~ ~
1 ROLES
2 STICKY @ST0823@             /* Birth of Marius */
2 STICKY @ST1015@             /* CHILD4, STEPCHILD, BRIDE, Marius de Zwart */
~ ~ ~
```
**📋 @I1016@ INDI – Bastiaan van den Akten**
```gedcom
0 @I1016@ INDI                /* Bastiaan van den Akten, Registrar */
1 NAME
2 FORM Bastiaan van den Akten
~ ~ ~
1 ROLES
2 STICKY @ST1016@             /* REGISTRAR at the marriage of Johanna and Willem */
```


[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-05"></a>  
## 🧮 Example 05: Census with Annotated Events

Imagine: a 1920 household census in Boston, featuring:  
- One multigenerational household (parents, kids, orphaned niece, maid, boarder, grandfather)  
- A live-in maid who arrived later, with annotated recommendation from bishop
- Several annotated events: death, departure, name alias, marriage  
- Lots of `FLEX` for page-level and person-specific details  
- All roles defined using `STICKY` + annotations (no `INDI` records)
- Uses special `FLEX` type `ANNOTATION` for all annotated notes in the census. That way user/software can decide to print these annotations or not.

**📜 @T1920@ TEMPLATE – 1920 household census in Boston**
```gedcom
0 @T1920@ TEMPLATE
1 TYPE RESIDENCE, POPCENSUS   /* PopulationCensus */
1 TITL 1920 US Federal Census – Deduction Household
2 PHRASE Household census, with later annotations in margins.
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 01 JAN 1920
1 SPLAC @SP1000@              /* Boston, Suffolk County, Massachusetts, USA */
1 CENS                        /* Event of the TEMPLATE */
2 TYPE Population
2 DATE 01 JAN 1920
2 SPLAC @SP1000@              /* Boston, Suffolk County, Massachusetts, USA */
2 ADDR
3 123 Main Street
3 CITY Boston
3 STAE MA
3 CTRY USA
1 FLEX REGNUMBER
2 PHRASE Dwelling Number
2 CONTENTS 17A
1 FLEX REGNUMBER
2 PHRASE Household ID
2 CONTENTS 4
1 FLEX ADDRESS
2 PHRASE Street and number
2 CONTENTS 123 Main Street
1 FLEX DESCRIPT
2 PHRASE Page note
2 CONTENTS "Top margin: 'Subdistrict 7A, Sheet 3A, Supervisor: E. Snoreworthy'"
1 ROLES
2 STICKY @ST0100@             /* Barnabas Deduction –  MAIN, HEAD, RESIDENT */
2 STICKY @ST0101@             /* Penny Deduction – SPOUSE, RESIDENT */
2 STICKY @ST0102@             /* Orville Deduction – Son - CHILD, RESIDENT */
2 STICKY @ST0103@             /* Edwina Deduction – Daughter - CHILD, RESIDENT */
2 STICKY @ST0104@             /* Willa Tinywhistle – Orphaned Niece - NIECE, RESIDENT */
2 STICKY @ST0105@             /* Augustus Deduction – Grandfather */
2 STICKY @ST0106@             /* Mabel Scrubbs – Live-in Maid - MAID, RESIDENT */
2 STICKY @ST0107@             /* Augustus Crumb - BOARDER, RESIDENT */
2 STICKY @ST0110@             /* Edwina's DEPARTURE - AN_LEAVE */
2 STICKY @ST0111@             /* Willa's ARRIVAL */
2 STICKY @ST0112@             /* Augustus's DEATH - AN_DEATH */
2 STICKY @ST0113@             /* Mabel's ARRIVAL */
2 STICKY @ST0114@             /* Barnabas's NAME ALIAS */
2 STICKY @ST0115@             /* Penny's MARRIAGE annotation */
1 NOTE Census household appears orderly. Marginal note mentions: "Excellent curtains."
1 CITA
2 SOUR @S0374@
2 PAGE 5
2 DATA
~  ~ ~
1 CREA 18 JUL 2025
1 CHAN 18 JUL 2025
```
### 🏠 Household Members

**🧓 @ST0026@ STICKY – Head of Household: Barnabas Deduction**
```gedcom
0 @ST0100@ STICKY             /* Barnabas Deduction: Head of Household */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE MAIN, FAMILYHEAD, RESIDENT
1 NAME
2 TYPE BIRTH                  /* Name at birth */
2 FORM Barnabas Deduction
2 PART Barnabas
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 12 JUN 1878
2 SPLAC @SP1001@              /* Concord, New Hampshire */
1 OCCU Tailor
1 RELI Unitarian
1 CENS
2 TYPE Population
2 DATE 01 JAN 1920
2 SPLAC @SP1000@              /* Boston, Suffolk County, Massachusetts, USA */
2 ADDR
3 123 Main Street
3 CITY Boston
3 STAE MA
3 CTRY USA
~ ~ ~
```
**👩 @ST0027@ STICKY – Wife: Penny Deduction**
```gedcom
0 @ST0101@ STICKY             /* Penny Deduction: Wife */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE SPOUSE, RESIDENT
1 NAME
2 FORM Penny Deduction
2 PART Penny
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 SEX F
1 BIRT
2 DATE 03 FEB 1880
2 SPLAC @SP1002@              /* Medford, MA */
1 OCCU Seamstress
1 RELI Methodist
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🧒 @ST0028@ STICKY – Son: Orville Deduction**
```gedcom
0 @ST0102@ STICKY             /* Orville Deduction: Son */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE CHILD, RESIDENT
1 NAME
2 FORM Orville Deduction
2 PART Orville
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 19 SEP 1905
2 SPLAC @SP1000@              /* Boston */
1 OCCU Newsboy
1 RELI Unitarian
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**👧 @ST0029@ STICKY – Daughter: Edwina Deduction**
```gedcom
0 @ST0103@ STICKY             /* Edwina Deduction: Daughter */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE CHILD, RESIDENT
1 NAME
2 FORM Edwina Deduction
2 PART Edwina
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 SEX F
1 BIRT
2 DATE 05 NOV 1907
2 SPLAC @SP1000@              /* Boston */
1 RELI Unitarian
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🧭 @ST0030@ STICKY – Niece: Willa Tinywhistle**
```gedcom
0 @ST0104@ STICKY             /* Willa Tinywhistle: Orphaned Niece */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE NIECE, RESIDENT
1 NAME
2 FORM Willa Tinywhistle
2 PART Willa
3 TYPE GIVN
2 PART Tinywhistle
3 TYPE SURN
1 SEX F
1 BIRT
2 DATE 20 APR 1913
2 SPLAC @SP1003@              /* Wobbleton, VT */
1 RELI Catholic
1 FLEX ANNOTATION
2 PHRASE Clerk’s note
2 CONTENTS Lives with aunt and uncle since parents’ death in 1918.
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**👴 @ST0105@ STICKY – Augustus Deduction: Grandfather**
```gedcom
0 @ST0105@ STICKY             /* Augustus Deduction: Grandfather */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE GRANDFATHER, RESIDENT
1 NAME
2 FORM Augustus Deduction
2 PART Augustus
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 01 MAR 1840
2 SPLAC @SP1004@              /* Lowell, MA */
1 NOTE Slightly deaf; always mishears census taker.
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🧽 @ST0106@ STICKY – Maid: Mabel Scrubbs**
```gedcom
0 @ST0106@ STICKY             /* Mabel Scrubbs: Maid */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE SERVANT, RESIDENT
1 NAME
2 FORM Mabel Scrubbs
2 PART Mabel
3 TYPE GIVN
2 PART Scrubbs
3 TYPE SURN
1 SEX F
1 AGE 24
1 OCCU Maid
1 RELI Presbyterian
1 FLEX ANNOTATION
2 PHRASE Side-entry remark
2 CONTENTS Joined household from Turnip Junction after mother’s passing.
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🧳 @ST0101@ STICKY – Boarder: Augustus Crumb**
```gedcom
0 @ST0101@ STICKY             /* Augustus Crumb - BOARDER, RESIDENT */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE BOARDER, RESIDENT
1 NAME
2 FORM Augustus Crumb
2 PART Augustus
3 TYPE GIVN
2 PART Crumb
3 TYPE SURN
1 SEX M
1 AGE 52
1 RESI
2 DATE 01 FEB 1923
2 SPLAC @SP0134@              /* Cluttsville, Arkansas */
1 FLEX ANNOTATION
2 PHRASE Recorded comment
2 CONTENTS "Moved into the Deduction household after losing his boarding contract with the Flapjack sisters."
1 OCCU Traveling Salesman
1 FLEX ANNOTATION
2 PHRASE Margin note
2 CONTENTS "Nominally a 'traveling salesman', though rarely seen selling anything."
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🪦 @ST0112@ STICKY – Augustus Dies**
```gedcom
0 @ST0112@ STICKY             /* Augustus Dies */
1 TYPE PERSON, AN_DEATH       /* A secondary "event" */
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE RESIDENT
1 NAME
2 FORM Augustus Deduction
2 PART Augustus
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 01 MAR 1840
2 SPLAC @SP1004@              /* Lowell, MA */
1 DEAT
2 DATE 14 SEP 1920
2 SPLAC @SP1000@              /* Boston */
1 FLEX ANNOTATION
2 PHRASE Side annotation
2 CONTENTS Passed quietly during afternoon nap. Marginal note: 'Gone but still snoring'.
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🟰 @ST0114@ STICKY – Alias for Barnabas**
```gedcom
0 @ST0114@ STICKY             /* Alias for Barnabas DOES NOT HAVE A DATE assigned on the TEMPLATE */
1 TYPE PERSON, AN_ALIAS       /* A secondary "event" */
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE RESIDENT
1 NAME
2 TYPE AKA                    /* Alias */
2 FORM Barnabas Deduction
2 PART Barnabas
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
2 FORM Barney
2 PART Barney
3 TYPE INFORMAL
1 SEX M
1 BIRT
2 DATE 12 JUN 1878
2 SPLAC @SP1001@              /* Concord, New Hampshire */
1 OCCU Tailor
1 RELI Unitarian
1 FLEX ANNOTATION
2 PHRASE Registry note
2 CONTENTS Also known informally as "Barney" in neighborhood.
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```

### 📝 Annotated Events

**🚂 @ST0110@ STICKY – Edwina Leaves**
```gedcom
0 @ST0110@ STICKY             /* Edwina Leaves */
1 TYPE PERSON, AN_LEAVE       /* A secondary "event" */
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE RESIDENT
1 NAME
2 FORM Edwina Deduction
2 PART Edwina
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 RESI                        /* Move from (leave) */
2 DATE UNTIL 10 NOV 1921
2 SPLAC @SP1000@              /* Boston */
1 RESI                        /* Move to */
2 DATE 18 NOV 1921
2 SPLAC @SP0052@              /* Scrubbington */
1 FLEX ANNOTATION
2 PHRASE Registry note
2 CONTENTS "Edwina moved to Scrubbington on 18 NOV 1920 to work as housemaid."
1 FLEX ANNOTATION
2 PHRASE Margin note
2 CONTENTS "Marginal note: 'Left home to work for Mrs. Butterworth in Scrubbington'."
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🛍️ @ST0111@ STICKY – Willa Arrives**
```gedcom
0 @ST0111@ STICKY             /* Willa Arrives */
1 TYPE PERSON, AN_ARRIVE      /* A secondary "event" */
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE NIECE, RESIDENT
1 NAME
2 FORM Willa Tinywhistle
2 PART Willa
3 TYPE GIVN
2 PART Tinywhistle
3 TYPE SURN
1 SEX F
1 BIRT
2 DATE 20 APR 1913
2 SPLAC @SP1003@              /* Wobbleton, VT */
1 RELI Catholic
1 RESI                        /* Moved in from unknown place (arrives) */
2 DATE
1 RESI
2 DATE 1922
2 SPLAC @SP1000@              /* Boston */
1 FLEX ANNOTATION
2 PHRASE Side annotation
2 CONTENTS Arrived in household 1922.
1 FLEX ANNOTATION
2 PHRASE Margin note
2 CONTENTS "Orphaned in influenza outbreak; moved in with Deduction family."
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**🚌 @ST0113@ STICKY – Mabel Moves In**
```gedcom
0 @ST0113@ STICKY             /* Mabel Moves In */
1 TYPE PERSON, AN_ARRIVE      /* A secondary "event" */
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE SERVANT, RESIDENT
1 NAME
2 FORM Mabel Scrubbs
2 PART Mabel
3 TYPE GIVN
2 PART Scrubbs
3 TYPE SURN
1 RESI                        /* arrived in early 1920 in the household */
2 DATE spring 1920
2 SPLAC @SP1000@              /* Boston */
1 SEX F
1 AGE 24
1 OCCU Maid
1 RELI Presbyterian
1 RESI
2 DATE BEFORE spring 1920     /* she arrived from Turnip Junction (previous resi) */
2 SPLAC @SP750@               /* Turnip Junction, NH */
1 FLEX ANNOTATION
2 PHRASE Side-entry remark
2 CONTENTS From Turnip Junction. Reference from local Bishop Snugglesworth.
1 FLEX ANNOTATION
2 PHRASE Marginal scribble
2 CONTENTS Hired maid, moved in spring 1920.
1 FLEX ANNOTATION
2 PHRASE Clerk’s note
2 CONTENTS "Mabel Scrubbs, housemaid, arrived from Turnip Junction in early 1920."
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```
**💍 @ST0114@ STICKY – Penny’s Marriage Note**
```gedcom
0 @ST0115@ STICKY             /* Penny’s Marriage Note */
1 TYPE PERSON, AN_MARRIAGE    /* A secondary "event" */
1 SUBM @B001@
1 TEMPLATE @T1920@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE RESIDENT  /* annotation about Penny's marriage date */
1 NAME
2 FORM Penny Deduction
2 PART Penny
3 TYPE GIVN
2 PART Deduction
3 TYPE SURN
1 MARR
2 DATE 20 AUG 1903
2 SPLAC @SP1005@              /* Nashua, NH */
1 FLEX ANNOTATION
2 PHRASE Clerk’s note
2 CONTENTS Separate record from town clerk attached to page.
1 CENS                        /* Identical to CENS for Barnabas */
~ ~ ~
```

[🔝 Back to top](#appendix-b-gedcom-examples)



---

<a name="example-06"></a>  
## 🎖️ Example 06: Medal awarded to individual

This GEDCOM 8 example models a military medal awarded to a soldier for bravery.  
The `TEMPLATE` is of type `MILITARY, AWARD` and connects a tangible object (the medal itself) with the recipient using `STICKY` roles.  
The example uses:  
- `ROLE GRANTOR` and `ROLE GRANTEE`, used in a `TRANSFER`.  
- Two `FLEX` entries to store the medal’s name and inscription  
- A fictional `SPLAC` record with dramatic flair
- An event of type `MILITARY, AWARD`.
- A `CITA` record with a lot of (fictional) info.
- A sober SOURCE — because someone has to be official  
- This example does NOT use an `ASSET` record, as the medal is only for this person and will not be granted to another.

**🪪 Awardings: @T0001@ – Medal for Bravery**

```gedcom
0 @T0001@ TEMPLATE            /* Awarding of Medal for Bravery */
1 TYPE MILITARY, AWARD
1 TITL Awarding of Medal for Bravery
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 07 JUN 1944
1 SPLAC @SP00213@             /* Battle Museum Archive */
1 EVEN MILITARY, AWARD
2 DATE 07 JUN 1944
2 SPLAC @SP00213@             /* Battle Museum Archive */
1 ROLES
2 STICKY @ST0001@             /* AWARD, MILITARY, Silver Star medal */
2 STICKY @ST0002@             /* MAIN, GRANTEE, James Bronson */
2 STICKY @ST0003@             /* ORGANIZATION, MILITARY, GRANTOR, Department of War */
1 TRANSFER @ST0001@           /* The medal itself */
2 GRANTOR @ST0003@            /* GRANTOR, Department of War  */
2 GRANTEE @ST0002@            /* GRANTEE, James Bronson */
1 CITA
2 SOUR @S0001@                /* U.S. Army Decorations Record, 1944 */
2 PAGE 88
2 DATA
3 DATE 1944-06-07
3 TEXT Official transcript describing the Silver Star award
4 MIME text/plain
4 LANG en
2 AUTHOR Department of War
2 TITL Awarding of the Silver Star to Pvt. James Bronson
2 DATES
3 CREATED 07 JUN 1944
3 RECORDED 08 JUN 1944
2 REPOSITORY National Archives, Boomtown
2 TEXTDISPLAY "Award issued for gallantry during the Normandy invasion"
2 TRANSCRIPT "Private Bronson distinguished himself by acts of bravery under enemy fire..."
2 FORMAT
3 TYPE application/pdf
2 URL https://www.archives.fake/us/bronson-silverstar.pdf
2 LANGUAGE en
2 RECORDID BRONSON19440607
2 VOLUME 29
2 CHAPTER Infantry Awards
2 SHORTTITLE Silver Star – Bronson
2 WWWLINK
3 VALUE https://valor.fake/wiki/Bronson_SilverStar
2 QUAY 3
2 NOTE Transcribed from original paper certificate
1 CREA 15 APR 2025
1 CHAN 15 APR 2025
```
**🥈 @ST0001@ STICKY – Silver Star medal**
```gedcom
0 @ST0001@ STICKY
1 TYPE AWARD, MILITARY
1 TEMPLATE @T0001@            /* Belongs to this TEMPLATE */
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 06 JUN 1944
1 FLEX DESCRIPT
2 PHRASE "Award Type"
2 CONTENTS "Silver Star medal"
1 FLEX MATERIAL
2 PHRASE "Award Material"
2 CONTENTS "Silver"
1 FLEX DESCRIPT
2 CONTENTS "Awarded after Normandy landing"
1 PHRASE "Inscription"
1 FLEX DESCRIPT
2 PHRASE "Award Reason"
2 CONTENTS "For gallantry in action"
~ ~ ~
```
**🪖 @ST0001@ STICKY – James Bronson**
```gedcom
0 @ST0002@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0001@            /* Belongs to this TEMPLATE */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 ROLE MAIN, RECIPIENT
1 EVEN MILITARY, AWARD
2 DATE 07 JUN 1944
2 SPLAC @SP00213@             /* Battle Museum Archive */
1 DATE 06 JUN 1944
1 NAME
2 FORM James Bronson
2 PART JAMES
3 TYPE GIVN
2 PART Bronson
3 TYPE SURN
1 SEX M
1 OCCU Private, 29th Infantry Division
1 EVEN                        /* Same eventtype as the TEMPLATE type. */
2 TYPE MILITARY, AWARD
2 DATE 07 JUN 1944
2 SPLAC @SP00213@             /* Battle Museum Archive */
~ ~ ~
```
**🏢 @ST0001@ STICKY – Department of War**
```gedcom
0 @ST0003@ STICKY
1 TYPE ORGANIZATION, MILITARY, GRANTOR
1 SUBM @B001@
1 TEMPLATE @T0001@            /* Belongs to this TEMPLATE */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 06 JUN 1944
1 NAME Department of War
2 ROLE GRANTOR
1 ADDRPLUS
2 ADDR Explosives Division, Bureau of Bravery 1 Heroism Plaza
3 CITY Boomtown
3 STAE BLZ
3 POST 99999
3 CTRY USA
2 PHON +1-202-555-1944
3 TITL War Medals Desk
2 PHON +1-202-555-1945
3 TITL Complaint Hotline (Unmonitored)
2 EMAIL medals@boom.gov
3 TITL Medal Distribution
~ ~ ~
```
**💾 @S0001@ SOURCE U.S. Army Decorations Record, 1944**
```gedcom
0 @S0001@ SOUR
1 TITL U.S. Army Decorations Record, 1944
1 AUTH "Department of War"
1 PUBL "National Archives"
1 DATA
~ ~ ~
```

[🔝 Back to top](#appendix-b-gedcom-examples)


---

<a name="example-07"></a>  
## 🌿 Example 07: Land Grant Record

This GEDCOM 8 example demonstrates a **nearly complete TEMPLATE** of type `PROPERTY, GRANT`, representing a **royal land grant** issued in 1811 to a private citizen, Hiram Mudshoe, as a reward for military service.  
It includes a structured `TRANSFER` with a defined `GRANTOR`, `GRANTEE`, and land parcel `ASSET`, as well as a properly detailed `CITA` section with archival metadata.  
The record balances formal archival clarity with a subtle touch of humor in names and phrasing.  
Useful for illustrating how property ownership and rights are modeled using the GEDCOM 8 `TRANSFER` structure.

**📜 @T0043@ TEMPLATE – Land Grant to Hiram Mudshoe**
```gedcom
0 @T0043@ TEMPLATE
1 TYPE PROPERTY, GRANT "Royal Land Grant for Service"
1 TITL Royal Land Grant Dossier: Parcel 98
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 MAY 1811
1 SPLAC @SP0392@              /* Crown Colony of Upper Fenshire */
1 EVEN PROPERTY, GRANT        /* Land Grant event */
2 DATE 12 MAY 1811
2 SPLAC @SP0392@              /* Crown Colony of Upper Fenshire */
1 ROLES
2 STICKY @ST0144@             /* MAIN, PERSON, GRANTEE Hiram Mudshoe */
2 STICKY @ST0244@             /* ORGANIZATION, GRANTOR */
2 STICKY @ST0344@             /* LAND, MEADOW (Land Parcel) */
1 TRANSFER @ST0344@           /* The land itself */
2 GRANTOR @ST0244@            /* GRANTOR Royal Survey and Appropriations Office */
2 GRANTEE @ST0144@            /* GRANTEE Hiram Mudshoe */
1 CITA
2 SOUR @S0043@                /* Royal Land Grant Dossier: Parcel 98 */
2 PAGE Volume 7, Folio 19
2 DATA
3 DATE 12 MAY 1811
3 TEXT "Deed issued to Mr. Hiram Mudshoe by crown order."
2 AUTHOR Clerk Tiddlebreech
2 TITL Royal Land Grant Archive Entry
2 DATES
3 RECORDED 12 MAY 1811
2 REPOSITORY "Royal Survey Archive, Box 7B"
2 SHORTTITLE "Land Grant: Parcel 98"
2 FORMAT
3 TYPE application/pdf
2 QUAY 3
2 TEXTDISPLAY "Land Grant entry for Parcel 98 – grantee: Hiram Mudshoe"
2 TRANSCRIPT "This document certifies the grant of Parcel 98 to Mr. Hiram Mudshoe, effective 12 MAY 1811."
2 RECORDID RG-1811-F98-MUD
2 LANGUAGE en
2 ITEMTYPE deed
2 WWWLINK
3 VALUE https://royalarchive.fenshire.gov/grants/parcel98
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🧑🏼‍🌾 @ST0144@ STICKY – Grantee: Hiram Mudshoe**
```gedcom
0 @ST0144@ STICKY             /* PERSON, Hiram Mudshoe */
1 TYPE PERSON
1 TEMPLATE @T0043@
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 MAY 1811
1 SPLAC @SP0392@              /* Crown Colony of Upper Fenshire */
1 EVEN PROPERTY, GRANT        /* Land Grant event */
2 DATE 12 MAY 1811
2 SPLAC @SP0392@              /* Crown Colony of Upper Fenshire */
1 ROLE GRANTEE
1 NAME
2 FORM Hiram Mudshoe
2 PART Hiram
3 TYPE GIVN
2 PART Mudshoe
3 TYPE SURN
1 SEX M
1 AGE 38
1 OCCU "Mosquito frontier defense strategist (unpaid)"
1 NOTE "Awarded land for bravery during the Foggy Skirmish of '09."
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🏛️ @ST0244@ STICKY – Grantor: Royal Survey and Appropriations Office**
```gedcom
0 @ST0244@ STICKY             /* ORGANIZATION, GRANTOR, Royal Survey and Appropriations Office */
1 TYPE ORGANIZATION, CROWN, Royal Survey and Appropriations Office
1 TITL Royal Survey and Appropriations Office
1 SUBM @B001@
1 TEMPLATE @T0043@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 MAY 1811
1 SPLAC @SP0392@              /* Crown Colony of Upper Fenshire */
1 ROLE GRANTOR
1 NAME
2 FORM Royal Survey and Appropriations Office
1 NOTE "Issued the grant under warrant #428-FogSouth-1811"
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🌾 @ST0344@ STICKY – Land Parcel: Lower Bogside (Parcel 98)**
```gedcom
0 @ST0344@ STICKY             /* LAND, MEADOW, Parcel 98 – Lower Bogside */
1 TYPE LAND, MEADOW, "Parcel 98 – Lower Bogside"
1 TITL Parcel 98 – Lower Bogside
1 SUBM @B001@
1 TEMPLATE @T0043@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 MAY 1811
1 SPLAC @SP0392@              /* Crown Colony of Upper Fenshire */
1 FLEX DECIMAL, CURR, GBP
2 PHRASE "Value"
2 CONTENTS 12.00
1 FLEX UNIT
2 PHRASE "Size"
2 CONTENTS 14 acres
1 FLEX DESCRIPT
2 PHRASE "Boundaries"
2 CONTENTS "North: Crooked Tree; South: Whispering Ditch; East: Sogstone Path; West: Unnamed Mound"
1 NOTE "Soggy but legally fertile. Includes exclusive fishing rights on Tuesdays."
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**👤 @I201@ INDI – Hiram Mudshoe**
```gedcom
0 @I201@ INDI                 /* INDI: Hiram Mudshoe */
1 NAME
2 FORM Hiram Mudshoe
2 PART HIRAM
3 TYPE GIVN
2 PART Mudshoe
3 TYPE SURN
1 SEX M
1 AGE 38
1 ROLES
2 STICKY @ST0144@             /* PERSON, GRANTEE */
1 ASSETS
2 STICKY @ST0344@             /* LAND, MEADOW (Land Parcel) */
2 DATE 12 MAY 1811
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```

**📦 @S0043@ SOUR – Land Grant Source**
```gedcom
0 @S0043@ SOUR
1 TITL Royal Land Grant Dossier: Parcel 98
1 AUTH Clerk Tiddlebreech
1 DATA
2 EVEN PROPERTY, GRANT
3 DATE 12 MAY 1811
3 SPLAC @SP0391@              /* Upper Fenshire Registry */
~ ~ ~
1 NOTE "Stored in the Royal Survey Archive, Box 7B. Filing clerk noted to beware ink spills."
1 REPO Royal Survey Archive   /* Not present in example */
2 CALN 13B-1234.01
1 CHAN 31 JUL 2025
```

[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-08"></a>  
## 🪪 Example 08: Naturalization and Passport

This example models the legal and bureaucratic trail of a European immigrant becoming a U.S. citizen and receiving a passport in the early 1900s. The individual, Leopold “Leo” Federwitz, was born in Kraków, naturalized in 1905, and received a passport in 1907.  
It uses **two separate TEMPLATES** — one for the naturalization certificate and one for the passport — both including roles, a STICKY asset for the physical document, and a separate SOURce each. This example is **fully updated for GEDCOM 8**, including structured CITA blocks, SPLAC tags, document assets, humorous notes, and proper QUAY levels.

🔖 **New feature shown here:** The `INDI` block now includes an **`ASSETS` section**, referencing both the **naturalization certificate** and the **passport** as document STICKYs. This is one of the few examples that demonstrates how personal document holdings can be tracked directly under an individual.

The updated template type lines use specific enums like `ORGANIZATION, COURT` or `IDENTITY, PASSPORT`. This version includes:
- Dual role mentions for Leopold Federwitz (naturalization and passport).
- Organizational roles: Immigration Court and Passport Bureau.
- Physical document tracking with STICKYs of type `ASSET, DOCUMENT`.
- Structured notes and sources.
- Playful yet informative annotation for testing, teaching, and demo purposes.
    
**🪪 @T0045@ TEMPLATE – Naturalization Certificate**
```gedcom
0 @T0045@ TEMPLATE
1 TYPE ORGANIZATION, COURT "Certificate of Naturalization"
1 TITL Certificate of Naturalization – Leopold Federwitz
2 PHRASE "Leopold Federwitz naturalized as U.S. citizen"
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 3 OCT 1905
1 SPLAC @SP592@               /* Cleveland, Ohio, USA */
1 NATU                        /* Naturalization event */
2 DATE 3 OCT 1905
2 SPLAC @SP592@               /* Cleveland, Ohio, USA */
2 AGNC United States Immigration Court, Cleveland
1 ROLES
2 STICKY @ST0146@             /* PERSON, SUBJECT */
2 STICKY @ST0246@             /* ORGANIZATION, AUTHORITY (Immigration Office) */
2 STICKY @ST0347@             /* Naturalization Certificat */
1 CITA
2 SOUR @S0045@
2 TITL Certificate of Naturalization – Leopold Federwitz
2 PAGE 1
1 DATA
~ ~ ~
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🧍 @ST0146@ STICKY – Person Leopold Federwitz**
```gedcom
0 @ST0146@ STICKY             /* PERSON, Leopold Federwitz */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0045@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 3 OCT 1905
1 SPLAC @SP592@               /* Cleveland, Ohio, USA */
1 ROLE MAIN, RECIPIENT        /* Recieves that certificate */
1 NAME
2 FORM Leopold Federwitz
2 PART Leopold
3 TYPE GIVN
2 PART Federwitz
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 28 FEB 1878
2 SPLAC @SP055@               /* Kraków, Austria-Hungary */
1 OCCU "Importer of educational teas and mustache oils"
1 NATU                        /* Naturalization event */
2 DATE 3 OCT 1905
2 SPLAC @SP592@               /* Cleveland, Ohio, USA */
2 AGNC United States Immigration Court, Cleveland
1 NOTE "Naturalized after confusing Cleveland with Lisbon. Decided to stay."
1 OBJE @O0751@                /* Multimedia record with file link  */
2 TITL Scanned certificate of naturalization
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🏛️ @ST0246@ STICKY – Organization: Immigration Authority**
```gedcom
0 @ST0246@ STICKY
1 TYPE ORGANIZATION, COURT, Immigration Court
1 TITLE United States Immigration Court, Cleveland
1 SUBM @B001@
1 TEMPLATE @T0045@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 3 OCT 1905
1 SPLAC @SP592@               /* Cleveland, Ohio, USA */
1 ROLE JUDGE, ISSUER          /* Released the document */
1 NATU                        /* Naturalization event */
2 DATE 3 OCT 1905
2 SPLAC @SP592@               /* Cleveland, Ohio, USA */
2 AGNC United States Immigration Court, Cleveland
1 NOTE "Processed oath of allegiance, filed under case #1905-328C"
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🪪 @ST0347@ STICKY – Naturalization Certificat as physical asset**
```gedcom
0 @ST0457@ STICKY             /* Naturalization Certificate as physical asset */
1 TYPE DOCUMENT, CERTIFICATE, "Naturalization Certificate"
1 TITL Naturalization Certificate of Leopold Federwitz
1 SUBM @B001@
1 TEMPLATE @T0045@            /* Naturalization Certificate for Leopold Federwitz */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE  3 OCT 1905            /* Date of issue on document */
1 SPLAC @SP592@               /* Cleveland, Ohio, USA */
1 NAME "Naturalization Certificate of Leopold Federwitz"
1 NOTE "Issued by United States Immigration Court, Cleveland"
1 CREA 1 JUL 2025
1 CHAN 31 JUL 2025
```
**🛄 @T0046@ TEMPLATE – Passport Issuance**
```gedcom
0 @T0046@ TEMPLATE
1 TYPE IDENTITY, PASSPORT "United States Passport"
1 TITL U.S. Passport for Leopold Federwitz
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 21 JUL 1907
1 SPLAC @SP843@               /* Washington, D.C., USA */
1 EVEN IDENTITY, PASSPORT
2 DATE  21 JUL 1907
2 SPLAC @SP843@               /* Washington, D.C., USA */
1 ROLES
2 STICKY @ST0746@             /* MAIN, RECIPIENT Leopold Federwitz */
2 STICKY @ST0046@             /* ORGANIZATION, role ISSUER (Passport Office) */
2 STICKY @ST0456@             /* DOCUMENT, ID, "passport" */
1 CITA
2 SOUR @S0046@
2 TITL U.S. Passport for Leopold Federwitz
~ ~ ~
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🏢 @ST0346@ STICKY – Organization: Passport Bureau**
```gedcom
0 @ST0346@ STICKY
1 TYPE ORGANIZATION, GOVERNMENT, U.S. Department of State
1 TITL United States Passport Bureau
1 SUBM @B001@
1 TEMPLATE @T0046@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 21 JUL 1907
1 SPLAC @SP843@               /* Washington, D.C., USA */
1 ROLE ISSUER
1 NOTE "Issued under file #P-88311. Destination vaguely listed as ‘abroad.’"
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🪪 @ST0346@ STICKY – Passport as physical asset**
```gedcom
0 @ST0456@ STICKY             /* Passport as physical asset */
1 TYPE DOCUMENT, ID, "passport"
1 TITL Passport of Leopold Federwitz
2 PHRASE "Issued by U.S. Passport Bureau after naturalization"
1 SUBM @B001@
1 TEMPLATE @T0146@            /* U.S. Passport for Leopold Federwitz */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 21 JUL 1907            /* Date of issue on document */
1 SPLAC @SP843@               /* Washington, D.C., USA */
1 NOTE "Physical document; original possibly stored in cigar box held by great-grandniece"
1 OBJ @O003@                  /* Photo of passport */
1 CREA 1 JUL 2025
1 CHAN 31 JUL 2025
```
**🧍 @ST0146@ STICKY – Person Leopold Federwitz**
```gedcom
0 @ST0746@ STICKY             /* PERSON, Leopold Federwitz */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0746@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 21 JUL 1907
1 SPLAC @SP843@               /* Washington, D.C., USA */
1 EVEN IDENTITY, PASSPORT
2 DATE  21 JUL 1907
2 SPLAC @SP843@               /* Washington, D.C., USA */
1 ROLE MAIN, RECIPIENT        /* Recieves that passport */
1 NAME
2 FORM Leopold Federwitz
~ ~ ~
1 SEX M
1 BIRT
2 DATE 28 FEB 1878
2 SPLAC @SP3810@              /* Kraków, Austria-Hungary */
1 OCCU "Importer of educational teas and mustache oils"
1 NOTE "Naturalized after confusing Cleveland with Lisbon. Decided to stay."
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**👤 @I401@ INDI for Leopold Federwitz**
```gedcom
0 @I401@ INDI
1 NAME
2 FORM Leopold Federwitz
2 PART Leopold
3 TYPE GIVN
2 PART Federwitz
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 28 FEB 1878
2 SPLAC @SP3810@              /* Kraków, Austria-Hungary */
1 ROLES
2 STICKY @ST0146@             /* Leopold Federwitz, recieves Naturalization Certificate */
2 STICKY @ST0746@             /* Leopold Federwitz, recieves passport */
1 ASSETS
2 @ST0456@ STICKY             /* Passport as physical asset */
2 @ST0457@ STICKY             /* Naturalization Certificate as physical asset *
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**💾 SOURCE @S0045@ for Naturalization**
```gedcom
0 @S0045@ SOUR
1 TITL Certificate of Naturalization – Leopold Federwitz
1 AUTH United States Immigration Court
1 PUBL "Filed in U.S. National Archives, case #1905-328C"
1 ABBR "Federwitz Naturalization 1905"
1 NOTE "Federwitz swore allegiance and was granted citizenship on 3 October 1905."
1 DATA
2 EVEN NATU                   /* Naturalization */
3 DATE 3 OCT 1905
4 PHRASE "Naturalization of Leopold Federwitz under U.S. law"
3 SPLAC @SP001@               /*  Cleveland, Ohio, USA */
2 AGNC U.S. Immigration Court, Cleveland
2 NOTE "Preserved in U.S. National Archives, box 12, folder 3"
~ ~ ~
1 OBJE @O0751@
2 TITL Scanned certificate of naturalization
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🖼️ OBJE @O0751@ – Scan of Naturalization Certificate**
```gedcom
0 OBJE @O0751@                /* Multimedia record with file link  */
1 FILE https://example.org/naturalizations/federwitz-1905-cert.pdf
2 FORM application/pdf
3 MIME application/pdf
2 TITL Scanned certificate of naturalization
1 NOTE "Photo slightly faded; corner stamped with embassy seal."
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**💾 SOURCE @S0046@ for Passport**
```gedcom
0 @S0046@ SOUR
1 TITL U.S. Passport for Leopold Federwitz
2 PHRASE "Passport issued to Leopold Federwitz"
1 AUTH United States Passport Bureau          /* created/authored the document */
1 PUBL "U.S. Department of State Records, 1907"
1 ABBR "Federwitz Passport 1907"
1 DATA                                        /* Info about the data inside the document */
2 EVENT IDENTITY, PASSPORT
3 DATE 21 JUL 1907
3 SPLAC @SP0006@                              /* Washington, D.C., USA */
2 AGNC United States Passport Bureau          /* handled or executed the event */
2 NOTE "Passport issued after naturalization"
~ ~ ~
1 OBJ @O003@                                  /* Picture of the passport */
2 TITL Scan of 1907 passport for Leopold Federwitz
1 NOTE "Original held by great-grandniece, possibly in a cigar box"
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```


[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-09"></a>  
## ⛪ Example 09: Adult baptism and religious roles

### ⛪ Full Example Bundle: Religious Roles in Action

📌 **Summary:** This example bundle demonstrates full lifecycle participation in religious roles, from infant baptism and conversion to ordination, with cross-linked individuals and heirlooms across decades.

### 📜 Explanation: Baptism, Confirmation, Ordination, Conversion
These four religious rites may appear across many traditions and have distinct purposes:

| Term       | Usual Age      | Purpose        | One-time? | Common `ROLE` / `SUBROLE` | Notes |
|------------|----------------|----------------|-----------|---------------------------|-------|
| `Baptism`     | Infant or Adult | Ritual of entry into the faith; often involves water |✅ | `RELIGIOUS` / `CHILD` or `INITIATE` | May be performed on newborns (infant baptism) or adults (convert baptism) |
| `Confirmation`| Teen or Adult   | Affirmation of earlier baptism; signifies maturity in faith | ✅ | `RELIGIOUS` / `INITIATE` | Often follows infant baptism; typical in Catholic, Anglican, Lutheran rites |
| `Ordination`  | Adult           | Designation as clergy or spiritual leader        | ✅ | `RELIGIOUS` / `CLERGY`    | Grants authority to lead services or administer sacraments |
| `Conversion`  | Any             | Formal switch of religious affiliation   | ✅ | `RELIGIOUS` / `INITIATE`  | May involve adult baptism and profession of faith |

### Overview
This combined example illustrates **all religious roles** in GEDCOM 8 `STICKY`'s, including:
- Adult conversion (Hans and Johannes)
- Infant baptism (Johannes)
- Ordination (Einar Voss)
- Clergy participation (Henrik Brodahl)
- Godparent and family witness roles (Marta, Karl)
- Religious assets (Baptism gown)

### 🧵 Main Participants

**Johannes Thomassen** (b. 1797)  
Baptized as a Catholic infant in Bergen, Johannes grows up in a Catholic household. As a young adult, he is confirmed and later undergoes a spiritual transformation, converting to Lutheranism in 1821 under Pastor Einar Voss, a close mentor figure.

**Einar Voss** (b. ~1790s)  
A devout Lutheran who entered theological seminary in 1814 and was ordained in 1820. Einar serves as a Lutheran pastor in Bergen and plays a pivotal role in receiving new converts, including Johannes and Hans Kristensen.

| Temp-ID | Date      | Event Type<br> and person         | Role/Notes         | TEMPLATE EVENT         | SPLAC (place) |
|--------|------------|--------------------|---------------------|------------------------|---------------|
|   —    | 14 MAY 1797| Birth<br>Johannes Thomassen  | —      | —   | SPLAC @SP0063@ Bergen Parish Church (Catholic) |
| @T771@ | 17 MAY 1797| Baptism<br>Johannes Thomassen | MAIN,<br>CHILD  | RELIGIOUS, BAPTISM | SPLAC @SP0063@ Bergen Parish Church (Catholic) |
| @T772@ | 30 JAN 1805| Rel.Commitment/ Vow<br>Einar Voss| MAIN,<br>INITIATE, VOW| RELIGIOUS,<br>ENTRY  | SPLAC @SP0123@ Stavanger Theological Seminary (Lutheran) |
| @T773@ | 30 JUL 1809| Confirmation<br>Johannes Thomassen| MAIN, CONFIRMEE | RELIGIOUS, CONFIRM  | SPLAC @SP0063@ Bergen Parish Church (Catholic) |
| @T774@ | 10 APR 1812| Ordination<br>Einar Voss| MAIN,<br>DEACON | RELIGIOUS, ORDINATION  | SPLAC @SP0081@ Stavanger Diocese Seminary (Lutheran) |
| @T775@ | 25 SEP 1814| Conversion<br>Hans Kristensen  | MAIN, CONVERT | RELIGIOUS, CONVERSION  | SPLAC @SP0097@ Oslo Cathedral (Vår Frelsers kirke) (Lutheran) |
| @T776@ | 12 JUL 1821| Conversion<br>Johannes Thomassen | MAIN, CONVERT  | RELIGIOUS, CONVERSION  | SPLAC @SP0044@ Lutheran Parish of Bergen (Lutheran) |


### Templates dates, places and information:
```
17 MAY 1797	@T771@	Infant baptism of Johannes Thomassen  SPLAC @SP0063@ Bergen Parish Church (Catholic)
                    baptism of Johannes as child, by Father Lucien Marceau (with baptism gown)
30 JAN 1805 @T772@  Entry of Einar Voss in SPLAC @SP0123@ Stavanger Theological Seminary (Lutheran)
30 JUL 1809 @T773@  Confirmation of Johannes Thomassen to Catholicism, at 12 years old
                    in SPLAC @SP0063@ Bergen Parish Church (Catholic)
10 APR 1812 @T774@	Ordination of Pastor Einar Voss   SPLAC @SP0081@ Stavanger Diocese Seminary (Lutheran)
                    by bishop Henrik Brodahl
25 SEP 1814 @T775@	Conversion of Hans Kristensen from Catholicism to Lutheranism SPLAC @SP0097@ Oslo Cathedral
                    (Vår Frelsers kirke) (Lutheran) Pastor is Einar Voss
12 JUL 1821 @T776@	Conversion of Johannes Thomassen 24 (adult), from Catholicism to Lutheranism
                    in SPLAC @SP0044@ Lutheran Parish of Bergen (Lutheran), Norway
                    Johannes Thomassen converting to Lutheranism by pastor Einar Voss, with friend Hans Kristensen.
```

### 📜 Example GEDCOM 
---
**💧 @T771@ – Nr 1: Religious Baptism - Johannes Thomassen as infant**

```gedcom
0 @T771@ TEMPLATE             /* RELIGIOUS, BAPTISM */
1 TYPE RELIGIOUS, BAPTISM
1 TITL Parish Register: Baptisms 1790–1800
2 PHRASE Baptism of Johannes Thomassen as a child in the Catholic Church of Bergen
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 17 MAY 1797            /* Date of the ceremony */
1 SPLAC @SP0063@              /* Bergen Parish Church */
1 BAPM
2 DATE 17 MAY 1797
2 SPLAC @SP0063@              /* Bergen Parish Church */
1 ROLES
2 STICKY @ST0101@             /* MAIN, CHILD (Johannes as infant) */
2 STICKY @ST0102@             /* FATHER Ivar Thomassen */
2 STICKY @ST0103@             /* MOTHER Solveig Thomassen */
2 STICKY @ST0104@             /* GODPARENT, AUNT, WITNESS (Marta) */
2 STICKY @ST0105@             /* CLERGY Father Lucien Marceau */
2 STICKY @ST0909@             /* RELIGIOUS, VESTMENT (baptism gown) */
2 STICKY @ST0118@             /* FRIEND, SPONSOR, WITNESS Karl Mikkelsen */
1 NOTE "Infant baptism of Johannes Thomassen"
1 CITA
2 SOUR @S0378@                /* Not written out in this example */
2 PAGE 5
2 DATA
~  ~ ~
```
**🍼 @ST0101@ – Johannes Thomassen (MAIN, CHILD): tiny toes and sacred water**
```gedcom
0 @ST0101@ STICKY             /* Johannes Thomassen MAIN, CHILD */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T771@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 17 MAY 1797            /* Date of the TEMPLATE, so ceremony date */
1 ROLE MAIN, CHILD
1 NAME
2 FORM Johannes Thomassen
1 BIRT
2 DATE 14 MAY 1797
2 SPLAC @SP0063@              /* Bergen Parish Church */
1 BAPM
2 DATE 17 MAY 1797
2 SPLAC @SP0063@              /* Bergen Parish Church */
1 AGE 3 days
1 RELI Catholic
1 NOTE "Baptized in family tradition with lace gown, later converted to Lutheranism in 1821"
~ ~ ~
```
**👨‍👦 @ST0102@ – Ivar Thomassen (FATHER): steady hands, family guide**
```gedcom
0 @ST0102@ STICKY             /* FATHER Ivar Thomassen */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T771@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 17 MAY 1797            /* Date of the TEMPLATE, so ceremony date */
1 ROLE FATHER
1 NAME
2 FORM Ivar Thomassen
1 AGE 32
1 RELI Catholic
~ ~ ~
```
**👩‍🍼 @ST0103@ – Solveig Thomassen (MOTHER): warmth wrapped in linen**
```gedcom
0 @ST0103@ STICKY             /* MOTHER Solveig Thomassen */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T771@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 17 MAY 1797            /* Date of the ceremony */
1 SPLAC @SP0063@              /* Bergen Parish Church */
1 ROLE MOTHER
1 NAME
2 FORM Solveig Thomassen
1 AGE 29
1 RELI Catholic
~ ~ ~
```
**🧣 @ST0104@ – Marta Thomassen (SISTER, FATHER, WITNESS, GODPARENT): brought the heirloom gown**
```gedcom
0 @ST0104@ STICKY             /* Marta Thomassen SISTER, FATHER, WITNESS, GODPARENT */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T771@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 17 MAY 1797            /* Date of the ceremony */
1 SPLAC @SP0063@              /* Bergen Parish Church */
1 ROLE SISTER, FATHER, WITNESS, GODPARENT
1 NAME
2 FORM Marta Thomassen
1 AGE 28
1 NOTE "Named on document as sister of Johannes’s father, so aunt of Johannes; carried lace gown"
```
**⛪ @ST0105@ – Father Lucien Marceau (CLERGY): visiting priest from abroad**
```gedcom
0 @ST0105@ STICKY             /* Father Lucien Marceau */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T771@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 17 MAY 1797            /* Date of the ceremony */
1 SPLAC @SP0063@              /* Bergen Parish Church */
1 ROLE CLERGY
1 NAME
2 FORM Father Lucien Marceau
1 OCCU Visiting Catholic Priest
1 NOTE "Presided over Catholic baptism. Performed the baptism as guest clergy"
```
**👗 @ST0909@ – Baptism Gown (RELIGIOUS, VESTMENT): lace, linen, legacy**
```gedcom
0 @ST0909@ STICKY             /* RELIGIOUS, VESTMENT */
1 TYPE RELIGIOUS, VESTMENT
1 SUBM @B001@
1 TEMPLATE @T00807@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE FROM 1780 TO 1800
1 ROLE ITEM
1 NOTE "Baptismal Gown of the Thomassen Family; lace trim hand-sewn heirloom gown."
1 NOTE "Wool gown with hand-embroidered cross and initials J.T., worn by three generations"
1 NOTE "Stored in a wooden box behind the altar since 1790. Slight moth nibble at hem."
```
**🥾 @ST0118@ – Karl Mikkelsen (FRIEND, SPONSOR, WITNESS): friend with muddy boots and clean faith**
```gedcom
0 @ST0118@ STICKY             /* Karl Mikkelsen */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T771@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 17 MAY 1797            /* Date of the ceremony */
1 SPLAC @SP0063@              /* Bergen Parish Church */
1 ROLE FRIEND, SPONSOR, WITNESS
1 NAME
2 FORM Karl Mikkelsen
1 NOTE "Former Lutheran; sponsored Johannes’s baptism, known for sturdy boots"
1 NOTE "Family friend and sponsor of Johannes' baptism"
```
---

**✝️ @T772@ – Nr 2: Religious Commitment - Einar Voss enters Lutheran seminary**

```gedcom
0 @T772@ TEMPLATE             /* RELIGIOUS, ENTRY */
1 TYPE RELIGIOUS, ENTRY
1 TITL Seminary Entry Logbook: Stavanger Lutheran Seminary
2 PHRASE Entry of Einar Voss into Lutheran seminary as novice initiate
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 30 JAN 1805            /* Date of the ceremony */
1 SPLAC @SP0123@              /* Stavanger Theological Seminary */
1 EVEN RELIGIOUS, ENTRY
2 DATE 30 JAN 1805
2 SPLAC @SP0123@              /* Stavanger Theological Seminary */
1 ROLES
2 STICKY @ST0101@             /* MAIN, INITIATE (Einar Voss) */
2 STICKY @ST0105@             /* CLERGY — Professor Ibsen Lindahl registered Einar */
1 NOTE "Einar Voss entered Lutheran seminary in presence of Registrar Prof. Ibsen Lindahl.
2 CONT Ceremony simple but formal."
1 CITA
2 SOUR @S0379@                /* Not written out in this example */
2 PAGE 2
2 DATA
~  ~ ~
```
**🎓 @ST0203@ – Einar Voss (MAIN, INITIATE): novice steps, big faith**
```gedcom
0 @ST0203@ STICKY             /* MAIN, INITIATE, Einar Voss */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T772@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 EVEN RELIGIOUS, ENTRY
2 DATE 30 JAN 1805
2 SPLAC @SP0123@              /* Stavanger Theological Seminary */
1 ROLE MAIN, INITIATE
1 NOTE "Entered Stavanger Theological Seminary as a Lutheran novice"
1 SEX M
1 BIRT
2 DATE 03 MAR 1787             /* around 18 years old now */
2 SPLAC @SP0119@               /* Åmøy, Rogaland, Island village near Stavanger */
1 RELI Lutheran
```
**📋 Professor Ibsen Lindahl – Seminary Registrar at Stavanger Lutheran Seminary**
```gedcom
0 @ST0105@ STICKY             /* CLERGY Professor Ibsen Lindahl */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T772@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 30 JAN 1805
1 SPLAC @SP0123@              /* Stavanger Theological Seminary */
1 ROLE CLERGY
1 NAME
2 FORM Professor Ibsen Lindahl
~ ~ ~
1 OCCU Seminary Registrar
1 NOTE "Recorded Einar’s entry into the Lutheran Seminary (firm hand, excellent penmanship).
2 CONT Ceremony simple but formal."
```
---


**🪪 @T773@ – Nr 3: Religious Confirmation - Johannes Thomassen as Catholic**

```gedcom
0 @T773@ TEMPLATE           /* RELIGIOUS, CONFIRM */
1 TYPE RELIGIOUS, CONFIRMATION
1 TITL Confirmation Register: Bergen Parish
2 PHRASE Religious confirmation of Johannes Thomassen as a young adult Catholic
1 DATE 30 JUL 1809
1 SPLAC @SP0063@              /* Bergen Parish Church */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 EVEN RELIGIOUS, CONFIRM
2 DATE 30 JUL 1809
2 SPLAC @SP0063@              /* Bergen Parish Church */
1 ROLES
2 STICKY @ST0307@             /* MAIN, CONFIRMEE Johannes Thomassen 12, confirming */
2 STICKY @ST0325@             /* PRIEST, CLERGY Father Gustav Lunde  */
1 NOTE "Johannes confirmed into Catholic faith by Father Gustav Lunde after period of catechism study"
1 CITA
2 SOUR @S0329@                /* Not written out in this example */
2 PAGE 23
2 DATA
~  ~ ~
```
**🕯️ @ST0301@ – Johannes Thomassen (MAIN, CONFIRMEE): youth confirmed, light embraced**
```gedcom
0 @ST0307@ STICKY             /* Johannes Thomassen MAIN, CONFIRMEE */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T773@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 30 JUL 1809            /* Date of the TEMPLATE, so ceremony date */
1 ROLE MAIN, CONFIRMEE
1 NAME
2 FORM Johannes Thomassen
1 BIRT
2 DATE 14 MAY 1797
2 SPLAC @SP0063@              /* Bergen Parish Church */
1 EVEN RELIGIOUS, CONFIRM
2 DATE 30 JUL 1809
2 SPLAC @SP0063@              /* Bergen Parish Church */
1 RELI Catholic
~ ~ ~
```
**📖 @ST0302@ – Confirming Clergy (PRIEST, CLERGY Father Gustav Lunde): steady hand on sacred word**
```gedcom
0 @ST0302@ STICKY             /* Father Gustav Lunde, PRIEST, CLERGY */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T773@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 30 JUL 1809            /* Date of the TEMPLATE, so ceremony date */
1 SPLAC @SP0063@              /* Bergen Parish Church */
1 ROLE PRIEST, CLERGY
1 NAME
2 FORM Father Gustav Lunde
1 NOTE "Conducted confirmation of Johannes at age 12, known for strict catechism lessons"
```
---


**✝️ @T774@ – Nr 4: Religious Ordination - Einar Voss becomes Pastor**

```gedcom
0 @T774@ TEMPLATE             /* RELIGIOUS, ORDINATION */
1 TYPE RELIGIOUS, ORDINATION
1 TITL Ordination Dossier: Diocese of Stavanger
2 PHRASE Religious ordination of Einar Voss as Lutheran pastor by Bishop Brodahl
1 SUBM @B001@
1 DATE 10 APR 1812
1 SPLAC @SP7751@              /* Stavanger Diocese, Norway */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 EVEN RELIGIOUS, ORDINATION
2 DATE 10 APR 1812
2 SPLAC @SP7751@              /* Stavanger Diocese, Norway */
1 ROLES
2 STICKY @ST0412@             /* MAIN, DEACON, becomes Pastor Einar Voss */
2 STICKY @ST0406@             /* CLERGY, ORDAINER, Bishop: Bishop Henrik Brodahl */
1 NOTE "Ordination of Pastor Einar Voss"
1 CITA
2 SOUR @S0377@
2 PAGE 5
2 DATA
~  ~ ~
```
**📯 @ST0412@ – Einar Voss (DEACON): robed and ready for calling**
```gedcom
0 @ST0412@ STICKY             /* DEACON, Pastor Einar Voss */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T774@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 10 APR 1812
1 EVEN RELIGIOUS, ORDINATION
2 DATE 10 APR 1812
2 SPLAC @SP7751@              /* Stavanger Diocese, Norway */
1 ROLE MAIN, DEACON
1 NAME
2 FORM Pastor Einar Voss
~ ~ ~
1 OCCU Lutheran priest
1 NOTE "Becomes Pastor of the Lutheran Parish of Bergen, Norway"
1 NOTE "Newly ordained pastor; took vows of chastity, obedience, and an impressive vow of punctuality"
```
**🎩 @ST0406@ – Bishop Henrik Brodahl (ORDINATION): hat of responsibility, staff of guidance**
```gedcom
0 @ST0406@ STICKY             /* CLERGY, ORDAINER, Bishop: Bishop Henrik Brodahl */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T774@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 10 APR 1812
1 SPLAC @SP7751@              /* Stavanger Diocese, Norway */
1 ROLE CLERGY, ORDAINER, Bishop
1 NAME
2 FORM Bishop Henrik Brodahl
1 OCCU Bishop of Stavanger
1 SPLAC Stavanger
1 NOTE "Conducted the ordination ceremony for Deacon Einar Voss, to become a Pastor."
```
---

**✝️ @T775@ – NR 5: Religious Conversion - Hans Kristensen from Catholicism to Lutheranism**

```gedcom
0 @T775@ TEMPLATE             /* RELIGIOUS, CONVERSION Hans Kristensen */
1 TYPE RELIGIOUS, CONVERSION
1 TITL Register of Religious Conversions (Early 1800s)
2 PHRASE Religious conversion of Hans Kristensen from Catholicism to Lutheranism
1 DATE 25 SEP 1814
1 SPLAC @SP333@               /* Oslo Mission House */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 EVEN RELIGIOUS, CONVERSION
2 DATE 25 SEP 1814
2 SPLAC @SP333@               /* Oslo Mission House */
1 ROLES
2 STICKY @ST0507@             /* MAIN, CONVERT Hans Kristensen, converting */
2 STICKY @ST0525@             /* CLERGY receiving Pastor Einar Voss */
1 NOTE "Conversion of Hans Kristensen from Catholicism to Lutheranism"
1 CITA
2 SOUR @S0379@
2 PAGE 5
2 DATA
~  ~ ~
```
**🧭 @ST0507@ – Hans Kristensen (MAIN, CONVERT): changing direction to Lutheran**
```gedcom
0 @ST0507@ STICKY             /* MAIN, CONVERT, Hans Kristensen */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T775@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 25 SEP 1814
1 SPLAC @SP333@               /* Oslo Mission House */
1 EVEN RELIGIOUS, CONVERSION
2 DATE 25 SEP 1814
2 SPLAC @SP333@               /* Oslo Mission House */
1 ROLE MAIN, CONVERT
1 NAME
2 FORM Hans Kristensen
1 RELI Lutheran
1 AGE 19
1 NOTE "Former Lutheran, embraced Catholic faith"
```
**📜 @ST0525@ – Pastor Einar Voss (CLERGY): giving guidance, again**
```gedcom
0 @ST0525@ STICKY             /* Pastor Einar Voss */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T775@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 25 SEP 1814
1 SPLAC @SP333@               /* Oslo Mission House */
1 ROLE CLERGY
1 NAME
2 FORM Pastor Einar Voss
~ ~ ~
1 NOTE "Received Hans Kristensen into the Lutheran Church"
```
---


**🪪 @T776@ – Nr 6: Religious Conversion - Johannes Thomassen becomes Lutheran**

```gedcom
0 @T776@ TEMPLATE             /* RELIGIOUS, CONVERSION */
1 TYPE RELIGIOUS, CONVERSION
1 TITL Adult Conversion Certificate: Lutheran Parish of Bergen
2 PHRASE Adult conversion of Johannes Thomassen from Catholicism to Lutheranism
1 SUBM @B001@
1 DATE 12 JUL 1821
1 SPLAC @SP0033@              /* Lutheran Parish of Bergen, Norway */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 EVEN RELIGIOUS, CONVERSION
2 DATE 12 JUL 1821
2 SPLAC @SP0033@              /* Lutheran Parish of Bergen, Norway */
1 ROLES
2 STICKY @ST0601@             /* MAIN, CONVERT Johannes Thomassen 24 (adult), converting to Lutheranism */
2 STICKY @ST0602@             /* CLERGY Pastor Einar Voss, receiving */
2 STICKY @ST0603@             /* FRIEND, WITNESS Hans Kristensen */
1 NOTE "Conversion of Johannes Thomassen from Catholicism to Lutheranism"
1 CITA
2 SOUR @S0376@
2 PAGE 5
2 DATA
~  ~ ~
```
**🌊 @ST0601@ – Johannes Thomassen (MAIN, CONVERT): plunged into new light**
```gedcom
0 @ST0601@ STICKY             /* Johannes Thomassen, MAIN, CONVERT */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T776@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 JUL 1821
1 SPLAC @SP0033@              /* Lutheran Parish of Bergen, Norway */
1 EVEN RELIGIOUS, CONVERSION
2 DATE 12 JUL 1821
2 SPLAC @SP0033@              /* Lutheran Parish of Bergen, Norway */
1 ROLE MAIN, CONVERT
1 NAME
2 FORM Johannes Thomassen
~ ~ ~
1 AGE 24
1 RELI Lutheran
1 NOTE "Converted from Catholicism, baptized in public ceremony in presence of friends and clergy"
```
**🧑‍🏫 @ST0602@ – Pastor Einar Voss (CLERGY): giving guidance, again, calm voice, firm faith**
```gedcom
0 @ST0602@ STICKY             /* CLERGY Pastor Einar Voss */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T776@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 JUL 1821
1 SPLAC @SP0033@              /* Lutheran Parish of Bergen, Norway */
1 ROLE CLERGY
1 NAME
2 FORM Pastor Einar Voss
~ ~ ~
1 OCCU Lutheran priest
1 NOTE "Performed baptism and received Johannes’s declaration of faith"
```
**🪗 @ST0603@ – Hans Kristensen (FRIEND, WITNESS): faithful companion, again by his side**
```gedcom
0 @ST0603@ STICKY             /* Hans Kristensen, FRIEND, WITNESS */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T776@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 12 JUL 1821
1 SPLAC @SP0033@              /* Lutheran Parish of Bergen, Norway */
1 ROLE FRIEND, WITNESS
1 NAME
2 FORM Hans Kristensen
~ ~ ~
1 NOTE "Supported Johannes during conversion, shared similar experience"
```


[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-10"></a>  
## 📙 Example 10: Family Bible

Example 10 – Family Bible


### ✝️ GEDCOM 8 Example: “The Eldridge Family Bible” 🏡  

This GEDCOM 8 example models a multigenerational family Bible with handwritten entries spanning from 1869 to 1936.  
It captures personal milestones—births, deaths, marriages, gifts, and illnesses—annotated over decades by members of the Eldridge household. The Bible includes decorative elements like inked messages, dried flowers, and affectionate symbols.

**Family context:**  
Walter and Martha Eldridge began recording family events upon their marriage in 1869. The Bible passed through generations, reflecting both factual and sentimental entries—from births and wedding dates to handwritten blessings, heirlooms, and personal notes. Even the household butler, Isaac, is remembered with affection.

**📜 This example demonstrates: 📜**
- A `SECONDARY, FAMILYBIBLE` TEMPLATE, with rich annotation support treated as the **single source**, with each STICKY anchored in the same template context.
- `STICKY TYPE` uses `AN_xxx` (e.g., `AN_BIRTH`, `AN_MARRIAGE`) to mark the annotated nature of **each person event**  
- `STICKY` sequencing using `TDABOVI`  
- Cross-role participation: parents, children, midwife, butler, witnesses  
- A full `ASSET` block representing the Bible, including `HISTORY` and owner `STICKY` references  
- Inheritance and non-inheritance gifting (`NECKLACE`, `BIBLE`)  
- Use of `FLEX ANNOTATION` to preserve original Bible phrasing and ink style  
- Emotional and material detail captured in annotations (e.g. hairlocks, pressed flowers)
- **It has some pictures to get into the atmosphere and mood 😁 🏡**

**Due to example length constraints:**
- Some `INDI` records are omitted  
- Many blocks end with **~ ~ ~** to indicate unshown lines  
- `NAME` structures use the new GEDCOM 8 format, but only partially expanded  
- No `CREA` or `CHAN` lines are shown

---

### 📸 Source: 🏡 Eldridge Homestead at Crystal Lake

#### The Eldridge family home might have looked a bit like this estate.

![Lakeland Farm / Eldridge Homestead](https://images.squarespace-cdn.com/content/v1/6385233d5c99740c75651c5c/f34c1ba7-ce82-4688-8dab-2ef44eee7c77/Dole+House?format=2500w)

#### Original: "The Dole Mansion" in Crystal Lake, Illinois. From:  https://www.thedole.org/history

```gedcom
0 @S0100@ SOUR
1 TITL Eldridge Homestead, Crystal Lake 
1 DATA
2 EVEN RESI
3 SPLAC @SP0100@              /* Crystal Lake, Illinois */
2 AGNC Unknown photographer / K.I.Co. photo archive
2 NOTE Originally labeled “Lakeland Farm, Crystal Lake Ill.”
~ ~ ~
1 OBJ @O0100@                 /* Photograph link or thumbnail in digital form */
1 NOTE Image chosen to visually represent the Eldridge family home in the Bible example.
1 NOTE Historical match — image reused from Lakeland Farm near Crystal Lake, IL.
~ ~ ~
```
---
### 🏘️ Places as `SPLAC` Structures
**🌐 @SP0008@ SPLAC – Eldridge Homestead in Crystal Lake, Illinois**
```gedcom
0 @SP0008@ SPLAC              /* Eldridge Homestead Crystal Lake, Illinois*/
1 LANG en
1 TYPE LOCATION, POLI, 121, Estate 
1 NOTE in German: "121=Gut" : "Manor farm or large landed estate, often owned by wealthy families."
 ~ ~ ~
```
**🌐 @SP0009@ SPLAC – Chicago**
```gedcom
0 @SP0009@ SPLAC              /* Chicago */
1 TYPE LOCATION, POLI, 51 , City (Chicago around those days )
 ~ ~ ~
```
**🌐 @SP0100@ SPLAC – Crystal Lake, Illinois, United States**
```gedcom
0 @SP0100@ SPLAC              /* Crystal Lake, Illinois, United States */
1 TYPE LOCATION, POLI, 55 , Village (55 = Village )
 ~ ~ ~
```
```gedcom
0 @SP051@ SPLAC               /* Nunda, Illinois, United States */
1 TYPE LOCATION, POLI, 55 , Village (55 = Village )
```
---

### 📚 TEMPLATE Structure
This `TEMPLATE` has some empty lines in between sections of `STICKY`s. This is done to keep it readable. In an original `TEMPLATE` in a GEDCOM file there ought to be **NO** empty lines.  
**📕🪶 TEMPLATE @T00003@ TEMPLATE NOTE: “Passed through 3 generations” — final entry by Marian Eldridge 📕🪶 📝**
```gedcom
0 @T00003@ TEMPLATE
1 TYPE SECONDARY, FAMILYBIBLE
1 TITLE Eldridge Family Bible with Births, Deaths, and Notes
1 SUBM @B0003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
2 NOTE Latest entries by Marian Eldridge
1 DATE 1870–1936              /* Time period the Bible was used and written in */
1 SPLAC @SP0100@              /* Crystal Lake, Illinois */
1 EVEN SECONDARY, FAMILYBIBLE
2 DATE 1870–1936              /* Time period the Bible was used and written in */
2 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 TDECUJUS @ST0001@           /* Walter Eldridge is the De Cujus */
1 ROLES
2 STICKY @ST0660@             /* Eldridge Family Bible */
2 STICKY @ST0001@             /* MAY 3 1838 Birth Walter Eldridge Patriarch of the family */
2 STICKY @ST0002@             /* JAN 1 1843 Birth Martha Green  Matriarch of the family */
2 STICKY @ST0003@             /* SEP 7 1869 Marriage Walter Eldridge */
2 STICKY @ST0004@             /* SEP 7 1869 Marriage Martha Green */
2 STICKY @ST0100@             /* Irene Green, Mother of Martha, hands Martha the Bible as a wedding present */

2 STICKY @ST0005@             /* JAN 1 1872 Birth John */
2 STICKY @ST0006@             /* OCT 4 1875 Birth Eleanor */
2 STICKY @ST0007@             /* JAN 3 1877 Birth Alfred */
2 STICKY @ST0008@             /* JAN 15 1877 Baptism Alfred*/
2 STICKY @ST0009@             /* MAY 31 1879 Birth Ruth*/
2 STICKY @ST0010@             /* FEB 2 1875 Birth Clara Watson */

2 STICKY @ST0011@             /* JUN 5 1893 Marriage John Eldridge */
2 STICKY @ST0012@             /* JUN 5 1893 Marriage Clara Watson */
2 STICKY @ST0013@             /* SEP 12 1899 Birth Edward */
2 STICKY @ST0014@             /* JAN 3 1902 Birth Mary */
2 STICKY @ST0015@             /* JAN 15 1902 Death Mary */
2 STICKY @ST0016@             /* Jan 19 1902 Martha hands Clare the Family Bible */

2 STICKY @ST0017@             /* Aug 8 1904 Birth Susan */
2 STICKY @ST0975@             /* Aug 8 1904 Midwife: Mrs. Abigail Dorsey assisted at birth Susan */
2 STICKY @ST0018@             /* Apr 26 1907 Birth William */
2 STICKY @ST0976@             /* Aug 8 1904 Midwife: Mrs. Abigail Dorsey assisted at William's birth */

2 STICKY @ST0019@             /* ABT OCT 8  1912 Death Isaac the Butler and friend of the family */
2 STICKY @ST0020@             /* MAR 17 1918 Marriage Edward Eldridge */
2 STICKY @ST0021@             /* MAR 17 1918 Marriage Rose Jacobs */
2 STICKY @ST0022@             /* DEC 2 1919 Birth Marian Eldridge */
2 STICKY @ST0977@             /* DEC 2 1919 Midwife: Mrs. Abigail Dorsey assisted at Marian's birth */
2 STICKY @ST0023@             /* 1923 Move: Susan Eldridge moves to Evanston */

2 STICKY @ST0035@             /* FEB 15 1922: Martha dies */
2 STICKY @ST0036@             /* NOV 18 1922: Walter dies */
2 STICKY @ST0024@             /* JAN 29 1936 Annotation from Marian about illness of Clara */
2 STICKY @ST0025@             /* JAN 29 1936 Clare hands Marian her Necklace */
2 STICKY @ST0026@             /* FEB 2 1936 death Clara Eldridge */
2 STICKY @ST0027@             /* FEB 3 1936 heir Marian Eldridge (gets the bible) */

1 TRANSFER @ST0660@           /* The transferred Bible */
2 GRANTOR @ST0100@            /* Irene Green, Mother of Martha, original owner of the Bible */
2 GRANTEE @ST0004@            /* SEP 7 1869 Marriage Martha Green, she gets the bible from her mother Irene */

1 TRANSFER @ST0660@           /* The transferred Bible */
2 GRANTOR @ST0002@            /* Martha Eldridge - Green, Mother */
2 GRANTEE @ST0016@            /* Clara, her daughter gets the Bible after her newborn Mary dies */
2 NOTE The bible is gifted by Martha to Clara

1 TRANSFER @ST0660@           /* The transferred Bible */
2 GRANTOR @ST0026@            /* Clara dies of pneumonia */
2 GRANTEE @ST0027@            /* Marian, as an heir, gets the Bible */
2 NOTE Marian gets the bible after her mother Clara died

1 NOTE "Passed through 3 generations of Eldridges. Final entry by Marian Eldridge."
1 CITA
2 SOUR @S0100@                /* Eldridge Homestead, Crystal Lake */
2 TITL Eldridge Homestead, Crystal Lake 
2 PAGE 5
2 DATA
~ ~ ~                         /* Further info left out to shorten example */
1 CREA 28 JUN 2025
1 CHAN 06 AUG 2025
```

---
### 📚 STICKY Structures
**📔 The family ✝️ Bible as an `ASSET - STICKY` Its holding the family events from 3 generations Eldridges. 📖 ✝️**
```gedcom
0 @ST0660@ STICKY             /* Eldridge Family Bible. Belonging to "Eldridge Homestead, Illinois" */
1 TYPE RELIGIOUS, BIBLE, Family Bible
2 PHRASE "Eldridge Family Bible from around 1850, leather bound."
1 TITL "Eldridge Family Bible from around 1850, leather bound."
2 PHRASE "The Bible is annotated with decorative script, side notes, and pressed flowers."
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE HEIRLOOM
1 EVEN RELIGIOUS, BIBLE, Family Bible
2 DATE SEP 7 1869
2 SPLAC @SP0100@              /* Crystal Lake, Illinois  */
1 ASSET @A0001@               /* The Eldridge Family Bible */
1 FLEX ANNOTATION
2 PHRASE Side-entry remark
2 CONTENTS Annotated first note inside the bible:
2 CONT September 7 1869
2 CONT "This bible is a gift to my daughter Martha and my son-in-law Walter
2 CONT on their beautifull sunny  weddingday on the Eldridge Homestead.
2 CONT With love and kisses, mom (Irene Green)"
2 CONT 
2 CONT It is followed by Irene's signature and a handdrawn heart with flowers around it.
~ ~ ~                         /* Further info left out to shorten example */
```
### 👨‍👩‍👧‍👦 Walter Eldridge and Martha Green📖, with their children: John, Eleanor, Alfred and Ruth. Generation 1
**🧔🏻‍♂️ 🎩 STICKY @ST0001@ Birth of Walter Eldridge on MAY 3 1838 — would one day manage orchards with quiet pride 🧔🏻‍♂️ 🎩 🍼**
```gedcom
0 @ST0001@ STICKY             /* MAY 3 1838 Birth Walter Eldridge */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Walter Eldridge        /* Further lines omitted to limit example lenght */
1 SEX M
1 BIRT
2 DATE MAY 3 1838
1 TDABOVI 1
1 FLEX ANNOTATION
2 PHRASE Written in dark brown ink on fine vellum
2 CONTENTS May 3rd, 1838 — Our son Walter was born beneath spring skies at the Eldridge Homestead.
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏻 🧵 STICKY @ST0002@ Birth of Martha Green on JAN 1 1843 — gifted in embroidery and gentle wisdom 👩🏻 🧵 🍼** 
```gedcom
0 @ST0002@ STICKY             /* JAN 1 1843 Birth Martha Green */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Martha Green           /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE JAN 1 1843
2 SPLAC @SP051@               /* Nunda, Illinois */
1 TDABOVI 1s
1 FLEX ANNOTATION
1 PHRASE Written in soft strokes with dark ink
2 CONTENTS January 1st, 1843 — Our darling Martha arrived in Nunda, Illinois, just as the new year dawned.
~ ~ ~                         /* Further info left out to shorten example */
```
**🧔🏻‍♂️ 📜 STICKY @ST0003@ Marriage of Walter Eldridge on SEP 7 1869 — liked quoting poetry by the hearth 🧔🏻‍♂️ 📜 💍** 
```gedcom
0 @ST0003@ STICKY             /* SEP 7 1869 Marriage Walter Eldridge */
1 TYPE PERSON, AN_MARRIAGE
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, GROOM
1 NAME
2 FORM Walter Eldridge        /* Further lines omitted to limit example lenght */
1 SEX M
1 MARR
2 DATE SEP 7 1869
2 PLAC Eldridge Homestead, Illinois
1 TDABOVI 1
1 FLEX ANNOTATION
2 PHRASE Neatly penned in black ink, likely by a family elder
2 CONTENTS September 7th, 1869 — Walter and Martha wed beneath the cottonwood tree on the homestead lawn.
~ ~ ~                         /* Further info left out to shorten example */
```
**👰🏻 🌸 STICKY @ST0004@ Marriage of Martha Green on SEP 7 1869 — cherished pressed flowers and keepsakes 👰🏻 🌸 💍**  
```gedcom
0 @ST0004@ STICKY             /* SEP 7 1869 Marriage Martha Green */
1 TYPE PERSON, AN_MARRIAGE, AN_INHERIT, Gift
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, BRIDE, BENEFICIARY /* She is getting married AND she recieves the Bible */
1 NAME
2 FORM Martha Green           /* Further lines omitted to limit example lenght */
1 SEX F
1 MARR
2 DATE SEP 7 1869
2 PLAC Eldridge Homestead, Illinois
1 ASSET @ST0660@              /* SEP 7 1869, Martha gets the Eldridge Family Bible. */
1 TDABOVI 1s
1 FLEX DESCRIPT
2 PHRASE Annotation on top of first page.
2 CONTENTS Annotated first note inside the bible
1 FLEX ANNOTATION
2 PHRASE Carefully written in elegant hand, signed by Irene (Green), inside a heart framed by floral doodles
2 CONTENTS "September 7 1869,
2 CONT This bible is a gift to my daughter Martha and my son-in-law Walter
2 CONT on their beautifull sunny  weddingday on the Eldridge Homestead.
2 CONT With love and kisses, mom"
~ ~ ~                         /* Further info left out to shorten example */
```
**👵🏻 🕯️ STICKY @ST0100@ Gift by Irene Green on SEP 7 1869 — wrote candlelit notes full of blessings 👵🏻 🕯️ 🎁** 
```gedcom
0 @ST0100@ STICKY             /* Irene Green, Mother of Martha, hands Martha the Bible as a wedding present */
1 TYPE PERSON, AN_TRANSFER, Gift
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED, INCOMPLETE /* Derived from text in first annotation, probably not complete */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE WITNESS, MOTHER, BRIDE, BENEFICIARY
1 NAME
2 FORM Irene Green            /* Further lines omitted to limit example lenght */
1 SEX F
1 EVEN AN_TRANSFER, Gift      /* Event is the transfer of the gift, the Bible */
2 DATE SEP 7 1869
2 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 FLEX ANNOTATION
2 PHRASE Personal message by Irene in black ink
2 CONTENTS  Annotated first note inside the Bible:
2 CONT September 7 1869
2 CONT "This bible is a gift to my daughter Martha and my son-in-law Walter
2 CONT on their beautifull sunny  weddingday on the Eldridge Homestead.
2 CONT With love and kisses, Mom (Irene)"
1 FLEX ANNOTATION
2 PHRASE Decorative remark in delicate hand
2 CONTENTS The note is signed by Irene and surrounded by a heart and tiny pressed flowers.
1 NOTE Irene Green, Mother of Martha, original owner of the Bible
~ ~ ~                         /* Further info left out to shorten example */
```
**🧑🏼 ⚒️ STICKY @ST0005@ Birth of John on JAN 1 1872 — later carved toys from walnut wood 🧑🏼 ⚒️ 🍼** 
```gedcom
0 @ST0005@ STICKY             /* JAN 1 1872 Birth John */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM John Eldridge          /* Further lines omitted to limit example lenght */
1 SEX M
1 BIRT
2 DATE JAN 1 1872
1 TDABOVI 1.1
1 FLEX ANNOTATION
2 PHRASE Written faintly in black ink on lined margin
2 CONTENTS January 1st, 1872 — John was born at home after a long night, arriving just past the winter bells.
~ ~ ~                         /* Further info left out to shorten example */
```
**👧🏼 🧺 STICKY @ST0006@ Birth of Eleanor on OCT 4 1875 — helped fold linens and carry picnic baskets 👧🏼 🧺 🍼**  
```gedcom
0 @ST0006@ STICKY             /* OCT 4 1875 Birth Eleanor */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Eleanor Eldridge       /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE OCT 4 1875
1 TDABOVI 1.2
1 FLEX ANNOTATION
2 PHRASE In the margin, beside the ribbon marker
2 CONTENTS Eleanor was born October 4 1875. She arrived early in the morning and her cradle stood by the window.
~ ~ ~                         /* Further info left out to shorten example */
```
**🧒🏻 🪀 STICKY @ST0007@ Birth of Alfred on JAN 3 1877 — known for spinning tops and quick laughter 🧒🏻 🪀 🍼**  
```gedcom
0 @ST0007@ STICKY             /* JAN 3 1877 Birth Alfred */
1 TYPE PERSON, AN_BIRTH 
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Alfred Eldridge        /* Further lines omitted to limit example lenght */
1 SEX M
1 BIRT
2 DATE JAN 3 1877
1 TDABOVI 1.3
1 FLEX ANNOTATION
2 PHRASE Written under John’s entry, in slightly slanted script
2 CONTENTS Alfred born on January 3rd, 1877 — storm outside, but inside all was warm.
~ ~ ~                         /* Further info left out to shorten example */
```
***🧒🏻 ✝️ STICKY @ST0008@ Baptism of Alfred on JAN 15 1877 — wore lace-trimmed white and was quiet 🧒🏻 ✝️ ✝️**  
```gedcom
0 @ST0008@ STICKY             /* JAN 15 1877 Baptism Alfred*/
1 TYPE PERSON, AN_BAPTISM
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Alfred Eldridge        /* Further lines omitted to limit example lenght */
1 SEX M
1 BAPM
2 DATE JAN 15 1877
1 TDABOVI 1.3
1 FLEX ANNOTATION
2 PHRASE Squeezed between two lines in brown ink
2 CONTENTS Baptized Jan 15th 1877. Reverend Morrison performed the rite after the thaw.
~ ~ ~                         /* Further info left out to shorten example */
```
**👧🏻 🪡 STICKY @ST0009@ Birth of Ruth on MAY 31 1879 — would one day stitch samplers with tulips 👧🏻 🪡 🍼**  
```gedcom
0 @ST0009@ STICKY             /* MAY 31 1879 Birth Ruth*/
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Ruth Eldridge          /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE MAY 31 1879
1 TDABOVI 1.4
1 FLEX ANNOTATION
2 PHRASE Faintly penciled beneath a flower doodle
2 CONTENTS Ruth was born May 31st 1879, in the late afternoon. Her cradle stayed untouched for weeks.
~ ~ ~                         /* Further info left out to shorten example */
```
### 👨‍👩‍👧‍👦 John Eldridge and Clara Watson📖, with their kids: Edward, Mary 🪦, Susan and William. Generation 2

**👩🏼 📖 STICKY @ST0010@ Birth of Clara Watson on FEB 2 1875 — loved writing stories and copying verses 👩🏼 📖 🍼**
```gedcom
0 @ST0010@ STICKY             /* FEB 2 1875 Birth Clara Watson */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, BIRTH
1 NAME
2 FORM Clara Watson           /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE FEB 2 1875
1 TDABOVI 1.1s
1 FLEX ANNOTATION
2 PHRASE Written below Psalm 121
2 CONTENTS "Clara was born this 2nd of February, 1875. A calm day with snow upon the porch."
~ ~ ~                         /* Further info left out to shorten example */
```
**👨🏻‍🦱 🛠️ STICKY @ST0011@ Marriage of John Eldridge on JUN 5 1893 — good with tools and kept a tidy barn 👨🏻‍🦱 🛠️ 💍**
```gedcom
0 @ST0011@ STICKY             /* JUN 5 1893 Marriage John Eldridge */
1 TYPE PERSON, AN_MARRIAGE
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, GROOM
1 NAME
2 FORM John Eldridge          /* Further lines omitted to limit example lenght */
1 SEX M
1 MARR
2 DATE JUN 5 1893
2 PLAC Eldridge Homestead, Illinois
1 TDABOVI 1.1
1 FLEX ANNOTATION
2 PHRASE Note in margin beside Corinthians 13
2 CONTENTS "June 5th, 1893 — John married today. May his days be steady and his evenings warm."
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏻 🎶 STICKY @ST0012@ Marriage of Clara Watson on JUN 5 1893 — sang hymns while sewing by the fire 👩🏻 🎶 💍**
```gedcom
0 @ST0012@ STICKY             /* JUN 5 1893 Marriage Clara Watson */
1 TYPE PERSON, AN_MARRIAGE
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, BRIDE
1 NAME
2 FORM Clara Watson           /* Further lines omitted to limit example lenght */
1 SEX F
1 MARR
2 DATE JUN 5 1893
2 PLAC Eldridge Homestead, Illinois
1 TDABOVI 1.1s
1 FLEX ANNOTATION
2 PHRASE Written in Clara’s careful script
2 CONTENTS "Clara wed on a clear June day. Her hymn book lay open to ‘Come Thou Fount.’"
~ ~ ~                         /* Further info left out to shorten example */
```
**👦🏻 🧃 STICKY @ST0013@ Birth of Edward Eldridge on SEP 12 1899 — always curious, clutching his wooden cup 👦🏻 🧃 🍼** 
```gedcom
0 @ST0013@ STICKY             /* SEP 12 1899 Birth Edward */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Edward Eldridge        /* Further lines omitted to limit example lenght */
1 SEX M
1 BIRT
2 DATE SEP 12 1899
1 TDABOVI 1.1.1
1 FLEX ANNOTATION
2 PHRASE Written in steady hand, upper margin
2 CONTENTS "Edward came to us September 12th, 1899. Rested well and curious from the start."
~ ~ ~                         /* Further info left out to shorten example */
```
**👧🏼 🧵 STICKY @ST0014@ Birth of Mary Eldridge on JAN 3 1902 — tiny hands often tangled in her mother’s thread 👧🏼 🧵 🍼**
```gedcom
0 @ST0014@ STICKY             /* JAN 3 1902 Birth Mary */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Mary Eldridge          /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE JAN 3 1902
1 TDABOVI 1.1.2
1 FLEX ANNOTATION
2 PHRASE Neatly noted beneath a pressed scrap of muslin
2 CONTENTS "Mary was born this 3rd of January, 1902. Such tiny hands, always reaching for Clara’s threads."
~ ~ ~                         /* Further info left out to shorten example */
```
**👼🏻 🕊️ STICKY @ST0015@ Death of Mary Eldridge on JAN 15 1902 — her cradle stayed untouched for weeks 👼🏻 🕊️ ✝️**
```gedcom
0 @ST0015@ STICKY             /* JAN 15 1902 Death Mary */
1 TYPE PERSON, AN_DEATH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, DECEASED
1 NAME
2 FORM Mary Eldridge          /* Further lines omitted to limit example lenght */
1 SEX F
1 DEAT
2 DATE JAN 15 1902
1 TDABOVI 1.1.2
1 FLEX ANNOTATION
2 PHRASE Written in faded ink, just below her birth entry
2 CONTENTS "Our little Mary passed on the 15th of January. Her cradle sits still, the blanket folded."
2 CONT A lock of her hair is glued here, beside a dried violet.
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏻 🌼 STICKY @ST0016@ Martha hands Clare the Family Bible on Jan 19 1902 — shared in a room that smelled of violets 👩🏻 🌼 🎁** 
```gedcom
0 @ST0016@ STICKY             /* Jan 19 1902 Martha hands Clare the Family Bible */
1 TYPE PERSON, AN_MENTION
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE ASSET, GIFT
1 NAME "The Eldridge Family Bible"
1 FLEX ANNOTATION
1 CONTENTS There is just a dated note here saying "My dearest Clara, find comfort in the Lords words herein.
2 PHRASE In blue ink
2 CONT Its yours now." With a signature that looks like Martha's.
1 EVEN
2 TYPE ASSET, GIFT
2 DATE Jan 19 1902
1 FLEX ANNOTATION
2 PHRASE Simple inscription, left margin near Psalms
2 CONTENTS "My dearest Clara, find comfort in the Lord’s words herein.
2 CONT It’s yours now." Signed by Martha, Jan 19th, 1902
~ ~ ~                         /* Further info left out to shorten example */
```
**👧🏻 🍓 STICKY @ST0017@ Birth of Susan on Aug 8 1904 — rosy-cheeked and born during berry season 👧🏻 🍓 🍼** 
```gedcom
0 @ST0017@ STICKY             /* Aug 8 1904 Birth Susan */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Susan Eldridge         /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE Aug 8 1904
1 TDABOVI 1.1.3
1 FLEX ANNOTATION
2 PHRASE Noted beside a drawn sprig of clover
2 CONTENTS "Susan arrived this 8th of August, 1904 — cheeks like berries and a cry that stirred the crows."
~ ~ ~                         /* Further info left out to shorten example */
```
**🧓🏻 🪡 STICKY @ST0975@ Midwife Mrs. Abigail Dorsey assists at Susan's birth — famous for her quilted shawls 🧓🏻 🪡 🍼**
```gedcom
0 @ST0975@ STICKY             /* Aug 8 1904 Midwife: Mrs. Abigail Dorsey assisted at birth Susan */
1 TYPE PERSON, AN_MENTION
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE BIRTH, MIDWIFE
1 NAME
2 FORM Mrs. Abigail Dorsey    /* Further lines omitted to limit example lenght */
1 SEX F
1 OCCU Midwife
1 NOTE Assisted with birth of Susan
1 FLEX ANNOTATION
2 PHRASE Penned neatly near Susan's name
2 CONTENTS "Abigail Dorsey came again, her shawl trailing threads as she moved,
2 CONT and brought Susan into the world with quiet confidence."
~ ~ ~                         /* Further info left out to shorten example */
```
**👶🏼 🪀 STICKY @ST0018@ Birth of William on Apr 26 1907 — strong lungs, fussed with a spinning top later 👶🏼 🪀 🍼**
```gedcom
0 @ST0018@ STICKY             /* Apr 26 1907 Birth William */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM William Eldridge       /* Further lines omitted to limit example lenght */
1 SEX M
1 BIRT
2 DATE Apr 26 1907
1 TDABOVI 1.1.4
1 FLEX ANNOTATION
2 PHRASE Inked plainly with a careful hand
2 CONTENTS "William came this April day, lungs strong and fists tight — such a boy already."
~ ~ ~                         /* Further info left out to shorten example */
```
**🧓🏻 🪡 STICKY @ST0976@ Midwife Mrs. Abigail Dorsey assists at William's birth — knitted booties for all newborns 🧓🏻 🪡 🍼**
```gedcom
0 @ST0976@ STICKY             /*  Aug 8 1904 Midwife: Mrs. Abigail Dorsey assisted at William's birth */
1 TYPE PERSON, AN_MENTION
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
2 DATE Apr 26 1907
1 ROLE BIRTH, MIDWIFE
1 NAME
2 FORM Mrs. Abigail Dorsey    /* Further lines omitted to limit example lenght */
1 SEX F
1 OCCU Midwife
1 EVEN
2 TYPE Assisting at birth
2 DATE Aug 4 1904             /* Date of assisting at birth */
1 NOTE Assisted with birth of William
1 FLEX ANNOTATION
2 PHRASE Written in warm brown ink beside William’s name
2 CONTENTS "Mrs. Dorsey was again by our side. Her booties, already finished, waited folded in the cradle."
~ ~ ~                         /* Further info left out to shorten example */
```
**🧔🏽 🍷 STICKY @ST0019@ Death of Isaac the Butler on ABT OCT 8 1912 — known for his port wine stories 🧔🏽 🍷 ✝️** 
```gedcom
0 @ST0019@ STICKY             /* ABT OCT 8  1912 Death Isaac the Butler and friend of the family */
1 TYPE PERSON, AN_DEATH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, DECEASED
1 NAME
2 FORM Isaac (butler)         /* Further lines omitted to limit example lenght */
1 SEX M
1 OCCU Butler
1 DEAT
2 DATE ABT OCT 8  1912
1 NOTE "Isaac our butler and friend died unexpectedly this week."
1 TDABOVI 0
1 FLEX ANNOTATION
2 PHRASE Written with care by Martha, in her soft, slanting script
2 CONTENTS "Our dear Isaac passed today. More than a butler—he was part of the family.
2 CONT Always the first to rise, the last to rest, and never short a story.
2 CONT We shall miss the quiet way he warmed the room with port, kind words and patience."
~ ~ ~                         /* Further info left out to shorten example */
```
### 👨‍👩‍👧 Edward Eldridge, and Rose Jacobs, with their child: Marian📖. Generation 3

**👨🏻 🎩 STICKY @ST0020@ Marriage of Edward Eldridge on MAR 17 1918 — arrived with polished boots and hope 👨🏻 🎩 💍**
```gedcom
0 @ST0020@ STICKY             /* MAR 17 1918 Marriage Edward Eldridge */
1 TYPE PERSON, AN_MARRIAGE
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, GROOM
1 NAME
2 FORM Edward Eldridge        /* Further lines omitted to limit example lenght */
1 SEX M
1 MARR
2 DATE MAR 17 1918
2 PLAC Eldridge Homestead, Illinois
1 TDABOVI 1.1.1
1 FLEX ANNOTATION              /* STICKY @ST0020@ Marriage Edward Eldridge */
2 PHRASE In Edward’s own neat hand
2 CONTENTS "Edward Eldridge was wed today, March 17 1918. May his steps be steady and his home warm."
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏻 🪞 STICKY @ST0021@ Marriage of Rose Jacobs on MAR 17 1918 — wore a violet ribbon in her dark hair 👩🏻 🪞 💍**
```gedcom
0 @ST0021@ STICKY             /* MAR 17 1918 Marriage Rose Jacobs */
1 TYPE PERSON, AN_MARRIAGE
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, BRIDE
1 NAME
2 FORM Rose Jacobs            /* Further lines omitted to limit example lenght */
1 SEX F
1 MARR
2 DATE MAR 17 1918
2 PLAC Eldridge Homestead, Illinois
1 TDABOVI 1.1.1s
1 FLEX ANNOTATION              /* STICKY @ST0021@ Marriage Rose Jacobs */
2 PHRASE Likely penned by her sister
2 CONTENTS "Rose looked radiant in her violet ribbon. Married Edward today. A lovely day in early spring."
~ ~ ~                         /* Further info left out to shorten example */
```
**👧🏼 🎀 STICKY @ST0022@ Birth of Marian Eldridge on DEC 2 1919 — cooed while clutching her mother’s locket 👧🏼 🎀 🍼** 
```gedcom
0 @ST0022@ STICKY             /* DEC 2 1919 Birth Marian Eldridge */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, CHILD
1 NAME
2 FORM Marian Eldridge        /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE DEC 2 1919
1 TDABOVI 1.1.1.1
1 FLEX ANNOTATION              /* STICKY @ST0022@ Birth Marian Eldridge */
2 PHRASE Delicate script with a faint stain
2 CONTENTS "A daughter born to Rose and Edward—Marian, on this December 2, 1919. She cries like a songbird."
~ ~ ~                         /* Further info left out to shorten example */
```
**🧓🏻 🪡 STICKY @ST0977@ Midwife Mrs. Abigail Dorsey assists at Marian's birth — “gentlest hands in the county” 🧓🏻 🪡 🍼**
```gedcom
0 @ST0977@ STICKY             /*  DEC 2 1919 Midwife: Mrs. Abigail Dorsey assisted at Marian's birth */
1 TYPE PERSON, AN_MENTION
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
2 DATE Apr 26 1907
1 ROLE BIRTH, MIDWIFE
1 NAME
2 FORM Mrs. Abigail Dorsey    /* Further lines omitted to limit example lenght */
1 SEX F
1 OCCU Midwife
1 EVEN
2 TYPE Assisting at birth
2 DATE DEC 2 1919             /* Date of assisting at birth */
1 NOTE Assisted with birth of Marian
1 FLEX ANNOTATION              /* STICKY @ST0977@ Midwife Mrs. Dorsey */
2 PHRASE Noted in Clara’s careful script
2 CONTENTS "Mrs. Abigail Dorsey was present at Marian’s birth. Her hands soothed both mother and child."
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏻 🚲 STICKY @ST0023@ Move of Susan to Evanston in 1923 — packed her trunk and rode away smiling 👩🏻 🚲 🧳** 
```gedcom
0 @ST0023@ STICKY             /* 1923 move Susan Eldridge moves to Evanston */
1 TYPE PERSON, AN_MOVE
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, SUBJECT
1 NAME
2 FORM Susan Eldridge         /* Further lines omitted to limit example lenght */
1 SEX F
1 NOTE "Susan moved to Evanston after her marriage"
1 DATE 1923
1 TDABOVI 1.1.3
1 FLEX ANNOTATION              /* STICKY @ST0023@ Susan moves to Evanston */
2 PHRASE Slanted handwriting, a small pressed flower nearby
2 CONTENTS "Susan packed her trunk today, and left for Evanston. A new chapter begins."
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏼 🫖 STICKY @ST0024@ Marian’s annotation on Clara’s illness on JAN 29 1936 — penned beside her teacup 👩🏼 🫖 ✏️**
```gedcom
0 @ST0024@ STICKY             /* JAN 29 1936 Annotation from Marian about illness of Clara */
1 TYPE PERSON, AN_OTHER, Annotation by Marian
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE PATIENT
1 NAME
2 FORM Clara Eldridge         /* Further lines omitted to limit example lenght */
1 SEX F
1 DATE 1870–1936
1 NOTE "Mom is very ill now, suffering pneumonia, we pray she will get better."
1 DATE JAN 29 1936
1 TDABOVI 1.1s
1 FLEX ANNOTATION              /* STICKY @ST0024@ Illness of Clara */
2 PHRASE Written hastily with ink smudges
2 CONTENTS "Mother’s breath is shallow. The doctor fears pneumonia. We keep hope in our hearts."
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏼 💎 STICKY @ST0025@ Clare hands Marian her Necklace on JAN 29 1936 — said “It’s yours now, child” 👩🏼 💎 🎁**
```gedcom
0 @ST0025@ STICKY             /* JAN 29 1936 Clare hands Marian her Necklace */
1 TYPE JEWELRY, NECKLACE
1 TITL "Necklace with pearl pendant"
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE ASSET, GIFT
1 NOTE Gifted by Clara to Marian
1 DATE JAN 29 1936
1 FLEX ANNOTATION              /* STICKY @ST0025@ Necklace gift to Marian */
2 PHRASE Carefully penned below the illness note
2 CONTENTS "Today, I gave Marian my pearl necklace. May she wear it in joy and sorrow alike."
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏻 🥀 STICKY @ST0026@ Death of Clara Eldridge on FEB 2 1936 — flowers faded in the vase by her bed 👩🏻 🥀 ✝️**
```gedcom
0 @ST0026@ STICKY             /* FEB 2 1936 death Clara Eldridge */
1 TYPE PERSON, AN_DEATH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, DECEASED, GRANTOR
1 NAME
2 FORM Clara Eldridge         /* Further lines omitted to limit example lenght */
1 SEX F
1 DEAT
2 DATE FEB 2 1936
1 TDABOVI 1.1s
1 FLEX ANNOTATION              /* STICKY @ST0026@ Death of Clara */
2 PHRASE Gently written with a drawn black border
2 CONTENTS "Clara passed this morning, February 2, 1936. The lilies by her bed had wilted overnight."
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏼 📘 STICKY @ST0027@ Heir Marian Eldridge receives the Bible on FEB 3 1936 — held it tight like a treasure chest 👩🏼 📘 🎁**
```gedcom
0 @ST0027@ STICKY             /* FEB 3 1936 heir Marian Eldridge (gets the bible) */
1 TYPE PERSON, AN_OTHER
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE GRANTEE                /* Marian Eldridge recieves the Bible */
1 NAME
2 FORM Marian Eldridge        /* Further lines omitted to limit example lenght */
1 SEX F
1 NOTE "As mom died, I Marian, have been granted this beautiful Bible,
2 CONT which I will keep and extend in her name."
1 DATE FEB 3 1936
1 TDABOVI 1.1.1.1
1 FLEX ANNOTATION              /* STICKY @ST0027@ Marian receives the Bible */
2 PHRASE A later addition in Marian’s hand
2 CONTENTS "Clara's Bible is now Marian’s. She holds it close—may it guide her days."
~ ~ ~                         /* Further info left out to shorten example */
```
**👵🏼 🕯️ STICKY @ST0035@ Death of Martha Eldridge on FEB 15 1922 — whispered something no one caught 👵🏼 🕯️ ✝️** 
```gedcom
0 @ST0035@ STICKY             /* JAN 1 1843 Martha Green dies*/
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936              /* Template DATE and SPLAC */
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, DECEASED
1 NAME
2 FORM Martha Green           /* Further lines omitted to limit example lenght */
1 SEX F
1 DEAT
2 DATE FEB 15 1922
2 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 TDABOVI 1s
1 FLEX ANNOTATION              /* STICKY @ST0035@ Death of Martha Green */
2 PHRASE Thin ink, fading at the edges
2 CONTENTS "Martha slipped away today, soft as a breath. No one heard her final words."
~ ~ ~                         /* Further info left out to shorten example */
```
**👴🏼 📜 STICKY @ST0036@ Death of Walter Eldridge on NOV 18 1922 — died of a broken heart 👴🏼 📜 ✝️** 
```gedcom
0 @ST0001@ STICKY             /* MAY 3 1838 Walter Eldridge dies */
1 TYPE PERSON, AN_BIRTH
1 TEMPLATE @T00003@
1 TORIGIN ORIGDOC, TRANSCRIBED /* Derived directly from original bible, entries copied into STICKYs */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 1870–1936
1 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 ROLE MAIN, DECEASED
1 NAME
2 FORM Walter Eldridge        /* Further lines omitted to limit example lenght */
1 SEX M
1 DEAT
2 DATE NOV 18 1922
2 SPLAC @SP0008@              /* Eldridge Homestead Crystal Lake, Illinois*/
1 TDABOVI 1
1 FLEX ANNOTATION              /* STICKY @ST0036@ Death of Walter Eldridge */
2 PHRASE Same ink and hand as Martha’s note
2 CONTENTS "Walter followed Martha not long after. His spirit had already left with hers."
~ ~ ~                         /* Further info left out to shorten example */
```

### 👥 INDI Structures, not all, just some of them because of the example length.

**👩🏼‍🦱 @I0052@ INDI – Martha Eldridge Green, Matriarch of the family**
```gedcom
0 @I0052@ INDI                /* Martha Eldridge Green */
1 NAME
2 FORM Martha Green           /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE JAN 1 1843
2 SPLAC @SP051@               /* Nunda, Illinois */
1 ROLES                       /* 9 STICKYs as Martha is mentioned 9 times in the TEMPLATE */
2 STICKY @ST0002@             /* JAN 1 1843 Birth Martha Green */
2 STICKY @ST0004@             /* SEP 7 1869 Marriage Martha Green and Walter Eldridge */
2 STICKY @ST0005@             /* JAN 1 1872 Birth John */
2 STICKY @ST0006@             /* OCT 4 1875 Birth Eleanor */
2 STICKY @ST0007@             /* JAN 3 1877 Birth Alfred */
2 STICKY @ST0008@             /* JAN 15 1877 Baptism Alfred*/
2 STICKY @ST0009@             /* MAY 31 1879 Birth Ruth*/
2 STICKY @ST0016@             /* Jan 19 1902 Martha hands Clare the Family Bible */
2 STICKY @ST0035@             /* FEB 15 1922: Martha dies */
1 ASSETS
2 STICKY @ST0660@             /* SEP 7 1869, Martha gets the Eldridge Family Bible. */
2 DATE 12 MAY 1811
~ ~ ~                         /* Further info left out to shorten example */
```
**👩🏼‍🦱 @I0053@ INDI – Clara Eldridge Watson, married to John Eldridge**
```gedcom
0 @I0053@ INDI                /* Clara Eldridge Watson */
1 NAME
2 FORM Clara Eldridge Watson  /* Further lines omitted to limit example lenght */
1 SEX F
1 BIRT
2 DATE FEB 2 1875
1 ROLES                       /* 12 STICKYs as Clara is mentioned 12 times in the TEMPLATE */
2 STICKY @ST0010@             /* FEB 2 1875 Birth Clara Watson */
2 STICKY @ST0012@             /* JUN 5 1893 Marriage Clara Watson */
2 STICKY @ST0013@             /* SEP 12 1899 Birth Edward */
2 STICKY @ST0014@             /* JAN 3 1902 Birth Mary */
2 STICKY @ST0015@             /* JAN 15 1902 Death Mary */
2 STICKY @ST0016@             /* Jan 19 1902 Martha hands Clare the Family Bible */
2 STICKY @ST0017@             /* Aug 8 1904 Birth Susan */
2 STICKY @ST0018@             /* Apr 26 1907 Birth William */
2 STICKY @ST0024@             /* JAN 29 1936 Annotation from Marian about illness of Clara */
2 STICKY @ST0025@             /* JAN 29 1936 Clare hands Marian her Necklace */
2 STICKY @ST0026@             /* FEB 2 1936 death Clara Eldridge */
2 STICKY @ST0027@             /* FEB 3 1936 heir Marian Eldridge (gets the bible) */
1 ASSETS
2 STICKY @ST0660@             /* Jan 19 1902, Martha hands Clara the Eldridge Family Bible. */
2 DATE 12 MAY 1811
~ ~ ~                         /* Further info left out to shorten example */
```

### 📔 The family ✝️ Bible as an ASSET

#### The Eldridge family bible might have looked a bit like this one:

![Handwritten page from the Turpin Bible (1815)](https://scmuseum.org/sites/default/files/styles/wysiwyg/public/2023-08/Handwritten%20Pages%20from%20the%20Turpin%20Bible%20in%20the%20Collection%20of%20the%20South%20Carolina%20State%20Museum.jpg?itok=oPNr4ZUA)

#### Original: William Turpin Bible (1815) - South Caroline State Museum: https://scmuseum.org/explore/exhibitions/online-exhibitions

```gedcom
0 @A0001@ ASSET               /* The Eldridge Family Bible, and its owners */
1 TYPE RELIGIOUS, BIBLE
1 TITL "Eldridge Family Bible, a gift from Irene Green on the wedding of her daughter Martha "
1 DATE SEP 7 1869             /* Wedding date of Walter and Martha */
1 SPLAC @SP0100@              /* Homestead at Crystal Lake, Illinois */
1 SUBM @B0001@
1 HISTORY                     /* Shows the owners of the Bible over time */
2 STICKY @ST0100@             /* Irene Green, Mother of Martha, original owner of the Bible */
2 STICKY @ST0004@             /* SEP 7 1869 Marriage Martha Green, she gets the bible from her mother Irene */
2 STICKY @ST0016@             /* Jan 19 1902 Martha hands Clare the Family Bible (after Mary dies) */
2 STICKY @ST0027@             /* FEB 3 1936 Bible to Marian Eldridge, after her mother Clare dies */
1 FLEX DESCRIPT
2 PHRASE "Bible"
2 CONTENTS "Eldridge Family Bible from around 1850, leather bound. "
3 LANG en
1 NOTE Passed through 3 generations of Eldridges. Final entry by Marian Eldridge.
1 FLEX ANNOTATION
2 PHRASE In black ink
2 CONTENTS Annotated first note inside the bible:
2 CONT September 7 1869
2 CONT "This bible is a gift to my daughter Martha and my son-in-law Walter
2 CONT on their beautifull sunny  weddingday on the Eldridge Homestead.
2 CONT With love and kisses, mom (Irene Green)"
2 CONT 
2 CONT It is followed by Irene's signature and a handdrawn heart with flowers around it.
1 OBJ @O003@                  /* Links to a picture of this bible */
1 CREA 06 JUL 2025
1 CHAN 13 AUG 2025
```

[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-11"></a> 

## 🧬 Example 11: DNA Test Results: Match Comparison and Genotype Report

This GEDCOM 8 example demonstrates two distinct but related DNA record types:

- A **DNA match report** comparing two individuals, modeled as a `TEMPLATE` of type `IDENTITY, DNATEST`, with structured `FLEX` fields describing the result details.
- A **direct genotype report**, modeled as a second `TEMPLATE` of the same type, but focused on recording raw marker data using the new `ARRAY_STRUCTURE`.

Together, these demonstrate the evolving support in GEDCOM 8 for structured genetic evidence, including:
- Roles like `SUBJECT`, `MATCH`, and `LABORATORY`
- The use of `FLEX ARRAY` to store tabular genotype values
- A newly defined data type (`TupleList`) and `ARRAY_STRUCTURE` format for multi-line marker-value pairs
- The reuse of entities like individuals and organizations across multiple `TEMPLATE`s

Both examples are drawn from plausible real-world test formats (e.g., autosomal comparison and genotype printout). While actual lab formats may vary, this illustrates how GEDCOM 8 can accommodate structured, verifiable genetic records in a consistent way.

---
**🧬 TEMPLATE @T0088@ – Autosomal DNA Test Match Report – Porridge & Quibble**
```gedcom
0 @T0088@ TEMPLATE            /* 06 MAR 2023 Autosomal DNA Comparison Report – Porridge & Quibble */
1 TYPE IDENTITY, DNATEST, "Autosomal DNA Test Match Report"
1 TITL Autosomal DNA Comparison Report – Porridge & Quibble
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 06 MAR 2023            /* Date of the test. */
1 SPLAC @SP0005@              /* Houston, TX, USA */
1 EVEN IDENTITY, DNATEST, "Autosomal DNA Test Match Report"
2 DATE 06 MAR 2023            /* Date of the test. */
2 SPLAC @SP0005@              /* Houston, TX, USA */
1 AGNC FamilyTreeDNA – Genealogy & Testing Services
1 ROLES
2 STICKY @ST0188@             /* ROLE MAIN, SUBJECT Gretchen Hazel Porridge */
2 STICKY @ST0288@             /* ROLE MATCH Daniel Quibble */
2 STICKY @ST0388@             /* ORGANIZATION, LABORATORY Genetic Information Research Institute (GIRI)*/
2 STICKY @ST0688@             /* ASSET, ITEM Test Report */
1 CITA
2 SOUR @S0088@
2 TITL Autosomal DNA Comparison Report – Porridge & Quibble
2 PAGE 1                      /* 1 document only */
~ ~ ~                         /* More lines from the CITA structure */
1 ADDRPLUS Contact information of: FamilyTreeDNA (FTDNA)
2 ADDR 1445 North Loop West, Suite 820
3 CITY Houston
3 STAE TX
3 POST 77008
3 CTRY USA
2 PHON +1-713-868-1438
3 TITL Main customer support
2 EMAIL info@familytreedna.com
3 TITL General inquiries
2 WWW https://www.familytreedna.com
3 TITL Official website
2 AGNC FamilyTreeDNA – Genealogy & Testing Services
1 CREA 01 MAY 2025
1 CHAN 07 AUG 2025
```
**👩‍🔬 STICKY @ST0188@ – Gretchen Hazel Porridge (Subject of DNA test)**
```gedcom
0 @ST0188@ STICKY             /* Gretchen's DNA is tested */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@            /* Autosomal DNA Comparison Report */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 06 MAR 2023            /* Date of the test. */
1 SPLAC @SP0005@              /* Houston, TX, USA */
1 ROLE MAIN, SUBJECT
1 NAME
2 FORM Gretchen Hazel Porridge
~ ~ ~
1 SEX F
1 BIRT
2 DATE 12 JAN 1984
2 SPLAC @SP6543@
1 EVEN IDENTITY, DNATEST, "Autosomal DNA Test Match Report"
2 DATE 06 MAR 2023            /* Date of the test. */
2 SPLAC @SP0005@              /* Houston, TX, USA */
1 FLEX DESCRIPT
2 PHRASE DNAType
2 CONTENTS "Autosomal"
1 FLEX DESCRIPT
2 PHRASE "Shared DNA (in cM)"
2 CONTENTS "142.3 cM"
1 FLEX INTEGER
2 PHRASE Number of DNA Segments
2 CONTENTS 18
1 FLEX DESCRIPT
2 PHRASE Longest Segment in cM (centimorgans)
2 CONTENTS "Longest = 23.1 cM"
1 FLEX DESCRIPT
2 PHRASE "Estimated Relationship"
2 CONTENTS "2nd to 3rd cousin"
1 CREA 01 MAY 2025
1 CHAN 07 AUG 2025
```
**👨‍🔬 STICKY @ST0288@ – Daniel Quibble (Match)**
```gedcom
0 @ST0288@ STICKY             /* Daniel Quibble's DNA is compared to Gretchen's DNA */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@            /* Autosomal DNA Comparison Report */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 06 MAR 2023            /* Date of the test. */
1 SPLAC @SP0005@              /* Houston, TX, USA */
1 ROLE MATCH
1 NAME
2 FORM Daniel Quibble
~ ~ ~
1 SEX M
1 BIRT
2 DATE 03 MAY 1979
2 SPLAC @SP0005@              /* Houston, TX, USA */
1 FLEX DESCRIPT
2 PHRASE DNAType
2 CONTENTS "Autosomal"
1 FLEX DESCRIPT
2 PHRASE "Shared DNA (in cM)"
2 CONTENTS "142.3 cM"
1 FLEX INTEGER
2 PHRASE Number of DNA Segments
2 CONTENTS 18
1 FLEX DESCRIPT
2 PHRASE Longest Segment in cM (centimorgans)
2 CONTENTS "Longest = 23.1 cM"
1 F2 PHRASE "Estimated Relationship"
2 CONTENTS "2nd to 3rd cousin"
1 CREA 01 MAY 2025
1 CHAN 07 AUG 2025
```
**📄 STICKY @ST0688@ – DNA Match Report (Asset-STICKY)**
```gedcom
0 @ST0688@ STICKY             /* Document with the testresults. */
1 TYPE DNA, RESULT, Match report /* DNA testresult (is a Match report) */
1 TITL DNA Test Report
2 PHRASE by FamilyTreeDNA – Genealogy & Testing Services
1 SUBM @B001@
1 TEMPLATE @T0088@            /* Autosomal DNA Comparison Report */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 06 MAR 2023            /* Date of the test. */
1 SPLAC @SP0005@              /* Houston, TX, USA */
1 ROLE ITEM, CERTIFICATE      /* The document itself */
1 FLEX DESCRIPT
2 PHRASE Case Nr 01
2 CONTENTS 1122442-10
1 FLEX DESCRIPT
2 PHRASE Case Nr 02
2 CONTENTS 1122442-11
1 FLEX REGNUMBER              /* Report #LG-2023-314  */
2 PHRASE Test number
2 CONTENTS #LG-2023-314
~ ~ ~                         /* More testresults here for STR Locus */
1 FLEX NOTE
2 PHRASE Statement of Result
2 CONTENTS The alleged father cannot be excluded as the biological father of the tested child.
2 CONT Based on the analysis of STR loci listed above, the probability of paternity
2 CONT is 99.999999999%
1 CREA 01 MAY 2025
1 CHAN 07 AUG 2025
```
**🧪 STICKY @ST0388@ – Laboratory: Genetic Information Research Institute (GIRI)**
```gedcom
0 @ST0388@ STICKY             /* Lab where the test was done */
1 TYPE ORGANIZATION, LABORATORY
1 TITL Genetic Information Research Institute (GIRI)
1 SUBM @B001@
1 TEMPLATE @T0088@            /* Autosomal DNA Comparison Report */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 06 MAR 2023            /* Date of the test. */
1 SPLAC @SP0005@              /* Houston, TX, USA */
1 ROLE ISSUER, Laboratory     /* officially issued the testresult */
~ ~ ~
1 CREA 01 MAY 2025
1 CHAN 07 AUG 2025
```
**👩 INDIVIDUAL @I888@ – Gretchen Hazel Porridge**
```gedcom
0 @I888@ INDI
1 NAME Gretchen Hazel Porridge
1 SEX F
1 ROLES
2 STICKY @ST0188@
3 SUBM @B001@
3 QUAY 3                      /* Direct and primary evidence */
1 CHAN 01 MAY 2025
1 CHAN 07 AUG 2025
```
**👨 INDIVIDUAL @I889@ – Daniel Quibble**
```gedcom
0 @I889@ INDI
1 NAME Daniel Quibble
1 SEX M
1 ROLES
2 STICKY @ST0288@
3 SUBM @001@
3 QUAY 3                      /* Direct and primary evidence */
1 CHAN 01 MAY 2025
1 CHAN 07 AUG 2025
```
**📚 SOURCE @S0088@ – Autosomal DNA Comparison Report – Porridge & Quibble**
```gedcom
0 @S0088@ SOUR
1 TITL Autosomal DNA Comparison Report – Porridge & Quibble
1 AUTH Genetic Information Research Institute (GIRI)
1 PUBL "Report #LG-2023-314"
1 DATA
2 DATE 06 MAR 2023
2 TEXT "Gretchen Porridge and Daniel Quibble share 142.3 centiMorgans across 18 segments."
2 LANG eng
2 MIME text/plain
~ ~ ~
1 OBJE @O0054@
2 TITL Plaintext Summary Report
~ ~ ~
```
**💾 OBJE @O0054@ – Multimedia record with Plaintext Summary Report**
```gedcom
0 @O0054@ OBJE                /* Multimedia record with file link  */
1 FILE https://leafgen.example/reports/lg-2023-314.txt
1 FORM text/plain
1 TITL Plaintext Summary Report
1 CREA 01 MAY 2025
1 CHAN 07 AUG 2025
```

**🧬 TEMPLATE @T0931@ – Direct DNA Genotype Report – Gretchen Hazel Porridge**
```gedcom
0 @T0931@ TEMPLATE
1 TYPE IDENTITY, DNATEST
1 TITL Direct DNA Genotype Report – Gretchen Hazel Porridge
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 04 JUL 2025
1 SPLAC @SP88332@             /* San Mateo, CA, USA */
1 EVEN IDENTITY, DNATEST
2 DATE 04 JUL 2025
2 SPLAC @SP88332@             /* San Mateo, CA, USA */
1 CITA
2 SOUR @S0094@
2 PAGE 1
~ ~ ~                         /* More lines from the CITA structure */
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
1 ROLES
2 STICKY @ST0411@  /* Gretchen Porridge – MAIN, SUBJECT */
2 STICKY @ST0388@  /* Genetic Information Research Institute – ISSUER */
1 OBJE @O0094@
1 CREA 20 JUL 2025
1 CHAN 07 AUG 2025
```
**👤 STICKY – Gretchen Hazel Porridge (Genotype)**
```gedcom
0 @ST0411@ STICKY  /* Gretchen Hazel Porridge */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0931@
1 TORIGIN ORIGDOC
1 QUAY 3
1 EVEN IDENTITY, DNATEST
2 DATE 04 JUL 2025
2 SPLAC @SP88332@             /* San Mateo, CA, USA */
1 ROLE MAIN, SUBJECT
1 NAME
2 FORM Gretchen Hazel Porridge
2 PART Gretchen
3 TYPE GIVN
2 PART Hazel
3 TYPE GIVN
2 PART Porridge
3 TYPE SURN
1 FLEX DNATYPE
2 PHRASE DNA test type
2 CONTENTS autosomal
1 FLEX ARRAY
2 PHRASE Raw genotype values
2 CONTENTS ARRAY
3 CONT (rs123456, A)
3 CONT (rs234567, T)
3 CONT (rs345678, G)
3 CONT (rs456789, C)
3 CONT (rs567890, T)
3 CONT (rs678901, A)
3 CONT (rs789012, G)
3 (… more rows omitted for clarity …)
1 CREA 20 JUL 2025
1 CHAN 07 AUG 2025
```

[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-12"></a>  

## 🛖 Example 12: Norwegian Farm Membership
###  – "Lien Farm Census, 1832"

This example shows how to represent a **traditional Norwegian farm** as a `GROUP`, linked to individual residents via `STICKY`. The example includes:

- A `TEMPLATE` of type `GROUP, FARM-MEM` describing a 19th-century **farm census**.
- A `GROUP` record representing the **Lien Farm**, marked with a `DATE` of origin and `SPLAC`.
- A `STICKY` showing **Ola Thorbjørnsen Lien** as a **farm resident** at that time.
- Structured `NAME` blocks for semantic clarity.
- Scandinavian naming customs reflected in surname usage.

It demonstrates how to use a `GROUP` record to represent a traditional Norwegian farm, and how to associate individuals with that group through a `STICKY` record:
- The `GROUP` representing the **Lien Farm**, is typed as `GROUP, FARM-MEM`, given an `SPLAC`, and marked with a historical `DATE` to suggest the general origin of the group.
- The `NAME` reflects the name of the farm, with a `PART` of type `LOCATION` to aid semantic clarity.
- The `INDI` record for Ola Lien shows a name consistent with the local naming tradition, where farm names often became surnames.
- Ola's `STICKY` record links Ola to the farm group, dated 1832, and uses the role `MAIN, LEADER, RESIDENT`. `MAIN` because he is the main person in this `TEMPLATE`, `LEADER` because he is head of the house, and `RESIDENT` because he lives on that farm.
- A comment ( /*  */ ) is used for precise clarification of the `STICKY`’s context.

This example reflects the traditional Scandinavian use of farm names. A farm (`GROUP`) represents a naming unit, and individuals link to it via `STICKY`.

| 🧑 Person         | 🧾 STICKY | Roles                     | OCCU           | Notes                   |
|-------------------|------------|---------------------------|----------------|-------------------------|
| Ola Thorbjørnsen Lien   | @ST0091@   | `MAIN, LEADER, RESIDENT`    | Farmer         | Head of household       |
| Ingebjørg Syversdatter Lien | @ST0092@ | `SPOUSE, MEMBER, RESIDENT` | Domestic work  | Wife of Ola             |
| Marit Olsdatter Lien  | @ST0093@   | `CHILD, MEMBER, RESIDENT`   | —              | Daughter, 6 years old   |
| Erik Knutsen Lien     | @ST0094@   | `WORKER, RESIDENT`          | Farmhand       | Hired laborer           |

**🛖📄 @T0073@ – TEMPLATE – Lien Farm Census, 1832, containg the household members in that year**
```gedcom
0 @T0073@ TEMPLATE            /* Lien Farm Census, 1832 */
1 TYPE GROUP, FARM-MEM        /* TEMPLATE TYPE from event enumtable */
1 TITL Lien Farm Census, 1832 /* This TEMPLATE came from a Lien Farm Census, 1832 */
1 PHRASE Census of farm members in Valdres, Norway
1 SUBM @B001@                 /* Standard submitter */
1 TORIGIN ORIGDOC             /* Derived from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 01 JAN 1832
1 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 EVEN GROUP, FARM-MEM2
2 DATE 01 JAN 1832
2 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 ROLES
2 STICKY @ST0091@             /* Ola Lien – MAIN, LEADER, RESIDENT */
2 STICKY @ST0092@             /* Ingebjørg Lien – MAIN, SPOUSE, MEMBER, RESIDENT */
2 STICKY @ST0093@             /* Marit Olsdatter – MAIN, CHILD, MEMBER, RESIDENT */
2 STICKY @ST0094@             /* Erik Knutsen – MAIN, WORKER, RESIDENT */
1 CITA
2 SOUR @S0361@                /* Original document (not present here) */
2 PAGE 5
2 DATA
~  ~ ~
1 CREA 17 JUL 2025
1 CHAN 08 AUG 2025
```
**🌾 @G0024@ – GROUP – Lien Farm Household. It has 4 members in the HISTORY section**
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
1 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 DATE 1700
1 MEMBERS
2 STICKY @ST0091@             /* Ola Thorbjørnsen Lien */
2 STICKY @ST0092@             /* Ingebjørg Syversdatter Lien */
2 STICKY @ST0093@             /* Marit Olsdatter Lien */
2 STICKY @ST0094@             /* Erik Knutsen Lien */
1 NOTE Residents of this farm traditionally adopted 'Lien' as a surname.
1 CREA 17 JUL 2025
1 CHAN 08 AUG 2025
```
**👨‍🦰 @ST0091@ – STICKY – Ola Thorbjørnsen Lien – MAIN, LEADER, RESIDENT**
```gedcom
0 @ST0091@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0073@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 01 JAN 1832
1 ROLE MAIN, LEADER, RESIDENT /* RESIDENT, so he is a member of the GROUP */
1 GROUP @G0024@               /* Lien Farm, Valdres, Norway */
1 EVEN GROUP, FARM-MEM2
2 DATE 01 JAN 1832
2 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 NAME
2 FORM Ola Thorbjørnsen Lien
2 PART Ola
3 TYPE GIVN
2 Part Thorbjørnsen           /* Original patronymic lastname */
3 TYPE SURN
2 PART Lien
3 TYPE LOCATION
1 AGE 39
1 SEX M
1 OCCU Farmer
1 NOTE Head of household residing at Lien Farm.
1 NOTE Ola Lien appears in farm census of 1832.
~ ~ ~
```
**👩🏼‍🦰 @ST0092@ – STICKY – Ingebjørg Syversdatter Lien – SPOUSE, MEMBER, RESIDENT**
```gedcom
0 @ST0092@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0073@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 01 JAN 1832
1 ROLE MAIN, SPOUSE, RESIDENT /* RESIDENT, so a member of the GROUP */
1 GROUP @G0024@               /* Lien Farm, Valdres, Norway */
1 EVEN GROUP, FARM-MEM2
2 DATE 01 JAN 1832
2 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 NAME
2 FORM Ingebjørg Syversdatter Lien /* Syversdatter is patronymic part */
~ ~ ~
1 AGE 36
1 OCCU Domestic work
1 NOTE Wife of Ola Lien, residing at the farm.
~ ~ ~
```
**👧🏼 @ST0093@ – STICKY – Marit Olsdatter Lien – CHILD, MEMBER, RESIDENT**
```gedcom
0 @ST0093@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0073@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 01 JAN 1832
1 ROLE MAIN, CHILD, RESIDENT  /* RESIDENT, so a member of the GROUP */
1 GROUP @G0024@               /* Lien Farm, Valdres, Norway */
1 EVEN GROUP, FARM-MEM2
2 DATE 01 JAN 1832
2 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 NAME
2 FORM Marit Olsdatter Lien   /* Olsdatter is patronymic part, daughter of Ola */
~ ~ ~
1 AGE 6
1 NOTE Daughter of Ola and Ingebjørg, born at the farm.
~ ~ ~
```
**👨🏻 @ST0094@ – STICKY – Erik Knutsen Lien – WORKER, RESIDENT**
```gedcom
0 @ST0094@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0073@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 01 JAN 1832
1 ROLE MAIN, WORKER, RESIDENT /* RESIDENT, so a member of the GROUP */
1 GROUP @G0024@               /* Lien Farm, Valdres, Norway */
1 EVEN GROUP, FARM-MEM2
2 DATE 01 JAN 1832
2 SPLAC @SP073@               /* Lien Farm, Valdres, Norway */
1 NAME
2 FORM Erik Knutsen Lien      /* Knutsen is patronymic part */
~ ~ ~
1 AGE 22
1 OCCU Farmhand
1 NOTE Hired worker living on the farm at time of census.
~ ~ ~
```
**👨‍🦰 @I0215@ – INDI – Ola Thorbjørnsen Lien**
```gedcom
0 @I0215@ INDI
1 NAME
2 FORM Ola Thorbjørnsen Lien
2 PART Ola
3 TYPE GIVN
2 Part Thorbjørnsen           /* Original patronymic lastname */
3 TYPE SURN
2 PART Lien
3 TYPE LOCATION
1 SEX M
1 ROLES
2 STICKY @ST0091@             /* Farm Census 1832 */
2 STICKY @ST0034@             /* Birth of Ola Lien (Template not present) */
2 STICKY @ST0042@             /* Marriage to Ingebjørg (Template not present) */
~ ~ ~
```


[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-13"></a>  

## 🏥 Example 13: Hospital Admission and Discharge Record

> **Example 13 – Hospital Admission and Discharge Record**  
>  
> This GEDCOM 8 example demonstrates how to document a medical event using two `TEMPLATE`s: one for admission and one for discharge. The example includes:
>
> - **Clara Wensley**, admitted to *County General Hospital* in 1933 for acute appendicitis  
> - The *hospital* modeled as an `ORGANIZATION` with role `SITE` (location where the event occurred)  
> - The *physician* involved in admission and treatment  
>  
> The admission and discharge are captured as two separate `TEMPLATE`s, **as each always has its own set of STICKYs** — even though the people and place are the same. This ensures all `TEMPLATE`s remain self-contained.
>
> The example also includes:
> - Usage of `ROLE` values like `PATIENT`, `PHYSICIAN`, and `SITE`  
> - Demonstration of `FLEX`, `SPLAC`, and `SOURCE` linking to a scanned register entry  
> - Touches of humor in `OCCU`, `NOTE`, and `PHRASE` to support clarity and reader engagement.

**👩🏼‍🦱 @T0048@ TEMPLATE – Hospital Admission Record of Edith Clara Wensley**
```gedcom
0 @T0048@ TEMPLATE            /* Hospital Admission Record of Edith Clara Wensley */
1 TYPE MEDICAL, ADMISSION "Hospital Admission Record"
1 TITL Hospital Admission Record – Edith Clara Wensley, 1933
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 17 FEB 1933
1 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 EVEN MEDICAL, ADMISSION 
2 DATE 17 FEB 1933
2 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 ROLES
2 STICKY @ST0148@             /* MAIN, PATIENT Edith Clara Wensley */
2 STICKY @ST0248@             /* PHYSICIAN Dr. Mortimer Hackett */
2 STICKY @ST0348@             /* ORGANIZATION, MEDICAL, Hospital */
1 CITA
2 SOUR @S0048@
2 TITL Hospital Admission Record – Edith Wensley, 1933
~ ~ ~
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**👩🏼‍🦱 @ST0148@ STICKY – MAIN, PATIENT Clara Wensley, admission to Hospital**
```gedcom
0 @ST0148@ STICKY             /* MAIN, PATIENT Edith Clara Wensley, admission to Hospital */
1 TYPE PERSON
1 TITL "Admission to County General Hospital"
1 SUBM @B001@
1 TEMPLATE @T0048@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 17 FEB 1933
1 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 ROLE MAIN, PATIENT
1 EVEN MEDICAL, ADMISSION 
2 DATE 17 FEB 1933
2 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 NAME
2 FORM Edith Clara Wensley
2 PART Edith
3 TYPE GIVN
2 PART Clara
3 TYPE GIVN
2 PART Wensley
3 TYPE SURN
1 SEX F
1 AGE 41
1 OCCU "Typesetter (known for near-perfect kerning)"
1 FLEX DESCRIPT
2 PHRASE "Reason for Admission"
2 CONTENTS "Acute appendicitis, with mild newspaper withdrawal symptoms"
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**👩🏼‍🦱 @ST0248@ STICKY – PHYSICIAN Dr. Mortimer Hackett 🪓**
```gedcom
0 @ST0248@ STICKY             /* PHYSICIAN Dr. Mortimer Hackett */
1 TYPE PERSON
1 TITL "Admitting Physician – Dr. Mortimer Hackett"1 SUBM @B001@
1 TEMPLATE @T0048@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 17 FEB 1933
1 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 ROLE PHYSICIAN
1 NAME
2 FORM Dr. Mortimer Hackett
2 PART Dr.
3 TYPE PREFIX
2 PART Mortimer
3 TYPE GIVN
2 PART Hackett
3 TYPE SURN
1 SEX M
1 OCCU "Senior Surgeon, specialist in rapid decisions"
1 NOTE "Once diagnosed a broken heart as literal. Reputation: uneven."
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**🏥 @ST0348@ STICKY – County General Hospital, Manchester 🏥**
```gedcom
0 @ST0348@ STICKY             /* County General Hospital, Manchester */
1 TYPE ORGANIZATION, MEDICAL, Hospital
1 TITL "Admission Location – County General Hospital, Manchester"1 SUBM @B001@
1 TEMPLATE @T0048@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 17 FEB 1933
1 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 ROLE SITE                   /* Hospital */
1 NAME
2 FORM County General Hospital, Manchester
~ ~ ~
1 NOTE "Operational since 1891. Tea breaks strictly enforced."
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**👩🏼‍🦱 @I601@ INDI – Edith Clara Wensley**
```gedcom
0 @I601@ INDI                 /* INDI of Edith Clara Wensley */
1 NAME
2 FORM Edith Clara Wensley
2 PART Edith
3 TYPE GIVN
2 PART Clara
3 TYPE GIVN
2 PART Wensley
3 TYPE SURN
1 SEX F
1 AGE 41
1 ROLES
2 STICKY @ST0148@             /* MAIN, PATIENT Edith Clara Wensley, admission to Hospital */
2 STICKY @ST0150@             /* MAIN, PATIENT Edith Clara Wensley, discharge from Hospital */
1 CHAN 08 AUG 2025
```
**💾 @S0048@  SOUR – County General Archives**
```gedcom
0 @S0048@ SOUR
1 TITL Hospital Admission Records, 1933
1 AUTH County General Archives
1 PUBL "Volume 3A: Medical Admissions 1930–1935"
1 ABBR "MedAdm 1933"
1 DATA
2 EVEN MEDICAL, ADMISSION
3 DATE 1933
3 PLAC Manchester, UK
2 AGNC County General Hospital
~ ~ ~
1 TEXT "Edith Wensley was admitted for appendicitis and treated by Dr. Mortimer Hackett."
2 MIME application/pdf
2 LANG eng
1 OBJE @O025@
2 TITL Scanned register entry
~ ~ ~
```
**💾 @O025@  OBJE – Multimedia record with file link**
```gedcom
0 @O025@ OBJE                 /* Multimedia record with file link  */
1 FILE https://example.org/hospital/wensley-admission-1933.pdf
1 FORM application/pdf
1 TITL Scanned register entry
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**👩🏼‍🦱 @T0048@ TEMPLATE – Hospital Discharge Record of Edith Clara Wensley**
```gedcom
0 @T0049@ TEMPLATE            /* Hospital Discharge Record of Edith Clara Wensley */
1 TYPE MEDICAL, DISCHARGE "Hospital Discharge Record"
1 TITL "Hospital Discharge Record of Edith Clara Wensley"
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 25 FEB 1933
1 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 EVEN MEDICAL, DISCHARGE 
2 DATE 25 FEB 1933
2 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 ROLES
2 STICKY @ST0150@             /* PERSON, MAIN, PATIENT Edith Clara Wensley */
2 STICKY @ST0250@             /* PERSON, PHYSICIAN */
2 STICKY @ST0350@             /* ORGANIZATION, FACILITY */
1 CITA
2 SOUR @S0049@                /* Hospital Discharge Record – Edith Wensley, 1933 */
2 PAGE 5
2 DATA
2 TITL "Hospital Discharge Record – Edith Wensley, 1933"
~ ~ ~
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**👩🏼‍🦱 @ST0150@ STICKY – PATIENT Edith Clara Wensley, discharge from Hospital**
```gedcom
0 @ST0150@ STICKY             /* PATIENT Edith Clara Wensley, discharge from Hospital */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0049@            /* Hospital Discharge Record of Edith Clara Wensley */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE MAIN, PATIENT
1 EVEN MEDICAL, DISCHARGE 
2 DATE 25 FEB 1933
2 SPLAC @SP5588@              /* County General Hospital, Manchester, UK */
1 NAME
2 FORM Edith Clara Wensley
2 PART Edith
3 TYPE GIVN
2 PART Clara
3 TYPE GIVN
2 PART Wensley
3 TYPE SURN
1 SEX F
1 AGE 41
1 OCCU "Typesetter (known for near-perfect kerning)"
1 FLEX DESCRIPT
2 PHRASE "Reason for Admission"
2 CONTENTS "Acute appendicitis, with mild newspaper withdrawal symptoms"
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**👩🏼‍🦱 @ST0250@ STICKY – PHYSICIAN Dr. Mortimer Hackett 🪓**
```gedcom
0 @ST0250@ STICKY             /* PHYSICIAN Dr. Mortimer Hackett */
1 TYPE PERSON
1 SUBM @B001@
1 ROLE PHYSICIAN
1 NAME
2 FORM Dr. Mortimer Hackett
2 PART Dr.
3 TYPE PREFIX
2 PART Mortimer
3 TYPE GIVN
2 PART Hackett
3 TYPE SURN
1 SEX M
1 OCCU "Senior Surgeon, specialist in rapid decisions"
1 NOTE "Once diagnosed a broken heart as literal. Reputation: uneven."
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**🏥 @ST0350@ STICKY – County General Hospital, Manchester 🏥**
```gedcom
0 @ST0350@ STICKY             /* County General Hospital, Manchester */
1 TYPE ORGANIZATION, MEDICAL, Hospital
1 SUBM @B001@
1 ROLE SITE
1 NAME
2 FORM County General Hospital, Manchester
1 NOTE "Operational since 1891. Tea breaks strictly enforced."
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```
**💾 @S0049@  SOUR – Hospital Discharge Record**
```gedcom
0 @S0049@ SOUR
1 TITL "Hospital Discharge Record – Edith Wensley, 1933"
1 AUTH County General Archives
1 PUBL "Volume 3A: Medical Discharges 1930–1935"
1 ABBR "Wensley Discharge 1933"
1 DATA
2 EVEN MEDICAL, DISCHARGE
3 DATE 25 FEB 1933
4 PHRASE "Successful recovery from appendectomy"
3 PLAC Manchester, UK
2 AGNC County General Hospital
~ ~ ~
1 NOTE "Edith Wensley discharged after full recovery and minor complaints about the tea."
1 OBJE @O062@
2 TITL Scanned discharge entry
~ ~ ~
```
**💾 @O062@  OBJE – Multimedia record with file link**
```gedcom
0 @O062@ OBJE                 /* Multimedia record with file link  */
1 FILE https://example.org/hospital/wensley-discharge-1933.pdf
1 FORM application/pdf
1 TITL Scanned discharge entry
1 CREA 30 APR 2025
1 CHAN 08 AUG 2025
```



[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-14"></a> 

## 🛠️ Example 14: Mid Century Employment Transfer Order

This GEDCOM 8 example documents the official transfer of Gertrude Elmsbottom, a long-serving employee of Western Office Supplies Co., from the Leiden branch to the Rotterdam headquarters in June 1954. It showcases how occupational changes can be modeled with detailed `STICKY` roles for both the employee and the organizations involved, including an issuer of the transfer. The record draws directly from an original corporate memo and includes:
- Clear `EMPLOYER` roles for both origin and destination workplaces
- Date-specific `OCCU` entries for old and new positions
- Use of `FLEX DESCRIPT` for job title details
- Address information for the destination workplace
- A source record referencing a scanned internal memo

It demonstrates how employment events can be precisely recorded with origin/destination tracking, organizational metadata, and asset linkage for documentary evidence.

**🏢 @T0050@ TEMPLATE – Employment Transfer Order for Gertrude Elmsbottom, 1954 🏢**
```gedcom
0 @T0050@ TEMPLATE
1 TYPE OCCUPATIONAL, EMPLOYMENT, "Employment Transfer Order"
1 TITL Employment Transfer – Gertrude Elmsbottom, 1954
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954
1 SPLAC @SP0046@              /* Rotterdam, Netherlands */
1 EVEN OCCUPATIONAL, EMPLOYMENT, "Employment Transfer Order"
2 DATE 18 JUN 1954
2 SPLAC @SP0046@              /* Rotterdam, Netherlands */
1 ROLES
2 STICKY @ST0150@             /* Gertrude Elmsbottom MAIN, EMPLOYEE */
2 STICKY @ST0250@             /* Western Office Supplies Co., Leiden Branch EMPLOYER */
2 STICKY @ST0251@             /* Western Office Supplies Co., Rotterdam HQ EMPLOYER */
2 STICKY @ST0350@             /* Mr. Cornelis P. Wriggle ISSUER */
1 CITA
2 SOUR @S0050@
2 TITL Employment Transfer – Gertrude Elmsbottom, 1954
~ ~ ~
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```
**👩🏼‍🦰 @ST0150@ – STICKY – Gertrude Elmsbottom MAIN, EMPLOYEE**
```gedcom
0 @ST0150@ STICKY             /* Gertrude Elmsbottom MAIN, EMPLOYEE */
1 TYPE PERSON
1 TITL Employment Transfer – Gertrude Elmsbottom, 1954
1 SUBM @B001@
1 TEMPLATE @T0050@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954
1 SPLAC @SP0046@              /* Rotterdam, Netherlands */
1 EVEN OCCUPATIONAL, EMPLOYMENT, "Employment Transfer Order"
2 DATE 18 JUN 1954
2 SPLAC @SP0046@              /* Rotterdam, Netherlands */
1 ROLE MAIN, EMPLOYEE
1 NAME
2 TYPE BIRTH
2 FORM Gertrude Elmsbottom
2 PART Gertrude
3 TYPE GIVN
2 PART Elmsbottom
3 TYPE SURN
1 SEX F
1 AGE 42
1 OCCU "Team lead, mailroom automation (1950–1954)" /* Current job */
2 SPLAC @SP0042@              /* Western Office Supplies Co., Leiden Branch (place from) */
2 DATE 17 JUN 1954            /* Last working day in old job in Leiden */
1 OCCU "Senior clerk, whisperer of paper clips" /* New job */
2 SPLAC @SP0043@              /* Western Office Supplies Co., Rotterdam HQ (place to) */
2 DATE 18 JUN 1954            /* Starting date for new job in Rotterdam */
1 FLEX DESCRIPT
2 PHRASE "New position"
2 CONTENTS "Departmental Correspondence Overlord, Level II"
1 NOTE "Gertrude Elmsbottom was officially reassigned to HQ effective immediately."
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```
**🏢 🧑‍🎓 @ST0250@ – STICKY – Western Office Supplies Co., Leiden Branch - ORGANIZATION, COMPANY 🏢 🧑‍🎓**
```gedcom
0 @ST0250@ STICKY             /* Western Office Supplies Co., Leiden Branch */
1 TYPE ORGANIZATION, COMPANY, WORKPLACE
1 TITL Western Office Supplies Co., Leiden Branch
1 SUBM @B001@
1 TEMPLATE @T0050@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954
1 SPLAC @SP0046@              /* Rotterdam, Netherlands */
1 ROLE EMPLOYER
1 NAME
2 FORM Western Office Supplies Co., Leiden Branch
~ ~ ~                         /* Rest of the NAME structure */
1 NOTE "Originating office. Known for lukewarm coffee and aggressive filing."
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```
**🏢 🚢 @ST0251@ – STICKY – Western Office Supplies Co., Rotterdam HQ (Destination) - ORGANIZATION, COMPANY 🏢 🚢**
```gedcom
0 @ST0251@ STICKY             /* Western Office Supplies Co., Rotterdam HQ (Destination) */
1 TYPE ORGANIZATION, COMPANY, WORKPLACE
1 TITL Western Office Supplies Co., Rotterdam HQ (Destination)
1 SUBM @B001@
1 TEMPLATE @T0050@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954
1 SPLAC @SP0046@              /* Rotterdam, Netherlands */
1 ROLE EMPLOYER
1 NAME
2 FORM Western Office Supplies Co., Rotterdam HQ
1 ADDR
2 STREET Clipfileplein 14
2 CITY Rotterdam
2 POST 3012 CD
2 CTRY Netherlands
1 NOTE "Receives employee. Boasts a third-floor nap corridor."
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```
**👨🏻‍🦱 @ST0350@ – STICKY – Mr. Cornelis P. Wriggle ISSUER**
```gedcom
0 @ST0350@ STICKY             /* Mr. Cornelis P. Wriggle ISSUER */
1 TYPE PERSON
1 TITL Mr. Cornelis P. Wriggle ISSUE
1 SUBM @B001@
1 TEMPLATE @T0050@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 18 JUN 1954
1 SPLAC @SP0046@              /* Rotterdam, Netherlands */
1 ROLE ISSUER
1 NAME
2 FORM Mr. Cornelis P. Wriggle
2 PART Cornelis
3 TYPE GIVN
2 PART P.
3 TYPE GIVN
2 PART Wriggle
3 TYPE SURN
1 SEX M
1 OCCU "HR Officer and certified form-stamp enthusiast"
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```
**👩🏼‍🦰 @I701@ – INDI – Gertrude Elmsbottom**
```gedcom
0 @I701@ INDI                 /* Gertrude Elmsbottom MAIN, EMPLOYEE */
1 NAME
2 TYPE BIRTH
2 FORM Gertrude Elmsbottom
2 PART Gertrude
3 TYPE GIVN
2 PART Elmsbottom
3 TYPE SURN
1 SEX F
1 ROLES
1 STICKY @ST0151@             /* OCCU: Junior typist (1938–1945) not in this example */
1 STICKY @ST0152@             /* OCCU: Wartime administrator (1945–1948) not in this example */
1 STICKY @ST0153@             /* OCCU: Team lead, mailroom automation (1950–1954) */
1 STICKY @ST0150@             /* OCCU: Senior clerk (1954 transfer to Rotterdam HQ) */
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```
**💾 @S0050@  SOUR – Employment Transfer – Gertrude Elmsbottom, 1954**
```gedcom
0 @S0050@ SOUR                /* Employment Transfer – Gertrude Elmsbottom, 1954 */
1 TITL Employment Transfer – Gertrude Elmsbottom, 1954
1 AUTH Western Office Supplies Co.
1 PUBL "Internal Memo Archive, Binder F-12"
1 ABBR "Transfer Order 1954"
1 DATA
2 EVEN OCCUPATIONAL, EMPLOYMENT, "Employment Transfer Order"
3 DATE 18 JUN 1954
4 PHRASE "Official transfer from Leiden to Rotterdam"
3 PLAC Rotterdam, Netherlands
2 AGNC Western Office Supplies Co.
~ ~ ~                         /* More from the SOUR */
1 OBJE @O0011@
2 TITL Scanned internal memo
~ ~ ~
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```
**💾 @O0011@  OBJE – Multimedia record with file link**
```gedcom
0 @O0011@ OBJE                /* Multimedia record with file link  */
1 FILE https://example.org/employment/elmsbottom-transfer-1954.pdf
1 TITL Scanned internal memo
1 FORM application/pdf
1 CREA 30 APR 2025
1 CHAN 12 AUG 2025
```


[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-15"></a>  

## 🧾 Example 15: Legal Will Creation and Execution with Estate Transfers

This GEDCOM 8 example models a **two-stage legal will process** using dual `TEMPLATE` records:

1. **Will Creation** (`TYPE DEATH, WILL, "Creation of the Will"`) — where the testator (Emil Rothenbühler) formally records their intentions.
2. **Will Execution** (`TYPE DEATH, WILL, "Execution of the Will"`) — following the testator's death, where the estate is distributed to named heirs.

The example includes:

- A **decedent**, whose two `STICKY` roles span both creation and execution phases.
- A **legal executor**, present in both `TEMPLATE`S with professional credentials and `STICKY` structure for reuse across stages.
- A **notary office**, modeled as an organization (`ORGANIZATION, NOTAR`) with official certification duties.
- Multiple **heirs**, each receiving a specific asset and a tailored percentage of the liquid estate to ensure equal inheritance value.
- Multiple **ASSET** `STICKY`s, each transferred via a `TRANSFER` structure with witty `NOTE`s included for flair and realism.
- A realistic **bank division** where the remaining money after asset assignment is split in calculated percentages to equalize the total value inherited by each heir.
- Use of `FLEX VALUE` for asset appraisal, and `SHARE` for partial distribution.
- Proper linkage to an `INDI` record for Emil Rothenbühler connecting both `STICKY`s.

This example demonstrates how GEDCOM 8 enables structured inheritance scenarios using linked `STICKY`, `TRANSFER`, and `TEMPLATE` blocks — reflecting complex legal and familial dynamics while remaining strictly spec-compliant.


**📜 @T016@ TEMPLATE – Creation of the Will of Emil Rothenbühler**
```gedcom
0 @T015@ TEMPLATE
1 TYPE DEATH, WILL, "Creation of the Will"
1 TITL Last Will and Testament of Emil Rothenbühler
2 PHRASE "Creation of the Will of Emil Rothenbühler"
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 8 SEP 1998
1 SPLAC @SP001@               /* Bern, Switzerland */
1 EVEN DEATH, WILL, "Creation of the Will"
2 DATE 8 SEP 1998
2 SPLAC @SP001@               /* Bern, Switzerland */
1 ROLES
2 STICKY @ST0151@             /* Emil Rothenbühler     - MAIN, GRANTOR - Will Creation */
2 STICKY @ST0251@             /* Franz Müller          - NOTARY - Will Creation */
2 STICKY @ST0252@             /* Notariat Bern Zentrum - ORGANIZATION, NOTARY - Will Creation */
1 CITA
2 SOUR @S0341@                /* Not present in this example */
2 PAGE 5
2 DATA
~  ~ ~
1 CREA 30 APR 2025
1 CHAN 20 JUL 2025
```
**🧔‍♂️ @ST0151@ STICKY – Emil Rothenbühler**
```gedcom
0 @ST0151@ STICKY             /* Emil Rothenbühler, GRANTOR, DECEDENT */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T015@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE MAIN, GRANTOR          /* NOT role DECEDENT as at this time he is still alive */
1 NAME
2 FORM Emil Rothenbühler
2 PART Emil
3 TYPE GIVN
2 PART Rothenbühler
3 TYPE SURN
1 SEX M
1 BIRT
2 DATE 1952
2 SPLAC @SP002@               /* Zürich, Switzerland */
1 OCCU Chocolatier
1 CREA 30 APR 2025
1 CHAN 20 JUL 2025
```
**🧑‍⚖️ @ST0251@ STICKY – Franz Müller**
```gedcom
0 @ST0251@ STICKY             /* Franz Müller NOTARY */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T015@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE NOTARY                 /* Helped writing the will, ensures proper legal formalities */
1 NAME
2 FORM Franz Müller
2 PART Franz
3 TYPE GIVN
2 PART Müller
3 TYPE SURN
1 OCCU Lawyer
1 CREA 30 APR 2025
1 CHAN 20 JUL 2025
```
**🏛️ @ST0252@ STICKY – Notariat Bern Zentrum**
```gedcom
0 @ST0252@ STICKY             /* Notariat Bern Zentrum */
1 TYPE ORGANIZATION, NOTARY
1 SUBM @B001@
1 TEMPLATE @T015@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE NOTARY
1 NAME
2 FORM Notariat Bern Zentrum
2 PART Notariat Bern Zentrum
3 TYPE ORGL
1 CREA 30 APR 2025
1 CHAN 20 JUL 2025
```
**📜 @T016@ TEMPLATE – Execution of the Will of Emil Rothenbühler**
```gedcom
0 @T016@ TEMPLATE             /* Execution of Will (Emil Rothenbühler) */
1 TYPE DEATH, WILL, "Execution of Will and Estate Transfer"
1 TITL "Execution of Will and Estate Transfer of Emil Rothenbühler"
2 PHRASE "Execution of the Will of Emil Rothenbühler"
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 01 JUN 2020
1 SPLAC @SP8585@              /* Bern, Switzerland */
1 EVEN DEATH, WILL
2 DATE 01 JUN 2020
2 SPLAC @SP8585@              /* Bern, Switzerland */
1 ROLES
2 STICKY @ST0152@             /* 👴 Emil Rothenbühler - MAIN, GRANTOR, DECEDENT */
2 STICKY @ST0253@             /* Franz Müller - EXECUTOR */
2 STICKY @ST0254@             /* Notariat Bern Zentrum - NOTARY */
2 STICKY @ST0351@             /* 🧔🏻‍♂️ Markus Rothenbühler - HEIR1, SON */
2 STICKY @ST0352@             /* 👱🏻‍♀️ Sophie Rothenbühler - HEIR2, DAUGHTER */
2 STICKY @ST0353@             /* 👩🏻‍🦰 Eliane Keller - HEIR3 */
2 STICKY @ST0451@             /* Alpine Chalet - ASSET ESTATE, COUNTRYHOUSE */
2 STICKY @ST0452@             /* ⌚Vintage Watch - ASSET BELONGINGS, CLOTHING, "Watch" */
2 STICKY @ST0453@             /* 📚Book Collection - ASSET BOOK, LITERATURE, "Book collection" */
2 STICKY @ST0454@             /* 💰Bank Account - ASSET FINANCE, ACCOUNTS */

1 TRANSFER @ST0451@           /* 🏡Alpine Chalet at Lake Oeschinen */
2 GRANTOR @ST0152@            /* 👴 Emil Rothenbühler - MAIN, GRANTOR, DECEDENT */
2 GRANTEE @ST0351@            /* 🧔🏻‍♂️ Markus Rothenbühler - HEIR1, SON */
1 NOTE "🏡 The house near Lake Oeschinen goes to Markus."

1 TRANSFER @ST0452@           /* ⌚Vintage Watch: Patek Philippe 1952 Ref. 2499 */
2 GRANTOR @ST0152@            /* 👴 Emil Rothenbühler - MAIN, GRANTOR, DECEDENT */
2 GRANTEE @ST0352@            /* 👱🏻‍♀️ Sophie Rothenbühler - HEIR2, DAUGHTER */
1 NOTE "⌚ Sophie gets the Patek Philippe — it's about time."

1 TRANSFER @ST0453@           /* 📚Book Collection */
2 GRANTOR @ST0152@            /* 👴 Emil Rothenbühler - MAIN, GRANTOR, DECEDENT */
2 GRANTEE @ST0353@            /* 👩🏻‍🦰 Eliane Keller - HEIR3 */
1 NOTE "📚 Eliane inherits the rare book collection — with no overdue fines."

1 TRANSFER @ST0454@           /* 💰Bank Account: # 718-348-B, Zürcher Kantonalbank */
2 GRANTOR @ST0152@            /* 👴 Emil Rothenbühler - MAIN, GRANTOR, DECEDENT */
2 GRANTEE @ST0351@            /* 🧔🏻‍♂️ Markus Rothenbühler - HEIR1, SON */
3 SHARE 5.13%
2 GRANTEE @ST0352@            /* 👱🏻‍♀️ Sophie Rothenbühler - HEIR2, DAUGHTER */
3 SHARE 46.15%
2 GRANTEE @ST0353@            /* 👩🏻‍🦰 Eliane Keller - HEIR3 */
3 SHARE 46.15%
1 NOTE "💸 Account funds divided to equalize asset value."
1 FLEX DESCRIPT
2 PHRASE "Bank Account"
2 CONTENTS NOTE
3 CONT The bankaccount with number # 718-348-B, Zürcher Kantonalbank,
3 CONT is reserved for estate tax and final obligations.
~ ~ ~
1 CITA
2 SOUR @S0331@                /* Not present in this example */
2 PAGE 5
2 DATA
~  ~ ~
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🧔‍♂️ @ST0152@ STICKY – Main Deceased Emil Rothenbühler**
```gedcom
0 @ST0152@ STICKY             /* Main Deceased Emil Rothenbühler */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 EVEN DEATH, WILL
2 DATE 01 JUN 2020
2 SPLAC @SP8585@              /* Bern, Switzerland */
1 ROLE MAIN, GRANTOR, DECEDENT
1 NAME
2 FORM Emil Rothenbühler
2 PART Emil
3 TYPE GIVN
2 PART Rothenbühler
3 TYPE SURN
1 DEAT
2 DATE 17 FEB 2020
1 SPLAC @SP001@               /* Bern, Switzerland */
1 NOTE "Long-time alpine chocolatier and hoarder of mechanical things."
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🧑‍⚖️ @ST0253@ STICKY – Franz Müller EXECUTOR**
```gedcom
0 @ST0253@ STICKY             /* Franz Müller EXECUTOR */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE EXECUTOR
1 NAME
2 FORM Franz Müller
2 PART Franz
3 TYPE GIVN
2 PART Müller
3 TYPE SURN
1 SEX M
1 AGE 61
1 ADDR
2 STREET Bundesgasse 12
2 CITY Bern
2 POST 3011
2 CTRY Switzerland
1 AGNC "Estate Administration Group – Canton Bern"
1 OCCU "Licensed Executor & Paper Inspector"
1 NOTE "Personally handled the chocolate vault inventory with surgical precision."
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🏛️ @ST0254@ STICKY – Notary: "Notariat Bern Zentrum"**
```gedcom
0 @ST0254@ STICKY             /* Notariat Bern Zentrum */
1 TYPE ORGANIZATION
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE NOTARY
1 NAME
2 FORM Notariat Bern Zentrum
~ ~ ~
1 ADDR
2 STREET Marktgasse 3
2 CITY Bern
2 POST 3011
2 CTRY Switzerland
1 AGNC "Canton Bern, Legal Division"
1 NOTE "Document sealed and verified by municipal authority"
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🧑‍🔧 @ST0351@ STICKY – Heir1 and Grantee: Son Markus Rothenbühler**
```gedcom
0 @ST0351@ STICKY             /* Heir1, Son, Grantee: Markus Rothenbühler */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR1, SON, GRANTEE
1 NAME
2 FORM Markus Rothenbühler
2 PART Markus
3 TYPE GIVN
2 PART Rothenbühler
3 TYPE SURN
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**👩‍💼 @ST0352@ STICKY – heir2, Daughter, Grantee: Sophie Rothenbühler**
```gedcom
0 @ST0352@ STICKY             /* heir2, Daughter, Grantee: Sophie Rothenbühler */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR2, DAUGHTER, GRANTEE
1 NAME
2 FORM Sophie Rothenbühler
2 PART Sophie
3 TYPE GIVN
2 PART Rothenbühler
3 TYPE SURN
1 SEX F
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🎓 @ST0353@ STICKY – Heir3 - Eliane Keller**
```gedcom
0 @ST0353@ STICKY             /* Heir3 - Eliane Keller */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR3
1 NAME
2 FORM Eliane Keller
2 PART Eliane
3 TYPE GIVN
2 PART Keller
3 TYPE SURN
1 SEX F
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🏡 @ST0451@ – STICKY – Alpine Chalet at Lake Oeschinen**
```gedcom
0 @ST0451@ STICKY             /* Alpine Chalet at Lake Oeschinen */
1 TYPE PROPERTY, HOUSE, "Alpine Chalet at Lake Oeschinen"
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE PROPERTY
1 FLEX DECIMAL, CURR, CHF
2 PHRASE "House Value"
2 CONTENTS 270000.00
1 NOTE "Transferred to Markus Rothenbühler"
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**⌚ @ST0452@ – STICKY – Vintage Watch: "Patek Philippe 1952 Ref. 2499"**
```gedcom
0 @ST0452@ STICKY             /* Patek Philippe 1952 Ref. 2499 */
1 TYPE BELONGINGS, KEEPSAKE, Watch: "Patek Philippe 1952 Ref. 2499"
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIRLOOM
1 FLEX DECIMAL, CURR, CHF
2 PHRASE "Appraised Watch Value"
2 CONTENTS 30000.00
1 NOTE "Bequeathed to Sophie Rothenbühler"
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**📚 @ST0453@ STICKY – Book Collection**
```gedcom
0 @ST0453@ STICKY             /* Book Collection */
1 TYPE BOOK, LITERATURE, "Book collection"
1 TITL Swiss Literature Collection
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE ITEM
1 FLEX DECIMAL, CURR, CHF
2 PHRASE Appraised Value
2 CONTENTS 30000.00
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🏦 @ST0454@ STICKY – Bank account: "# 718-348-B, Zürcher Kantonalbank**
```gedcom
0 @ST0454@ STICKY             /* Account # 718-348-B, Zürcher Kantonalbank */
1 TYPE FINANCE, ACCOUNTS, "Account # 718-348-B, Zürcher Kantonalbank"
1 SUBM @B001@
1 TEMPLATE @T016@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE ITEM
1 NAME
~ ~ ~
1 FLEX DECIMAL, CURR, CHF
2 PHRASE Bank Balance
2 CONTENTS CHF 585000.00
1 FLEX ACCOUNTNR
2 PHRASE "Account-number"
2 CONTENTS 985FT650003AB009
1 FLEX DESCRIPT
2 PHRASE "Bank Account"
2 CONTENTS NOTE
3 CONT The bankaccount with number # 718-348-B, Zürcher Kantonalbank,
3 CONT is reserved for estate tax and final obligations.
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```
**🧾 @I015@ INDI – Emil Rothenbühler**
```gedcom
0 @I015@ INDI                 /* Emil Rothenbühler */
1 NAME
2 FORM Emil Rothenbühler
2 PART Emil
3 TYPE GIVN
2 PART Rothenbühle
3 TYPE SURN
1 ROLES
2 STICKY @ST0151@             /* Emil Rothenbühler - Will Creation DATE 8 SEP 1978 */
2 STICKY @ST0152@             /* Emil Rothenbühler - GRANTOR Will Executed DATE 01 JUN 2020 */
1 ASSETS
2 STICKY @ST0451@             /* 🏠Alpine Chalet - PROPERTY, HOUSE, "Alpine Chalet at Lake Oeschinen" */
2 STICKY @ST0452@             /* ⌚Vintage Watch - BELONGINGS, KEEPSAKE, Watch: "Patek Philippe 1952 Ref. 2499" */
2 STICKY @ST0453@             /* 📚Book Collection - BOOK, LITERATURE, "Book collection" */
2 STICKY @ST0454@             /* 💰Bank Account - FINANCE, ACCOUNTS, "Account # 718-348-B, Zürcher Kantonalbank" */
1 NOTE The ASSETS struture here, only shows the STICKYs at the time of granting.
2 CONT In fact there should also be 4 STICKYs in the ASSETS section for the same entities
2 CONT at time of acquisition ! But they are not mentioned here.
~ ~ ~
1 CREA 30 APR 2025
1 CHAN 10 AUG 2025
```


[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-16"></a>  

## ⚔️ Example 16: Historical Title and Nobility Inheritance


This GEDCOM 8 example models the transfer of a noble title and ancestral property upon the death of a titled individual.
The record includes:
- • A deceased baron who had the title (`MAIN, DECEASED, TITLED`)
- • An heir receiving both a title and an estate
- • A symbolic heraldic medallion as an object with ROLE HEIRLOOM
- • A monarch or state official confirming the transition
- • A `STICKY` with extended attributes (`ADDR, OCCU, AGNC, NOTE`)
- • Example of a noble title via `TITLE, Baron`, with `ROLE DIGNITY`
- • A simple land asset using `FLEX DECIMAL, LAND`  
- • A dedicated `STICKY` and `TRANSFER` to reflect the noble title passing
- • An `ASSET` with `HISTORY` showing previous barons by `STICKY` reference only

This showcases how nobility, symbolic inheritance, and property can be represented using enhanced GEDCOM 8 structures.  

***
**IMPORTANT**  

>- The first 4 barons show a `STICKY` here, but the `TEMPLATE`s they belong to are not presented, to keep the example short.
***

**⚔️ @T0052@ TEMPLATE - Historical Title and Nobility Inheritance**
```gedcom
0 @T0052@ TEMPLATE            /* Inheritance of Noble Title and Estate */
1 TYPE DEATH, WILL, Title
1 TITL Inheritance of Noble Title and Estate
1 SUBM @B001@
1 DATE 14 NOV 1812
1 SPLAC @SP0052@              /* County of Northumberland, United Kingdom */
1 ROLES
2 STICKY @ST0152@     /* MAIN, DECEASED, TITLED: Alaric Montmorency 5th baron of Ashcroft died November 2 1812 👑 */
2 STICKY @ST0252@             /* HEIR, SON: Percival Montmorency 6th baron of Ashcroft 👑 */
2 STICKY @ST0352@             /* George III – Monarch */
2 STICKY @ST0451@             /* Baronial Title – ROLE DIGNITY 🫅 */
2 STICKY @ST0452@             /* Ashcroft Hall – ESTATE MANOR "Ashcroft Hall and grounds" 🏡*/
2 STICKY @ST0453@             /* Heraldic Medallion – JEWELRY CHAIN with ROLE HEIRLOOM ⭐*/
2 STICKY @ST0551@             /* Baronial Lineage Asset */
1 TRANSFER @ST0451@           /* Baronial Title – DIGNITY 🫅*/
2 GRANTOR @ST0152@    /* MAIN, DECEASED, TITLED: Alaric Montmorency 5th baron of Ashcroft died November 2 1812 👑 */
2 GRANTEE @ST0252@            /* HEIR, SON: Percival Montmorency becomes 6th baron of Ashcroft 👑 */
1 TRANSFER @ST0452@           /* Ashcroft Hall – ASSET */
2 GRANTOR @ST0152@    /* MAIN, DECEASED, TITLED: Alaric Montmorency 5th baron of Ashcroft died November 2 1812 👑 */
2 GRANTEE @ST0252@            /* HEIR, SON: Percival Montmorency as 6th baron of Ashcroft 👑 */
1 FLEX ANNOTATION
2 PHRASE "Handwritten annotation on the will"
2 CONTENTS "A title weighs nothing but carries centuries."
1 CITA
2 SOUR @S0321@
2 PAGE 5
2 DATA
~  ~ ~
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**🪦 @ST0152@ STICKY – Alaric Montmorency 5th baron of Ashcroft died November 2 1812 👑**
```gedcom
0 @ST0152@ STICKY             /* Alaric Montmorency MAIN, DECEASED, TITLE */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0052@            /* Inheritance of Noble Title and Estate */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE MAIN, DECEASED, TITLED /* Role TITLED, because he had the title */
1 ASSET @A032@                /* Connects STICKY to the ASSET of the title */
1 NAME
2 FORM Alaric James Montmorency
2 PART Alaric
3 TYPE GIVN
2 PART James
3 TYPE GIVN
2 PART Montmorency
3 TYPE SURN
1 SEX M
1 DEAT
2 DATE 3 NOV 1812
2 SPLAC @SP0451@              /* Ashcroft Hall, Northumberland */
1 TITL                        /* Official GEDCOM tag */
2 TYPE Baron
1 FLEX ANNOTATION             /* More flexible way of representing the TITLE */
2 PHRASE "Title held"
2 CONTENTS NOTE
3 CONT "5th Baron of Ashcroft"
1 OCCU "Landowner, foxhunting enthusiast, parliamentary absentee"
1 NOTE "Known for impromptu speeches and thorough moustache twirling"
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**🧔‍♂️ @ST0252@ STICKY – Percival Montmorency 6th baron of Ashcroft 👑**
```gedcom
0 @ST0252@ STICKY             /* Percival Montmorency – HEIR, SON, TITLE */
1 TYPE HEIR, SON
1 SUBM @B001@
1 TEMPLATE @T0052@            /* Inheritance of Noble Title and Estate */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR, SON, TITLED
1 ASSET @A032@                /* Connects STICKY to the ASSET of the title */
1 NAME
2 FORM Percival Alaric Montmorency
2 PART Percival
3 TYPE GIVN
2 PART Alaric
3 TYPE GIVN
2 PART Montmorency
3 TYPE SURN
1 SEX M
1 AGE 26
1 ADDR
2 STREET Ashcroft Hall
2 CITY Northumberland
2 POST --
2 CTRY United Kingdom
1 SPLAC @SP0451@              /* Ashcroft Hall, Northumberland */
1 TITL                        /* Official GEDCOM tag */
2 TYPE Baron
1 FLEX ANNOTATION
2 PHRASE "New title granted"
2 CONTENTS NOTE
3 CONT "6th Baron of Ashcroft"
1 NOTE "Inherited title and responsibilities; inherited eyebrows uncertain"
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**👑 @ST0352@ STICKY – George III**
```gedcom
0 @ST0352@ STICKY             /* George III */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0052@            /* Inheritance of Noble Title and Estate */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE LEGAL, RULER, "Monarch" /* Ruling Monarch George III */
1 NAME
2 FORM George III
2 PART George
3 TYPE GIVN
2 PART III
3 TYPE SUFFIX
1 OCCU "King of the United Kingdom"
1 AGNC "Royal Crown, by Grace of God"
1 FLEX ANNOTATION
2 PHRASE Authorise Reason
2 CONTENTS "Authorized hereditary transition as per letters patent"
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**🫅 @ST0451@ STICKY – Baronial Title DIGNITY 🫅**
```gedcom
0 @ST0451@ STICKY             /* Baronial Title */
1 TYPE TITLE, Baron 
1 TITLE "Baron of Ashcroft"
1 SUBM @B001@
1 TEMPLATE @T0052@            /* Inheritance of Noble Title and Estate */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE DIGNITY
1 NOTE "A hereditary honor with ceremonial duties and inherited prestige"
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**🏰 @ST0452@ STICKY – Ashcroft Hall**
```gedcom
0 @ST0452@ STICKY             /* Ashcroft Hall */
1 TYPE ESTATE MANOR "Ashcroft Hall and grounds"
1 SUBM @B001@
1 TEMPLATE @T0052@            /* Inheritance of Noble Title and Estate */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE ASSET
1 FLEX DECIMAL, LANDSIZE, Acres
2 PHRASE "Size of the land"
2 CONTENTS 512
1 FLEX ANNOTATION
2 PHRASE Written by clerck
2 CONTENTS "Acres of rolling hills, 3 gables, 2 peacocks, 1 confusing attic"
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**🪙 @ST0453@ STICKY – Heraldic Medallion**
```gedcom
0 @ST0453@ STICKY             /* Heraldic Medallion */
1 TYPE JEWELRY CHAIN "Baronial Heraldic Medallion"
1 SUBM @B001@
1 TEMPLATE @T0052@            /* Inheritance of Noble Title and Estate */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIRLOOM
1 FLEX DECIMAL, GBP
2 PHRASE "Value of the Medallion"
2 CONTENTS 1400
1 FLEX MATERIAL
2 PHRASE "Material"
2 CONTENTS "Silver"
1 NOTE "Silver medallion engraved with stag and crown; symbolic, not negotiable"
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**🫅 @A032@ ASSET – Title: "Baron of Ashcroft"**
```gedcom
0 @A032@ ASSET                /* ASSET for Title: "Baron of Ashcroft" */
1 TYPE TITLE, Baron           /* Same as for Title STICKY */
1 TITL Baron of Ashcroft      /* Same as for Title STICKY */
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* ORIGDOC, as this ASSET is created from info on the @T0052@ TEMPLATE */
1 QUAY 3
1 DATE 21 JUL 2025
1 SPLAC @SP0451@              /* Ashcroft Hall, Northumberland */
1 HISTORY
2 STICKY @ST0651@             /* Aloysius Montmorency 1th baron of Ashcroft died March 1 1712👑 */
2 STICKY @ST0652@             /* Bartholomew Montmorency 2nd baron of Ashcroft died February 5 1742👑 */
2 STICKY @ST0653@             /* Wilberforce Montmorency 3rd baron of Ashcroft died June 19 1776👑 */
2 STICKY @ST0654@             /* Thaddeus Montmorency 4th baron of Ashcroft died October 29 1794👑 */
2 STICKY @ST0152@             /* Alaric Montmorency 5th baron of Ashcroft died November 2 1812 👑 */
2 STICKY @ST0252@             /* Percival Montmorency 6th baron of Ashcroft 👑 */
1 CREA 21 JUL 2025
1 CHAN 11 AUG 2025
```
**👑 👑 👑 👑 4 STICKY's – "Barons of Ashcroft" THEY DONT HAVE A TEMPLATE IN THIS EXAMPLE  !!!**  

**🧔‍♂️ @ST0252@ STICKY – Aloysius Montmorency 1th baron of Ashcroft died March 1 1712👑**
```gedcom
0 @ST0651@ STICKY             /* Aloysius Montmorency – 1st Baron */
1 TYPE HEIR, SON
1 SUBM @B001@
1 TEMPLATE @T01001@           /* Inh. of Noble Title and Estate MAR 1 1712 */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR, SON, TITLED
1 ASSET @A032@                /* Connects STICKY to the ASSET of the title */
1 NAME
2 FORM Aloysius Montmorency
2 PART Aloysius
3 TYPE GIVN
2 PART Montmorency
3 TYPE SURN
1 SEX M
1 AGE 34
1 DEAT
2 DATE 01 MAR 1712
2 SPLAC @SP0451@              /* Ashcroft Hall, Northumberland */
1 SPLAC @SP0451@              /* Ashcroft Hall, Northumberland */
1 TITL
2 TYPE Baron
1 FLEX TITLE
2 PHRASE "New title granted"
2 CONTENTS "1st Baron of Ashcroft"
1 NOTE "Kept a pet mole named Bertrand. Claimed it once outdebated a bishop."
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**👴🏻 @ST0252@ STICKY – Bartholomew Montmorency 2nd baron of Ashcroft died February 5 1742👑**
```gedcom
0 @ST0652@ STICKY             /* Bartholomew Montmorency – 2nd Baron */
1 TYPE HEIR, SON
1 SUBM @B001@
1 TEMPLATE @T01002@           /* Inh of Noble Title and Estate FEB 5 1742 */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR, SON, TITLED
1 ASSET @A032@
1 NAME
2 FORM Bartholomew Montmorency
2 PART Bartholomew
3 TYPE GIVN
2 PART Montmorency
3 TYPE SURN
1 SEX M
1 AGE 37
1 DEAT
2 DATE 05 FEB 1742
2 SPLAC @SP0451@
1 SPLAC @SP0451@
1 TITL
2 TYPE Baron
1 FLEX TITLE
2 PHRASE "New title granted"
2 CONTENTS "2nd Baron of Ashcroft"
1 NOTE "Wore two monocles, one per eye. Declared forks ‘an ungodly invention.’"
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**👴🏼 @ST0252@ STICKY – Wilberforce Montmorency 3rd baron of Ashcroft died June 19 1776👑**
```gedcom
0 @ST0653@ STICKY             /* Wilberforce Montmorency – 3rd Baron */
1 TYPE HEIR, SON
1 SUBM @B001@
1 TEMPLATE @T01003@           /* Inh of Noble Title and Estate JUN 19 1776 */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR, SON, TITLED
1 ASSET @A032@
1 NAME
2 FORM Wilberforce Montmorency
2 PART Wilberforce
3 TYPE GIVN
2 PART Montmorency
3 TYPE SURN
1 SEX M
1 AGE 41
1 DEAT
2 DATE 19 JUN 1776
2 SPLAC @SP0451@
1 SPLAC @SP0451@
1 TITL
2 TYPE Baron
1 FLEX TITLE
2 PHRASE "New title granted"
2 CONTENTS "3rd Baron of Ashcroft"
1 NOTE "Chronically late; insisted time was a rumor. Once missed his own knighthood."
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```
**🧔‍♂️ @ST0252@ STICKY – Thaddeus Montmorency 4th baron of Ashcroft died October 29 1794👑**
```gedcom
0 @ST0654@ STICKY             /* Thaddeus Montmorency – 4th Baron */
1 TYPE HEIR, SON
1 SUBM @B001@
1 TEMPLATE @T01004@           /* Inh of Noble Title and Estate OCT 29 1794 */
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE HEIR, SON, TITLED
1 ASSET @A032@
1 NAME
2 FORM Thaddeus Montmorency
2 PART Thaddeus
3 TYPE GIVN
2 PART Montmorency
3 TYPE SURN
1 SEX M
1 AGE 48
1 DEAT
2 DATE 29 OCT 1794
2 SPLAC @SP0451@
1 SPLAC @SP0451@
1 TITL
2 TYPE Baron
1 FLEX TITLE
2 PHRASE "New title granted"
2 CONTENTS "4th Baron of Ashcroft"
1 NOTE "Grew sideburns so vast they required seasonal pruning."
1 CREA 30 APR 2025
1 CHAN 11 AUG 2025
```

[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-17"></a>  
## 🛡️ Example 17: Guild Membership Certificate 

This GEDCOM 8 example models a **Guild Membership Certificate** issued on 15 March 1702 in London to John Smith by the Worshipful Company of Blacksmiths. It demonstrates:

- Representing a historical membership record as both an **event** (`GROUP, GUILD-MEM`) and an **asset** `STICKY`
- Linking multiple roles (`MEMBER`, `MASTER`, `WITNESS`, `ITEM, CERTIFICATE`) to the same `TEMPLATE`
- Incorporating a **period-style transcription** (“Be it knowne unto all men by these presentes…”) within a `FLEX ANNOTATION` to preserve historical context and style
- Using `FLEX` fields for structured details like membership number, fee, duration, status, and seal description
- Associating a scanned copy of the certificate as an `OBJE`

The example captures not only the facts of membership but also the ceremonial and legal style of the time. It shows how GEDCOM 8 can integrate factual, structured metadata with verbatim historical language to create a rich, verifiable record.

**⚒️ @T0070@ TEMPLATE – Guild Membership Certificate of John Smit in London ⚒️**
```gedcom
0 @T0070@ TEMPLATE            /* Guild Membership Certificate of John Smith */
1 TYPE GROUP, GUILD-MEM
1 TITL "Guild Membership Certificate – Worshipful Company of Blacksmiths"
1 SUBM @B001@
1 TORIGIN ORIGDOC
1 QUAY 3
1 DATE 15 MAR 1702            /* Date of issue on document */
1 SPLAC @SP0070@              /* London, Middlesex, England */
1 FLEX REGNUMBER
2 PHRASE Guild Membership Number
2 CONTENTS 12345-BS
1 FLEX DECIMAL, CURR, GBP
2 PHRASE Fee paid
2 CONTENTS 2.0
1 FLEX Descript
2 PHRASE Membership duration
2 CONTENTS Lifetime
1 FLEX DESCRIPT
2 PHRASE Member status
2 CONTENTS Active
1 FLEX DESCRIPT
2 PHRASE Official Seal or Stamp
2 CONTENTS Red wax with hammer and anvil emblem
1 FLEX ANNOTATION
2 PHRASE Document description
2 CONTENT NOTE
3 CONT Document includes official wax seal, handwritten signatures, details of training,
3 CONT journeyman certification, and record of a skills examination required for guild entry.
3 CONT Document issued by the Worshipful Company of Blacksmiths.
1 FLEX ANNOTATION
2 PHRASE Full period-style text of membership certificate, summarizing training, qualification, method of entry, rights, oath, and signatories
2 CONTENTS NOTE
3 CONT Be it knowne unto all men by these presentes, that I, John Smith, having faithfully served a full seaven
3 CONT years’ apprenticeship under Master Robert Turner in the noble craft of blacksmithing — forging of tools,
3 CONT horseshoeing, welding of iron, and sundry works — am hereby admitted as a free journeyman of the Worshipful
3 CONT Company of Blacksmiths.
3 CONT By virtue of mine completed service and the passing of the masters’ examination, I am granted liberty
3 CONT to keep my own forge, take apprentices, and sell wares within the city bounds.
3 CONT I doe solemnly sweare to uphold the statutes of this Company, to set forth honest measure, true workmanship,
3 CONT and just price, according to the ancient custom.
3 CONT In witnesse hereof, this charter is sealed and subscribed by our hands:
3 CONT
3 CONT John Smith, Edward Clarke, and the said Master Robert Turner,
3 CONT 
3 CONT in the Year of Our Lord 1702.
1 EVEN GROUP, GUILD-MEM
2 DATE 15 MAR 1702            /* Date of issue on document */
2 SPLAC @SP0070@              /* London, Middlesex, England */
1 ROLES
2 STICKY @ST0100@             /* Journeyman John Smith – Becomes official certified member */
2 STICKY @ST0101@             /* Robert Turner – Guild Master */
2 STICKY @ST0102@             /* Edward Clarke – Witness */
2 STICKY @ST0103@             /* Guild Membership Certificate */
1 CITA
2 SOUR @S0045@
2 TITL Scan of Guild Membership Certificate - 
2 PAGE 1
1 DATA
~ ~ ~
1 CREA 26 APR 2025
1 CHAN 11 AUG 2025
```
**📜 @ST0103@ STICKY – Guild Membership Certificate as physical asset**
```gedcom
0 @ST0103@ STICKY             /* Guild Membership Certificate as physical asset */
1 TYPE DOCUMENT, CERTIFICATE, "Guild Membership Certificate"
1 TITL Guild Membership Certificate of John Smith
2 PHRASE "Issued by Worshipful Company of Blacksmiths in London"
1 SUBM @B001@
1 TEMPLATE @T0070@            /* Guild Membership Certificate of John Smit in London */
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 15 MAR 1702            /* Date of issue on document */
1 SPLAC @SP0070@              /* London, Middlesex, England */
1 FLEX DESCRIPT
2 PHRASE Material of certificate
2 CONTENTS Parchment with handwritten calligraphy and embossed guild seal
1 OBJ @O0031@                 /* Scan of Guild Membership Certificate of John Smith */
1 CREA 01 JUL 2025
1 CHAN 31 JUL 2025
```
**🧔🏻‍♂️ @ST0100@ STICKY – John Smith - admitted into the guild 🧔🏻‍♂️**
```gedcom
0 @ST0100@ STICKY             /* John Smith */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0070@
1 TORIGIN ORIGDOC
1 QUAY 3
1 EVEN GROUP, GUILD-MEM
2 DATE 15 MAR 1702            /* Date of issue on document */
2 SPLAC @SP0070@              /* London, Middlesex, England */
1 ROLE MEMBER
1 FLEX ANNOTATION
2 PHRASE Details of professional training
2 CONTENTS NOTE
3 CONT Seven-year apprenticeship under Master William Carter, specializing in forging tools and horseshoeing
1 FLEX ANNOTATION
2 PHRASE Level of trade qualification
2 CONTENTS NOTE
3 CONT Certified journeyman status awarded by the Worshipful Company of Blacksmiths
1 FLEX ANNOTATION
2 PHRASE Membership obtained by:
2 CONTENTS NOTE
3 CONT Apprenticeship completion and successful skills examination, including demonstration of forging, welding, and tool-making
1 FLEX ANNOTATION
2 PHRASE Membership rights granted
2 CONTENTS NOTE
3 CONT Right to operate a forge, employ apprentices, and sell iron goods in the city market
1 FLEX ANNOTATION
2 PHRASE Membership oath text
2 CONTENTS NOTE
3 CONT Sworn oath to uphold guild rules, fair pricing, and quality standards
1 FLEX ANNOTATION
2 PHRASE Signatories on certificate
2 CONTENTS NOTE
3 CONT John Smith, Robert Turner, Edward Clarke
1 NOTE Person admitted into the guild.
1 NAME
2 FORM John Smith
2 PART John
3 TYPE GIVN
2 PART Smith
3 TYPE SURN
1 SEX M
1 AGE 35
1 CREA 26 APR 2025
1 CHAN 09 AUG 2025
```
**👨🏻‍🦱 @ST0101@ STICKY – Robert Turner - Guild master approving the membership 👨🏻‍🦱**
```gedcom
0 @ST0101@ STICKY             /* Robert Turner */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0070@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE MASTER
1 NOTE Guild master approving the membership.
1 NAME
2 FORM Robert Turner
2 PART Robert
3 TYPE GIVN
2 PART Turner
3 TYPE SURN
1 SEX M
1 AGE 50
1 CREA 26 APR 2025
1 CHAN 09 AUG 2025
```
**👨‍🦲 @ST0102@ STICKY – Edward Clarke - witnessing the admission 👨‍🦲**
```gedcom
0 @ST0102@ STICKY             /* Edward Clarke */
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0070@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE WITNESS
2 PHRASE Person witnessing the admission.
1 NAME
2 FORM Edward Clarke
2 PART Edward
3 TYPE GIVN
2 PART Clarke
3 TYPE SURN
1 SEX M
1 AGE 42
1 CREA 26 APR 2025
1 CHAN 09 AUG 2025
```
**📜 @ST0103@ STICKY – Scan of Guild Membership Certificate of John Smit in London - STICKY 📜**
```gedcom
0 @ST0103@ STICKY             /* Certificate */
1 TYPE CERTIFICATE
2 PHRASE "Guild Membership Certificate of John Smit in London"
1 SUBM @B001@
1 TEMPLATE @T0070@
1 TORIGIN ORIGDOC
1 QUAY 3
1 FLEX MATERIAL
2 PHRASE Material of certificate
2 CONTENTS Parchment with handwritten calligraphy and embossed guild seal
1 ROLE ITEM, CERTIFICATE      /* The certificate itself. */
1 OBJ @O003@                  /* Scan of The certificate itself. (not present in example)*/
2 TITLE "Scan of Guild Membership Certificate of John Smit 15 MAR 1702"
1 CREA 26 APR 2025
1 CHAN 11 AUG 2025
```
**🧔🏻‍♂️ @I0500@ INDI – John Smith - admitted into the guild 🧔🏻‍♂️**
```gedcom
0 @I0500@ INDI
1 NAME
2 FORM John Smith
2 PART John
3 TYPE GIVN
2 PART Smith
3 TYPE SURN
1 SEX M
1 AGE 35
1 ROLES
2 STICKY @ST0100@             /* John Smith – Member */
1 CREA 26 APR 2025
1 CHAN 09 AUG 2025
```
**👨🏻‍🦱 @I0501@ INDI – Robert Turner - Guild master approving the membership 👨🏻‍🦱**
```gedcom
0 @I0501@ INDI
1 NAME
2 FORM Robert Turner
2 PART Robert
3 TYPE GIVN
2 PART Turner
3 TYPE SURN
1 SEX M
1 AGE 50
1 ROLES
2 STICKY @ST0101@             /* Robert Turner – Guild Master */
2 STICKY @ST0201@             /* Robert Turner – Member */
1 CREA 26 APR 2025
1 CHAN 09 AUG 2025
```
**👨‍🦲 @I0502@ INDI – Edward Clarke - witnessing the admission 👨‍🦲**
```gedcom
0 @I0502@ INDI
1 NAME
2 FORM Edward Clarke
2 PART Edward
3 TYPE GIVN
2 PART Clarke
3 TYPE SURN
1 SEX M
1 AGE 42
1 ROLES
2 STICKY @ST0102@             /* Edward Clarke – Witness */
2 STICKY @ST0202@             /* Edward Clarke – Member */
1 CREA 26 APR 2025
1 CHAN 09 AUG 2025
```
**🏘️ @SP0070@ SPLAC – London, Middlesex, England 🏘️**
```gedcom
0 @SP0070@ SPLAC              /* London, Middlesex, England */
1 TYPE CITY, POLI, 51, City   /* Gov type 51 is City*/ 
~ ~ ~
```
**🛡️ @SP0070@ GROUP – Worshipful Company of Blacksmiths, London, Middlesex, England 🛡️**
```gedcom
0 @T0071@ GROUP
1 TYPE ORGANIZATION, TRADEUNION, Guild
1 TITL "Worshipful Company of Blacksmiths, London"
1 TORIGIN ORIGDOC
1 QUAY 3
1 SUBM @B001@
1 SPLAC @SP0070@              /* London, Middlesex, England */
1 DATE 15 MAR 1702
1 SPLAC @SP0070@              /* London, Middlesex, England */
1 MEMBERS
2 STICKY @ST0100@             /* John Smith – Member */
2 STICKY @ST0201@             /* Robert Turner – Member */
2 STICKY @ST0202@             /* Edward Clarke – Member */
1 FLEX NOTE
2 PHRASE Official Seal or Stamp
2 CONTENTS NOTE
3 CONT Official Seal or Stamp:
3 CONT Red wax with hammer and anvil emblem
1 CREA 26 APR 2025
1 CHAN 09 AUG 2025
```
**💾 @S0045@ SOURCE for Guild Membership Certificate**
```gedcom
0 @S0045@ SOUR
1 TITL Guild Membership Certificate of John Smit in London
1 AUTH Worshipful Company of Blacksmiths in London
1 PUBL "Filed in London National Archives, case #1905-328C"
1 ABBR "John Smith 1702"
1 DATA
2 EVEN GROUP, GUILD-MEM
3 DATE 15 MAR 1702            /* Date of issue on document */
4 PHRASE "Guild Membership Certificate of John Smit in London"
3 SPLAC @SP0070@              /* London, Middlesex, England */
2 AGNC Worshipful Company of Blacksmiths in London
2 NOTE "Preserved in London National Archives, box 12, folder 3"
~ ~ ~
1 OBJ @O0031@                 /* Scan of Guild Membership Certificate of John Smith */
2 TITL Scanned Guild Membership Certificate of John Smit in London
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```
**🖼️ @O0031@ OBJE – Scan of Guild Membership Certificate of John Smith - OBJE 🖼️**
```gedcom
0 OBJE @O0031@                /* Multimedia record with file link  */
1 FILE https://example.org/guildcertifs/John Smith-1702-cert.pdf
2 FORM application/pdf
3 MIME application/pdf
2 TITL Scanned Guild Membership certificate
1 CREA 29 APR 2025
1 CHAN 31 JUL 2025
```


[🔝 Back to top](#appendix-b-gedcom-examples)


<a name="example-18"></a>  

## ⚖️ Example 18: Court Trial Record, Humorous Fictional Case

This example shows how a GEDCOM 8 structure can model a court trial involving many roles, using only `STICKY` blocks with `ROLE` info.  
The case? A dramatic but highly fictional courtroom battle involving various characters — each linked to a single `TEMPLATE` using a properly structured `STICKY`.  
This is a **fun** and slightly absurd illustration designed to help users understand the many `ROLE` types usable in legal records.

**⚖️ @T0088@ – TEMPLATE – Verdict of Guilty, Custodial Sentence**
```gedcom
0 @T0088@ TEMPLATE
1 TYPE LEGAL, JUDGMENT
1 TITL Verdict of Guilty - Custodial Sentence
2 PHRASE Verdict of Guilty for Jack Hammer
1 SUBM @B001@
1 TORIGIN ORIGDOC             /* Derived directly from original document */
1 QUAY 3                      /* Direct and primary evidence */
1 DATE 01 APR 2024
1 SPLAC @SP0999@              /* Fictional Courthouse, Funtown */
1 EVEN
2 DATE 01 APR 2024
2 SPLAC @SP0999@              /* Fictional Courthouse, Funtown */
1 ROLES
2 STICKY @ST0090@             /* Defendant: Jack Hammer MAIN, DEFENDANT */
2 STICKY @ST0091@             /* Defense Lawyer: Habeas Jokers LAWYER, DEFENSE*/
2 STICKY @ST0092@             /* Prosecutor: Blaise Hearsay PROSECUTOR */
2 STICKY @ST0093@             /* Judge: Bench Warmers JUDGE */
2 STICKY @ST0094@             /* Jury Foreman: Luke Atmey JURY, FOREMAN */
2 STICKY @ST0095@             /* Defense Witness: William Havamug WITNESS, DEFENSE */
2 STICKY @ST0096@             /* Prosecution Witness: Joe Starbuck WITNESS, PROSECUTION */
2 STICKY @ST0097@             /* Victim: Delicia Scones VICTIM */
1 CITA
2 SOUR @S0071@
2 PAGE 5
2 DATA
~ ~ ~
1 CREA 16 APR 2025
1 CHAN 10 AUG 2025
```
**🔨 @ST0090@ STICKY – Defendant: Jack Hammer**
```gedcom
0 @ST0090@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 EVEN
2 DATE 01 APR 2024
2 SPLAC @SP0999@              /* Fictional Courthouse, Funtown */
1 ROLE MAIN, DEFENDANT
1 NAME
2 FORM Jack Hammer
~ ~ ~
1 SEX M
1 AGE 37
1 OCCU Freelance Demolitionist
1 NOTE Known to carry a literal hammer everywhere.
~ ~ ~
```
**🕶️ @ST0091@ STICKY – Defense Lawyer: Habeas Jokers**
```gedcom
0 @ST0091@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE LAWYER, DEFENSE
1 NAME
2 FORM Habeas Jokers
~ ~ ~
1 SEX M
1 AGE 63
1 NOTE Claimed 327 years of combined courtroom experience.
~ ~ ~
```
**📢 @ST0092@ STICKY – Prosecutor: Blaise Hearsay**
```gedcom
0 @ST0092@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE PROSECUTOR
1 NAME
2 FORM Blaise Hearsay
~ ~ ~
1 SEX F
1 AGE 42
1 OCCU State Attorney
1 NOTE Famous for never saying "Objection!"
~ ~ ~
```
*👩‍⚖️ @ST0093@ STICKY – Judge: Bench Warmers**
```gedcom
0 @ST0093@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE JUDGE
1 NAME
2 FORM Bench Warmers
~ ~ ~
1 SEX M
1 AGE 78
1 NOTE Known to nap during opening statements.
~ ~ ~
```
**🎯 @ST0094@ STICKY – Jury Foreman: Luke Atmey**
```gedcom
0 @ST0094@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE JURY, FOREMAN
1 NAME
2 FORM Luke Atmey
~ ~ ~
1 SEX M
1 AGE 51
1 NOTE Jury voted 11-1 until Luke convinced them over pizza.
~ ~ ~
```
**☕ @ST0095@ STICKY – Defense Witness: William Havamug**
```gedcom
0 @ST0095@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE WITNESS, DEFENSE
1 NAME
2 FORM William Havamug
~ ~ ~
1 SEX M
1 AGE 89
1 NOTE “I saw everything through my monocle,” he claimed.
~ ~ ~
```
**🔍 @ST0096@ STICKY – Prosecution Witness: Joe Starbuck**  
```gedcom
0 @ST0096@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE WITNESS, PROSECUTION
1 NAME
2 FORM Joe Starbuck
~ ~ ~
1 SEX M
1 AGE 29
1 OCCU Barista
1 NOTE Eyewitness because trial took place next to his café.
~ ~ ~
```
**💔 @ST0097@ STICKY – Victim: Delicia Scones**
```gedcom
0 @ST0097@ STICKY
1 TYPE PERSON
1 SUBM @B001@
1 TEMPLATE @T0088@
1 TORIGIN ORIGDOC
1 QUAY 3
1 ROLE VICTIM
1 NAME
2 FORM Delicia Scones
~ ~ ~
1 SEX F
1 AGE 34
1 NOTE Lost a bakery window in the altercation.
~ ~ ~
```


[🔝 Back to top](#appendix-b-gedcom-examples)

---

<a name="example-19"></a>  
## 🪦 Example 19: Gravestone with Named and Implied Persons

This example demonstrates a `MEMORIAL, GRAVESTONE` `TEMPLATE` built from a single photographed tombstone — but reveals much more. It shows how careful attention to inscriptions can yield named individuals, inferred family relationships, roles, dates, and annotations.

**Highlights:**

- **Deep analysis of inscriptions**: Each name, role, and date was derived from text on the gravestone (e.g., "beloved father" implies a child; "gran" implies a grandchild born later).
- **Rich CITA structure**: The `TEMPLATE` includes a fully developed `CITA` with `DATA`, `TRANSCRIPT`, `TEXTDISPLAY`, `URL`, `RECORDID`, and more — useful for rigorous source linking.
- **STICKY roles**:
  - Thaddeus (`ROLE MAIN, DECEASED`, `AN_DEATH`)
  - Euphemia (`ROLE WIDOW, DECEASED`, `AN_DEATH`)
  - One `CHILD` and one `GRANDCHILD` implied (`AN_MENTION`)
- **Estimated data**: `MARR` date ranges are included for the couple, along with a `BIRT` date for the grandchild (after Thaddeus’s death).
- **FLEX ANNOTATION** captures:
  - Epitaphs with emojis and musical symbols (e.g., 🎵 “Forever in His arms”)
  - Religious quotes and Bible verses (`John 14:1`)
- **Occupation** ("Pastor") is justified by context and reinforced by the gravestone’s biblical tone.
- **Document chain**:
  - The `TEMPLATE` links to a `SOURCE` (cemetery register)
  - The `SOURCE` links to a `REPO` (cemetery records office) using a full `<<SOURCE_REPOSITORY_CITATION>>` with `CALN`, `MEDI`, and `NOTE`
  - A linked `OBJE` contains a fictional photo of the stone
- `TORIGIN ORIGDOC, INCOMPLETE` signals that some persons are only partially documented.
- `TORIGIN ORIGDOC, GUESSED` signals that some persons (the children) were only "guessed" to exist. as all other info about them is missing.
- `QUAY` values are used to reflect varying certainty per person.

*🪦 This example shows how even minimal physical evidence can be maximally encoded using GEDCOM 8 structures — when parsed with care.*



**🪦 @T019@ - Gravestone for Thaddeus and Euphemia Stoneworthy**
```gedcom
0 @T019@ TEMPLATE
1 TYPE MEMORIAL, GRAVESTONE
1 TITL Gravestone for Thaddeus and Euphemia Stoneworthy
1 SUBM @B001@
1 TORIGIN ORIGDOC, INCOMPLETE
1 QUAY 2
1 DATE 15 APR 1924
1 SPLAC @SP019@               /* Roseview Cemetery, Northmoor */
1 FLEX ANNOTATION
2 PHRASE Tombstone inscription
2 CONTENTS "In loving memory of Thaddeus Stoneworthy — beloved husband and father."
1 FLEX ANNOTATION
2 PHRASE Tombstone inscription
2 CONTENTS "Euphemia Stoneworthy — dearly loved mother and gran. 🎵 Forever in His arms."
1 FLEX ANNOTATION
2 PHRASE Bible verse from tombstone
2 CONTENTS "Let not your heart be troubled." (John 14:1)
1 CITA
2 SOUR @S019@                 /* Roseview Cemetery Tombstone Register */
2 PAGE Section 5, Row B, Plot 12
2 DATA
3 DATE 18 MAR 1932
3 TEXT “Gravestone of Thaddeus and Euphemia Stoneworthy, Section 5, Row B, Plot 12”
4 MIME text/plain
4 LANG en
2 AUTHOR Northmoor Cemetery Administration
2 TITL Tombstone Register of Roseview Cemetery, 1890–1950
2 DATES
3 RECORDED 18 MAR 1932
2 TEXTDISPLAY “Roseview Cemetery Register: Section 5, Row B, Plot 12”
2 TRANSCRIPT “Gravestone of Thaddeus and Euphemia Stoneworthy, Section 5, Row B, Plot 12”
2 FORMAT
3 TYPE image/jpeg
2 URL https://roseviewcemetery.example.org/stoneworthy-gravestone.jpg
2 LANGUAGE en
2 RECORDID RCV-STN-5B12
2 CONTAINER Roseview Cemetery Archives
2 ITEMTYPE Memorial Gravestone Record
2 SHORTTITLE Roseview Tombstones
2 WWWLINK
3 VALUE https://roseviewcemetery.org/register
2 QUAY 3
2 OBJE @O019@                 /* Gravestone photograph */
1 ROLES
2 STICKY @ST1901@             /* Thaddeus Stoneworthy, main */
2 STICKY @ST1902@             /* Euphemia Stoneworthy, widow */
2 STICKY @ST1903@             /* child (implied) */
2 STICKY @ST1904@             /* grandchild (implied) */
1 CREA 27 JUL 2025
1 CHAN 27 JUL 2025
```
**🪦 @ST1901@ STICKY – Main (Thaddeus Stoneworthy)**
```gedcom
0 @ST1901@ STICKY             /* Thaddeus Stoneworthy */
1 TYPE PERSON, AN_DEATH
1 SUBM @B001@
1 TEMPLATE @T019@
1 TORIGIN ORIGDOC
1 QUAY 2
1 ROLE MAIN, DECEASED
1 NAME
2 FORM Thaddeus Stoneworthy
2 PART Thaddeus
3 TYPE GIVN
2 PART Stoneworthy
3 TYPE SURN
1 BIRT
2 DATE 21 NOV 1858
1 DEAT
2 DATE 07 APR 1924
1 BURI
2 DATE 09 APR 1924
1 MARR
2 DATE BET 1880 AND 1890
1 OCCU Pastor
1 CREA 27 JUL 2025
1 CHAN 27 JUL 2025
```
**🕊️ @ST1902@ STICKY – Widow (Euphemia Stoneworthy)**
```gedcom
0 @ST1902@ STICKY             /* Euphemia Stoneworthy */
1 TYPE PERSON, AN_DEATH
1 SUBM @B001@
1 TEMPLATE @T019@
1 TORIGIN ORIGDOC
1 QUAY 2
1 ROLE WIDOW, DECEASED
1 NAME
2 FORM Euphemia Stoneworthy
2 PART Euphemia
3 TYPE GIVN
2 PART Stoneworthy
3 TYPE SURN
1 BIRT
2 DATE 04 FEB 1862
1 DEAT
2 DATE 12 MAR 1932
1 BURI
2 DATE 14 MAR 1932
1 MARR
2 DATE BET 1880 AND 1890
1 CREA 27 JUL 2025
1 CHAN 27 JUL 2025
```
**👶 @ST1903@ STICKY – Child (implied)**
```gedcom
0 @ST1903@ STICKY             /* child of Thaddeus and Euphemia */
1 TYPE PERSON, AN_MENTION
1 SUBM @B001@
1 TEMPLATE @T019@
1 TORIGIN ORIGDOC, GUESSED
1 QUAY 1
1 ROLE CHILD
1 CREA 27 JUL 2025
1 CHAN 27 JUL 2025
```
**👼 @ST1904@ STICKY – Grandchild (implied)**
```gedcom
0 @ST1904@ STICKY             /* grandchild of Euphemia */
1 TYPE PERSON, AN_MENTION
1 SUBM @B001@
1 TEMPLATE @T019@
1 TORIGIN ORIGDOC, GUESSED
1 QUAY 1
1 ROLE GRANDCHILD
1 BIRT
2 DATE AFT 07 APR 1924        /* Date unknown, but the birth probably came after Thaddeus death */
1 CREA 27 JUL 2025
1 CHAN 27 JUL 2025
```
**📚 @S019@ SOURCE – Northmoor Cemetery Tombstone Registry**
```gedcom
0 @S019@ SOUR
1 TITL Tombstone Register of Roseview Cemetery, Northmoor (1890–1950)
1 AUTH Northmoor Cemetery Administration
1 PUBL Office of Records, Roseview Cemetery
1 ABBR Roseview Tombstone Register
1 TEXT Registry index with engraved inscriptions and burial details. Covers headstones, memorials, and niche plates for interments from 1890–1950
1 DATA
~ ~ ~
1 REPO @R019@
2 CALN Section 5B, Registry Volume 3
3 MEDI BOOK
3 PHRASE Roseview Cemetery Burial Records
2 NOTE Original burial register used for verifying inscriptions and burial locations
```
**🖼️ @O019@ OBJE – Photo of the Stoneworthy Gravestone**
```gedcom
0 @O019@ OBJE
1 FILE https://roseviewcemetery.example.org/stoneworthy-gravestone.jpg
2 FORM image/jpeg
3 MEDI Image
2 TITL Gravestone of Thaddeus and Euphemia Stoneworthy 18 MAR 1932
1 NOTE Digitized photo of gravestone in Section 5, Row B, Plot 12 of Roseview Cemetery
```
**🏛️ @R019@ REPO – Roseview Cemetery Records Office**
```gedcom
0 @R019@ REPO
1 NAME Roseview Cemetery Records Office
1 ADDR 777 Memorial Lane
2 CITY Northmoor
2 POST NM44 2TG
2 CTRY United Kingdom
1 EMAIL records@roseviewcemetery.org
1 WWW https://roseviewcemetery.org/records
```

[🔝 Back to top](#appendix-b-gedcom-examples)

