
### `g8:enumset-EVENT-TYPE` 

Each `TEMPLATE` must declare a `TYPE`. These are the main categories of life events, legal actions, affiliations, or other documented situations that a template can represent.

| ICO | TYPE         | Description |
|--|----------------|-------------|
| 👶 | `CHILD`     | Births, baptisms, christenings, adoptions, foundlings — any record focused on the appearance of a child. |
| 🏛️ | `CIVIL`     | State or municipal processes like registrations, citizen declarations, civic permits, or local obligations. May include stepchild declarations or civil status. |
| ⚰️ | `DEATH`     | Deaths, burials, funerals, probates, wills, and related documents marking the end of life or its aftermath. |
| 📚 | `EDUCATIONAL` | Records of schooling, degrees, apprenticeships, certifications, or academic achievements. |
| 👨‍👩‍👧 | `FAMILY`    | Marriages, banns, divorces, separations, engagements, and formal unions — plus notices, contracts, and filings. |
| 🛡️ | `GROUP`     | Membership or interaction with a social group, clan, caste, tribe, guild, political body, or religious sect. Often includes joining, exiting, or holding a position. |
| 🪪 | `IDENTITY`  | DNA, Name changes, nationalities, IDs, passports, or any documentation of personal or cultural identity. |
| 🖋️ | `LEGAL`     | Legal or judicial documents: trials, court rulings, testimonies, lawsuits, licenses, contracts, etc. |
| 🎞️ | `MEDIA`     | Items with genealogical value that appear in print or media — photos, articles, portraits, posters, publications. |
| 🩺 | `MEDICAL`    | Health-related documents such as illness reports, surgeries, hospitalizations, autopsies, and DNA summaries. |
| 🕯️ | `MEMORIAL`  | Posthumous recognitions: gravestones, obituaries, memorial plaques, funeral cards, digital tributes. |
| ✈️ | `MIGRATION` | Moves, emigrations, immigration, travel, arrival/departure, border crossings, visas, ship manifests. |
| 🪖 | `MILITARY`  | Enlistment, service records, deployment, draft, pensions, weapons, awards, discharges, and military tribunals. |
| 🏗️ | `OCCUPATIONAL` | Employment, trades, job titles, licenses, guild activity, or professional qualifications. |
| 🛍️ | `PERSONAL`  | Biographical or introspective records: diaries, autobiographies, statements, or personal descriptions. |
| 🏘️ | `PROPERTY`  | Property deeds, transfers, ownership, inventory lists, estate sales, or asset-related events. |
| ✝️ | `RELIGIOUS` | Baptisms, confirmations, ordinations, blessings, LDS-specific ordinances, or ritual ceremonies. |
| ⚓ | `RESIDENCE` | Addresses, housing, relocation records, census entries showing place of living. |
| 📚 | `SECONDARY` | Published or culturally transmitted sources that interpret, compile, retell, or reflect on primary events. Includes oral tradition, family lore, books, and inferred information not derived from direct evidence.|
| 🌐 | `SOCIAL`    | Club memberships, community roles, awards, honors, participation in events or social recognition. |
| 🌈 | `STATUSCHANGE` | Namechange, naturalization, graduation, enslavement, retirement, discharge, elected etc |
| 🌀 | `OTHER`     | Any event type not captured above. A `PHRASE` field must be used to clarify the event. |

### `g8:enumset-EVENT-SUBTYPE`

Each `TEMPLATE` of a given `TYPE` must also specify a more specific `SUBTYPE` to better describe the nature of the event or record. These subtypes help clarify the function, format, or context of the template, especially for complex or recurring categories.  
Both, `TYPE` and `SUBTYPE` must be mentioned. So for instance;  
`TYPE CHILD, BIRTH`

## In the below table, correct filling of the column `TAG` is not finished

| ICO |  `TYPE` |  `SUBTYPE`       |  Description | TAG |
|---|-------------|------------------|----------------|--|
| 👶 | `CHILD`   | `ABORTION`    | Intentional termination of pregnancy, typically elective and legally recorded. |  |
| 👶 | `CHILD`   | `ADOPTION`    | Legal process in which a person becomes the child of someone other than their biological parent. |  |
| 👶 | `CHILD`   | `BIRTH`       | Documented birth of a person, typically via a certificate, registry, or hospital record. |  |
| 👶 | `CHILD`   | `BIRTHNOTICE` | Public or official announcement of birth, such as in a newspaper or church bulletin. |  |
| 👶 | `CHILD`   | `CHRISTENING` | Religious naming or infant baptism shortly after birth. Use `ADULTCHRISTENING` for later-life ceremonies. |  |
| 👶 | `CHILD`   | `CONCEPTION`  | Documented or estimated date of conception (e.g., in fertility cases or religious contexts). |  |
| 👶 | `CHILD`   | `FOUNDLING`   | Abandoned infant with unknown parents, typically documented by a parish, orphanage, or municipal office. Distinct from standard birth registration. |  |
| 👶 | `CHILD`   | `GUARDIANSHIP`| Assignment or change of legal guardianship for a minor, distinct from adoption. May appear in court or municipal records. |  |
| 👶 | `CHILD`   | `MISCARRIAGE` | Spontaneous loss of a pregnancy before viability; not a stillbirth. |  |
| 👶 | `CHILD`   | `MULTIPLE`    | Indicates birth as part of a multiple (twin, triplet, etc.) set. May appear on certificates or medical files. |  |
| 👶 | `CHILD`   | `RECOGNITION` | Legal or social acknowledgment of parentage by one or both parents, often retroactive. |  |
| 👶 | `CHILD`   | `STEPCHILD`   | Declaration or recognition of a stepchild within a family context. Not a birth or adoption — often noted at marriage or legal guardianship. |  |
| 👶 | `CHILD`   | `STILLBIRTH`  | Non-viable birth recorded officially; child did not survive birth. |  |
| 👶 | `CHILD`   | `SURROGACY`   | Child born via a surrogate; may be recorded in medical, legal, or contractual documents. Modern but increasingly present. |  |
| 👶 | `CHILD`   | `OTHER`       | Child-related event not captured by other subtypes. Use with caution and consider context-specific naming. Must use PHRASE to clarify. |  |
| 🏛️ | `CIVIL`   | `APPOINTMENT` | Official assignment to a civil position, post, or government office. |  |
| 🏛️ | `CIVIL`   | `CITATION`    | Official warning or minor civil penalty, such as traffic or public order citations. Can appear in administrative registries. |  |
| 🏛️ | `CIVIL`   | `COMMISSION`  | Formal grant of power or responsibility, such as to a military or civic commission. |  |
| 🏛️ | `CIVIL`   | `LICENSE`     | Granting of official permits for business, firearms, vehicles, or other regulated rights, excluding marriage. |  |
| 🏛️ | `CIVIL`   | `NOMINATION`  | Named as candidate for honor, election, or position. May not result in appointment. |  |
| 🏛️ | `CIVIL`   | `OATH`        | Oath of service or office — common for judges, civil servants, mayors. May include pledges of allegiance or public duty. |  |
| 🏛️ | `CIVIL`   | `RECALL`      | Removed from civil office by authority or process, such as a vote or decree. |  |
| 🏛️ | `CIVIL`   | `RESIGNATION` | Formal withdrawal from public or civil office, often documented with date and role. May appear in council or personnel registers. |  |
| 🏛️ | `CIVIL`   | `OTHER`       | Other civil events or appointments not described by specific subtypes. Must use PHRASE to clarify. |  |
| ⚰️ | `DEATH` | `BURIAL` | Disposition of remains after death. |  |
| ⚰️ | `DEATH` | `CREMATION` | A cremation event. Burning of remains after death. |  |
| ⚰️ | `DEATH` | `DEATH` | A death event. Record of life termination. |  |
| ⚰️ | `DEATH` | `DEATHNOTICE` | Formal or public announcement of death. |  |
| ⚰️ | `DEATH` | `DISAPPEARED` | Unresolved or unexplained vanishing of a person. May or may not involve presumed death. |  |
| ⚰️ | `DEATH` | `DISINTERMENT` | Exhumation or removal of remains after initial burial. |  |
| ⚰️ | `DEATH` | `ENTOMBMENT` | Burial in a tomb or mausoleum. Alternative to in-ground burial. |  |
| ⚰️ | `DEATH` | `FUNERAL` | A funeral event. Ceremony held after death, often associated with burial or memorial. |  |
| ⚰️ | `DEATH` | `FUNERALNOTICE` | Notification or announcement of a funeral service. |  |
| ⚰️ | `DEATH` | `INQUEST` | Legal investigation into the cause or circumstances of a death. Often conducted when suspicious. |  |
| ⚰️ | `DEATH` | `INURNMENT` | Placement of cremated remains into an urn. |  |
| ⚰️ | `DEATH` | `LOST` | Person or remains never found or recovered. May involve presumed death. |  |
| ⚰️ | `DEATH` | `OBITUARY` | Public death announcement, often in a newspaper. Summary of life and passing. |  |
| ⚰️ | `DEATH` | `PROBATE` | Granting of legal authority over a deceased person's estate. |  |
| ⚰️ | `DEATH` | `PROBATENOTICE` | Public notice of pending or granted probate action. |  |
| ⚰️ | `DEATH` | `WILL` | Legal will or testament. Creation, registration, or execution of final wishes, including inheritance of property, titles, and symbolic assets. Use STICKYs and TRANSFER to model specific elements. |  |
| ⚰️ | `DEATH` | `YAHRZEIT` | Anniversary of death on the Hebrew calendar. Jewish memorial tradition. |  |
| ⚰️ | `DEATH` | `OTHER` | Death-related events not covered by other subtypes. May include alternative customs or unknown disposition. |  |
 📚| `EDUCATIONAL` | `AWARD` | A recognition of academic achievement, merit, or service. Includes honors, prizes, or scholarships. |  |
 📚| `EDUCATIONAL` | `ACHIEVEMENT` | Educational achievement such as a diploma, graduation, or scholarship. |  |
 📚| `EDUCATIONAL` | `APPRENTICESHIP` | Structured skill-learning program under supervision. Often trade-based. |  |
 📚| `EDUCATIONAL` | `CERTIFICATE` | Completion of a formal course or professional training resulting in certification. |  |
 📚| `EDUCATIONAL` | `ENROLLMENT` | Enrollment in an educational institution or program. Includes first-time enrollment or reenrollment. |  |
 📚| `EDUCATIONAL` | `OTHER` | Educational events not covered elsewhere. May include exams, field schools, or informal learning. |  |
