
### `g8:enumset-ENTITY-TYPE`

Describes the kind of entity referred to by a `STICKY` or `ASSET` record.
- `PERSON` is a special case usable only in `STICKY`s that describe people. All others describe entities.
- This enumset is used in both `STICKY.TYPE` and `ASSET.TYPE`.  

| ICO | TYPE           | Description |
|-----|----------------|-------------|
| 🖼️ | `ARTWORK`      | Works of art including paintings, sculptures, performances, and other creative items. Use PHRASE for detail: [painting, sculpture, drawing, embroidery]. |
| 🏅 | `AWARD`        | Awards or recognitions, including military, civic, or honorary distinctions. Use PHRASE for detail: [medal, honor, prize]. |
| ☂️ | `BELONGINGS`   | Household items, clothing, furniture, musical instruments, or everyday personal objects. Only those that do NOT fit into one of the other main categories! Use PHRASE for detail: [clothing, furniture, instrument]. |
| 📖 | `BOOK`         | Manuscripts, scrolls, ledgers, or published books. Use PHRASE for detail: [Bible, ledger, diary, manuscript]. |
| 🐎 | `CREATURES`    | Animals kept for use or pleasure, including livestock, dogs, horses, etc. Use PHRASE for detail: [horse, cattle, sheep, dog]. |
| 🧬 | `DNA`          | Registered genetic profiles, test results, or kit IDs. Often linked to ancestry services, forensic reports, or medical archives. Use PHRASE for detail: [DNA kit, Y-DNA, mtDNA]. |
| 📜 | `DOCUMENT`     | Official papers, certificates, letters, contracts, legal documents, or records. Use PHRASE for detail: [certificate, contract, letter, passport]. |
| 🏡 | `ESTATE`       | A legally recognized unit combining land and its associated rights, which may include forests, islands, or agricultural areas such as farms or orchards. Use when emphasizing *ownership*, *inheritance*, or *named tracts*. Use PHRASE for detail: [farm, manor, island, vineyard]. |
| 💰 | `FINANCE`      | Financial instruments and institutional holdings not held as physical cash. Includes accounts, insurance, bonds, investments, tax records, and debt instruments. Use PHRASE for detail: [account, bond, investment, insurance]. |
| 💎 | `JEWELRY`      | Rings, crowns, brooches, necklaces, earrings, and other personal adornments. Refers to **worn or wearable items**. Does **not** include loose diamonds, gemstones, or precious metals held purely as financial assets — those belong in `MONEY`. Use PHRASE for detail: [ring, necklace, brooch, crown]. |
| 🧠 | `INTANGIBLE`   | Non-physical property or rights that can be owned, transferred, or inherited. Includes intellectual property, shares, easements, and other valuable rights. Use PHRASE for detail: [copyright, patent, trademark, shareholding, franchise, easement, digital asset]. |
| 🌿 | `LAND`         | Natural or cultivated areas not primarily defined by buildings or ownership, such as fields, forests, orchards, gardens, islands, cemeteries, or wilderness zones. Use when emphasizing *terrain, use*, or *natural classification*. Use PHRASE for detail: [field, orchard, forest, garden]. |
| 🎞️ | `MEDIA`        | Any type of media: photos, recordings, videos, or publications. Use PHRASE for detail: [photograph, film, audio, postcard]. |
| 🕊️ | `MEMORIAL`     | Physical or symbolic items created to honor or remember a deceased individual. Includes graves, urns, memorial trees, cards, inscriptions, and culturally-specific commemorative objects. These may record names, dates, relationships, or rituals, and can serve as primary or secondary genealogical evidence.<br>⚠️ MEMORIAL entity types are intended for commemorative, symbolic, or ceremonial objects.<br>Legal or administrative records related to death events should instead be categorized under DOCUMENT. Use PHRASE for detail: [grave, urn, plaque, monument]. |
| 🪖 | `MILITARY`     | Items related to military service, such as uniforms, medals, etc. Use PHRASE for detail: [uniform, medal, sword, insignia]. |
| 💶 | `MONEY`        | Coins, banknotes, and physical forms of value such as bullion, gems, or other portable wealth. Includes **loose diamonds**, **precious metals**, **rare coins**, and **treasured valuables** stored or traded for their financial worth. Excludes **worn jewelry** like rings or necklaces — those belong in `JEWELRY`. Use PHRASE for detail: [coin, gold, silver, diamond]. |
| 🏢 | `ORGANIZATION` | Named institutions that issue, regulate, record, or otherwise appear as active agents in genealogical records. Examples: adoption agencies, schools, parishes, registries, consulates, courts, trade unions, and historical archives. Use PHRASE for detail: [school, court, parish, guild, archive]. |
| 👤 | `PERSON`       | ⚠️ Only valid in STICKYs that refer to a person. Not valid in ASSETs‼️. Use PHRASE for detail: [individual name, title, alias]. |
| 🏘️ | `PROPERTY`     | Man-made structures or built real estate, including homes, castles, stables, churches, and infrastructure. Use when emphasizing *buildings* or *constructs*. Does *not* include terrain or personal objects. Use PHRASE for detail: [house, church, castle, stable]. |
| ✝️ | `RELIGIOUS`    | Religious items or assets, e.g., holy books, artifacts, relics. Use PHRASE for detail: [cross, chalice, icon, scripture]. |
| 🛠️ | `TOOLS`        | Instruments, weapons, farming tools, or other useful objects. Use PHRASE for detail: [hammer, plough, sword, anvil]. |
| 🚗 | `TRANSPORT`    | Cars, boats, carts, carriages, sleds, bikes, planes, trains, ferries, and any other transport vehicles. Use PHRASE for detail: [boat, carriage, bicycle, cart]. |
| ❓ | `OTHER`        | Anything that does not fit in another category; must include a `PHRASE`. Use PHRASE for detail: [custom object, unique asset]. |

#### 💡 Usage Notes

