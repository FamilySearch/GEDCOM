

### `g8:enumset-STICKY-MAINROLE`

There is a `STICKY-MAINROLE` table and a `STICKY_ROLE` table. That is only done to be able to divide the `STICKY-ROLE` table in **"bite-sized chunks"**. So we can more easily see what `ROLE`'s we can choose from.   
As for a `ROLE`-tag inside a `STICKY` we only put **1 or more `ROLE`'s from the `STICKY-ROLE` table**, after the `SUBROLE` tag.  
We dont put values from the `STICKY-MAINROLE` table after the `ROLE` tag in a `STICKY`! So we **never** put a `STICKY-MAINROLE` there.

This table describes the high-level category of function or relationship this `STICKY` had in the context of the `TEMPLATE`. Roles describe a person's or entity's involvement in a given event or situation, and determine what kind of roles are valid.

| ICO | MAINROLE     | Description                                                                |
|-----| ------------ | ----------------------------------------------------------------------- |
| 🗂️ | `ADMIN`      | Person acted in an administrative or bureaucratic role (e.g. official, clerk, registrar, census). |
| 🧱 | `ASSET`      | Person or Asset who/that was connected to the possession, transfer, or status of a non-human entity (e.g., land, object). |
| 👶 | `BIRTH`      | Person was born or played a key role in a birth event. (child, parent, midwife)|
| 🏢 | `CORPORATION`| Person was involved in an institution (e.g. school, guild, company). |
| 🔁 | `CROSSROLE`  | Role applicable in multiple contexts (e.g., witness, guardian). |
| ⚰️ | `DEATH`      | Person died or had a role in the context of death (e.g. deceased, undertaker, mourner). |
| 🧬 | `DNA`        | Roles related to genetic testing in analysis labs or research programs, genealogical matching, lab processing, and interpretation of DNA test results. Includes both professional and familial participation  — with focus on identity, inheritance, and kinship confirmation. |
| 📚 | `EDUCATIONAL`| Person acted in an educational setting (e.g. teacher, student, examiner). |
| 🗓️ | `EVENT`      | Person participated in a general event (e.g. spectator, officiant). |
| 👨‍👩‍👧 | `FAMILY`     | Role defines kinship or household relationship. (parent, child, spouse) |
| 🛡️ | `GROUP`      | Role in a collective or institutional context (e.g. tribe, church, farm, guild). |
| 🪪 | `IDENTITY`   | Roles associated with formal or legal identification (e.g. renamed, declared), such as declared identity, proven relationships, or official recognitions. Includes DNA-based identity roles such as matched individual or inferred parent. |
| 📜 | `INHERITANCE`| Person was involved in inheritance or estate transfer. |
| ⚖️ | `JUDICIAL`   | Role in legal or courtroom setting. (judge, magistrate, court officer, plaintiff) |
| 🖋️ | `LEGAL`      | Role in legal matters outside court (e.g., agent, claimant, notary, lawyer). |
| 💍 | `MARRIAGE`   | Person participated in a marriage or similar union. |
| 🎞️ | `MEDIA`      | Person involved in creation, subject, or handling of media (e.g., author, illustrator, subject). |
| 🩺 | `MEDICAL`    | Roles related to medical, clinical, or biological activities, including examination, treatment, testing, and sample collection. Includes roles related to DNA testing, sample handling, or biological analysis. |
| 🪖 | `MILITARY`   | Person served in or was affected by military service. (soldier, officer, commander, or veteran) |
| 📜 | `OFFICIAL`   | Government or civic ceremonial role (e.g., mayor, consul). |
| 🏘️ | `PROPERTY`   | Person held or transferred ownership, use, or involvement in real estate. |
| ✝️ | `RELIGIOUS`  | Person participated in or officiated religious rites. (priest, nun, initiate) |
| 🌐 | `SOCIAL`     | Participant in social events, ceremonies, or symbolic roles. |
| 🌀 | `OTHER`      | Everything that does not fit a standard category; must include a `PHRASE`. |

### `g8:enumset-STICKY-ROLE`

This table defines all standardized combinations of `MAINROLE` and `ROLE` used in the `STICKY` structure. Each row represents a unique pairing allowed in the model. The third column explains the usage context and includes examples where relevant. Categories are alphabetized by `ROLE` and `SUBROLE`. Use this as a master reference or pruning sheet.