| 👨‍👩‍👧 | `FAMILY` | `ANNIVERSARY` | Published notice or event commemorating a couple's marriage anniversary. |  |
| 👨‍👩‍👧 | `FAMILY` | `ANNULMENT` | Formal annulment of a marriage. Declares marriage legally void. |  |
| 👨‍👩‍👧 | `FAMILY` | `BREAKUP` | The termination of a domestic partnership or civil union, without formal divorce. (Parthership dissolution) | DIV |
| 👨‍👩‍👧 | `FAMILY` | `CENSUS` | Census entry listing household or family members. Overlaps with RESIDENCE. | CENS |
| 👨‍👩‍👧 | `FAMILY` | `CIVILUNION` | Legal civil union. Recognized partnership without the title of marriage. |  |
| 👨‍👩‍👧 | `FAMILY` | `CLMARRIAGE` | Non-ceremonial marital union (Common-law marriage). Recognized marriage through cohabitation or time. |  |
| 👨‍👩‍👧 | `FAMILY` | `COHABITATION` | Two people living together in a long-term relationship without formal marriage. May appear in housing records or census. |  |
| 👨‍👩‍👧 | `FAMILY` | `DIVORCE` | Dissolution of a marriage. Legal termination of spousal relationship. | DIV |
| 👨‍👩‍👧 | `FAMILY` | `DIVORCEFILING` | Filing for divorce. Legal beginning of divorce proceedings. | DIVF |
| 👨‍👩‍👧 | `FAMILY` | `ENGAGEMENT` | Formal declaration or promise to marry. | ENGA |
| 👨‍👩‍👧 | `FAMILY` | `ENG_NOTICE` | Public or formal announcement of engagement. | ENGA |
| 👨‍👩‍👧 | `FAMILY` | `MARRIAGE` | Marriage event. Legal or religious union of two people. | MARR |
| 👨‍👩‍👧 | `FAMILY` | `MARRIAGEBANNS` | Public proclamation of intended marriage, often in religious context. | MARB |
| 👨‍👩‍👧 | `FAMILY` | `MARRIAGECONTRACT` | Legal or religious agreement detailing terms of marriage. | MARC |
| 👨‍👩‍👧 | `FAMILY` | `MARRIAGELICENSE` | Government-issued license permitting a marriage. | MARL |
| 👨‍👩‍👧 | `FAMILY` | `MARRIAGENOTICE` | Public announcement or posting of intended marriage. |  |
| 👨‍👩‍👧 | `FAMILY` | `PARTNERSHIP` | Partnership or cohabiting couple without formal marriage. (domestic partnership) |  |
| 👨‍👩‍👧 | `FAMILY` | `RECONCILIATION` | Formal or informal event where a previously separated couple resumes their relationship. |  |
| 👨‍👩‍👧 | `FAMILY` | `SEPARATION` | Marital or partnership separation, with or without legal divorce. | DIV |
| 👨‍👩‍👧 | `FAMILY` | `OTHER` | Family-related events not covered by other subtypes. Could include legal status changes, failed engagements, or partnership revisions. |  |
| 🛡️ | `GROUP` | `CASTE-MEM`   | Membership in a caste or hereditary status group. Typically cultural or social in nature. Examples: caste registry, census caste column, social classification roll. |  |
| 🛡️ | `GROUP` | `CHARTER`     | Founding or regulatory document of a group. Examples: charter, constitution, covenant, manifesto, founding deed, bylaws, articles of association, guild registration. |  |
| 🛡️ | `GROUP` | `CLAN-MEM`    | Cultural or lineage-based group affiliation. Examples: clan registers, ancestral rolls, kinship group entries, family branch listings. |  |
| 🛡️ | `GROUP` | `DISSOLUTION` | Official end of a society, guild, or group. Examples: dissolution decree, registry closure, church deconsecration, guild disbandment notice. |  |
| 🛡️ | `GROUP` | `ENTERING`    | Entry into a group or affiliation. Examples: guild enrollment forms, monastery entry scrolls, union admission certificates (military unit), sworn brotherhood oaths. |  |
| 🛡️ | `GROUP` | `EXITING`     | Voluntary or forced departure from a group or affiliation. Examples: retirement, expulsion notice, resignation letter, excommunication decree, discharge record. |  |
| 🛡️ | `GROUP` | `FARM-MEM`    | Membership or registration in a farming community or co-op. Examples: farm roll, land-allocation list, peasant commune register, rural collective record. |  |
| 🛡️ | `GROUP` | `GROUP-MEM`   | Generic group or community not covered elsewhere. Examples: club rosters, association cards, lodge directories, union lists, social fellowship rolls. |  |
| 🛡️ | `GROUP` | `GUILD-MEM`   | Individual’s registration or certification from a guild. Examples: apprenticeship contract, membership scroll, guild stamp, journeyman’s certificate. |  |
| 🛡️ | `GROUP` | `HEIR`        | Named as a successor or group-designated inheritor. Often part of tribal, guild, or clan succession. Examples: tribal succession listing, guild inheritance certificate, heirship nomination scroll. |  |
| 🛡️ | `GROUP` | `INITIATION`  | Ritual or formal process of acceptance into a group. Examples: initiation rite record, lodge oath, bar mitzvah certificate, religious conversion form, apprentice entry document. |  |
| 🛡️ | `GROUP` | `MEMBERSHIP`  | Proof of joining or belonging to a group. Examples: membership card, congregation register, enrollment ledger, tribal roll, church book, scout registration. |  |
| 🛡️ | `GROUP` | `OTHER`       | Other affiliation-related event not captured elsewhere. Use a `PHRASE` to clarify nature or context of the record. |  |
| 🛡️ | `GROUP` | `PARTICIPATION` | Documentation of involvement in group activity. Examples: minutes of meetings, group event roll, attendance sheet, committee participation form. |  |
| 🛡️ | `GROUP`  | `PLACE`     | Indicates the person's rank or role within the group (e.g., `LEADER`, `FOUNDER`, `HONORARY`, `REPRESENTATIVE`, ). Use `ROLE` to specify. |  |
| 🛡️ | `GROUP` | `REJOINING`   | Re-entering a group after prior departure. Often includes a formal readmission process. Examples: reinitiation scroll, renewed union card, second guild entry, readmission petition. |  |
| 🛡️ | `GROUP` | `ROLE`        | Indicates the person's role, title or rank in the group. Examples: appointment letter, leadership decree, founder acknowledgment, honorary membership plaque. Use `ROLE` structure to specify. |  |
| 🛡️ | `GROUP` | `SECT-MEM`    | Religious subgroup affiliation. a sect or division within a larger religious tradition. Examples: sect registry, church division listing, doctrinal certificate, sect enrollment form, ordination certificate. |  |
| 🛡️ | `GROUP` | `SUSPENSION`  | Temporary removal or inactive status in the group. Examples: disciplinary letter, suspended union card, guild inactivity notice. |  |
| 🛡️ | `GROUP` | `TRIBE-MEM`   | Documented link to an ethnic or tribal group. Examples: tribal enrollment, census appearance, group register, tribal land allocation, kinship confirmation letter. |  |
| 🪪 | `IDENTITY` | `ALIAS` | A declared alternative or assumed name used by the individual. May appear on official documents, employment, or residence records. |  |
| 🪪 | `IDENTITY` | `BLOODTYPE`   | Stated or documented blood type (e.g., on IDs or medical certificates). |  |
| 🪪 | `IDENTITY` | `CITIZENSHIP` | Legal belonging to a nation or state. Right to participate in civic life. |  |
| 🪪 | `IDENTITY` | `DNATEST`     | Certified or formally reported DNA results used in official identity resolution. |  |
| 🪪 | `IDENTITY` | `ETHNICITY` | Stated or documented cultural, ethnic, or racial identity. |  |
| 🪪 | `IDENTITY` | `GENDERMARKER` | Declared or legal gender marker as recorded on an official document. Can be relevant in transitions, adoptions, or mismatches. |  |
| 🪪 | `IDENTITY` | `IDENTITY` | General identification record. Could include identity cards or papers. |  |
| 🪪 | `IDENTITY` | `NAMECHANGE` | Legal name change or declaration of a new identity. Could include marriage-related name changes, adoption, or witness protection. |  |
| 🪪 | `IDENTITY` | `NATIONALID` | Government-issued national identification number. |  |
| 🪪 | `IDENTITY` | `NATIONALITY` | Declared or assigned national affiliation. |  |
| 🪪 | `IDENTITY` | `PASSPORT` | Issuance or use of a passport or travel document. |  |
| 🪪 | `IDENTITY` | `RESIDENCYPERM` | Official record granting permission to live in a certain country or region, "residency permission" (e.g., visa, green card). |  |
| 🪪 | `IDENTITY` | `OTHER` | Identity-related events or documents not otherwise categorized. Examples: alias, name corrections, or biometric records. |  |
| 🖋️ | `LEGAL` | `ARREST`           | Detainment by legal authorities. Legal event of being taken into custody. |  |
| 🖋️ | `LEGAL` | `BANKRUPTCY`       | Legal declaration of insolvency. |  |
| 🖋️ | `LEGAL` | `CONTRACT`         | Legal agreement between parties. |  |
| 🖋️ | `LEGAL` | `COURT`            | Appearance of a person in a court proceeding. Legal court appearance or judicial hearing. |  |
| 🖋️ | `LEGAL` | `CUSTODIANSHIP`    | Legal or informal designation of someone to care for another. |  |
| 🖋️ | `LEGAL` | `DEPOSITION`       | Sworn statement or pre-trial testimony. |  |
| 🖋️ | `LEGAL` | `ESTATESALE`       | Sale of property from a deceased person’s estate. |  |
| 🖋️ | `LEGAL` | `GUARDIANSHIP`     | Legal responsibility or authority over another individual. |  |
| 🖋️ | `LEGAL` | `IMPEACHMENT`      | Formal charges brought against a public official. |  |
| 🖋️ | `LEGAL` | `INDENTURE`        | Binding contract, typically for labor or service, often historical. |  |
| 🖋️ | `LEGAL` | `JUDGMENT`         | Court ruling or final legal decision. |  |
| 🖋️ | `LEGAL` | `LAWSUIT`          | Legal dispute or case involving a person. |  |
| 🖋️ | `LEGAL` | `LICENSE`          | Document granting permission (e.g., business, weapon, marriage). |  |
| 🖋️ | `LEGAL` | `PARDON`           | Formal legal forgiveness; distinct from amnesty. |  |
| 🖋️ | `LEGAL` | `PROBATION`        | Conditional release with legal supervision. |  |
| 🖋️ | `LEGAL` | `REGISTRATION`     | Official recording or certification of a legal event. |  |
| 🖋️ | `LEGAL` | `TESTIMONY`        | Eyewitness account or formal statement given under oath. |  |
| 🖋️ | `LEGAL` | `TRANSCRIPT`       | Verbatim record or full copy of legal proceedings. |  |
| 🖋️ | `LEGAL` | `TRANSFER`         | Legal shift in possession, rights, or custody of an item or person. |  |
| 🖋️ | `LEGAL` | `TRIAL`            | Judicial examination of facts and law. |  |
| 🖋️ | `LEGAL` | `OTHER`            | Any other legal document; should include a PHRASE to explain specifics. |  |
| 🎞️ | `MEDIA`    | `AUDIO`               | Oral or musical source passed down without formal recording. |  |
| 🎞️ | `MEDIA`    | `AUDIOVISUAL` | Combined audio and video material (e.g., recordings, family movies, interviews on tape). |  |
| 🎞️ | `MEDIA`    | `BOOK`                | Book excerpt or citation relevant to genealogical events or people. |  |
| 🎞️ | `MEDIA`    | `EXHIBIT` | Museum or public display item with genealogical or historical relevance (e.g., exhibit placards, curated artifacts). |  |
| 🎞️ | `MEDIA`    | `INTERVIEW`           | Transcript or notes of an interview; may include oral history. |  |
| 🎞️ | `MEDIA`    | `NEWSPAPER`           | Newspaper clipping or article used as a source. |  |
| 🎞️ | `MEDIA`    | `NOTICE`              | Printed or digital announcements such as posters, flyers, event notices, or proclamations. |  |
| 🎞️ | `MEDIA`    | `OBJECT`              | Tangible item like jewelry, clothing, or furniture with genealogical context. |  |
| 🎞️ | `MEDIA`    | `PHOTO`               | Photograph with genealogical value. |  |
| 🎞️ | `MEDIA`    | `PORTRAIT`            | Paintings, busts, or likenesses that identify or represent an individual. |  |
| 🎞️ | `MEDIA`    | `PUBLISHMENT`         | Appearance in magazine or formal publication (excluding newspapers). |  |
| 🎞️ | `MEDIA`    | `RECORDING` | Digitized or analog recording of voice, music, or spoken biography. |  |
| 🎞️ | `MEDIA`    | `TRACES`  | Archived media sources with genealogical value — obituaries, online trees, memorials. |  |
| 🎞️ | `MEDIA`    | `WEBSITE` | Online resource with genealogical value (e.g., personal family pages, grave index sites). |  |
| 🎞️ | `MEDIA`    | `OTHER`  | Any other media item; must include a PHRASE to describe its significance. |  |
| 🩺| `MEDICAL`  | `ADMISSION`| Admission to a hospital for medical care. |  |
| 🩺| `MEDICAL`  | `AUTOPSY` | Postmortem examination performed to determine cause of death. |  |
| 🩺| `MEDICAL`  | `CAUSEOFDEATH` | Official or noted cause of death from a record (e.g., death cert, autopsy, family note). |  |
| 🩺| `MEDICAL`  | `DISABILITY` | Declared or documented disability with genealogical implications. (e.g., pension claim, census disability marker). |  |
| 🩺| `MEDICAL`  | `DISCHARGE`| Discharge from hospital. |  |
| 🩺| `MEDICAL`  | `DNA` | Non-documentary genetic source, such as resemblance or home DNA kits. |  |
| 🩺| `MEDICAL`  | `DNAMATCH` | Genetic connection confirmed between individuals. |  |
| 🩺| `MEDICAL`  | `HOSPITAL` | Official document from a health institution. |  |
| 🩺| `MEDICAL`  | `ILLNESS` | Record or mention of significant illness. |  |
| 🩺| `MEDICAL`  | `IMMUNIZATION` | Vaccination or immunization record. May include historical smallpox, polio, or modern vaccines. |  |
| 🩺| `MEDICAL`  | `LIVING`              | Confirmation or evidence of life status — such as proof of life during wartime or legal proceedings. May appear in official registries or notarized statements. |  |
| 🩺| `MEDICAL`  | `MEDICAL`  | General health-related event or condition. |  |
| 🩺| `MEDICAL`  | `MEDICALTRAITS` | Inherited traits confirmed by examination or report — used in diagnosis or eligibility. |  |
| 🩺| `MEDICAL`  | `PROCEDURE` | Medical or therapeutic procedure performed. |  |
| 🩺| `MEDICAL`  | `SURGERY` | Operative medical procedure. |  |
| 🩺| `MEDICAL`  | `OTHER` | Any other medical event; must include a PHRASE to clarify. |  |
| 🕯️ | `MEMORIAL` | `COMMEMORATION` | Formal or informal event commemorating a person (e.g., memorial day, annual remembrance). |  |
| 🕯️ | `MEMORIAL` | `COMMEM_OBJECT` | Symbolic item like a bench, medal, or statue dedicated to someone deceased. |  |
| 🕯️ | `MEMORIAL` | `FUNERALPROGRAM`      | Printed leaflet or booklet from a funeral, including biography and service order. |  |
| 🕯️ | `MEMORIAL` | `GRAVESTONE`          | Traditional headstone or tombstone at a burial site, inscribed with genealogical info. |  |
| 🕯️ | `MEMORIAL` | `HONORING` | Act or record of publicly honoring someone posthumously (e.g., honorary name, street sign). |  |
| 🕯️ | `MEMORIAL` | `INSCRIPTION`         | Memorial text carved or engraved on stone, buildings, or monuments. |  |
| 🕯️ | `MEMORIAL` | `MEMNOTICE`      | Public remembrance such as newspaper notices or anniversary bulletins. |  |
| 🕯️ | `MEMORIAL` | `ONLINEMEM`      | Digital tribute page "online memorial" (e.g., FindAGrave, social platforms) with biographical elements. |  |
| 🕯️ | `MEMORIAL` | `PLAQUES`             | Plaques on walls or monuments (e.g., war memorials, honorary dedications). |  |
| 🕯️ | `MEMORIAL` | `PRAYERPICTURE`       | Small devotional card from funerals, often with photo and dates. |  |
| 🕯️ | `MEMORIAL` | `TRIBUTE` | Written or spoken tribute honoring someone’s memory (e.g., speech, poem, story). |  |
| 🕯️ | `MEMORIAL` | `OTHER` | Any other memorial item or practice; must include a PHRASE for interpretation. |  |
| ✈️ | `MIGRATION` | `ARRIVAL` | Arriving at a destination. Entering a place for travel, work, or relocation (non-immigration). |  |
| ✈️ | `MIGRATION` | `BORDER` | Border crossing or customs control. Includes documentation at entry/exit points, inspections, or customs declarations. |  |
| ✈️ | `MIGRATION` | `DEPARTURE` | Leaving a location, not necessarily for emigration. Travel away from a place of residence. |  |
| ✈️ | `MIGRATION` | `DEPORTED` | Forced removal from a country or region by legal or governmental order. |  |
| ✈️ | `MIGRATION` | `EMIGRATION` | Event where someone moves out of a country or region to live elsewhere. |  |
| ✈️ | `MIGRATION` | `FLIGHT` | Travel by air, either as part of migration or movement. Can include flight manifests or boarding records. |  |
| ✈️ | `MIGRATION` | `GROUP-MIGR` | Group Migration Manifest/List. Like a Mennonite trek family list or a shared relocation journey. |  |
| ✈️ | `MIGRATION` | `HEIMAT` | Cultural or ancestral place of origin. May refer to legal place of citizenship or clan affiliation. |  |
| ✈️ | `MIGRATION` | `IMMIGRATION` | Entering a country to reside. May include naturalization intent or documents. |  |
| ✈️ | `MIGRATION` | `MOVE` | General move from one residence to another. |  |
| ✈️ | `MIGRATION` | `MOVEFROM` | Departure from a specific location (e.g., “moved away from Rotterdam”). |  |
| ✈️ | `MIGRATION` | `MOVETO` | Arrival at a new location (e.g., “moved to Amsterdam”). |  |
| ✈️ | `MIGRATION` | `QUARANTINE` | Temporary confinement due to travel regulations or health concerns. |  |
| ✈️ | `MIGRATION` | `REENTRY` | Returning to a previous country or region after temporary departure. |  |
| ✈️ | `MIGRATION` | `RELOCATION` | Permanent or semi-permanent move to a new residence. |  |
| ✈️ | `MIGRATION` | `SHIP` | Ship manifest or passenger list. Maritime travel documentation. |  |
| ✈️ | `MIGRATION` | `TRANSIT` | Temporary movement through a country or zone without settling. |  |
| ✈️ | `MIGRATION` | `TRAVEL` | General travel documentation not tied to permanent relocation. |  |
| ✈️ | `MIGRATION` | `VACATION` | Leisure travel or temporary recreational relocation. |  |
| ✈️ | `MIGRATION` | `VISA` | Entry, exit, or travel visa. May include permits or endorsements. |  |
| ✈️ | `MIGRATION` | `VISIT` | A temporary visit to a location different from the person’s residence. |  |
| ✈️ | `MIGRATION` | `VOYAGE` | Long journey by sea or land. May include documentation of migration or exploration. |  |
| ✈️ | `MIGRATION` | `OTHER` | Any other migration-related document or event; must include a PHRASE. |  |
| 🪖 | `MILITARY` | `AWARD` | Military honor or decoration granted for service, merit, bravery, or achievement. Includes medals, citations, and formal recognitions. |  |
| 🪖 | `MILITARY` | `CAMPAIGN` | Participation in a named or numbered military campaign. May include medals, unit actions, or citations. |  |
| 🪖 | `MILITARY` | `CONSCRIPTION` | Mandatory enlistment in military service. A situation imposed by law, typically at a certain age.  (Drafted without voluntary enlistment) |  |
| 🪖 | `MILITARY` | `DEMOTION` | Reduction in rank due to disciplinary or administrative reason. |  |
| 🪖 | `MILITARY` | `DEPLOYMENT` | Assignment to an active duty location or military station. May include departure/arrival orders. |  |
| 🪖 | `MILITARY` | `DESERTION` | Leaving service without authorization. Considered a punishable offense. |  |
| 🪖 | `MILITARY` | `DISCHARGE` | Official release from military service. May include honorable, dishonorable, or medical discharge. |  |
| 🪖 | `MILITARY` | `DRAFTREG` | Enrollment into a registry of military-eligible individuals. (Draft registration) |  |
| 🪖 | `MILITARY` | `ENLISTMENT` | Voluntary or accepted entry into military service. May include contract or oath. |  |
| 🪖 | `MILITARY` | `INDUCTION` | Official incorporation into military ranks after acceptance. (through draft or voluntary process) Often follows `DRAFTREG`. |  |
| 🪖 | `MILITARY` | `MILDRAFTREG` | Registration for compulsory military service. Similar to `DRAFTREG`. |  |
| 🪖 | `MILITARY` | `MILSERVICE` | Period of active duty in the military. A general situation covering unspecified events. May include enlistment, duty period, deployments, battles, unit assignments or campaigns. |  |
| 🪖 | `MILITARY` | `MUSTERROLL` | Roster of service members; includes lists like regimental rolls. |  |
| 🪖 | `MILITARY` | `PENSION` | Record of application for or receipt of military pension. May include eligibility, duration, and amount. |  |
| 🪖 | `MILITARY` | `PRISONEROFWAR` | Capture or detainment during conflict. |  |
| 🪖 | `MILITARY` | `PROMOTION` | Advancement in rank, position, or pay grade during military service. Typically based on merit, time served, or vacancy. |  |
| 🪖 | `MILITARY` | `RANKSTATUS` | A fact of a person’s military role or position (e.g., Lieutenant, General, Field Medic). Use this to capture `ROLE` titles in a `STICKY`. |  |
| 🪖 | `MILITARY` | `RECRUITMENT` | Event or document related to the process of attracting individuals for voluntary military service. May include advertisements, posters, or oral accounts. |  |
| 🪖 | `MILITARY` | `SERVICE` | General term for a person’s service record. May overlap with `MILITARYSERVICE`, but used in narrative or informal sources. |  |
| 🪖 | `MILITARY` | `TRANSFER` | Reassignment within or between military units or locations. |  |
| 🪖 | `MILITARY` | `UNIT` | Unit affiliation without full muster roll. |  |
| 🪖 | `MILITARY` | `UNIT-ROLL` | Roster or muster list of a military unit. Useful for establishing presence at a location and role within unit. Like a Muster roll of the 12th Infantry. |  |
| 🪖 | `MILITARY` | `OTHER` | Any other military-related document or record; must include a `PHRASE`. |  |
| 🏗️ | `OCCUPATIONAL` | `APPRENTICESHIP` | Training period under a mentor to learn a skilled trade or profession. |  |
| 🏗️ | `OCCUPATIONAL` | `APPOINTMENT` | Assignment or nomination to an office or post. |  |
| 🏗️ | `OCCUPATIONAL` | `CERTIFICATION` | Credential earned for a skill or profession (e.g., teaching, trade license, midwife license, guild license). |  |
| 🏗️ | `OCCUPATIONAL` | `EMPLOYMENT` | Job or career participation. May include contracts, roles, or employer data. |  |
| 🏗️ | `OCCUPATIONAL` | `FREELANCE` | Independent work engagement (e.g. traveling barber, document writer). |  |
| 🏗️ | `OCCUPATIONAL` | `GUILD` | Reference to a historical trade or craft guild membership (see also AFFILIATION). |  |
| 🏗️ | `OCCUPATIONAL` | `LICENSE` | Professional or trade license (e.g., medical, legal, barber). (may overlap with certification |  |
| 🏗️ | `OCCUPATIONAL` | `OCCUPATION` | Statement or source identifying profession or trade, often as listed in a document. |  |
| 🏗️ | `OCCUPATIONAL` | `OFFICEHOLDING` | Serving in an official post, especially civic, religious, or guild-related. |  |
| 🏗️ | `OCCUPATIONAL` | `OFFICEHOLDER` | Role or title in a workplace (e.g. Mayor, Overseer, Bailiff). |  |
| 🏗️ | `OCCUPATIONAL` | `PARTNERSHIP` | Professional partnership record (e.g. law firm, business co-founder). |  |
| 🏗️ | `OCCUPATIONAL` | `PENSION` | Retirement benefits record related to a former occupation. |  |
| 🏗️ | `OCCUPATIONAL` | `RANK` | Job classification, hierarchy level (e.g., foreman, journeyman, master). |  |
| 🏗️ | `OCCUPATIONAL` | `RESIGNATION` | Resignation or leaving an official or occupational role. |  |
| 🏗️ | `OCCUPATIONAL` | `RETIREMENT` | Exit from employment due to age or tenure. |  |
| 🏗️ | `OCCUPATIONAL` | `SERVICEBOOK` | Logbook or document tracking duties, often military or maritime. |  |
| 🏗️ | `OCCUPATIONAL` | `TAXASSESSMENT` | Property or income tax evaluation. |  |
| 🏗️ | `OCCUPATIONAL` | `TENURE` | Holding a specific role or job over a period of time. |  |
| 🏗️ | `OCCUPATIONAL` | `TITLE` | Job title (e.g., Miller, Master Smith, Doctor, Parish Clerk). Use `ROLE` in STICKY to capture the `TITLE` itself. |  |
| 🏗️ | `OCCUPATIONAL` | `UNION` | Documented labor union membership or activity. |  |
| 🏗️ | `OCCUPATIONAL` | `WAGE` | Payment records or salary history. |  |
| 🏗️ | `OCCUPATIONAL` | `WORKPLACE` | Document referencing location of work (e.g. factory, mill, print shop). |  |
| 🏗️ | `OCCUPATIONAL` | `OTHER` | Any other occupation-related document; must include a `PHRASE`. |  |
| ☂️ | `PERSONAL` | `ADULTSTATUS` | A fact of reaching adulthood or majority. |  |
| ☂️ | `PERSONAL` | `BIRTHORDER` | Relative order of birth (e.g., "first son", "third child"). |  |
| ☂️ | `PERSONAL` | `BIOGRAPHY` | Summary or narrative life account. |  |
| ☂️ | `PERSONAL` | `CHARACTER` | Notation of moral or social behavior (e.g., "of good character", "troublesome youth"). |  |
| ☂️ | `PERSONAL` | `FAVORITE` | Individual favored by someone of status (e.g., "King’s Favorite"). |  |
| ☂️ | `PERSONAL` | `INTERESTS` | Hobbies, passions, or recurring topics mentioned in documents. |  |
| ☂️ | `PERSONAL` | `LOOKS` | Appearance or traits noted in documents, "Physical appearance" (e.g., scars, height). |  |
| ☂️ | `PERSONAL` | `REPUTATION` | Social standing, fame, notoriety. |  |
| ☂️ | `PERSONAL` | `STATUS` | Social position or condition (e.g. illegitimacy, social class, marital status if not covered elsewhere). (or a descriptive label used in source (e.g., "widow") |  |
| ☂️ | `PERSONAL` | `TITLES` | Honorifics, noble titles, or inherited rank (e.g. Baron, Sir, Countess). use `ROLE` in `STICKY` for title itself. (Also see ` DEATH, WILL`) |  |
| ☂️ | `PERSONAL` | `WEALTH` | Statement of financial or material condition (e.g. property, fortune, poverty). |  |
| ☂️ | `PERSONAL` | `OTHER` | Other personal data not listed above; must include a `PHRASE`. |  |
| 🏘️ | `PROPERTY` | `ACQUISITION` | Gaining ownership through purchase, inheritance, or other means. |  |
| 🏘️ | `PROPERTY` | `APPRAISAL` | Document assigning monetary value to property or estate. Often used in legal, insurance, or probate contexts. |  |
| 🏘️ | `PROPERTY` | `AUCTION` | Public sale event for property or goods, typically to the highest bidder. |  |
| 🏘️ | `PROPERTY` | `BOUNDARYCHANGE` | Legal redrawing or adjustment of property lines, often filed with land or cadastral registers. |  |
| 🏘️ | `PROPERTY` | `CONFISCATION` | Seizure of property by authority or force. Often without compensation. |  |
| 🏘️ | `PROPERTY` | `DEED` | Legal document transferring property ownership. |  |
| 🏘️ | `PROPERTY` | `DONATION` | Transfer of property without compensation; gift or bequest. |  |
| 🏘️ | `PROPERTY` | `ESTATERECORD` | Document describing contents or value of an estate. May include multiple assets. |  |
| 🏘️ | `PROPERTY` | `GRANT` | Land or property grant issued by authority (e.g., crown or government). |  |
| 🏘️ | `PROPERTY` | `INHERITANCE` | Receipt of property or possessions from a deceased person. (Also see ` DEATH, WILL`)  |  |
| 🏘️ | `PROPERTY` | `INVENTORY` | List of possessions or estate property. May accompany probate or guardianship. |  |
| 🏘️ | `PROPERTY` | `LANDTRANS` | Legal recording of a land-related change "Land transaction" (e.g., sale, trade, claim). Transaction tied to land rights. |  |
| 🏘️ | `PROPERTY` | `LEASE` | Temporary granting of use or access to property, usually in exchange for payment. |  |
| 🏘️ | `PROPERTY` | `LIEN` | Legal claim on property as security for a debt or obligation. |  |
| 🏘️ | `PROPERTY` | `LOSS` | Property lost due to disaster, war, expropriation, or abandonment. |  |
| 🏘️ | `PROPERTY` | `MAP` | Map or diagram showing property layout, boundaries, or structures. May accompany land deed or plan. |  |
| 🏘️ | `PROPERTY` | `MORTGAGE` | Loan secured by property as collateral. Record of lien or obligation. |  |
| 🏘️ | `PROPERTY` | `OWNERSHIP` | Evidence of ownership without explicit transfer (e.g. tax records). |  |
| 🏘️ | `PROPERTY` | `PURCHASE` | Buying of land, goods, or other assets. May include price, date, parties involved. |  |
| 🏘️ | `PROPERTY` | `RECORD` | General-purpose document about property or real estate. Use when no other subtype applies and context is limited. |  |
| 🏘️ | `PROPERTY` | `RENTAL` | Property rented or leased, not owned. May include terms or occupant info. |  |
| 🏘️ | `PROPERTY` | `SALE` | Event or document indicating transfer of ownership in exchange for money. |  |
| 🏘️ | `PROPERTY` | `TRANSFER` | General term for shifting property rights, ownership, or stewardship. Duplicate of LEGAL:TRANSFER, but placed here for easier discovery. |  |
| 🏘️ | `PROPERTY` | `WARRANTYDEED` | Specific form of deed with legal guarantee of clear title. |  |
| 🏘️ | `PROPERTY` | `ZONING` | Zoning or land-use designation record. May include permitted uses or restrictions. |  |
| 🏘️ | `PROPERTY` | `OTHER` | Any other property-related document; must include a `PHRASE`. |  |
| ✝️ | `RELIGIOUS` | `ADULTBAPT`    | Christian baptism performed on an adult, usually after personal faith declaration. Use PHRASE for detail: [adult baptism, convert, declaration, late baptism, water rite] |  |
| ✝️ | `RELIGIOUS` | `ANATHEMA`     | Formal ecclesiastical (church-related) condemnation or curse, typically to excommunicate or denounce someone. Use PHRASE for detail: [curse, ban, excommunication, heresy, condemnation, spiritual penalty] |  |
| ✝️ | `RELIGIOUS` | `BAPTISM`      | Standard Christian rite of spiritual cleansing and entry into the faith, often for infants. See also `CHRISTENING`. Use PHRASE for detail: [infant baptism, sacrament, water blessing, faith entry] |  |
| ✝️ | `RELIGIOUS` | `BAPTISM_LDS`  | LDS Church baptism performed at age 8 or later by priesthood authority. Use PHRASE for detail: [Mormon baptism, LDS, church ordinance, age 8 rite, convert ritual] |  |
| ✝️ | `RELIGIOUS` | `BARMITZVAH`   | Jewish coming-of-age ceremony for boys at age 13, marking full religious responsibility. Use PHRASE for detail: [Jewish rite, adulthood, synagogue, Torah reading, male ceremony] |  |
| ✝️ | `RELIGIOUS` | `BATMITZVAH`   | Jewish coming-of-age ceremony for girls at age 12, signifying religious maturity. Use PHRASE for detail: [Jewish rite, daughter, synagogue, female adulthood, bat mitzvah] |  |
| ✝️ | `RELIGIOUS` | `BLESSING`     | Formal spiritual or religious invocation of grace, protection, or approval. Use PHRASE for detail: [benediction, favor, invocation, sacred wish, religious approval] |  |
| ✝️ | `RELIGIOUS` | `BRITMILAH`    | Jewish circumcision ritual for male infants on the eighth day after birth. Use PHRASE for detail: [circumcision, Jewish covenant, mohel, infant rite, bris] |  |
| ✝️ | `RELIGIOUS` | `CHRISTENING`  | Infant baptism or naming rite in Christian traditions. See also `BAPTISM`. Use PHRASE for detail: [naming, baby blessing, infant baptism, godparent, sacred naming] |  |
| ✝️ | `RELIGIOUS` | `CIRCUMC`      | Religious or cultural circumcision, often linked to birth or adult conversion. ("Circumcision"). Use PHRASE for detail: [ritual cutting, foreskin, male rite, convert, cultural surgery] |  |
| ✝️ | `RELIGIOUS` | `CONFIRM`      | Religious rite affirming one's faith, typically after baptism; symbolizes spiritual maturity and personal commitment. Use PHRASE for detail: [confirmation, rite of passage, affirmation, Holy Spirit, church membership] |  |
| ✝️ | `RELIGIOUS` | `CONL`         | LDS confirmation of church membership following baptism. Use PHRASE for detail: [LDS, laying on of hands, church entry, Mormon rite, confirmation] |  |
| ✝️ | `RELIGIOUS` | `CONVERSION` | Change of religion or entry into a new faith tradition. May involve adult baptism, public declaration, or vows. Use PHRASE for detail: [convert, change of faith, new religion, religious transition] |  |
| ✝️ | `RELIGIOUS` | `DECLARATION`  | Public affirmation of faith or religious status, often before a rite like baptism or confirmation. Use PHRASE for detail: [faith statement, belief declaration, spiritual vow, verbal affirmation, creed] |  |
| ✝️ | `RELIGIOUS` | `ENDOWMENT`    | LDS temple ceremony granting spiritual knowledge, covenants, and blessings. Use PHRASE for detail: [LDS rite, Mormon temple, spiritual gift, sacred knowledge, priesthood covenant] |  |
| ✝️ | `RELIGIOUS` | `ENTRY` | Entry into a religious institution, such as a monastery, convent, or seminary. May include initial vows or commitment to religious formation. Use PHRASE for detail: [monastery, seminary, convent, religious life, postulant, entry ceremony, vows] |  |
| ✝️ | `RELIGIOUS` | `EXCOMMUN`     | Formal removal or exclusion from a religious community. Use PHRASE for detail: [ban, exclusion, excommunication, excision, censure, rejection, church penalty, expulsion] |  |
| ✝️ | `RELIGIOUS` | `FIRSTCOM`     | First communion: Catholic rite of receiving the Eucharist for the first time, usually in childhood. Use PHRASE for detail: [Eucharist, Holy Communion, Catholic rite, child sacrament, mass] |  |
| ✝️ | `RELIGIOUS` | `HAJJ`         | Islamic pilgrimage to Mecca, required once in a lifetime for able Muslims. Use PHRASE for detail: [Mecca, pilgrimage, Five Pillars, sacred journey, Islam] |  |
| ✝️ | `RELIGIOUS` | `INIL`         | LDS initiatory ordinance performed in temples; preparation for further rites. Use PHRASE for detail: [LDS initiation, anointing, Mormon temple, ordinance, washing] |  |
| ✝️ | `RELIGIOUS` | `KIDDUSHIN`    | First stage of a traditional Jewish wedding, involving legal betrothal. Use PHRASE for detail: [Jewish marriage, engagement, betrothal, ketubah, contract] | ENGA |
| ✝️ | `RELIGIOUS` | `LASTRITES`    | Catholic sacrament before death, including confession, anointing, and Eucharist. Use PHRASE for detail: [dying rite, anointing, viaticum, Catholic, final sacrament] |  |
| ✝️ | `RELIGIOUS` | `MISSION`      | Assignment or period of religious service, often evangelical or aid-based. Use PHRASE for detail: [missionary, religious service, outreach, evangelism, deployment] |  |
| ✝️ | `RELIGIOUS` | `MONMOVE`    | Transfer of a monk or nun between monastic institutions or orders. Use PHRASE for detail: [convent move, monastic transfer, reassignment, cloister change, abbey shift] |  |
| ✝️ | `RELIGIOUS` | `NISSUIN`      | Second part of a Jewish wedding ceremony, focused on consummation and shared home. Use PHRASE for detail: [Jewish marriage, canopy, chuppah, home blessing, union] |  |
| ✝️ | `RELIGIOUS` | `OBSERVANCE`    | Participation in a religious event, ritual, or holy day. Use PHRASE for detail: [holy day, feast, sabbath, ritual, participation] |  |
| ✝️ | `RELIGIOUS` | `ORDINATION`    | Ceremony conferring spiritual office (e.g., priest, rabbi, imam). Use PHRASE for detail: [clergy, spiritual authority, religious title, ordain, investiture] |  |
| ✝️ | `RELIGIOUS` | `PILGRIMAGE`    | Sacred journey to a religious site or destination. Use PHRASE for detail: [pilgrim, sacred travel, holy place, devotion journey, shrine visit] |  |
| ✝️ | `RELIGIOUS` | `REASSIGNMENT`  | Change of religious office or transfer of clerical duties. Use PHRASE for detail: [clergy move, new post, parish shift, office change, appointment] |  |
| ✝️ | `RELIGIOUS` | `RECONV`        | Reconversion: re-adopting a previous faith after leaving it. Use PHRASE for detail: [return to faith, religious renewal, reconvert, rejoin religion] |  |
| ✝️ | `RELIGIOUS` | `RELIGION`      | Declaration or registration of religious affiliation. Use PHRASE for detail: [faith, belief, religious status, religion stated, change of belief] |  |
| ✝️ | `RELIGIOUS` | `ORDER`         | Joining a religious order or congregation. Use PHRASE for detail: [convent, brotherhood, nunnery, society, vows] |  |
| ✝️ | `RELIGIOUS` | `RENOUNCE`      | Formal rejection or departure from a religion. Use PHRASE for detail: [leave faith, withdraw, religious resignation, reject belief, renunciation, apostasy] |  |
| ✝️ | `RELIGIOUS` | `RETREAT`       | Period of spiritual reflection, often in isolation. Use PHRASE for detail: [sabbatical, prayer retreat, silent stay, meditative period, cloister] |  |
| ✝️ | `RELIGIOUS` | `SACRAMENTAL`   | Receiving a sacrament not separately listed (e.g., anointing, confession). Use PHRASE for detail: [rite, Catholic sacrament, spiritual act, blessing] |  |
| ✝️ | `RELIGIOUS` | `SEALING`       | LDS ordinance binding family members for eternity. Use PHRASE for detail: [eternal marriage, LDS temple, family sealing, spiritual bond] |  |
| ✝️ | `RELIGIOUS` | `SEPARATION`    | Leaving or removal from a religious group, voluntary or not. Use PHRASE for detail: [expulsion, resignation, departure, removal from congregation] |  |
| ✝️ | `RELIGIOUS` | `SHUNNING`      | Social or religious ostracism, especially without formal excommunication. Use PHRASE for detail: [exile, avoidance, exclusion, anabaptist, Amish] |  |
| ✝️ | `RELIGIOUS` | `SPIRITCALL`    | Recognition of a perceived divine calling or mission. Use PHRASE for detail: [vocation, divine summons, spiritual mission, spiritual calling, call to service] |  |
| ✝️ | `RELIGIOUS` | `VOWS`          | Formal sacred vows such as chastity, poverty, or obedience. Use PHRASE for detail: [religious promise, oath, commitment, monastery, celibacy] |  |
| ✝️ | `RELIGIOUS` | `OTHER`         | Any religious event not covered by other entries; must use PHRASE. Use PHRASE for detail: [custom, rare rite, local tradition, undefined religious act] |  |
| ⚓ | `RESIDENCE` | `ADDRESS` | Document explicitly listing an individual’s residence; e.g. ID card, driver’s license, or utility bill. |  |
| ⚓ | `RESIDENCE` | `CENSUSOTHER` | Residence-based census not falling under household or tax types; e.g. lodging census, institutional census. | CENS |
| ⚓ | `RESIDENCE` | `DOMICILIECENSUS` | Older or regional term for place-based listing; e.g. French "recensement de domicile" showing household occupancy. | CENS |
| ⚓ | `RESIDENCE` | `DWELLINGCERT` | Official certificate confirming where a person lives; e.g. municipal residence proof, "Wohnsitzbescheinigung". |  |
| ⚓ | `RESIDENCE` | `FARM-OCCU` | Farm residency register; e.g. Scandinavian husmann lists or tenant farmer records. |  |
| ⚓ | `RESIDENCE` | `HOUSINGLIST` | Urban housing or rental occupancy listing; e.g. Amsterdam housing ledger or rent control rosters. |  |
| ⚓ | `RESIDENCE` | `HOUSEHOLDREG` | Record showing residents at a specific address, often over time; e.g. Swedish “husförhörslängd”, Dutch "Bevolkingsregister". (Household register) |  |
| ⚓ | `RESIDENCE` | `MILCENSUS` | (MILITARYCENSUS) Enrollment lists tied to place of residence for conscription; e.g. draft boards, military eligibility censuses. | CENS |
| ⚓ | `RESIDENCE` | `POPCENSUS` | (POPULATIONCENSUS) General household or population census; e.g. U.S. Federal Census, UK census returns. | CENS |
| ⚓ | `RESIDENCE` | `REGISTRATION` | Government or institutional registry of residence; e.g. Anmeldung in Germany, civil residence registry. |  |
| ⚓ | `RESIDENCE` | `TAXCENSUS` | Census used for tax purposes including residence data; e.g. hearth tax lists, poll tax registers. | CENS |
| ⚓ | `RESIDENCE` | `OTHER` | Any other residence-related record not listed above; must include a PHRASE. |  |
| 📚 | `SECONDARY` | `ADOPT-FOSTER`   | Adoption or fostering customs — informal, cultural, or undocumented practices. |  |
| 📚 | `SECONDARY` | `BLOODTYPE`      | Reported or assumed blood type used in family context or paternity speculation. |  |
| 📚 | `SECONDARY` | `DNATEST`        | Unverified DNA test results, notes, or discussions, including home kits or shared interpretations. |  |
| 📚 | `SECONDARY` | `FAMILYBIBLE` | A family Bible used as a multigenerational record of births, marriages, and deaths — often handwritten by relatives. May include marginal notes about migrations, household members (e.g. servants), land ownership, heirlooms, or religious customs. Treated as a secondary source. |  |
| 📚 | `SECONDARY` | `FARM-LAND`      | Usage patterns of farmland passed within families — noted through tradition, not deed. |  |
| 📚 | `SECONDARY` | `HEIRLOOMS`      | Family items with historical significance — clocks, rings, etc. — identified via memory or tradition. |  |
| 📚 | `SECONDARY` | `HISTORY-LORE`   | Portraits or items attributed by family tradition or oral story, not documented evidence. |  |
| 📚 | `SECONDARY` | `HOUSE`          | Residence continuity across generations — identified through habit, not official record. |  |
| 📚 | `SECONDARY` | `INHERITANCE`    | Traditional craft or occupational inheritance — passed generationally, not certified. |  |
| 📚 | `SECONDARY` | `JEWELRY`        | Jewelry identified as significant by engraving or memory — e.g., family crest ring. |  |
| 📚 | `SECONDARY` | `LANG-DIALECT`   | Regional language or dialect retention, used as cultural or genealogical clue. |  |
| 📚 | `SECONDARY` | `LORE`           | General cultural or familial traditions that influence understanding of ancestry. |  |
| 📚 | `SECONDARY` | `MARR-TRADITIONS`| Customs such as cousin marriage, dowry, or bride price — preserved orally. |  |
| 📚 | `SECONDARY` | `MEDICALTRAITS`  | Shared inherited traits or conditions mentioned in family context. |  |
| 📚 | `SECONDARY` | `NAMING`         | Naming conventions across generations (e.g., patronymics, suffixes, repeated names). |  |
| 📚 | `SECONDARY` | `NICKNAMES`      | Inherited or family-based nicknames that serve as alternate identifiers. |  |
| 📚 | `SECONDARY` | `PATTERNS`       | Migration, religious, or social patterns inferred from broader community behavior. |  |
| 📚 | `SECONDARY` | `SONG-TOTEM`     | Clan-specific songs, totems, or symbolic items passed through memory. |  |
| 📚 | `SECONDARY` | `STORIES`        | Family stories or narratives about people, places, or events — not directly evidenced. |  |
| 📚 | `SECONDARY` | `TATTOO`         | Cultural or generational tattoo practices referenced in oral or visual tradition. |  |
| 📚 | `SECONDARY` | `TRACES`         | Online artifacts (photos, social media, blogs) that inform family history without certification. |  |
| 🌐 | `SOCIAL` | `ACCIDENT` | Documented incident causing injury, damage, or death — often public or recorded for insurance/legal/social purposes. |  |
| 🌐 | `SOCIAL` | `AWARD` | A non-military award or recognition received. Examples: civic medals, academic honors, public commendations. |  |
| 🌐 | `SOCIAL` | `COMMUNITYSERVICE` | Involvement in community or volunteer service. Sometimes documented in local newsletters or recognition forms. |  |
| 🌐 | `SOCIAL` | `GIFT` | Uncompensated transfer of item, land, or benefit. Can include ceremonial or formal gift-giving. |  |
| 🌐 | `SOCIAL` | `GUESTBOOK` | Signed presence in an event guestbook. May include location, occasion, and date. |  |
| 🌐 | `SOCIAL` | `INITIATION` | Entry into a social club, order, or association. Often tied to rituals or certificates. |  |
| 🌐 | `SOCIAL` | `MEETING` | Participation in a public or organizational meeting. May be recorded in minutes or attendance rolls. |  |
| 🌐 | `SOCIAL` | `PARTY` | Documented social gathering, such as invitations, event photos, or commemorative cards. |  |
| 🌐 | `SOCIAL` | `RECEPTION` | Public or ceremonial reception event. Often follows weddings, retirements, or promotions. |  |
| 🌐 | `SOCIAL` | `REUNION` | Event bringing together family, veterans, alumni, or communities. Frequently documented. |  |
| 🌐 | `SOCIAL` | `SOCIALSTATUS` | Declared social standing or role (e.g., nobility, caste membership). Sometimes appears in formal listings. |  |
| 🌐 | `SOCIAL` | `SPONSORING` | Supportive role in social or religious context (e.g., godparent, witness). May be listed in event records. |  |
| 🌐 | `SOCIAL` | `TRAGEDY` | Record of disasters, crimes, or public accidents involving the person. Examples: arson reports, public mourning, disaster registries. |  |
| 🌐 | `SOCIAL` | `OTHER` | Any other social-related record not listed above; must include a `PHRASE`. |  |
| 🌈 | `STATUSCHANGE` | `AMNESTY` | Official pardon for people convicted of political or civil offenses. Legal absolution. |  |
| 🌈 | `STATUSCHANGE` | `DEMOTION` | Loss of rank or formal downgrade in position, often occupational or military. |  |
| 🌈 | `STATUSCHANGE` | `ELECTED` | Appointment via public or official vote to a role or office. |  |
| 🌈 | `STATUSCHANGE` | `EMANCIPATION` | Legal freedom from parental or guardianship control. Often marks adulthood or independence. |  |
| 🌈 | `STATUSCHANGE` | `ENSLAVEMENT` | Formal record or recognition of being enslaved. Includes purchase, sale, or status documentation. |  |
| 🌈 | `STATUSCHANGE` | `EXCOMMUNICATION` | Formal religious expulsion or loss of group standing. May involve public or clerical declaration. |  |
| 🌈 | `STATUSCHANGE` | `GENDERCHANGE` | Transition of gender identity. May include legal, medical, or social recognition. |  |
| 🌈 | `STATUSCHANGE` | `GRADUATION` | Completion of an academic program or degree conferral. Can mark social or career status change. |  |
| 🌈 | `STATUSCHANGE` | `IMPRISONMENT` | Period of incarceration. Legal detainment by judicial or political authority. |  |
| 🌈 | `STATUSCHANGE` | `INDUCTION` | Official entry into a recognized role, group, or service. May involve oath, ceremony, or legal act. |  |
| 🌈 | `STATUSCHANGE` | `MANUMISSION` | Release from slavery. Granting of freedom through official decree or document. |  |
| 🌈 | `STATUSCHANGE` | `MIL_DISCHARGE` | Completion or termination of military service. May be honorable, dishonorable, or other. |  |
| 🌈 | `STATUSCHANGE` | `MIL_INDUCTION` | Entry into military via official process or draft. Beginning of service. |  |
| 🌈 | `STATUSCHANGE` | `NAMECHANGE` | Legal or official change of personal name. May involve court record or announcement. |  |
| 🌈 | `STATUSCHANGE` | `NATURALIZATION` | Legal acquisition of new citizenship or nationality. May include renunciation of former. |  |
| 🌈 | `STATUSCHANGE` | `ORDINATION` | Formal recognition as religious leader or clergy. Typically follows training or calling. |  |
| 🌈 | `STATUSCHANGE` | `PROMOTION` | Advancement in rank, position, or title. Often used in military, government, or clergy. |  |
| 🌈 | `STATUSCHANGE` | `RESIGNATION` | Voluntary departure from official position or membership. Can include letter or formal notice. |  |
| 🌈 | `STATUSCHANGE` | `RETIREMENT` | Withdrawal from occupation or role, often due to age or service completion. |  |
| 🌈 | `STATUSCHANGE` | `TITLEOFNOBILITY` | Recognition or grant of a noble title. Use STICKY `ROLE` to indicate title specifics (e.g., Baron, Countess). (Also see ` DEATH, WILL`) |  |
| 🌈 | `STATUSCHANGE` | `OTHER` | Any other personal status-shift not listed here; must include a `PHRASE`. |  |
| 🌀 | `OTHER`        | `OTHER` | Any other category not listed here; must include a `PHRASE`. |  |

- Each `SUBTYPE` is only valid in combination with the `TYPE` shown in the left column. You may not use a `SUBTYPE` under a different `TYPE` unless explicitly allowed. The `OTHER` value under each type provides an escape hatch for non-standard subtypes; it must always be accompanied by a `PHRASE`.

- Although censuses capture a wide range of personal data, they are categorized under `RESIDENCE` because their core organizing principle is the enumeration of individuals at a particular place and time.

- `TYPE`and `SUBTYPE` work together, and must be written on one and the same line, separated by ", ".

- Subtypes are intended to assist in organizing and interpreting source documents more accurately. The set is open-ended; implementations may extend it using `OTHER` when a more specific match is unavailable. In that case a  `PHRASE` must be included.

:::example  
How to use `OTHER` for a non mentioned `PROPERTY`:
```gedstruct
0 @T0093@ TEMPLATE
1 TYPE PROPERTY, OTHER, "This is some other Property."
```
- Instead of `PROPERTY` any other of the above mentioned `TYPE`s can be used.
- When using `OTHER` there must always be a `PHRASE` to further specify.   
:::