- This enumset is used in both `STICKY.TYPE` and `ASSET.TYPE`.
- In `STICKY` records, all types are valid — including `PERSON`, which is used when the `STICKY` points to a human individual.
- In `ASSET` records, **all types are valid _except_ `PERSON`**. People are represented with `@INDI@` records instead.
- The `OTHER` type can be used when none of the defined types fit. It **must always** be accompanied by a `PHRASE` that clarifies the nature of the object.
- The `AN_OTHER` can be used for `PERSON` `STICKY`'s, in case of **secondary** events in a `TEMPLATE`. `AN_OTHER` is used in the same way as `OTHER`, and it also must have a `PHRASE`.

### `g8:enumset-ENTITY-SUBTYPE`

These values define the allowed `SUBTYPE` values for the `STICKY` and`ASSET` record.
Each entity must declare exactly one `TYPE`, and refine it using one `SUBTYPE` value.  

It is used as:  
`TYPE ARTWORK, PAINTING`  
So not just the `SUBTYPE`, but also the `TYPE` itself must be mentioned.  


| ICO | TYPE | SUBTYPE | Description |
|-----|------|---------|-------------|
| 🖼️ | `ARTWORK` | `CALLIGRAPHY` | Decorative or meaningful handwriting and script: illuminated verses, framed (hand)writing, stylized characters |
| 🖼️ | `ARTWORK` | `DECORATIVE` | Artistically crafted household items such as carved utensils, embellished vessels, or ornamental fixtures, embroidery, or artistic household items |
| 🖼️ | `ARTWORK` | `DRAWING` | Graphite, ink, or chalk illustrations; includes sketches, drafts, design plans,  illustrations and artistic diagrams. |
| 🖼️ | `ARTWORK` | `MINIATURE` | Small-scale paintings, sculptures, or models intended for detail and fine craftsmanship. Often portraiture or architectural. |
| 🖼️ | `ARTWORK` | `MIXED` | Artworks combining multiple media (e.g., textile with wood, painting with carving, or metal with stone). |
| 🖼️ | `ARTWORK` | `OTHER` | Any non-listed ARTWORK form; must include PHRASE to clarify |
| 🖼️ | `ARTWORK` | `PAINTING` | Painted surfaces on canvas, wood, plaster, or parchment. Includes oil paintings, framed portraits, and wall art. |
| 🖼️ | `ARTWORK` | `PERFORMANCE` | Ephemeral or live artistic acts such as dance, theater, or musical presentations. |
| 🖼️ | `ARTWORK` | `SCULPTURE` | Carved, molded, or assembled three-dimensional forms, or statues. Including free-standing works and reliefs. |
| 🖼️ | `ARTWORK` | `TEXTILE` | Embroidered or woven designs made to be admired or symbolic / Embroidered, woven, or stitched designs made primarily for aesthetic, symbolic, or ceremonial purposes. |
| 🏅 | `AWARD` | `CIVILIAN` | Non-military honors granted for civil service, artistic, humanitarian, or academic achievement; may include certificates, framed documents, or symbolic objects. |
| 🏅 | `AWARD` | `HONORARY` | Ceremonial or symbolic titles, often not involving a physical object; includes honorary degrees, symbolic memberships, or posthumous recognitions. |
| 🏅 | `AWARD` | `INSTITUTIONAL` | Awards given by schools, universities, or professional organizations, such as diplomas, badges, or graduation medals. |
| 🏅 | `AWARD` | `MILITARY` | Decorations or medals awarded for military service, bravery, rank, or campaigns; includes orders like "the Militaire Willems-Orde". |
| 🏅 | `AWARD` | `ORDER` | Formal ranks of merit or chivalric orders, often linked to monarchy or state recognition; may be accompanied by insignia, titles, or ceremonial garments. |
| 🏅 | `AWARD` | `OTHER` | Any award not covered by other categories; must include PHRASE to describe nature, issuer, or context of the honor. |
| ☂️ | `BELONGINGS` | `BEDDING` | Mattresses, quilts, blankets, furniture or other items associated with sleeping comfort. |
| ☂️ | `BELONGINGS` | `CLOTHING` | Garments, outerwear, undergarments, footwear, or accessories worn on the body. |
| ☂️ | `BELONGINGS` | `DECOR` | Decorative but not artistic household objects: vases, figurines, wall hangings |
| ☂️ | `BELONGINGS` | `FURNITURE` |  Larger household objects such as chairs, tables, mirrors and dressers. Includes carved or built furniture unless clearly ARTWORK. |
| ☂️ | `BELONGINGS` | `HYGIENE` | Personal grooming or cleaning objects including mirrors, combs, basins, and toiletries. |
| ☂️ | `BELONGINGS` | `KEEPSAKE` | Sentimental or inherited personal items |
| ☂️ | `BELONGINGS` | `MUSICAL` | Musical instrument, use `PHRASE` to specify. |
| ☂️ | `BELONGINGS` | `OTHER` | Any non-listed BELONGINGS item; must include PHRASE to clarify. |
| ☂️ | `BELONGINGS` | `TEXTILE` | Everyday-use cloth or fabric items like towels, curtains, tablecloths, or cushions. Not primarily decorative or symbolic. |
| ☂️ | `BELONGINGS` | `TOY` | Objects designed for play or amusement, such as dolls, figurines, or mechanical toys. May include both handmade and manufactured items. |
| 📖 | `BOOK` | `ACCOUNT` | Ledgers, bookkeeping logs, financial records, or legal/inventory ledgers / Ledgers, bookkeeping logs, or financial records |
| 📖 | `BOOK` | `DIARY` | Personal journals or memoirs |
| 📖 | `BOOK` | `GENEALOGY` | Family trees, pedigree charts, or ancestor books |
| 📖 | `BOOK` | `LEDGER` | Financial, legal, or inventory ledgers |
| 📖 | `BOOK` | `LEGAL` | Statute books, law manuals, or legal codes |
| 📖 | `BOOK` | `LITERATURE` | Poems, plays, novels, or literary works |
| 📖 | `BOOK` | `MANUSCRIPT` | Handwritten books or scrolls |
| 📖 | `BOOK` | `OTHER` | Any other type of book; must include PHRASE to clarify |
| 📖 | `BOOK` | `PRINTED` | Published books, newspapers, or pamphlets |
| 📖 | `BOOK` | `RELIGIOUS` | Scriptures, hymnals, or sacred texts |
| 📖 | `BOOK` | `SCHOLARLY` | Academic texts, treatises, or scientific manuscripts |
| 🐎 | `CREATURES` | `CATTLE` | Cows, oxen, or other bovines kept for meat, milk, or labor (livestock) |
| 🐎 | `CREATURES` | `DOG` | Working or companion dogs |
| 🐎 | `CREATURES` | `DOMESTIC` | Companion animals like dogs, cats, parrots, or rabbits |
| 🐎 | `CREATURES` | `FEATHERED` | Poultry, game birds, or show birds (chickens, ducks, geese) |
| 🐎 | `CREATURES` | `FLOCK` | Sheep, goats, or other small livestock herded for resources |
| 🐎 | `CREATURES` | `HORSE` | Horses, donkeys, mules, ponies, or riding animals used for transport or labor |
| 🐎 | `CREATURES` | `OTHER` | Any other creature; must include PHRASE to clarify |
| 🐎 | `CREATURES` | `SYMBOLIC` | Mythical, ceremonial, or named animals with symbolic value |
| 🐎 | `CREATURES` | `WILD` | Non-domesticated animals in captivity or known individual animals |
| 📜  | `DOCUMENT` | `CERTIFICATE`  | Legal/verifiable document: birth, death, **burial**, **cremation**, **coroner’s** certificates; baptism or marriage records. Naturalization certificate|
| 📜 | `DOCUMENT` | `CONTRACT` | Agreements: sales, employment, military service, indenture, etc. Wills, deeds, legal or business agreements |
| 📜 | `DOCUMENT` | `CORRESPONDENCE` | Official correspondence, NO personal records |
| 📜 | `DOCUMENT` | `DECREE` | Orders issued by a legal, military, or religious authority |
| 📜 | `DOCUMENT` | `ID` | Identification: passports, licenses, permits, etc. |
| 📜 | `DOCUMENT` | `INTELLECTUAL` | Patents, trademarks, copyrights, or other legally registered intellectual properties and creative rights. |
| 📜 | `DOCUMENT` | `LIST` | Inventories, rosters, censuses, tax rolls |
| 📜 | `DOCUMENT` | `OTHER` | Must include a PHRASE to clarify subtype not listed above |
| 📜 | `DOCUMENT` | `PERSONAL` | Letters, diaries, or personal records |
| 📜  | `DOCUMENT` | `RECORD`  | Entries in logs, court books, **inquest reports**, **death or burial registrations**, church registers, or compiled official documents. (official or legal records) |
| 📜  | `DOCUMENT` | `TESTAMENT` | Wills, deeds, contracts, codicils, notarized records or related testamentary instructions. May include related **court files**. |
| 📜 | `DOCUMENT` | `WRITTEN` | Formal written orders (summonses, mandates, authorizations). Includes **burial permits**, **interment or disinterment orders**, and official **municipal burial approvals**. |
| 🧬 | `DNA`    | `TESTKIT`   | Identifiable genetic kit used in analysis (e.g., 23andMe barcode). |
| 🧬 | `DNA`    | `PROFILE`   | Final interpreted profile (e.g., mtDNA, Y-DNA haplogroup). |
| 🧬 | `DNA`    | `RESULT`    | Summary finding or match (e.g., paternity result, region). |
| 🧬 | `DNA`    | `OTHER`     | Any other DNA-related record; must use PHRASE to clarify. |
| 🏡 | `ESTATE` | `COMPOUND` | Legally defined residential or mixed-use parcel with multiple buildings |
| 🏡 | `ESTATE` | `COUNTRYHOUSE` | A rural residence of notable size, typically encompassing a substantial house, outbuildings, and extensive grounds like gardens, farmland, and woodlands (often used seasonally or by the upper class). |
| 🏡 | `ESTATE` | `DOMAIN`   | Historical or noble estate with named boundaries or jurisdiction |
| 🏡 | `ESTATE` | `FARMHOUSE`| A central residential building in a rural estate, typically where the landowner or steward lives. |
| 🏡 | `ESTATE` | `FREEHOLD` | Land or buildings held with full legal title |
| 🏡 | `ESTATE` | `GAMEKEEP` | A structure or enclosed area used to house game animals, or where the gamekeeper resides. |
| 🏡 | `ESTATE` | `HUNTGROUNDS` | Land set aside for organized hunting, often legally defined and inherited. |
| 🏡 | `ESTATE` | `LEASED`   | Property or parcel held temporarily under a lease |
| 🏡 | `ESTATE` | `LODGE`    | A smaller estate building used for temporary stays, especially in rural or forested properties. |
| 🏡 | `ESTATE` | `MANOR`    | Large residential house with estate land |
| 🏡 | `ESTATE` | `PARCEL`   | Defined unit of land, often registered or mapped |
| 🏡 | `ESTATE` | `PARKLAND` | Landscaped grounds around a manor, sometimes extending into wild or semi-wild areas for hunting or grazing. |
| 🏡 | `ESTATE` | `REAL`     | General term for legally owned land or real estate |
| 🏡 | `ESTATE` | `RESIDENCE` | Primary or significant dwelling associated with land ownership |
| 🏡 | `ESTATE` | `TERRITORY` | Broader named area under control of estate or title |
| 🏡 | `ESTATE` | `VILLAGE`  | A self-contained estate-based hamlet, often with tenant housing, chapel, and service buildings. |
| 🏡 | `ESTATE` | `OTHER`    | Any other estate-related asset or structure; must include PHRASE to clarify. |
| 💰 | `FINANCE` | `ACCOUNTS` | Bank accounts, funds, savings books or similar holdings |
| 💰 | `FINANCE` | `BOND` | Government or private debt instruments with maturity dates |
| 💰 | `FINANCE` | `CREDIT` | Bonds, ledgers, debts or claims ( Claims, IOUs, or loans owed to the individual) |
| 💰 | `FINANCE` | `DEBT` | Outstanding amounts owed by the individual |
| 💰 | `FINANCE` | `INSURANCE` | Life or property policies with financial outcomes |
| 💰 | `FINANCE` | `INVESTMENT` | Share certificates, company stakes, speculative holdings |
| 💰 | `FINANCE` | `OTHER` | Any other finance-related item; must include `PHRASE` to clarify. |
| 💰 | `FINANCE` | `SECURITY` | Stocks, bonds, or financial instruments |
| 💰 | `FINANCE` | `STOCKS` | Tradable shares in companies or funds (Stocks, bonds, investments) |
| 💰 | `FINANCE` | `TAX` | Tax records, obligations, or rebates |
| 🧠 | `INTANGIBLE` | `AIR-RIGHT` | Rights to build or use space above property. Use PHRASE for detail: [overbuild, balcony, signage]. |
| 🧠 | `INTANGIBLE` | `BUILDRIGHT` | **Build Construction**: Permits to erect structures. Use PHRASE for detail: [churches, mills]. |
| 🧠 | `INTANGIBLE` | `COPYRIGHT`     | Legal right granting the creator of an original work exclusive rights to its use and distribution. Common in wills for authors, artists, or heirs to creative works. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`. Use PHRASE for detail: [book copyright, artwork copyright, software copyright]. |
| 🧠 | `INTANGIBLE` | `DIGASSET` | **Digital Asset**: Non-physical assets stored electronically, including domain names, cryptocurrency, and NFTs. Increasingly appearing in modern wills and trusts. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`, `ADMINISTRATOR`. Use PHRASE for detail: [domain name, Bitcoin, NFT, social media account]. |
| 🧠 | `INTANGIBLE` | `EXPLOITATION` | Right to commercially exploit a resource. Use PHRASE for detail: peat cutting, timber harvesting]. |
| 🧠 | `INTANGIBLE` | `EASEMENT`      | Legal right to use another person’s land for a specific purpose without owning it. Can be transferred or inherited if tied to property rights. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`. Use PHRASE for detail: [right of way, water access, utility access]. |
| 🧠 | `INTANGIBLE` | `FISHRIGHT` | **Fishing Right**: Exclusive rights to fish in a body of water. Often recorded alongside hunting rights in noble charters. Use PHRASE for detail: [river, lake, coastal]. |
| 🧠 | `INTANGIBLE` | `FRANCHISE`     | Authorization to operate a business using the branding and model of an established company. Transfer may require guild, trade body, or franchisor approval. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`, `TRUSTEE`. Use PHRASE for detail: [restaurant franchise, retail franchise, service franchise]. |
| 🧠 | `INTANGIBLE` | `GUILDRIGHT` | **Guild Right**: Membership rights in a trade or craft guild, including privileges to work, vote, or hold office. Use PHRASE for detail: [blacksmith, goldsmith, weaver]. |
| 🧠 | `INTANGIBLE` | `HUNTRIGHT` | **Hunting Right**: Long-term or hereditary right to hunt in a defined region. Use PHRASE for detail: [forest, deer, boar]. |
| 🧠 | `INTANGIBLE` | `MINERALRIGHT` | **Mineral Right**: Legal right to extract minerals from land without owning the land itself. Use PHRASE for detail: [coal, gold, salt]. |
| 🧠 | `INTANGIBLE` | `MONOPRIGHT` | **Monopoly Right**: Historically granted exclusive rights to produce or sell specific goods. Use PHRASE for detail: [salt, beer, textiles]. |
| 🧠 | `INTANGIBLE` | `NAVIGATION`   | Rights to use a river/port for trade. Use PHRASE for detail: [river passage, port access, toll exemption, customs privilege, waterway transit, bridge passage, ferry rights, wharf usage, anchorage, cargo loading, market access, trade route, channel navigation, harbor berth, quay rights, lock passage, weir transit, mill stream, tidal waters, international waters]. |
| 🧠 | `INTANGIBLE` | `PATENT`        | Government grant giving the inventor exclusive rights to an invention for a set period. Often listed as an asset to be transferred to heirs or trusts. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`. Use PHRASE for detail: [mechanical patent, chemical patent, process patent]. |
| 🧠 | `INTANGIBLE` | `PERFRIGHT` | **Performance Right**: Exclusive right to perform specific works or hold performances. Use PHRASE for detail: [Theatre, fairs, play, music, opera, market festival]. |
| 🧠 | `INTANGIBLE` | `PROFLICENSE` | Professional License: Lifelong or transferable professional rights. Use PHRASE for detail: [medical, notary, surveyor]. |
| 🧠 | `INTANGIBLE` | `ROYALTY`       | Payment received for the ongoing use of a property or right, such as intellectual property or natural resources. Often bequeathed with attached rights to collect future payments. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`, `TRUSTEE`. Use PHRASE for detail: [book royalty, music royalty, mining royalty]. |
| 🧠 | `INTANGIBLE` | `SHAREHOLDING`  | Ownership interest in a company or corporation represented by shares. May require legal transfer documentation during probate. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`, `ADMINISTRATOR`. Use PHRASE for detail: [stock, equity stake, voting share]. |
| 🧠 | `INTANGIBLE` | `TITLE` | Hereditary or granted noble titles and dignities. Use PHRASE for detail: [duke, baron, count]. |
| 🧠 | `INTANGIBLE` | `TRADEMARK`     | Symbol, word, or phrase legally registered to represent a company or product. Can be inherited or transferred via business succession. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`, `TRUSTEE`. Use PHRASE for detail: [logo trademark, brand name, service mark]. |
| 🧠 | `INTANGIBLE` | `TRADERIGHT` | **Trade right**: Certified right to trade in a specific commodity or region. Use PHRASE for detail: [spices, silk, town market]. |
| 🧠 | `INTANGIBLE` | `WATERRIGHT` | **Water Right**: Right to use water for irrigation, milling, or other purposes. Use PHRASE for detail: [millstream, irrigation]. |
| 🧠 | `INTANGIBLE` | `OTHER`         | Any other intangible property or right not listed above. Must use PHRASE to clarify. Related ROLEs: `BENEFICIARY`, `HEIR`, `EXECUTOR`, `TRUSTEE`. Use PHRASE for detail: [custom right, unusual intangible asset]. |
| 💎 | `JEWELRY` | `BRACELET` | Wrist or arm bands, decorative or commemorative |
| 💎 | `JEWELRY` | `BROOCH` | Decorative fastening pins or clasps / Fastening pins or brooches |
| 💎 | `JEWELRY` | `CHAIN` | Neck or wrist chains, including medallions |
| 💎 | `JEWELRY` | `CROWN` | Crowns, tiaras, or coronets |
| 💎 | `JEWELRY` | `EARRING` | Pairs or singles of worn ear jewelry / Pierced or clip-on ear ornaments |
| 💎 | `JEWELRY` | `LARGE` | Substantial or prominent jewelry (crowns, ceremonial pieces) |
| 💎 | `JEWELRY` | `NECKLACE` | Worn around the neck; chains, beads, or pendants |
| 💎 | `JEWELRY` | `OTHER` | Any other jewelry; must include PHRASE to clarify |
| 💎 | `JEWELRY` | `RING` | Finger rings, signets, symbolic rings, or bands|
| 💎 | `JEWELRY` | `SMALL` | Miscellaneous or miniature items (e.g. cufflinks, tie pins) |
| 🌿 | `LAND` | `FIELD` | Specific cultivated or named open land plots (Open terrain used for crops or grazing) |
| 🌿 | `LAND` | `FOREST` | Wooded area for hunting or timber |
| 🌿 | `LAND` | `GARDEN` | Cultivated private or estate gardens, including ornamental, vegetable, or mixed-use areas. Also private gardens for ornamentals, vegetables |
| 🌿 | `LAND` | `ISLAND` | Defined islands or riverbanks, or small natural landforms in a body of water |
| 🌿 | `LAND` | `LAKE` | Freshwater bodies, enclosed ponds, or estate lakes |
| 🌿 | `LAND` | `MEADOW` | Hayfields, wet grassland, flat or damp terrain with grass and wildflowers or flat pastures |
| 🌿 | `LAND` | `ORCHARD` | Tree-based production areas such as apple or cherry orchards, vineyards |
| 🌿 | `LAND` | `OTHER` | Other types of land. Must include a `PHRASE` to clarify subtype not listed above |
| 🌿 | `LAND` | `TREE` | Singular marked trees (possibly commemorative), groves, or commemorative plantings |
| 🌿 | `LAND` | `VINEYARD` | Cultivated grape-growing areas |
| 🪪 | `LICENSE` | `HUNTING`   | Right to hunt in a specific region. Common in noble or rural records. |
| 🪪 | `LICENSE` | `MARRIAGE`  | Formal license to marry, typically from church or municipality. |
| 🪪 | `LICENSE` | `MEDICAL`   | Authority to practice medicine or related healing professions. |
| 🪪 | `LICENSE` | `TRADE`     | Certification for commercial or craft activity. May be linked to guilds. |
| 🪪 | `LICENSE` | `WEAPON`    | Legal permit to carry or own firearms or swords. |
| 🪪 | `LICENSE` | `OTHER`     | Any other license; must use PHRASE to clarify. |
| 🎞️ | `MEDIA` | `CLIPPING` | Cutouts from periodicals, often found in scrapbooks |
| 🎞️ | `MEDIA` | `DIGITAL` | Purely digital assets, like image files or PDFs |
| 🎞️ | `MEDIA` | `MANUSCRIPT` | Unpublished written/typed material |
| 🎞️ | `MEDIA` | `OTHER` | Any other media; must include PHRASE to clarify |
| 🎞️ | `MEDIA` | `PHOTO` | Photographs, negatives, or albums |
| 🎞️ | `MEDIA` | `POSTER` | Visual print item, often event- or era-specific |
| 🎞️ | `MEDIA` | `PUBLICATION` | Books, newspapers, or printed media |
| 🎞️ | `MEDIA` | `RECORDING` | Audio or video recordings, tapes, or discs |
| 🎞️ | `MEDIA` | `VIDEO` | Video recordings, films, or VHS tapes |
| 🕊️ | `MEMORIAL` | `ANCESTORTABLET`    | East Asian — traditional altar tablets with names of ancestors |
| 🕊️ | `MEMORIAL` | `BURIALPLOT`        | Designated area in cemetery where remains are interred |
| 🕊️ | `MEMORIAL` | `CARD`              | Printed card formats used for remembrance or ceremony: includes `INVITATIONCARD` (inviting recipient to a memorial or funeral event), `NOTICECARD` (General printed notice about death, memorial, or event), `SERVICECARD` (Small printed handout from funeral or wake), and similar formats except `MEMORIALCARD`. |
| 🕊️ | `MEMORIAL` | `CENOTAPH`          | Symbolic grave without remains |
| 🕊️ | `MEMORIAL` | `INSCRIPTION`       | Wording etched or engraved onto stone/memorial |
| 🕊️ | `MEMORIAL` | `MEMOIR`            | Published or private written remembrance of deceased |
| 🕊️ | `MEMORIAL` | `MEMORIALCANDLE`    | Religious or commemorative candle lit in memory |
| 🕊️ | `MEMORIAL` | `MEMORIALCARD`      | Bidprentje (Dutch), "memorial card", often handed out at funerals, sometimes mailed later |
| 🕊️ | `MEMORIAL` | `MEMORIALTREE`      | Modern — planted in memory of someone, often with plaque |
| 🕊️ | `MEMORIAL` | `MONUMENT`          | Statue or obelisk |
| 🕊️ | `MEMORIAL` | `NICHE`             | Columbarium niche for storing urns |
| 🕊️ | `MEMORIAL` | `OTHER`             | Anything that does not fit in these subtypes. Must have a `PHRASE` |
| 🕊️ | `MEMORIAL` | `PLAQUE`            | Affixed plate or wall |
| 🕊️ | `MEMORIAL` | `PRINTED`           | Funeralprogram (Printed service order or program from funeral), Memorial Notice (More generic – may refer to church bulletin, digital memorial, etc.), Obituary or probate clip (Printed newspaper obituary or probate or public posting about probate) (if clipped/saved), or Generic public announcement regarding a death or probate.)
| 🕊️ | `MEMORIAL` | `RELIGIOUSOBJECT`   | Religious item associated with remembrance (rosary, tablet, candle) |
| 🕊️ | `MEMORIAL` | `SHRINE`            | General — especially in Japan or indigenous cultures |
| 🕊️ | `MEMORIAL` | `STUMBLINGSTONE`    | Stolperstein – Holocaust marker |
| 🕊️ | `MEMORIAL` | `TOMBSTONE`         | Inscribed stone marking a grave; or gravestone (Physical headstone) |
| 🕊️ | `MEMORIAL` | `URN`               | Container for cremated remains, possibly with attached label, inscription, or ID |
| 🕊️ | `MEMORIAL` | `YAHRZEITBOARD`     | Jewish — wall of lights in synagogue for death anniversaries |
| 🪖 | `MILITARY` | `BADGE`     | Emblems indicating rank, unit, qualification, or skill (distinct from medals). |
| 🪖 | `MILITARY` | `DOCUMENT` | Service records or honorable discharge papers |
| 🪖 | `MILITARY` | `EQUIPMENT` | Military-issued gear such as field packs, binoculars, entrenching tools, or radios. |
| 🪖 | `MILITARY` | `MEDALS` | Military medals, awards, badges, or official decorations |
| 🪖 | `MILITARY` | `OTHER` | Any other military; must include PHRASE to clarify |
| 🪖 | `MILITARY` | `PASS`      | Military leave papers, deployment orders, or identification documents. |
| 🪖 | `MILITARY` | `UNIFORMS` | Military uniforms, clothing or gear issued during military service |
| 💶 | `MONEY`    | `BANKNOTE` | Paper currency including bills and notes. |
| 💶 | `MONEY`    | `COIN` | Minted metal currency for trade or collection. |
| 💶 | `MONEY`    | `CURRENCY`| Tangible cash assets: coins, paper, or historic money. |
| 💶 | `MONEY`    | `CREDIT` | Bonds, ledgers, debts or claims |
| 💶 | `MONEY`    | `DIAMOND`  | Loose or set diamonds held as assets or heirlooms. |
| 💶 | `MONEY`    | `GOLD`  | Bullion, coins, or gold-based valuables. |
| 💶 | `MONEY`    | `JEWEL`  | High-value individual gems (rubies, emeralds, sapphires). |
| 💶 | `MONEY`    | `OTHER` | Any other money; must include PHRASE to clarify |
| 💶 | `MONEY`    | `SILVER`     | Silver coins, bullion, or silverware with monetary value. |
| 💶 | `MONEY`    | `TREASURE`   | Hoards, strongboxes, or unrecovered stored wealth. |
| 🏢 | `ORGANIZATION` | `ADOPTIONAGENCY` | Organization that issued or facilitated an adoption certificate or placement. Use PHRASE for detail: [adoption office, placement agency, foster bureau] |
| 🏢 | `ORGANIZATION` | `ARCHIVE` | Repository for official or historical documents. Use PHRASE for detail: [city archive, family archive, digital archive] |
| 🏢 | `ORGANIZATION` | `CHARITY` | Nonprofit organization offering aid, shelter, or social care. Use PHRASE for detail: [soup kitchen, shelter, mutual aid society] |
| 🏢 | `ORGANIZATION` | `CHURCH` | Religious body or denomination functioning as a certifier or recorder. Use PHRASE for detail: [diocese, parish, synod, membership, vows] Also see `MONASTERY` or `RELIGIOUSORDER` |
| 🏢 | `ORGANIZATION` | `CIVILREGISTRY` | Government office recording births, deaths, marriages, etc. Use PHRASE for detail: [register office, population register, vital records bureau, ID, emigration permit, birth/death certificate, marriage record, drivers license, passport, emigration permit, exit stamp] Also see `GOVERNMENT` or `COURT`|
| 🏢 | `ORGANIZATION` | `COMPANY` | Named employer, business, corporate entity, or commercial institution that may act as employer, landowner, colonizer, or contractor. Use PHRASE for detail: [factory, shop, shipyard, publishing house, trading company, colonial company, plantation owner, land lease office, chartered company, brand, land lease, employer, charter, colonizing company] |
| 🏢 | `ORGANIZATION` | `CONSULATE` | Foreign affairs or consular office that handles migration, identification, and legal documents for citizens abroad. Use PHRASE for detail: [embassy, visa office, passport service, passport, visa, identity certificate, emigration service, immigration office/checkpoint, border control/crossing, birth abroad] |
| 🏢 | `ORGANIZATION` | `COURT` | Legal body issuing decisions, rulings, licenses, decrees, or certifications. Use PHRASE for detail: [family court, guardianship, name change, adoption decree, naturalization court, probate court, tribunal, will, inheritance]  Also see `GOVERNMENT` or `CIVILREGISTRY` |
| 🏢 | `ORGANIZATION` | `CROWN` | Sovereign authority or ruling monarchy acting as grantor, endorser, or legal arbiter. Granting rights, privileges, or land. Use PHRASE for detail: [kingdom, crown estate, monarch, colonial crown office, (royal) patent, crown/land grant, sovereign authority] |
| 🏢 | `ORGANIZATION` | `GOVERNMENT` | Named government body or agency not covered elsewhere, often involved in citizenship, identification, or administration. Sometimes responsible for military reward, land grant, or surveying not covered by `COURT` or `CIVILREGISTRY`. Use PHRASE for detail: [municipality, land grant office, cabinet, national agency, legislative body, colonial authority, parliament, agency, immigration office, citizenship service, tax office/records, building permit, trade license, homestead, zoning, registration, charter, passport, ID card, military discharge, pensions, social rights (widow claims), border control, visa center, naturalization (certificate), emigration permit, exit stamp, customs, residence permit, social security, ministry] |
| 🏢 | `ORGANIZATION` | `LANDOFFICE` | Designated office for managing, granting, or surveying public land. Use PHRASE for detail: [land grant board, homestead bureau, general land office, royal surveyor, appropriation bureau, allotment office, (house) contract, land deed, property transfer] |
| 🏢 | `ORGANIZATION` | `MEDICAL` | Institution related to health, treatment, or (DNA) testing. Can also be listed as a place of birth, death, or treatment (appearing in death, birth, or illness records). Use PHRASE for detail: [hospital, clinic, sanatorium, (DNA) laboratory, testing center] |
| 🏢 | `ORGANIZATION` | `MILITARY` | Armed services institution or unit listed on military records. Use PHRASE for detail: [infantry, regiment, navy bureau, discharge] |
| 🏢 | `ORGANIZATION` | `MONASTERY` | Religious residence or authority that records vows, ordinations, or membership. Use PHRASE for detail: [abbey, convent, priory, membership, vows] Also see `CHURCH` |
| 🏢 | `ORGANIZATION` | `NOTARY` | Office where a public officer called a notary public provides services related to document authentication and witnessing of legal documents. Use PHRASE for detail: [notarial archive, deed office, legal desk, will, deed, marriage contract, guardianship, property deed, land deed, power of attorney, business contract, affidavits, loan documents, partnership, inheritance] |
| 🏢 | `ORGANIZATION` | `OTHER` | Any organization not covered above. Must include a PHRASE. Use PHRASE for detail: [commission, taskforce, cooperative] |
| 🏢 | `ORGANIZATION` | `PRISON` | Penal institution mentioned in legal or identity documents. Use PHRASE for detail: [penitentiary, correctional facility, jail] |
| 🏢 | `ORGANIZATION` | `REGISTRY` | Civil registry or governmental record-holding or administrative body, sometimes involved in ownership transfer or land survey. Use PHRASE for detail: [land registry, property register/transfer, cadastral archive, trade register, record office, land title office, civil registration, ownership archive, title, land ownership] |
| 🏢 | `ORGANIZATION` | `RELIGIOUSORDER` | Specific religious group distinct from `CHURCH`. Use PHRASE for detail: [Jesuits, Benedictines, Franciscans] |
| 🏢 | `ORGANIZATION` | `RIGHT` | Organization or authority granting legal, civic, natural, or usage rights. Use PHRASE for detail: [(fishing- hunting- grazing- etc right, mineral right, logging permit, canal access, building right, broadcast license, licenses, airspace, toll right, franchise, water right, trademark, copyright, brand, patent, usage permit, access right, zoning right] |
| 🏢 | `ORGANIZATION` | `SCHOOL` | Academic or degree-granting institution where education occurs or credentials are issued. Use PHRASE for detail: [school, college, university, seminary, academy, institute] |
| 🏢 | `ORGANIZATION` | `TRADEUNION` | Guild, craft organization, or labor union involved in employment, advocacy, or disputes. Use PHRASE for detail: [apprenticeship record, (guild)certification board, professional license, worker association, work permit, carpenter’s guild, miners’ union, textile association, workers’ council] |
| 🏢 | `ORGANIZATION` | `UNION` | Group formed for representation, support, or shared interests. Use PHRASE for detail: [marriage registrar, trade union, brotherhood, Masonic lodge, labor union, professional guild, trade license] |
| 👤 | `PERSON`   | `AN_ADOPTION` | Annotated: Adoption status noted or changed (e.g., “now adopted by X”). |
| 👤 | `PERSON`   | `AN_ALIAS`    | Annotated: Alternative or assumed name noted. |
| 👤 | `PERSON`   | `AN_ARRIVE`   | Annotated: Person appears as newly arrived in the household or area. |
| 👤 | `PERSON`   | `AN_BAPTISM`  | Person babtized during the record’s timeframe (e.g., family marginal note). |
| 👤 | `PERSON`   | `AN_BIRTH`    | Person born during the record’s timeframe (e.g., census marginal note). |
| 👤 | `PERSON`   | `AN_DEATH`    | Annotated: Person died during the record’s timeframe (often as marginal or side entry). |
| 👤 | `PERSON`   | `AN_DEPORTATION`| Annotated: Person forcibly removed or relocated (e.g., institutional or state record). |
| 👤 | `PERSON`   | `AN_DISCHARGE`| Annotated: Person officially released from service, duty, or institution. |
| 👤 | `PERSON`   | `AN_DIVORCE`  | Annotated: Person is divorced , often also gives the date |
| 👤 | `PERSON`   | `AN_INHERIT`  | Annotated: Gift, Inheritance or succession noted. Use PHRASE for detail: [Gift, Inheritance or Succession] (e.g., on land or property registers) |
| 👤 | `PERSON`   | `AN_LEAVE`    | Annotated: Person moved out or left the location, household, or institution. |
| 👤 | `PERSON`   | `AN_MARRIAGE` | Annotated: Marriage note about this person (e.g., “now wife of X” — not the main event). |
| 👤 | `PERSON`   | `AN_MENTION`  | Annotated: Person mentioned in a marginal note or side entry, with no event detail. |
| 👤 | `PERSON`   | `AN_MOVE`     | Annotated: Informal address or location change noted. |
| 👤 | `PERSON`   | `MAIN`        | Primary individual described by the document (e.g., census row, applicant, owner). |
| 👤 | `PERSON`   | `AN_OCCUPATION`| Annotated: Occupation or role added informally (e.g., “now a carpenter”).  |
| 👤 | `PERSON`   | `AN_OTHER`    | Annotated: Involved in an annotated non-standard way; use `PHRASE` to clarify. |
| 👤 | `PERSON`   | `OTHER`       | Involved in a non-standard way; use `PHRASE` to clarify. |
| 👤 | `PERSON`   | `AN_PROMOTION`| Annotated: Person noted as promoted in rank or job (e.g., in military, employment). |
| 👤 | `PERSON`   | `AN_RETURN`   | Annotated: Person noted as returned to household or prior location. |
| 👤 | `PERSON`   | `AN_TRANSFER` | Annotated: Relocated between units, schools, prisons, or institutions. Could also be the original owner for gifts or inheritance. Use PHRASE for detail: [Gift, Inheritance or Succession, land, benefit, unit, school, prison, institution and more] |
| 👤 | `PERSON`   | `AN_WITNESS`  | Annotated: Present in official or witnessing capacity (e.g., signer, observer). |
| 🏘️ | `PROPERTY` | `BUILDING` | Houses, barns, or other standalone structures |
| 🏘️ | `PROPERTY` | `BUSINESS` | Commercial premises or named shops |
| 🏘️ | `PROPERTY` | `COTTAGE` | Small dwellings or single-family homes |
| 🏘️ | `PROPERTY` | `ESTATE` | Named residential estates or manors |
| 🏘️ | `PROPERTY` | `FARM` | Agricultural land with functional buildings |
| 🏘️ | `PROPERTY` | `HOMESTEAD` | Self-sufficient dwellings, often family-run |
| 🏘️ | `PROPERTY` | `HOUSE` | Individual dwellings, including townhouses |
| 🏘️ | `PROPERTY` | `OTHER` | Any other property; must include PHRASE to clarify |
| 🏘️ | `PROPERTY` | `PLOT` | Undeveloped or minimally developed parcels of land |
| 🏘️ | `PROPERTY` | `SHED` | Outbuildings for storage or minor functions |
| 🏘️ | `PROPERTY` | `STABLE` | Horse or livestock buildings |
| 🏘️ | `PROPERTY` | `STRUCTURE` | Built items not fitting other categories (sheds, windmills, etc.) |
| 🏘️ | `PROPERTY` | `TOWER` | Watchtowers, bell towers, or isolated structures |
| 🏘️ | `PROPERTY` | `WORKSHOP` | Places used for craft or trade activities |
| ✝️ | `RELIGIOUS` | `ALTAR` | Fixed or movable altars |
| ✝️ | `RELIGIOUS` | `ARTIFACT` | Ritual objects or relics |
| ✝️ | `RELIGIOUS` | `BIBLE` | Sacred book — can also be a family-held Bible recording vital events, often annotated by multiple generations |
| ✝️ | `RELIGIOUS` | `BOOK` | Bound volumes used in liturgy or instruction — such as hymnals, prayer books, or printed scriptures. |
| ✝️ | `RELIGIOUS` | `ICON` | Painted or sculpted sacred images |
| ✝️ | `RELIGIOUS` | `OTHER` | Any other religious; must include PHRASE to clarify |
| ✝️ | `RELIGIOUS` | `RELIQUARY` | Containers or holders of relics |
| ✝️ | `RELIGIOUS` | `TEXT` | Sacred writings or manuscript excerpts — including scrolls, copied passages, or unbound religious documents. |
| ✝️ | `RELIGIOUS` | `VESTMENT` | Religious clothing or priestly or ceremonial garments |
| 🛠️ | `TOOLS` | `AGRICULTURE` | Implements for farming or animal care (plow, scythe, shears, yoke) – includes FARMING / Implements for farming or animal care (plow, scythe, shears, yoke) – includes FARMING |
| 🛠️ | `TOOLS` | `BLACKSMITH` | Tools used in smithing or forging (anvil, tongs, bellows, hammer) – part of TRADESMAN / Tools used in smithing or forging (anvil, tongs, bellows, hammer) – part of TRADESMAN |
| 🛠️ | `TOOLS` | `CARPENTRY` | Woodworking or joinery tools (saw, plane, chisel, square, lathe) – part of TRADESMAN / Woodworking or joinery tools (saw, plane, chisel, square, lathe) – part of TRADESMAN |
| 🛠️ | `TOOLS` | `DOMESTIC` | Household implements (butter churn, spinning wheel, mangle, iron) – includes KITCHEN / Household implements (butter churn, spinning wheel, mangle, iron) – includes KITCHEN |
| 🛠️ | `TOOLS` | `EQUIPMENT` | Machinery, tools, or business-related gear used in production, repair, or trade. |
| 🛠️ | `TOOLS` | `FARMING` | Plows, hoes, scythes, or similar instruments |
| 🛠️ | `TOOLS` | `KITCHEN` | Household tools for preparing food |
| 🛠️ | `TOOLS` | `MEASUREMENT` | Devices for length, weight, volume, time (scale, clock, astrolabe) |
| 🛠️ | `TOOLS` | `MEDICAL` | Surgical or diagnostic tools (forceps, lancet, stethoscope) |
| 🛠️ | `TOOLS` | `MILITARY` | Swords, muskets, or other weapons / Weapons and related gear (sword, musket, pike, bayonet, powder horn, cartridge pouch, scabbard, training sabres) |
| 🛠️ | `TOOLS` | `MUSICAL` | Tuners, bows, metronomes, pipe reamers — not the instruments, just the tools |
| 🛠️ | `TOOLS` | `NAVIGATION` | Compasses, sextants, maps, logbooks used for travel and sea navigation |
| 🛠️ | `TOOLS` | `OTHER` | Specialized tools not covered above (e.g., glassblowing pipe, cobbler’s last) |
| 🛠️ | `TOOLS` | `TEXTILE` | Looms, needles, shuttles, distaffs, and thread winders – part of TRADESMAN |
| 🛠️ | `TOOLS` | `TRADESMAN` | Artisan tools, tailor’s kit, smith gear, bakery, butcher etc. Use `PHRASE` to clarify. |
| 🛠️ | `TOOLS` | `WEAPON` | Any possible weapon, use `PHRASE` to clarify. |
| 🛠️ | `TOOLS` | `WRITING` | Inkwells, styluses, typewriters, wax tablets, rulers, scribal gear |
| 🚗 | `TRANSPORT` | `BICYCLE` | Two- or three-wheeled pedal-powered vehicles, including bicycles, tricycles, tandems and cargo cycles. |
| 🚗 | `TRANSPORT` | `BOAT` | Watercraft of any size — from small rowboats to yachts or fishing vessels. Includes personal or commercial use. |
| 🚗 | `TRANSPORT` | `CARRIAGE` | Traditional horse-drawn vehicles for people or cargo |
| 🚗 | `TRANSPORT` | `CART` | Two-wheeled or utility carts, often for manual or animal use |
| 🚗 | `TRANSPORT` | `COACH` | Passenger or ceremonial transport, often enclosed |
| 🚗 | `TRANSPORT` | `OTHER` | Any other transport; must include PHRASE to clarify |
| 🚗 | `TRANSPORT` | `SHIP` | Large sea-going vessels, often named — used in immigration, military, or long-distance commercial transport. |
| 🚗 | `TRANSPORT` | `SLED` | Land or snow-based sleds, sleighs |
| 🚗 | `TRANSPORT` | `VEHICLE` | General motorized or wheeled transport (unspecified) |
| 🚗 | `TRANSPORT` | `WAGON` | Larger transport, often four-wheeled, cargo or passenger use |
| 🚗 | `TRANSPORT` | `WHEELCHAIR` | Self-propelled or assisted mobility chairs |
| 🌀 | `OTHER`     | `OTHER` | Any other entity; must include PHRASE to clarify |