| ICO | MAINROLE      | ROLE              | Description (with examples) |
|---|---------------|-------------------|-----------------------------|
| 🗂️ | `ADMIN`       | `ARCHIVIST`       | Keeper of records  |
| 🗂️ | `ADMIN`       | `BUREAUCRAT`      | Managed procedural or governmental duties  |
| 🗂️ | `ADMIN`       | `CHART`           | Diagram or tabular record used for tracking, planning, or reporting. Use PHRASE for detail: [chart type, purpose, date] |
| 🗂️ | `ADMIN`       | `CONSUL`          | Held a state or municipal office with civic duties    |
| 🗂️ | `ADMIN`       | `ENUMARATOR`      | An enumerator is an official data recorder — usually employed by a state, church, or institution to record households or individuals |
| 🗂️ | `ADMIN`       | `INSPECTOR`       | Government or institutional inspector, e.g., for emigration or public health.  |
| 🗂️ | `ADMIN`       | `INVENTORYM`      | INVENTORYMAKER — Compiles asset list (also appears in legal) |
| 🗂️ | `ADMIN`       | `ISSUER`          | Person officially authorized to issue a certificate, license, or document. Often |overlaps with registrar. |
| 🗂️ | `ADMIN`       | `LEDGER`          | Book or record of accounts, transactions, or inventories. Use PHRASE for detail: [ledger type, date range, archive] |
| 🗂️ | `ADMIN`       | `MAP`             | Cartographic representation of a location or area. Use PHRASE for detail: [map type, date, creator] |
| 🗂️ | `ADMIN`       | `MESSENGER`       | Courier or person delivering                            |
| 🗂️ | `ADMIN`       | `RECIPIENT`       | Person formally receiving an object, credential, or authorization — such as a passport, certificate, permit, or official document. Use when granted something in an administrative or governmental context. |
| 🗂️ | `ADMIN`       | `REGISTER`       | Official or historical register listing people, events, or items. Use PHRASE for detail: [register type, date range, archive] |
| 🗂️ | `ADMIN`       | `ROLL`            | Historical roll (e.g., tax roll, muster roll). Use PHRASE for detail: [roll type, date, jurisdiction] |
| 🗂️ | `ADMIN`       | `SITE`| General-purpose administrative or bureaucratic workplace.<br>Use PHRASE for detail: [office, registry, administration wing, civil desk, records department] |
| 🗂️ | `ADMIN`       | `TRANSCRIBER`     | Enters information  |
| 🗂️ | `ADMIN`       | `VERIFIER`        | Verifies document authenticity  |
| 🧱 | `ASSET`       | `ASSIGNEE`        | Assigned asset  |
| 🧱 | `ASSET`       | `AUCTION`         | Asset offered for sale via auction (e.g. toolset or furniture in probate)  |
| 🧱 | `ASSET`       | `AWARD`           | Prize or honor, given in recognition or as a prize. Use PHRASE for detail: [medal, certificate, award name, event, date]  |
| 🧱 | `ASSET`       | `BENEFICIARY`     | Legal or named recipient of an object, particularly in the context of a will or deed. |
| 🧱 | `ASSET`       | `BEQUEST`         | Asset being inherited through a will or succession document   |
| 🧱 | `ASSET`       | `CERTIFICATE`     | Asset representing the document itself.  |
| 🧱 | `ASSET`       | `COLLATERAL`      | Asset pledged as security for a loan or legal agreement (e.g. land in a bond)  |
| 🧱 | `ASSET`       | `CREATOR`         | Original maker or fabricator of the item (e.g., artisan who crafted the medal). |
| 🧱 | `ASSET`       | `DONOR`           | Person who gives or gifts the item voluntarily. |
| 🧱 | `ASSET`       | `GIFT`            | Asset being donated or given or ceremonially transferred(e.g. a cow given to a daughter on marriage) |
| 🧱 | `ASSET`       | `HOLDER`          | Person who was the **recipient**, **bearer**, or **user** of an item such as a passport, license, or medal. Includes **legal**, **formal**, or **official** document reception. Posession can be pemanent or temporarely. |
| 🧱 | `ASSET`       | `ISSUER`          | Person (or organization) who created, issued, awarded, or granted the item. Often official or institutional. (e.g., organization issuing a medal, license, passport, testresult)|
| 🧱 | `ASSET`       | `ITEM`            | Catch-all for miscellaneous movable assets (e.g. book, cart, sword) |
| 🧱 | `ASSET`       | `LISTED`          | Mentioned in a record but not transferred, often for valuation or record (e.g. farm in a will) |
| 🧱 | `ASSET`       | `LOT`             | Grouped or undivided set of items treated as a unit (e.g. “lot of 6 chairs”) |
| 🧱 | `ASSET`       | `OTHER`           | Catch-all; must clarify with `PHRASE`  |
| 🧱 | `ASSET`       | `PROPERTY`        | General asset (real estate or fixed structure) being transferred between parties (e.g. house, land parcel) |
| 🧱 | `ASSET`       | `RECIPIENT`       | Person receiving the asset.   |
| 🧱 | `ASSET`       | `REPAIRER`        | Person tasked with maintaining or restoring the object. |
| 🧱 | `ASSET`       | `STOCKRENTAL`     | Asset temporarily assigned or rented (e.g. oxen or horse or cart lent for a season) |
| 🧱 | `ASSET`       | `USER`            | Individual actively using the item (e.g., someone operating a machine or using a passport). |
| 🧱 | `ASSET`       | `WITNESS`         | Person who observed or certified the object’s issuance, transfer, or destruction. |
| 👶 | `BIRTH`       | `CHILD`           | Child being born    |
| 👶 | `BIRTH`       | `DOULA`           | Provided non-medical support to the mother during labor, birth, and early postpartum. Focused on emotional, physical, and informational care. |
| 👶 | `BIRTH`       | `FATHER`          | Biological father    |
| 👶 | `BIRTH`       | `MATERNITY-AST`   | (maternity assistant) Assisted with newborn care, mother recovery, household support during NL-"kraamtijd" (postnatal period). |
| 👶 | `BIRTH`       | `MIDWIFE`         | Midwife or person assisting at birth   |
| 👶 | `BIRTH`       | `MULTIPLE`        | A sibling from the same pregnancy (twin, triplet, quadruplet, and so on). A PHRASE can be used to specify the kind of multiple birt|
| 👶 | `BIRTH`       | `MOTHER`          | Biological mother   |
| 👶 | `BIRTH`       | `SITE`| Location where the birth occurred (indoors or outdoors).<br>Use PHRASE for detail: [maternity ward, midwife house, roadside, ship] |
| 👶 | `BIRTH`       | `WITNESS`         | Legal or informal witness to the birth    |
| 🏢 | `CORPORATION` | `ASSOCIATED`      | Linked but unclear role    |
| 🏢 | `CORPORATION` | `BONDHOLDER`      | person owning a bond or bonds issued by a government or a public company |
| 🏢 | `CORPORATION` | `CLIENT`          | Organization receiving goods or services from another party. Use PHRASE for detail: [service/product, provider, date] |
| 🏢 | `CORPORATION` | `CONTRACTOR`      | Organization engaged to perform a service or project. Use PHRASE for detail: [project type, client, location] |
| 🏢 | `CORPORATION` | `EMPLOYEE`        | Works for the institution     |
| 🏢 | `CORPORATION` | `EMPLOYER`        | Entity that offers jobs and compensates individuals for their work with salary or wages. Also offering a workplace and often "tools" to work withand sometimes health insurance and retirement plans. Use `PHRASE` for detail [boss, manager, patron, director, principal, president, proprietor, chief, executive, supervisor, foreman, master, leader]|
| 🏢 | `CORPORATION` | `EXPELLED`        | Forced removal or banishment     |
| 🏢 | `CORPORATION` | `FOUNDER`         | Person who initiated or created the institution     |
| 🏢 | `CORPORATION` | `ISERVANT`        | Indentured person: legally bound to work for another, for a fixed period, in exchange for passage to a new country, payment of a debt, or training in a trade  |
| 🏢 | `CORPORATION` | `JOINED`          | Entry into the group or institution |
| 🏢 | `CORPORATION` | `LEADER`          | Official or informal leader    |
| 🏢 | `CORPORATION` | `LEFT`            | Voluntary or general departure |
| 🏢 | `CORPORATION` | `LICENSOR`        | Organization granting rights to use something (e.g., software, patent). Use PHRASE for detail: [licensed item, jurisdiction, term] |
| 🏢 | `CORPORATION` | `LICENSEE`        | Organization receiving rights under a license agreement. Use PHRASE for detail: [licensed item, licensor, jurisdiction] |
| 🏢 | `CORPORATION` | `MANUFACTURER`    | Organization producing goods or products. Use PHRASE for detail: [product type, brand, facility location] |
| 🏢 | `CORPORATION` | `MEMBER`          | Person belongs to group (school, club, church, etc.)     |
| 🏢 | `CORPORATION` | `PARTNER`         | Organization collaborating in a joint venture or partnership. Use PHRASE for detail: [partner name, project, date] |
| 🏢 | `CORPORATION` | `PUBLISHER`       | Entity releasing books, newspapers, maps, or other published materials. Use PHRASE for detail: [publication name, medium, date range] |
| 🏢 | `CORPORATION` | `RETIRED`         | Ceased formal role due to age or tenure      |
| 🏢 | `CORPORATION` | `SITE`| Workplace or professional facility connected to the organization.<br>Use PHRASE for detail: [factory, headquarters, lab, facility, warehouse, shop] |
| 🏢 | `CORPORATION` | `SPONSOR`         | Organization providing financial or resource support. Use PHRASE for detail: [sponsored event, amount/type, date] |
| 🏢 | `CORPORATION` | `STUDENT`         | Learns or trains there      |
| 🏢 | `CORPORATION` | `SUPPLIER`        | Organization providing materials or goods to others. Use PHRASE for detail: [materials supplied, client type, delivery region] |
| 🏢 | `CORPORATION` | `TRANSFERRED`     | Moved from one institution to another (e.g., schools, prisons)      |
| 🏢 | `CORPORATION` | `VENDOR`          | Entity selling goods or services, often in a retail context. Use PHRASE for detail: [goods/service type, sales method, location] |
| 🔁 | `CROSSROLE`   | `ADVOCATE`        | Spoke or acted on behalf of another in multiple contexts |
| 🔁 | `CROSSROLE`   | `BENEFACTOR`      | Donated or supported across legal, asset, or social settings |
| 🔁 | `CROSSROLE`   | `FRIEND`          | Social companion, friend, often mentioned in wills, letters, etc. |
| 🔁 | `CROSSROLE`   | `GUARDIAN`        | Person acting in a protective or decision-making role for another (e.g., legal guardian, sponsor). May appear in both legal and informal settings. Person also took legal/parental responsibility in inheritance, custody, etc. |
| 🔁 | `CROSSROLE`   | `HEALER`          | Provided healing across religious, medical, or folk contexts. |
| 🔁 | `CROSSROLE`   | `INTERPRETER`     | Provided translation or language assistance during testimony, legal process, or religious rite. |
| 🔁 | `CROSSROLE`   | `JUDGE`           | May appear in both legal and group contexts; adjudicated disputes |
| 🔁 | `CROSSROLE`   | `MAIN`            | Primary person of the event; not specific to event type |
| 🔁 | `CROSSROLE`   | `NEIGHBOUR`       | Nearby resident; often witness, helper, or informant |
| 🔁 | `CROSSROLE`   | `OBSERVER`        | Passive witness to an event, without formal testimony. Often included for context or reporting. |
| 🔁 | `CROSSROLE`   | `OWNER`           | Owner of land, a property or otherwise |
| 🔁 | `CROSSROLE`   | `SITE`| General site, location, locus, origin or scene when no specific mainrole applies.<br>Use PHRASE for detail: [cemetery, cave, hill, bridge, crossroads, villa, castle, embassy, station, mansion, outdoors] |
| 🔁 | `CROSSROLE`   | `TESTATOR`        | Wrote or signed a will; usually a deceased individual |
| 🔁 | `CROSSROLE`   | `TRUSTEE`         | Appointed to manage property/assets for others |
| 🔁 | `CROSSROLE`   | `WORKER`          | Generic laborer; unclear if military, farm, domestic, etc. |
| 🔁 | `CROSSROLE`   | `WITNESS`         | Saw or verified an act across many domains |
| ⚰️ | `DEATH`       | `BURIAL_OFFICIANT`| Clergy or person leading burial rituals  |
| ⚰️ | `DEATH`       | `CREMATION`       | Process of disposing of a deceased person's body by burning it   |
| ⚰️ | `DEATH`       | `DECEASED`        | Person who died   |
| ⚰️ | `DEATH`       | `DECEDENT`        | Person who died (official twerminology)  |
| ⚰️ | `DEATH`       | `FUNERAL`         | A ceremony held in remembrance of a deceased person, typically involving a gathering of family and friend |
| ⚰️ | `DEATH`       | `INFORMANT`       | Person who reported the death  |
| ⚰️ | `DEATH`       | `NOTICE`          | Notice of death  |
| ⚰️ | `DEATH`       | `OBITUARY`        | Notice of death.  |
| ⚰️ | `DEATH`       | `PALLBEARER`      | A person who helps carry the casket at a funeral.   |
| ⚰️ | `DEATH`       | `SITE`| Place of death; can include institution, home, or natural setting.<br>Use PHRASE for detail: [hospice, roadside, forest, sea] |
| ⚰️ | `DEATH`       | `WITNESS`         | Person present at death  |
| 🧬 | `DNA`         | `ANALYST`     | Trained technician or geneticist, staff or forensic worker comparing DNA profiles or evaluating result reliability, or performing or supervising the analysis. |
| 🧬 | `DNA`         | `COLLECTOR`   | Staff or person who physically collected or registered the DNA sample (e.g., nurse, lab aide, swab taker, medical staff). |
| 🧬 | `DNA`         | `EXPLAINER`   | Person (interpreter) who explained or translated DNA results to others (e.g., family member, caseworker). |
| 🧬 | `DNA`         | `GENETICIST`  | Certified specialist who reviewed, confirmed, or interpreted the DNA results. |
| 🧬 | `DNA`         | `KITOWNER`    | Registered owner or account holder of the DNA test kit, possibly different from the test subject. |
| 🧬 | `DNA`         | `LABTECH`  | Laboratory or technical worker responsible for processing or validating the DNA sample. |
| 🧬 | `DNA`         | `MATCH`       | Individual whose genetic material matched the subject’s, either fully or partially. (e.g. relative match, segment overlap) |
| 🧬 | `DNA`         | `PARENTAL`    | Biological parent, ancestor or presumed biological contributor, confirmed through DNA evidence (e.g. paternity test). |
| 🧬 | `DNA`         | `SITE`| Location connected to testing, analysis, or reporting of DNA.<br>Use PHRASE for detail: [lab, laboratory, testing center, facility, analysis center, clinic] |
| 🧬 | `DNA`         | `SPONSOR`     | Person or organization that funded or facilitated the DNA test. (e.g. gift, project, third-party study) |
| 🧬 | `DNA`         | `SUBJECT`     | Person whose DNA was tested, submitted, or reported. May include self-testers or individuals analyzed by third parties; may also appear as "testee" or "donor". |
| 📚 | `EDUCATIONAL` | `EXAMINER`        | Official evaluating exams (inspecting, certifying, examining)  |
| 📚 | `EDUCATIONAL` | `SITE`| Site where instruction or academic activity took place.<br>Use PHRASE for detail: [school, university, boarding school, classroom, academy] |
| 📚 | `EDUCATIONAL` | `STUDENT`         | Person recieving instruction. Enrolled or studying ; pupil, student, apprentice |
| 📚 | `EDUCATIONAL` | `TEACHER`         | Delivered lessons or instruction; includes instructors, tutors |
| 🗓️ | `EVENT`       | `OFFICIANT`       | Conducts ceremony or signs something, e.g. priest, registrar    |
| 🗓️ | `EVENT`       | `ORGANIZER`       | Person coordinating or arranging the event                                      |
| 🗓️ | `EVENT`       | `PARTICIPANT`     | General event role, not further specified           |
| 🗓️ | `EVENT`       | `PARTYMEMBER`     | Someone who is part of a group celebrating a specific even |
| 🗓️ | `EVENT`       | `RECORDER`        | Person who documented or recorded details of the event.     |
| 🗓️ | `EVENT`       | `SPECTATOR`       | Passive observer                                           |
| 🗓️ | `EVENT`       | `TARGET`          | Person affected by the event, e.g. victim or beneficiary               |
| 🗓️ | `EVENT`       | `WITNESS`         | Person who saw the event (e.g. accident, birth, signing)             |
| 👨‍👩‍👧 | `FAMILY`      | `ADOPTEE`         | The child being adopted  |
| 👨‍👩‍👧 | `FAMILY`      | `ADOPTER`         | Legal adoptive parent  |
| 👨‍👩‍👧 | `FAMILY`      | `AUNT`            | Aunt  |
| 👨‍👩‍👧 | `FAMILY`      | `BIRTHPARENT`     | Biological parent  |
| 👨‍👩‍👧 | `FAMILY`      | `BOARDER`         | Person receiving regular meals somewhere, in return for payment or services |
| 👨‍👩‍👧 | `FAMILY`      | `BROTHER`         | Brother   |
| 👨‍👩‍👧 | `FAMILY`      | `CHILD`           | [Listed as child of someone in family grouping] [Biological, adoptive, or recognized child] |
| 👨‍👩‍👧 | `FAMILY`      | `COUSIN`          | Cousin  |
| 👨‍👩‍👧 | `FAMILY`      | `DAUGHTER`        | Daughter |
| 👨‍👩‍👧 | `FAMILY`      | `FAMILYHEAD`      | Person acts as the representative of a household — responsible for legal, social, or census identification of the family unit |
| 👨‍👩‍👧 | `FAMILY`      | `FATHER`          | Father  |
| 👨‍👩‍👧 | `FAMILY`      | `FRIEND`          | Friend |
| 👨‍👩‍👧 | `FAMILY`      | `GRANDCHILD`      | Grandchild  |
| 👨‍👩‍👧 | `FAMILY`      | `GRANDFATHER`     | Grandfather  |
| 👨‍👩‍👧 | `FAMILY`      | `GRANDMOTHER`     | Grandmother  |
| 👨‍👩‍👧 | `FAMILY`      | `GRANDPARENT`     | Grandparent  |
| 👨‍👩‍👧 | `FAMILY`      | `GUARDIAN`        | Legal guardian. Person with legal responsibility, not necessarily parent (foster parent) |
| 👨‍👩‍👧 | `FAMILY`      | `HUSBAND`         | Husband   |
| 👨‍👩‍👧 | `FAMILY`      | `MAIN`            | Points to the main person from a `TEMPLATE`.| 
| 👨‍👩‍👧 | `FAMILY`      | `MOTHER`          | Mother   |
| 👨‍👩‍👧 | `FAMILY`      | `NEPHEW`          | Nephew  |
| 👨‍👩‍👧 | `FAMILY`      | `NIECE`           | Niece  |
| 👨‍👩‍👧 | `FAMILY`      | `PARENT`          | [Listed as parent of someone (birth, adoptive, foster if known)] [General parent-child link; can be refined with SEX] [Biological, adoptive, or acknowledged paren] |
| 👨‍👩‍👧 | `FAMILY`      | `SIBLING`         | Listed as brother, sister, or half-siblin; same generation |
| 👨‍👩‍👧 | `FAMILY`      | `SISTER`          | Sister                               |
| 👨‍👩‍👧 | `FAMILY`      | `SITE`| Residential or domestic setting central to household life or event.<br>Use PHRASE for detail: [home, house, apartment, flat, garden, yard, dwelling, kitchen] |
| 👨‍👩‍👧 | `FAMILY`      | `SON`             | Son                                  |
| 👨‍👩‍👧 | `FAMILY`      | `SOCIOPARENT`     | Sociological Parent: an adult who functions as a parent to a child, but is not legally or biologically related to the child |
| 👨‍👩‍👧 | `FAMILY`      | `SPOUSE`          | Spouse                               |
| 👨‍👩‍👧 | `FAMILY`      | `STEP`            | Step-parent, step-child, step-sibling  |
| 👨‍👩‍👧 | `FAMILY`      | `STEPCHILD`       | Stepchild                            |
| 👨‍👩‍👧 | `FAMILY`      | `STEPPARENT`      | Stepparent                           |
| 👨‍👩‍👧 | `FAMILY`      | `SURPARENT`       | Surrogate parent: a person who makes educational decisions for a child when the child's parents or guardians are unavailable or unable to fulfill this role |
| 👨‍👩‍👧 | `FAMILY`      | `UNCLE`           | Uncle                                |
| 👨‍👩‍👧 | `FAMILY`      | `WARD`            | The child or dependent in a guardianship relationship  |
| 👨‍👩‍👧 | `FAMILY`      | `WIDOW`           | A surviving spouse (female) |
| 👨‍👩‍👧 | `FAMILY`      | `WIDOWER`         | A surviving spouse (male) |
| 👨‍👩‍👧 | `FAMILY`      | `WIFE`            | Wife   |
| 🛡️ | `GROUP`       | `AFFILIATE`       | Member or casual participant in group or event |
| 🛡️ | `GROUP`       | `APPRENTICE`      | In training under a master in a trade or craft   |
| 🛡️ | `GROUP`       | `ASSOCIATED`      | Linked but unclear role    |
| 🛡️ | `GROUP`       | `COUNSELOR`       | Advisor, spiritual guide, or emotional support figure|
| 🛡️ | `GROUP`       | `DEPUTY`          | Second-in-command or acting authority|
| 🛡️ | `GROUP`       | `EMPLOYEE`        | Works for the institution     |
| 🛡️ | `GROUP`       | `EXPELLED`        | Forced removal or banishment|
| 🛡️ | `GROUP`       | `FOUNDER`         | Helped establish or formalize the group |
| 🛡️ | `GROUP`       | `GUEST`           | The person temporarily stayed, studied, or worked in the group context. |
| 🛡️ | `GROUP`       | `HEALER`	        | Role of caregiver or medical staff (religious sects)|
| 🛡️ | `GROUP`       | `HONOREE`         | Granted status for ceremonial or recognition reasons
| 🛡️ | `GROUP`       | `INITIATE`        | New entrant, often still in training or probation|
| 🛡️ | `GROUP`       | `JOINED`          | Entry into the group or institution|
| 🛡️ | `GROUP`       | `JUDGE`           | Arbitrator or internal adjudicator (guild court, tribal dispute)|
| 🛡️ | `GROUP`       | `LANDLORD`        | Granted tenancy or rights to others   |
| 🛡️ | `GROUP`       | `LEADENTITY`      | Principal non-human entity in a group (e.g., flagship, headquarters building). Use PHRASE for detail: [entity name, group, date] |
| 🛡️ | `GROUP`       | `LEADER`          | Primary figure of authority (chief, headmaster, familyhead (in a group), warden, etc.)|
| 🛡️ | `GROUP`       | `LEFT`            | Voluntary or general departure|
| 🛡️ | `GROUP`       | `MASTER`          | Skilled person mentoring others  |
| 🛡️ | `GROUP`       | `MEMBER`          | Person belongs to a kin-based lineage or extended family group  |
| 🛡️ | `GROUP`       | `MEMBERENTITY`    | Non-human entity that is part of a group (e.g., ship in a fleet, building in a monastery). Use PHRASE for detail: [group name, entity type, date] |
| 🛡️ | `GROUP`       | `NOVICE`          | Religious/semi-religious entry level (monasteries, sects)|
| 🛡️ | `GROUP`       | `OFFICER`         | Formal administrator, guard, or enforcer (esp. in guilds)|
| 🛡️ | `GROUP`       | `PATRON`          | Financial or moral supporter, not necessarily active
| 🛡️ | `GROUP`       | `REJECTED`        | The person applied but was not accepted or was expelled.                |
| 🛡️ | `GROUP`       | `REMEMBERED`      | Deceased figure held in group memory (e.g., tribal ancestors)
| 🛡️ | `GROUP`       | `RESIDENT`        | Lived within institutional group (e.g., Farm, Sect).  |
| 🛡️ | `GROUP`       | `RETIRED`         | Ceased formal role due to age or tenure|
| 🛡️ | `GROUP`       | `SAINTED`         | Canonized or revered figure (esp. SECT)
| 🛡️ | `GROUP`       | `SERVANT`         | Subordinate function role (esp. historical guilds)
| 🛡️ | `GROUP`       | `SITE`| Communal or organizational setting used by a defined group.<br>Use PHRASE for detail: [farm, commune, compound, guildhall, tribe center, association building] |
| 🛡️ | `GROUP`       | `SPOKESMAN`       | Spoke or acted on behalf of the group (representative) |
| 🛡️ | `GROUP`       | `SPONSOR`         | Acted as spiritual or legal backer (e.g., godparent, confirmation)    |
| 🛡️ | `GROUP`       | `SPONSORED`       | The person was vouched for or introduced by someone else.               |
| 🛡️ | `GROUP`       | `STUDENT`         | Learns or trains there      |
| 🛡️ | `GROUP`       | `TEACHER`         | Knowledge provider (esp. in sects)|
| 🛡️ | `GROUP`       | `TENANT`          | Inhabited land or property under lease from institution or estate     |
| 🛡️ | `GROUP`       | `TRANSFERRED`     | Moved from one group to another |
| 🛡️ | `GROUP`       | `WORKER`          | General laborer or active contributor|
| 🪪 | `IDENTITY`    | `APPLICANT`       | Person who filed or initiated an application for identity-related documents (e.g., passport, visa, name change). |
| 🪪 | `IDENTITY`    | `ASSIGNED`        | Someone else gives the identity, e.g. "He is John Smith"        |
| 🪪 | `IDENTITY`    | `DECLARED`        | Person says who they are, e.g. "I am John Smith"   |
| 🪪 | `IDENTITY`    | `EXAMINER`        | Person responsible for inspecting or verifying submitted identity documents or biometric records. |
| 🪪 | `IDENTITY`    | `INTERPRETER`     | Present to assist in cases where language barriers existed during identity proceedings (common in immigration or legal name change). |
| 🪪 | `IDENTITY`    | `NAMED`           | A name is stated without a formal declaration              |
| 🪪 | `IDENTITY`    | `RECORDER`        | Person who entered or copied the identity data into a formal register (e.g., civil clerk, church scribe). |
| 🪪 | `IDENTITY`    | `RENAMED`         | Explicit change of name, e.g. adoption, alias, name change    |
| 🪪 | `IDENTITY`    | `SPONSOR`         | Person vouching for or supporting the identity/residency claim of another, especially in immigration or residency permission cases. |
| 🪪 | `IDENTITY`    | `WITNESS`         | Individual attesting to someone’s identity (e.g., in affidavit, oath, or testimony). Often required for birth, alias, or passport paperwork. |
| 📜 | `INHERITANCE` | `ATTORNEY`        | Attorny, also called Solicitor. The legal professional who provides legal advice during will creation and ensures it meets all legal requirements. |
| 📜 | `INHERITANCE` | `ASSET`           | Specific items (e.g., a house, jewelry, money) that are part of the inheritance. |
| 📜 | `INHERITANCE` | `BENEFICIARY`     | Person receiving inheritance, bequest, legacy or transferred asset. |
| 📜 | `INHERITANCE` | `BENEFACTOR`      | Person granting or donating something
| 📜 | `INHERITANCE` | `BEQUEATHER`      | Legacy/Will donor  |
| 📜 | `INHERITANCE` | `BEQUEST`         | Asset specifically passed on through a will or legal instrument. Use PHRASE for detail: [item type, recipient, date] |
| 📜 | `INHERITANCE` | `CLAIMANT`        | Person claiming (or contesting) rights to the inheritance |
| 📜 | `INHERITANCE` | `CUSTODIAN`       | Person named to manage property inherited by a minor |
| 📜 | `INHERITANCE` | `DIGNITY`         | Hereditary or conferred title being passed on through inheritance. Use PHRASE for detail: [title name, rank, jurisdiction, Title holding, Style] |
| 📜 | `INHERITANCE` | `ENTAIL`          | Property bound to pass along a defined line of succession. Use PHRASE 
for detail: [property name, heir, date] |
| 📜 | `INHERITANCE` | `ENTERINGH`       | Entering heir: The person who is first in line to inherit a title, property, or estate, and whose claim cannot be superseded by the birth of another heir.
| 📜 | `INHERITANCE` | `ESTATE`          | The entire collection of assets and liabilities owned by the deceased person at the time of death. Use PHRASE for detail: [property name, heir, date] |
| 📜 | `INHERITANCE` | `EXECUTOR`        | The person executing the will (may or may not be heir). Responsible for executing a will |
| 📜 | `INHERITANCE` | `EXITINGH`        | Exiting heir: The person who is next in line to inherit a title or property, and whose right of inheritance is not subject to being defeated by the birth of a closer relative. 
| 📜 | `INHERITANCE` | `GARDIAN`         | Appointed for minor heirs |
| 📜 | `INHERITANCE` | `GRANTEE`         | One who receives a right or property |
| 📜 | `INHERITANCE` | `GRANTOR`         | Establishes trust or grants asset One who grants a right or property|
| 📜 | `INHERITANCE` | `HEIR`            | Designated recipient of legacy or estate. Inheritor, may have legal or familial tie |
| 📜 | `INHERITANCE` | `HEIRLOOM`        | An item of sentimental or historical value passed down through the family for generations.  |
| 📜 | `INHERITANCE` | `INHERITANCE`     | General term for anything received from a deceased person's estate, including both assets and liabilities.  |
| 📜 | `INHERITANCE` | `NOTARY`          | Official who legally authenticates the will, administers oaths to witnesses, and ensures proper legal formalities are followe |
| 📜 | `INHERITANCE` | `SCRIVENER`       | Historically, this was the person who physically wrote out the will, especially in times when literacy was limited. They were often legal professionals skilled in proper legal language and formatting |
| 📜 | `INHERITANCE` | `SITE`| Location where inheritance was managed or distributed.<br>Use PHRASE for detail: [law office, reading room, executor’s house] |
| 📜 | `INHERITANCE` | `TESTATOR`        | Manages property/assets on behalf of a beneficiary |
| 📜 | `INHERITANCE` | `TRUSTEE`         | The person who made the will (often the deceased) |
| ⚖️   | `JUDICIAL`     | `ARBITRATOR`    | Neutral third party appointed to resolve a dispute outside of court. Use PHRASE for detail: [mediation, dispute resolution, settlement] |
| ⚖️   | `JUDICIAL`     | `BONDSMAN`      | Provided bail or financial guarantee for release from custody. Use PHRASE for detail: [surety, bail, guarantor] |
| ⚖️   | `JUDICIAL`     | `COURTCLERK`    | Maintained legal records for the court. Use PHRASE for detail: [record keeping, docket, case files] |
| ⚖️   | `JUDICIAL`     | `DECLARANT`     | Made a declaration. Use PHRASE for detail: [statement, affidavit, deposition] [also as: LEGAL, DECLARANT — meaning: Person who made a formal statement or sworn declaration, e.g., for identity, relationship, property, or DNA test results. Use PHRASE for detail: [identity, property, age, allegiance]] |
| ⚖️   | `JUDICIAL`     | `HEARSAY`       | Mentioned indirectly by another; not a primary witness but appears by reference in a record. Use PHRASE for detail: [rumor, secondhand, indirect testimony] |
| ⚖️   | `JUDICIAL`     | `INFORMANT`     | Provided information for a record. Use PHRASE for detail: [tip, report, statement] |
| ⚖️   | `JUDICIAL`     | `INMATE`        | Person who is (involuntarily) confined or held in a prison, hospital, or other institution. Use PHRASE for detail: [prisoner, detainee, confined] |
| ⚖️   | `JUDICIAL`     | `INTERPRETER`   | Witness acting in a translation capacity. Use PHRASE for detail: [translator, language, interpreter] |
| ⚖️   | `JUDICIAL`     | `INTERVIEWER`   | Person tasked with gathering information through questioning. Use PHRASE for detail: [questioner, investigator, interviewer, police, census, journalist] |
| ⚖️   | `JUDICIAL`     | `INTERVIEWEE`   | Person providing information when questioned. Use PHRASE for detail: [respondent, suspect, source, witness] |
| ⚖️   | `JUDICIAL`     | `JUDGE`         | Rendered legal decisions. Use PHRASE for detail: [court, ruling, verdict] [also as: LEGAL, JUDGE — meaning: Legal authority who ruled or confirmed. Use PHRASE for detail: [decision, confirmation, judgment]] |
| ⚖️   | `JUDICIAL`     | `LAWENFORCEMENT`| Enforced legal orders (e.g., bailiff, constable). Use PHRASE for detail: [police, constable, sheriff] |
| ⚖️   | `JUDICIAL`     | `OBSERVER`      | Passive presence at a legal act or proceeding. Observed but did not testify. Use PHRASE for detail: [spectator, bystander, attendee] |
| ⚖️   | `JUDICIAL`     | `PLAINTIFF`     | Person seeking legal redress — recipient of court attention. Use PHRASE for detail: [complainant, claimant, petitioner] [also as: LEGAL, PLAINTIFF — meaning: Person initiating a legal case. Use PHRASE for detail: [claimant, initiator, complainant]] |
| ⚖️   | `JUDICIAL`     | `PROOF`         | Asset that proves a legal fact or event. Use PHRASE for detail: [certificate, document, evidence] |
| ⚖️   | `JUDICIAL`     | `SCRIBE`        | Person who handwrites or copies legal documents, often for record keeping. Use PHRASE for detail: [copier, transcriber, clerk] |
| ⚖️   | `JUDICIAL`     | `SIGNATORY`     | Signed something with legal/social force. Use PHRASE for detail: [contract, treaty, agreement] [also as: LEGAL, SIGNATORY — meaning: Person whose signature confirms agreement, consent, or validation. Use PHRASE for detail: [consent, agreement, validation]] |
| ⚖️ | `JUDICIAL`    | `SITE`| Legal or procedural setting linked to the act or ruling.<br>Use PHRASE for detail: [courtroom, courthouse, tribunal, notary office, justice hall. jail, prison] |
| ⚖️   | `JUDICIAL`     | `STENOGRAPHER`  | Recorded proceedings in shorthand during a legal event. Use PHRASE for detail: [court reporter, shorthand, transcript] |
| ⚖️   | `JUDICIAL`     | `WITNESS`       | Person attesting to a legal act or document. Use PHRASE for detail: [testimony, observation, affidavit] [also as: LEGAL, WITNESS — meaning: Attested to a legal act or document. Use PHRASE for detail: [legal act, signature, evidence]] |
| 🖋️ | `LEGAL`       | `ACCUSED`         | Person accused in a criminal case. Use PHRASE for detail: [accused, defendant, suspect] |
| 🖋️ | `LEGAL`       | `AGENT`           | Legal or official representative acting on behalf of another. Use PHRASE for detail: [agent, representative, proxy] |
| 🖋️ | `LEGAL`       | `ALDERMAN`        | A member of a city or town government (Dutch "Schepen"). Use PHRASE for detail: [alderman, council, town government] |
| 🖋️ | `LEGAL`       | `ATTORNEY`        | An attorney is a lawyer who has been admitted to the bar and is licensed to practice law. This includes the ability to represent clients in legal proceedings and provide legal advice. Use PHRASE for detail: lawyer, advocate, counsellor, solicitor, prosecutor, representative, counsel] |
| 🖋️ | `LEGAL`       | `BAILIFF`         | Enforcement agent. An official who takes possession of someone's property when they cannot pay their debts (Dutch "Schout"). Use PHRASE for detail: [bailiff, enforcement, property seizure] |
| 🖋️ | `LEGAL`       | `BENEFACTOR`      | Person granting or donating something. Use PHRASE for detail: [benefactor, donor, grantor] |
| 🖋️ | `LEGAL`       | `BENEFICIARY`     | Named person entitled to assets or rights through legal process (will, trust, insurance). Use PHRASE for detail: [beneficiary, heir, recipient] |
| 🖋️ | `LEGAL`       | `CLAIMANT`        | Person filing a legal claim (applicant). Use PHRASE for detail: [claimant, applicant, petitioner] |
| 🖋️ | `LEGAL`       | `CLIENT`          | Engaged legal representative. Use PHRASE for detail: [client, represented party] |
| 🖋️ | `LEGAL`       | `DEFENDANT`       | Person defending a case. Use PHRASE for detail: [defendant, accused, respondent] |
| 🖋️ | `LEGAL`       | `DEFENSE`         | Attorney, advocate, or representative acting on behalf of the accused in a legal case. Use PHRASE for detail: [defense, lawyer, counsel] |
| 🖋️ | `LEGAL`       | `EXECUTOR`        | Person executing a will. Use PHRASE for detail: [executor, estate administrator] |
| 🖋️ | `LEGAL`       | `FOREMAN`         | Designated leader or spokesperson of a jury, often responsible for delivering the verdict. Use PHRASE for detail: [jury foreman, spokesperson] |
| 🖋️ | `LEGAL`       | `GUARDIAN`        | Legal guardian or custodian for a child or adult. Use PHRASE for detail: [guardian, custodian, caregiver] |
| 🖋️ | `LEGAL`       | `HEIR`            | A person legally entitled to inherit the property or title of another person, typically after their death. Named or acknowledged as heir in will or succession. Use PHRASE for detail: [heir, successor, inheritor] |
| 🖋️ | `LEGAL`       | `INVENTORYM`      | INVENTORYMAKER — Compiles asset list (also appears in ADMIN). Use PHRASE for detail: [inventory, asset list, record keeper] |
| 🖋️ | `LEGAL`       | `ISSUER`          | The individual, organization, or entity that creates and releases the document (e.g., corporation issuing financial statements, government issuing identity documents, university issuing transcripts). Use PHRASE for detail: [issuer, creator, publisher] |
| 🖋️ | `LEGAL`       | `JURY`            | Member of the jury responsible for evaluating evidence and reaching a verdict. Legal authority who ruled or confirmed. Use PHRASE for detail: [jury, juror, verdict] |
| 🖋️ | `LEGAL`       | `LAWYER`          | Represented party in legal matters; legal representative or advocate. Use PHRASE for detail: [lawyer, advocate, counsel] |
| 🖋️ | `LEGAL`       | `NOTARY`          | A public official authorized to authenticate and certify the validity of legal documents and transactions, often involving an international element.  Use PHRASE for detail: [notary, certification, witness, powers of attorney, property transactions, including deeds and mortgages, testament, documents for: immigration; emigration; company registration; business transactions. oaths, affirmations, protests, bills of exchange] |
| 🖋️ | `LEGAL`       | `PARTY`           | Formal participant in a legal action (e.g., plaintiff, defendant). Use PHRASE for detail: [party, participant, litigant] |
| 🖋️ | `LEGAL`       | `PROBATEJUDGE`   | A judicial official who presides over legal matters related to the estates of deceased individuals, handles guardianship cases for minors or incapacitated adults. Ensure the proper administration and distribution of assets according to the will or, if there isn't one, according to state law. Use PHRASE for detail: [probate, judge, estate] |
| 🖋️ | `LEGAL`       | `PROSECUTOR`      | Legal representative or authority pursuing charges against an accused individual. Use PHRASE for detail: [prosecutor, attorney, district attorney] |
| 🖋️ | `LEGAL`       | `RECIPIENT`       | Person who received a legal document, status, or authorization — such as a license, permit, court summons, or adoption order. Use PHRASE for detail: [recipient, grantee, licensee] |
| 🖋️ | `LEGAL`       | `RULER`           | Monarch or governing authority confirming a right/title (Confirmant). Use PHRASE for detail: [ruler, monarch, confirmant] |
| 🖋️ | `LEGAL`       | `TESTATOR`        | Person whose will is recorded. Use PHRASE for detail: [testator, will, estate] |
| 🖋️ | `LEGAL`       | `VICTIM`          | Person harmed or affected by a criminal act or civil dispute; subject of the case. Use PHRASE for detail: [victim, harmed, injured party, underdog] |
| 💍 | `MARRIAGE`    | `BESTMAN`         | Witness or supporter for groom   |
| 💍 | `MARRIAGE`    | `BRIDE`           | Female partner in marriage-type event   |
| 💍 | `MARRIAGE`    | `ENGAGED`         | Betrothed or fiancée/fiancé  |
| 💍 | `MARRIAGE`    | `EX-SPOUSE`       | Previously married to the person; now separated or divorced |
| 💍 | `MARRIAGE`    | `FIANCÉ(E)`       | Engaged to be married; may not result in marriage |
| 💍 | `MARRIAGE`    | `GROOM`           | Male partner in marriage-type event   |
| 💍 | `MARRIAGE`    | `MAIDOFHONOR`     | Witness or supporter for bride   |
| 💍 | `MARRIAGE`    | `MARRIAGE-WITNESS`| Someone witnessing the marriage, e.g. best man       |
| 💍 | `MARRIAGE`    | `OFFICIANT`       | Person leading the ceremony                         |
| 💍 | `MARRIAGE`    | `PARTNER`         | Unmarried long-term partner, registered or informal. Or one of the marrying persons                                          |
| 💍 | `MARRIAGE`    | `SPOUSE`          | Married partner, legally recognized. Used where sex or role is unspecified or later in life |
| 💍 | `MARRIAGE`    | `WITNESS`         | Witnesses signing or present at marriage                          |
| 🎞️ | `MEDIA`       | `ARCHIVE`         | Media stored as part of a permanent collection. Use PHRASE for detail: [archive name, location, reference code] |
| 🎞️ | `MEDIA`       | `AUTHOR`          | Wrote accompanying text, article, caption, or media description |
| 🎞️ | `MEDIA`       | `COPYRIGHT`       | Media holding copyright status. Use PHRASE for detail: [copyright holder, jurisdiction, term] |
| 🎞️ | `MEDIA`       | `CURATOR`         | Organized or selected items for publication/exhibit |
| 🎞️ | `MEDIA`       | `EDITOR`          | Reviewed or prepared content for publication or release |
| 🎞️ | `MEDIA`       | `ILLUSTRATOR`     | Visual artist or designer of the media object (e.g. sketch, diagram, enhancement) |
| 🎞️ | `MEDIA`       | `INTERVIEWEE`     | Provided personal answers or narrative used in the media content |
| 🎞️ | `MEDIA`       | `MENTIONED`       | Referenced inside the media                          |
| 🎞️ | `MEDIA`       | `PHOTOGRAPHER`    | Took or captured the photo or visual image |
| 🎞️ | `MEDIA`       | `PUBLISHER`       | Released, printed, or distributed the media item |
| 🎞️ | `MEDIA`       | `SIGNATORY`       | Signed a text or formal communication (can differ from author) |
| 🎞️ | `MEDIA`       | `SITE`| Creative or performance environment tied to recording or presentation.<br>Use PHRASE for detail: [studio, concert hall, sound booth, stage, newsroom, gallery, concert hall] |
| 🎞️ | `MEDIA`       | `SOURCE`          | Provided original information, artifacts, or stories used in the media  |
| 🎞️ | `MEDIA`       | `SOURCEITEM`      | Physical or digital media serving as the primary source for information. Use PHRASE for detail: [media type, origin, date] |
| 🎞️ | `MEDIA`       | `SUBJECT`         | Subject of the image, article, or portrayal (e.g., in photo, portrait or article, named in piece)|
| 🎞️ | `MEDIA`       | `TRANSLATOR`      | Translator involved                                                   |
| 🩺 | `MEDICAL`     | `CORONER`         | Investigated death                   |
| 🩺 | `MEDICAL`     | `DOCTOR`          | Provided medical care (Physician or healer)     |
| 🩺 | `MEDICAL`     | `MIDWIFE`         | Assisted in childbirth               |
| 🩺 | `MEDICAL`     | `NURSE`           | Assisted medical care                |
| 🩺 | `MEDICAL`     | `PATIENT`         | Received medical care or diagnosis |
| 🩺 | `MEDICAL`     | `PRACTITIONER`    | Gave medical care; doctor, nurse, healer |
| 🩺 | `MEDICAL`     | `REPORTER`       | Person filing a medical report   |
| 🩺 | `MEDICAL`     | `SITE`| Medical setting tied to diagnosis, care, or treatment.<br>Use PHRASE for detail: [hospital, clinic, infirmary, sanatorium, ER, maternity ward, surgery room] |
| 🪖 | `MILITARY`    | `CASUALTY`       | Person who is wounded, missing, killed  |
| 🪖 | `MILITARY`    | `COMMANDER`      | Leader (Officer) of group or unit; may be temporary |
| 🪖 | `MILITARY`    | `CONSCRIPT`      | Drafted into service; may include limited service duration |
| 🪖 | `MILITARY`    | `ENLISTED`       | Non-officer member of military (e.g. private, corporal) Signed up for military service |
| 🪖 | `MILITARY`    | `OFFICER`        | Held formal military role; rank may be known |
| 🪖 | `MILITARY`    | `RECIPIENT`      | Person awarded a medal, rank insignia, commendation, or military honor. |
| 🪖 | `MILITARY`    | `RECRUITOR`      | Recruits others |
| 🪖 | `MILITARY`    | `SITE`| Locations of military relevance or deployment.<br>Use PHRASE for detail: [barracks, base, fort, battlefield, warzone, military camp, trench] |
| 🪖 | `MILITARY`    | `SOLDIER`        | Member of armed forces] [Any enlisted person]               |
| 🪖 | `MILITARY`    | `SUPPORT`        | Logistics, admin, medical support                    |
| 🪖 | `MILITARY`    | `VETERAN`        | Former soldier or combatant (Served previously), often linked to pension or memorial |
| 🪖 | `MILITARY`    | `VICTIM`         | Civilian or soldier harmed or killed      |
| 📜 | `OFFICIAL`    | `CONSUL`         | Consul or diplomatic agent           |
| 📜 | `OFFICIAL`    | `MAYOR`          | Mayor                                |
| 📜 | `OFFICIAL`    | `NOTARY`         | Notary or legal recorder             |
| 📜 | `OFFICIAL`    | `OFFICER`        | Generic official                     |
| 📜 | `OFFICIAL`    | `PROCLAMATION`   | Document or object formally declaring an action or status. Use PHRASE for detail: [topic, issuing body, date] |
| 📜 | `OFFICIAL`    | `REGISTRAR`      | Civil registrar (issuer)   |
| 📜 | `OFFICIAL`    | `SCRIBE`         | Official writer or record keeper     |
| 📜 | `OFFICIAL`    | `SEAL`           | Physical seal or emblem representing authority. Use PHRASE for detail: [seal type, issuing body, date] |
| 📜 | `OFFICIAL`    | `SITE`| Government or civil authority locations.<br>Use PHRASE for detail: [municipality, passport bureau, city hall, records office, agency, consulate] |
| 🏘️ | `PROPERTY`    | `AGENT`          | Real estate agent or similar mediator                      |
| 🏘️ | `PROPERTY`    | `BUILDER`        | Architect, builder, or renovator                 |
| 🏘️ | `PROPERTY`    | `BUYER`          | Purchased the property. (Buyer in a transaction) Party purchasing or receiving ownership  |
| 🏘️ | `PROPERTY`    | `DESTINATION`    | Location where an event or journey ends. Use PHRASE for detail: [event, location, date] |
| 🏘️ | `PROPERTY`    | `GUEST`          | Temporary occupant or visitor              |
| 🏘️ | `PROPERTY`    | `HOLDING`        | Property owned or controlled as part of an estate or organization. Use PHRASE for detail: [owner, type, location] |
| 🏘️ | `PROPERTY`    | `LESSOR`         | a person who leases or lets a property to another; a landlord. |
| 🏘️ | `PROPERTY`    | `LESSEE`         | a person who holds the lease of a property; a tenant.             |
| 🏘️ | `PROPERTY`    | `OWNER`          | Person or group who owns the property (Landowner or leaseholder) (legal or practical owner) |
| 🏘️ | `PROPERTY`    | `OCCUPANT`       | Current inhabitant of a property  |
| 🏘️ | `PROPERTY`    | `ORIGIN`         | Location where an event or journey begins. Use PHRASE for detail: [event, location, date] |
| 🏘️ | `PROPERTY`    | `RECORDED-BY`    | Someone listing or describing the property/asset (e.g. inventoried it)        |
| 🏘️ | `PROPERTY`    | `RESIDENT`       | Lives on the property (house, farm, etc.)           |
| 🏘️ | `PROPERTY`    | `SCENE`          | Location where a notable event occurred. Use PHRASE for detail: [event type, location, date] |
| 🏘️ | `PROPERTY`    | `SELLER`         | Sold the property. (Seller in a transaction) Party selling or transferring ownership |
| 🏘️ | `PROPERTY`    | `SITE`| Physical site associated with land, ownership, or property transfer.<br>Use PHRASE for detail: [farm, estate, parcel, homestead, land tract, dwelling] |
| 🏘️ | `PROPERTY`    | `TENANT`         | Has use or lease of the property without owning |
| 🏘️ | `PROPERTY`    | `VENUE`          | Property used as the location for an event. Use PHRASE for detail: [event type, location, date] |
| 🏘️ | `PROPERTY`    | `WITNESS`        | Attested to the transaction involving property |
| 🏘️ | `PROPERTY`    | `WORKER`         | Employed or active on the property (farmer, tenant, servant) 
| ✝️ | `RELIGIOUS`   | `BELIEVER`       | Identified with the religion but not formally initiated. <br>Use PHRASE for detail: [faith, layperson, religion, affiliation] |
| ✝️ | `RELIGIOUS`   | `CATECHUMEN`     | Unbaptized person receiving instruction before entry into the faith. <br>Use PHRASE for detail: [catechism, instruction, baptism, preparation] |
| ✝️ | `RELIGIOUS`   | `CELEBRANT`      | Person who performs a rite, especially a priest at the Eucharist. <br>Use PHRASE for detail: [mass, eucharist, rite, officiant] |
| ✝️ | `RELIGIOUS`   | `CLERGY`         | Religious official in event; implies OFFICIATOR. General role for priest, pastor, monk, etc. <br>Use PHRASE for detail: [priest, minister, pastor, officiant] |
| ✝️ | `RELIGIOUS`   | `COMMUNICANT`    | Recipient of communion. <br>Use PHRASE for detail: [eucharist, sacrament, mass, recipient] |
| ✝️ | `RELIGIOUS`   | `CONFIRMEE`      | A person who is receiving the religious sacrament of confirmation. <br>Use PHRASE for detail: [confirmation, rite, sacrament, initiation] |
| ✝️ | `RELIGIOUS`   | `CONFSPONSOR`    | (Confirmation sponsor) Guided initiate through rite of passage. <br>Use PHRASE for detail: [confirmation, sponsor, spiritual guide, mentor] |
| ✝️ | `RELIGIOUS`   | `CONVERT`        | Adopted the religion, often in a ritual or noted event. <br>Use PHRASE for detail: [conversion, faith change, baptism, religious shift] |
| ✝️ | `RELIGIOUS`   | `DEACON`         | Ordained assistant below priest; helps in services.Is in the final stage to become a priest<br>Use PHRASE for detail: [assistant clergy, liturgy, transitional, church] |
| ✝️ | `RELIGIOUS`   | `EXPELLED`       | Excommunicated, renounced, banished, or excluded from Church fellowship. <br>Use PHRASE for detail: [excommunicated, shunned, disfellowshipped, renounced] |
| ✝️ | `RELIGIOUS`   | `GODPARENT`      | Named sponsor in baptism or confirmation. <br>Use PHRASE for detail: [baptism, godmother, godfather, sponsor, witness] |
| ✝️ | `RELIGIOUS`   | `IMAM`           | Muslim religious leader. <br>Use PHRASE for detail: [mosque, islamic cleric, friday prayer] |
| ✝️ | `RELIGIOUS`   | `INITIATE`       | Recipient of religious rite or spiritual inclusion. <br>Use PHRASE for detail: [baptism, entry, vows, inclusion, rite] |
| ✝️ | `RELIGIOUS`   | `MINISTER`       | Religious minister. <br>Use PHRASE for detail: [pastor, church leader, protestant, service] |
| ✝️ | `RELIGIOUS`   | `MONK`           | Monastic religious figure. <br>Use PHRASE for detail: [abbey, cloister, vows, friar, monastic] |
| ✝️ | `RELIGIOUS`   | `NOVICE`         | Person in early stage of religious life, not yet fully vowed or ordained. <br>Use PHRASE for detail: [initiate, training, probation, monastery] |
| ✝️ | `RELIGIOUS`   | `NUN`            | Female monastic. <br>Use PHRASE for detail: [convent, sister, habit, cloister, vows] |
| ✝️ | `RELIGIOUS`   | `OFFICIANT`      | Performed a religious function (e.g. marriage, baptism). <br>Use PHRASE for detail: [marriage, baptism, religious duty, clergy] |
| ✝️ | `RELIGIOUS`   | `ORDAINER`       | Someone who has the right to ordain deacons and others. <br>Use PHRASE for detail: [ordination, bishop, authority, consecrate] |
| ✝️ | `RELIGIOUS`   | `PASTOR`         | Pastor or church leader. <br>Use PHRASE for detail: [preacher, leader, service, congregation] |
| ✝️ | `RELIGIOUS`   | `PRIEST`         | Religious officiant or cleric. <br>Use PHRASE for detail: [mass, church, clergy, ordination] |
| ✝️ | `RELIGIOUS`   | `RABBI`          | Jewish religious leader. <br>Use PHRASE for detail: [synagogue, torah, teacher, sermon] |
| ✝️ | `RELIGIOUS`   | `REVEREND`       | A person who is ordained (to a diocese). <br>Use PHRASE for detail: [ordination, bishop, pastor, deacon, Father, vicar, rector, church] |
| ✝️ | `RELIGIOUS`   | `SITE`| Sacred or religious building where a rite or ceremony was held.<br>Use PHRASE for detail: [church, temple, mosque, monastery, cloister, convent, chapel, sanctuary] |
| ✝️ | `RELIGIOUS`   | `SUPERIOR`       | Monastic or religious leader of a community (male or female). Use PHRASE for detail: [abbot, abbess, prior, prioress, mother superior, convent leader, monastic head, cloister] |
| ✝️ | `RELIGIOUS`   | `VOW`            | Made a solemn promise or commitment in a religious context. <br>Use PHRASE for detail: [monastic, commitment, oath, devotion] |
| ✝️ | `RELIGIOUS`   | `WITNESS`        | For example, godparent or spiritual sponsor. <br>Use PHRASE for detail: [witness, sponsor, ceremony, signature] |
| 🌐 | `SOCIAL`      | `ATTENDEE`      | Person present at a ceremony, unveiling, memorial event    |
| 🌐 | `SOCIAL`      | `AUDIENCE`      | Present at the event    |
| 🌐 | `SOCIAL`      | `COWORKER`      | Participated in joint task or work; not hierarchical |
| 🌐 | `SOCIAL`      | `DEDICATOR`     | Person who organized or dedicated the memorial    |
| 🌐 | `SOCIAL`      | `ENSLAVER`      | Person who held others in involuntary servitude or bondage. |
| 🌐 | `SOCIAL`      | `GUEST`         | Attended or featured at the event |
| 🌐 | `SOCIAL`      | `HONOREE`       | [The person being commemorated (e.g. on a gravestone or memorial)]  [Person being honored in a tribute event]|
| 🌐 | `SOCIAL`      | `HOST`          | Gave the party, reception, or event |
| 🌐 | `SOCIAL`      | `INSCRIBED`     | Person named in writing, e.g. on a war memorial      |
| 🌐 | `SOCIAL`      | `MENTOR`        | Guided or advised another; includes apprenticeships |
| 🌐 | `SOCIAL`      | `PARTICIPANT`   | Present in public or semi-public event marking something, e.g. parade, unveiling |
| 🌐 | `SOCIAL`      | `REPRESENTATIVE`| Portrayed or represented another person, usually in a theatrical or ceremonial setting. |
| 🌐 | `SOCIAL`      | `SITE`| Setting of public or private gatherings and social events.<br>Use PHRASE for detail: [ballroom, village square, party tent, pub, dining hall, cinema] |
| 🌐 | `SOCIAL`      | `SLAVE`         | Person held in bondage or forced labor; property of another. |
| 🌐 | `SOCIAL`      | `SPEAKER`       | Person giving a speech                                             |
| 🌐 | `SOCIAL`      | `SUBJECT`       | The person being remembered (e.g. named on grave or monument)             |
| 🌐 | `SOCIAL`      | `TARGET`        | Person being commemorated (e.g. war dead, founder, jubilee) |
| 🌐 | `SOCIAL`      | `TITLED`        | Holder of a hereditary or civic title (e.g., baron, alderman, viscount). Reflects social rank or status. |
| 🌀 | `OTHER`       | `OTHER`         | Role not yet categorized or too vague;  Must include a `PHRASE` |


