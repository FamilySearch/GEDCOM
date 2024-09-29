# Appendix B: GEDCOM Examples


## General remarks:

These examples differ a bit from **"Real GEDCOM"**.  
Thats because of the following:

- For easier reading the lines are indented. Now it is "visible" where the "blocks" inside a GEDCOM structure start and end.  
- Also, comment is added behind some of the GEDCOM lines, so its easier to see where a certain line is based on (what GEDCOM7 and/or GEDCOM-L tags)
- Some lines look like "....." that means they are left out for that example. But should be filled, in a real GEDCOM.
- A line that says "CREA and CHAN" should be the real values instead.

#### $\color{red}{The\ above\ should\ ofcourse\ be\ done\ right\ in\ a\ real\ GEDCOM\ file!}$ 
**It only serves as explanation and better visibility here.**

Many examples have some explaining text added, about the "What" and "Why" of certain parts of it.

***

## Examples for SPLAC:
Here some examples for `SPLAC` are worked out, as complete as possible. Because with that we can see the possibilities of the extended `SPLAC`Record.  

`SPLAC`, as it is already designed at this moment, is a newer and way better version of the original `PLAC` data as it is defined now.  

This add's some changes to that design, and made it a bit of a combination with the `_LOC` from the GEDCOM-L specs. The comments after the TAG's often point to that.

#### $\color{red}{SPLAC\ example 1:}$ 

Here a cemetery and a (fantasy) addres in Sneek are used, which is a city in the province of Friesland in the Netherlands. The cemetery had 2 locations (and names) depending on a date.  
Sneek had a different name, before and after 1230.  
The province Friesland had more names and belonged in a different hierarchy depending on a date period.  
Same for the Country The Netherlands itself.  
So a lot of different problems are in this one example.

Here the cemetery probably should have been in a religious hierarchy, but to keep it simple it is said to be in a political hierarchy.

### SPLAC of the RK Cemetery in Sneek (Valid from 1892)
From 1892, there was an RK Cemetery in Sneek (described in the first `PERIOD`), but before the year 1892 the General Cemetery was used also for Catholics (this cemetery is described in the second `PERIOD`)  

**Just as an example**, this `SPLAC` uses 5 systems of determining the position: `MAP, ADDR, POST, GOV` and `MAID`.  
Also, the 2 `PERIOD`s in this `SPLAC`, **both point to the same City: Sneek**.  

#### This SPLAC has a LOCATION TYPE with 4 parameters:
**1 TYPE LOCATION, POLI, 89, Cemetery**
- The type: `LOCATION` itself
- Followed by the type of the administrative hierarchy, here POLI (political)
- Followed bij the `GOV` number type of a cemetery
- Followed by an optional descriptive text
- Each separated by a comma.

Refer to the specification itself, for a definition of this `TYPE`.
(Compare them in the examples, to the `SPLAC`-Types of the other `SPLAC`s.)

```gedcom
0 @SP53@ SPLAC RK Begraafplaats Sneek   Roman catholic cemetery 
  1 LANG nl
  1 TYPE LOCATION, POLI, 89, Cemetery    (89=cemetery, POLI=Political hierarchy) 
  1 PERIOD FROM 1892
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM 1892          (existed since 1892)
    2 TRAN RK Begraafplaats Sneek
      3 LANG nl
    2 MAP
      3 LATI N53.040175
      3 LONG E5.669792
    2 ADDR Leeuwarderweg 83
      3 CONT 8603 CM Sneek
      3 CONT Nederland
    2 POST 8603CM             (<POSTAL_CODE>)
    2 GOV RKBEEKJO23UA
    2 MAID JO23ua             (Maidenhead code: https://www.egloff.eu/qralocator/)
    2 SPLAC @SP1@             ((_LOC in GEDCOM_L) SPLAC: City Sneek)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1230        (City Sneek existed AFTER 1230)
  1 PERIOD From 1827
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1827          (existed since 1827)
    2 TRAN Algemene Begraafplaats Sneek  (Other cemetery, used before 1892
      3 LANG nl
    2 MAP                     Slightly diff. position then the other cemetery in the first PERIOD
      3 LATI N53.039586
      3 LONG E5.661156
    2 ADDR Kerkhoflaan 31a
      3 CONT 8602 TX Sneek
      3 CONT Nederland
    2 POST 8602TX             (<POSTAL_CODE>)
    2 GOV ALGEEKJO23TA
    2 MAID JO23ta             (Maidenhead code: https://www.egloff.eu/qralocator/)
    2 SPLAC @SP1@             ((_LOC in GEDCOM_L) link to SPLAC: City Sneek)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1230        (City Sneek existed AFTER 1230)
  1 CREA
    2 DATE 22 JUL 2022
      3 TIME 20:56:25
  1 CHAN
    2 DATE 29 SEP 2024
      3 TIME 15:25:18
```
***
###  SPLAC of a Home address in Sneek.
#### The address links to the City of Sneek itself.
```gedcom
0 @SP8@ SPLAC Marktstraat 123 Sneek   9Home at non-existing nr in the Marktstraat in Sneek0
  1 LANG nl
  1 TYPE LOCATION, POLI, 236, House (House includes GOV-Type) 
  1 PERIOD FROM 1400
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 1400          (Fantasy: The Marktstraat existed since 1400)
    2 TRAN Marktstraat 125 Sneek
      3 LANG nl
    2 MAP
      3 LATI 53.03243992883088
      3 LONG 5.6588164028087515
    2 ADDR Marktstraat 125    (Constructed according to GEDCOM-L)
      3 CONT 8601 CR Sneek
      3 CONT Nederland
    2 POST 8601CR             (<POSTAL_CODE>)
    2 SOUR .......        
    2 NOTE .......
    2 SPLAC @SP1@             ((_LOC in GEDCOM_L) link to SPLAC: City Sneek)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1230        (City Sneek existed AFTER 1230)
  1 CREA
    2 DATE 22 JUL 2022
      3 TIME 20:56:25
  1 CHAN
    2 DATE 21 SEP 2024
      3 TIME 15:25:18
```
***
###  SPLAC of todays City of Sneek.
#### Sneek links to the province of Friesland today AND in the old days
So there are 2 links inside, 1 in each `PERIOD` structure. Both go to the same City Sneek.
```gedcom
0 @SP1@ SPLAC Sneek   This is the "Main Name", shown in tree's and records
  1 LANG nl
  1 TYPE CITY, POLI, 51       (regional authority, includes GOV-Type) 
  1 PERIOD From 1230
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1230
    2 TRAN SNEEK
      3 LANG nl
    2 TRAN Snits 
      3 LANG fy
    2 MAP
      3 LATI N12.3
      3 LONG W45.6
      3 RADIUS 3km
      3 EXID .........
      3 NOTE ........
    2 GOV  GEMEEKJO23TA       (https://gov.genealogy.net/item/show/GEMEEKJO23TA)
    2 GOV  object_1305874     (https://gov.genealogy.net/item/show/object_1305874)
    2 SOUR @S77@
      3 QUAY 2
    2 OBJE
      3 TITL The City: Sneek
      3 FILE https://nl.wikipedia.org/wiki/Sneek_(stad)
        4 FORM HTML
      3 NOTE
    2 SPLAC @SP2@    (_LOC in GEDCOM_L) link to SPLAC: province Friesland as it is today)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1 JAN 1880 TO 31 DEC 1899
    2 PHRASE Some text here
    2 NOTE  Texts about the Shared place structure. (can be many notes)
  1 PERIOD FROM 1000 TO 1230
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM 1000 TO 1230
    2 TRAN Ter Snake 
      3 LANG nl
      3 NOTE Notes about the "province" in those days.
      3 SOUR @S1@
        4 multimedia link
        4 NOTE's for the Source
    2 SPLAC @S2@              (links to SPLAC:Friesland, "KINGDOM" PERIOD)     
      3 TYPE CULT             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1 JAN 1000 TO 31 DEC 1500
    2 PHRASE Some text here
    2 NOTE about the Shared place structure. (can be many notes)
  1 CREA
    2 DATE 22 JUL 2022
      3 TIME 20:56:25
  1 CHAN
    2 DATE 26 SEP 2024
      3 TIME 15:25:18
```
***
###  SPLAC of the province of Friesland.

#### First PERIOD, the default period.
This default period, is valid since 1450. It links to the general `SPLAC` from the Netherlands.
#### Second PERIOD in here, is only about NAME change, so it has no further link.
This period links to the same "higher" Jurisdiction as the first `PERIOD` in this `SPLAC`, as it does not have a link of its own. (But if someone wished a link can be added)  

But we could also define that each `PERIOD` ALWAYS must have a link, to make it easier for programs to deal with them.  
#### Third PERIOD, is type USER
Contents here is partly fantasy.  
Because the third `PERIOD` is of type `USER`, there is a link to a `SUBM` record added, to be able to define the SUBMitter responsible for the "conclusion" of the information.
```gedcom
0 @SP2@ SPLAC Friesland
  1 LANG nl
  1 ABBR FR                   (abbreviation of the NAME, optional)
    2 TYPE ISO 3166           (official abbreviation type of the Province Name Friesland)
  1 TYPE PROVINCE, POLI, 45   (division smaller then country) 
  1 PERIOD FROM 1450
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM 1450
    2 GOVID FRIANDJO23VE      (<GOV_IDENTIFIER>)  
      3 SOUR @S9@
        4 QUAY 2
      3 OBJE
        4 TITL Province of Friesland
        4 FILE https://gov.genealogy.net/item/show/FRIANDJO23VE
          5 FORM HTML
        4 NOTE
    2 SPLAC @SP10@            (link to the SPLAC: NETHERLANDS)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1 JAN 1880
    2 PHRASE Some text here
    2 NOTE  Texts about the Shared place structure. (can be many notes)
  1 PERIOD FROM 1 JAN 1997
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM 1 JAN 1997
    2 NAME Friesland
      3 LANG nl
    2 TRAN Fryslân 
      3 LANG fy
    2 NAME It Heitelân
      3 LANG fy
    2 TRAN Het Vaderland
      3 LANG nl
  1 PERIOD FROM 1000 TO 1450
    2 TYPE USER               (USER= conclusion perspective)
    2 DATE FROM 1000 TO 1450
    2 NAME Ter Snake          (Name of the province in this timeframe)
      3 LANG nl
  - - -
  - - -
    2 SPLAC @SP10@            (link SPLAC: De Lage Landen (Later: The Netherlands))
      3 TYPE RELI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE DATE 0 TO 1648
    2 PHRASE Some text here
    2 NOTE  Texts about the Shared place structure. (can be many notes)
    2 SUBM @B001@             (SUBMitter responsable for the "conclusion" of the information)
CREA and CHAN
```
***
### SPLAC of the NETHERLANDS after 1648
#### This is the first description of the Netherlands, as "Country" from 1648 till today.

```gedcom
0 @SP10@ SPLAC NEDERLAND
  1 LANG nl
  1 TYPE COUNTRY, POLI, 7     (Federal State) 
  1 PERIOD FROM 1648
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM 1648
    2 GOV  object_1280959     (<GOV_IDENTIFIER> of the Netherlands)
      3 SOUR @S99@
        4 QUAY 2
      3 OBJE
        4 TITL Kingdom of the Netherlands
        4 FILE https://gov.genealogy.net/item/show/object_1280959
          5 FORM HTML
        4 NOTE
    2 SPLAC @SP2000@          (link to the SPLAC: EARTH)
      3 TYPE GEOG             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
    2 PHRASE Some text here
    2 NOTE  Texts about the Netherlands. (can be many notes)
  1 PERIOD FROM 0 TO 1648
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM 0 TO 1648
    2 SPLAC @SP2000@          (link to the SPLAC: EARTH)
      3 TYPE GEOG             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
    2 PHRASE Some text here
    2 NOTE  Texts about the Netherlands in those days
CREA and CHAN
```
***
### SPLAC of the Netherlands before 1648
#### Second description of the Netherlands before 1648, as part of the Roman Empire.
(Partly fantasy)
```gedcom
0 @SP11@ SPLAC De lage Landen
  1 LANG nl
  1 TYPE COUNTRY, POLI, 31    (Kingdom, Part of the Holy Roman Empire) 
  1 PERIOD FROM 0 TO 1648
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 0 TO 1648
    2 SPLAC @SP2000@          (link to the SPLAC: EARTH)
      3 TYPE GEOG             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
    2 PHRASE Some text here
    2 NOTE  Texts about the Netherlands in those days
CREA and CHAN
```
***
### SPLAC of the Earth (highest Jurisdiction)
#### The EARTH jurisdiction, fantasy. Just to have a complete jurisdiction system from high to low.
```gedcom
0 @SP2000@ SPLAC EARTH
  1 LANG en
  1 TYPE EARTH
  1 PERIOD
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM  UNKNOWN
CREA and CHAN
```

***

#### $\color{red}{SPLAC\ example\ 2:}$ 

### SPLAC of the city of Amsterdam and some of its suburbs

The "parent" of a City (or other jurisdiction) changed over the years:  

Amsterdam was first mentioned in a doc around 1275 as "Amstelledamme" (a dam in the "river" Amstel). But it was a way smaller city. Over the years it grew and "has eaten" some of the smaller little villages around it. (Sloten, Buiksloot, Nieuwendam, Nieuwer Amstel)  
But those smaller villages, once were independant too, and pointed to the province of Noord-Holland. Until one day they became part of Amsterdam, so from that day their "parent" was no longer a province, but another city: Amsterdam, which in turn pointed to the province Noord-Holland.

In `SPLAC's` that looks like this:

```gedcom  
0 @SP5@ SPLAC Sloten
  1 LANG nl
  1 TYPE CITY, POLI, 51       (regional authority, includes GOV-Type) 
  1 PERIOD From 800
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 800
  .....                       (MAP structure or other location definition)
  .....
    2 SPLAC @SP2@             (link to SPLAC: province Noord-Holland)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 800
  1 PERIOD FROM 1921
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1921
  .....                       (MAP structure ot other location definition)
  .....
    2 SPLAC @SP1@             (link to SPLAC: City Amsterdam)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1921
CREA and CHAN

0 @SP6@ SPLAC Buiksloot
  1 LANG nl
  1 TYPE CITY, POLI, 51       (regional authority, includes GOV-Type) 
  1 PERIOD From 1100
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1100
  .....                       (MAP structure or other location definition)
  .....
    2 SPLAC @SP2@             (link to SPLAC: province Noord-Holland)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1100
  1 PERIOD FROM 1921
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1921
  .....                       (MAP structure ot other location definition)
  .....
    2 SPLAC @SP1@             (link to SPLAC: City Amsterdam)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1921
CREA and CHAN

0 @SP7@ SPLAC Nieuwer Amstel
  1 LANG nl
  1 TYPE CITY, POLI, 51       (regional authority, includes GOV-Type) 
  1 PERIOD From 1200
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1200
  .....                       (MAP structure or other location definition)
  .....
    2 SPLAC @SP2@             (link to SPLAC: province Noord-Holland)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1200
  1 PERIOD FROM 1896
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1896
  .....                       (MAP structure ot other location definition)
  .....
    2 SPLAC @SP1@             (link to SPLAC: City Amsterdam)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1896
CREA and CHAN

0 @SP1@ SPLAC Amsterdam
  1 LANG nl
  1 TYPE CITY, POLI, 51       (regional authority, includes GOV-Type) 
  1 PERIOD From 1275
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE From 1275          (First mentioned in a doc as "Amstelledamme")
  .....                       (MAP structure ot other location definition)
  .....
    2 SPLAC @SP2@             (link to SPLAC: province Noord-Holland)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1 JAN 1880 TO 31 DEC 1899
CREA and CHAN

0 @SP2@ SPLAC Noord-Holland
  1 LANG nl
  1 TYPE PROVINCE, POLI, 45   (division smaller then country) 
  1 PERIOD FROM 1000
    2 TYPE SOURCE             (SOURCE=researcher perspective)
    2 DATE FROM 1000
  .....
  .....
    2 SPLAC @SP10@            (link to the SPLAC: NETHERLANDS)
      3 TYPE POLI             (HIERARCHICAL_RELATIONSHIP,POLI,RELI,GEOG,CULT)
      3 DATE FROM 1200        (fantasy)
CREA and CHAN
```

***

#### $\color{red}{SPLAC\ example\ 3:}$ 

### SPLAC of the city of Subotica in Serbia, that "moved" from 1 parent to another.

The "Parent SPLAC" of a Place, might have changed over the years. (town that was in the Austo-Hungarian empire, and at another time Hungary, and at another time Serbia)  

As an example we look at Subotica in Serbia for that. Now the following scheme is not complete and might contain errors, but for our example thats not so important.

Schematically it is:

| **DATE**          | **Place name**               | **Parent SPLAC (State/Political Entity)**                | **Description**                                                      | **Relationship**                                  |
|-------------------|------------------------------|----------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------|
| **Before 1526**    | Zabotka / Zabatka            | Kingdom of Hungary (1000–1526)                           | Pre-Ottoman rule during the independent medieval Kingdom of Hungary   | POLI                                              |
| **1526**           | Zabadka / Zabatka            | Ottoman Empire                                            | City nearly destroyed during the Ottoman conquest                    | POLI / RELI (due to Ottoman religious influence)  |
| **1686**           | Zabatka / Szabadka           | Habsburg Monarchy (Royal Hungary, 1526–1867)              | Ottoman rule ended, became part of the Habsburg Monarchy             | POLI / RELI (Catholic influence of the Habsburgs) |
| **1779**           | Maria-Theresiapolis          | Habsburg Monarchy (Hungarian Empire, part of Habsburg-controlled Hungary) | Named after Maria Theresia and given royal city status | CULT (cultural influence due to royal recognition)|
| **1849**           | Subotica / Szabadka          | Voivodeship of Serbia and Banat of Temeschwar             | After Hungarian Revolution of 1848, became part of this entity       | POLI / GEOG (geographically redefined)            |
| **1876**           | Subotica / Szabadka          | Austro-Hungarian Empire (Kingdom of Hungary, 1867–1918)   | Integrated back into the Hungarian Kingdom under the Austro-Hungarian Empire | POLI                                              |
| **1918**           | Szabadka (Subotica)          | Kingdom of Serbs, Croats, and Slovenes (unofficially)     | Post-World War I change                                              | POLI                                              |
| **June 4, 1920**   | Subotica / Szabadka          | Kingdom of Serbs, Croats, and Slovenes                    | Officially part of the Kingdom after the Treaty of Trianon           | POLI                                              |
| **October 3, 1929**| Subotica / Szabadka          | Yugoslavia                                                | Kingdom of Yugoslavia formed under King Alexander I                  | POLI                                              |
| **1941**           | Subotica (Szabadka in Hungarian)| Hungary                                                 | Annexed by Hungary during World War II                               | POLI / CULT (Hungarian cultural influence)        |
| **1945**           | Subotica (Szabadka in Hungarian)| Socialist Federal Republic of Yugoslavia                | Socialist state under Tito                                           | POLI                                              |
| **1946**           | Subotica (Szabadka in Hungarian)| Socialist Federal Republic of Yugoslavia                | Established as part of post-war Yugoslavia                           | POLI                                              |
| **April 27, 1992** | Subotica (Szabadka in Hungarian)| Federal Republic of Yugoslavia (Serbia and Montenegro) | After Yugoslavia broke up                                            | POLI                                              |
| **2006**           | Subotica (Szabadka in Hungarian)| Independent Serbia                                       | Serbia becomes fully independent                                     | POLI                                              |

#### As we see here, some realations were in fact a combination, for instance "POLI/RELI", so maybe we should allow this enum tag to have 2 values, separated by a slash **("/")**, as in the following examples.

There will be a subset of this scheme in the following SPLAC's and not all Parent SPLAC's will contain all information.  

 **Its just to get an idea how to solve this problem!**

## SPLAC City: Subotica (Zabadka / Zabatka) in Serbia
This City has had its Name changed over the years and also the "superior" of the place changed many times.

```gedcom
0 @SP001@ SPLAC Subotica      ( City in Serbia) 
  1 LANG en
  1 TYPE CITY, POLI,          (regional authority, includes GOV-Identifier)
  1 PERIOD
    2 TYPE SOURCE             SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 27 APR 1992         
    2 TRAN Subotica
      3 LANG en
    2 tran Szabadka
      3 LANG hu
    2 MAP
      3 LATI 46.09609651
      3 LONG 19.680925168
  .....
  .....
    2 SPLAC @SP002@           ( (_LOC in GEDCOM_L) link to SPLAC: Independant Serbia (today)
      3 TYPE POLI             
      3 DATE FROM 27 APR 1992
  .....
  1 PERIOD 
    2 TYPE SOURCE             
    2 DATE TO 1526        
    2 TRAN Zabadka
      3 LANG hu
    2 TRAN Zabatka
      3 LANG hu
  .....
    2 SPLAC @SP003@           (link to SPLAC: Kingdom of Hungary (1000-1526)  )
      3 TYPE POLI             
      3 DATE TO 1526
  .....
  1 PERIOD 
    2 TYPE SOURCE             
    2 DATE FROM 1526 TO 1686       
    2 TRAN Zabotka
      3 LANG hu
    2 TRAN Zabatka
      3 LANG hu
  .....
    2 SPLAC @SP004@           ( (_LOC in GEDCOM_L) link to SPLAC: Ottoman Empire)
      3 TYPE POLI / RELI      (Due to Ottoman religious influence)       
      3 DATE FROM 1526 TO 1686
  .....
  1 PERIOD                    (Ottoman rule ended became part of the Habsburg Monarchy)
    2 TYPE SOURCE             
    2 DATE FROM 1686 TO 1779       
    2 TRAN Zabotka            Name did not change so it MUST be set otherw. Name is from 1ePeriod
      3 LANG hu
    2 TRAN Zabatka
      3 LANG hu
  .....
    2 SPLAC @SP005@           (link SPLAC: Habsburg Monarchy - Royal Hungary, 1526-1867)
      3 TYPE POLI/ RELI       (Due to religious Catholic influence of the Habsburgs)             
      3 DATE FROM 1686 TO 1779
  .....
  1 PERIOD 
    2 TYPE SOURCE             
    2 DATE FROM 1779 TO 1849  (Hungarian Empire, part of Habsburg controlled Hungary)     
    2 TRAN Maria-Theresiapolis   (Given by Empress Maria Theresia)
      3 LANG nl
  .....
    2 SPLAC @SP005@           (link SPLAC: Hungarian Empire - Hungarian Empire, part of Habsburg controlled Hungary)
      3 TYPE CULT             (Cultural influence due to royal recognition)             
      3 DATE FROM 1779 TO 1849
  .....
  1 PERIOD 
    2 TYPE SOURCE             
    2 DATE FROM 1849 TO 1876  (parent:Voivodeship of Serbia and Banat of Temeschwar)     
    2 TRAN Zabotka            
      3 LANG hu
    2 TRAN Zabatka
      3 LANG hu
  .....
    2 SPLAC @SP007@           (Voivodeship of Serbia and Banat of Temeschwar FROM 1849 TO 1918)
      3 TYPE POLI/ GEOG       (geographically redefined as part of a larger region)             
      3 DATE FROM 1849 TO 1876
  .....
  1 PERIOD 
    2 TYPE SOURCE             
    2 DATE FROM 1876 TO 1918  (Austro-Hungarian Empire, Kingdom of Hungary, 1867-1918)     
    2 TRAN Zabotka            
      3 LANG hu
    2 TRAN Zabatka
      3 LANG hu
  .....
    2 SPLAC @SP006@           (Link to SPLAC: Austro-Hungarian Empire, Kingdom of Hungary, 1867-1918)
      3 TYPE POLI             
      3 DATE FROM 1876 TO 1918 (integrated back in Hungarian empire)
 .....
 .....
  1 CREA
    2 DATE 22 JUL 2022
      3 TIME 20:56:25
  1 CHAN
    2 DATE 21 SEP 2024
      3 TIME 15:25:18
```

**Now the "Countries" that Subotica "links" to**

**In fact there might have been Jurisdictions in between the City and the Country / Kingdom, but we leave that out! !**  
In this case the ""Countries"
Subotica links to were very diferent, also in size, thats why here is choosen to have separate `SPLAC's` for each "Country".  
Further, the information inside the following SPLAC's is limited, its just an example.

## SPLAC Country: Independent Serbia (today) FROM 27 APR 1992

```gedcom
0 @SP002@ SPLAC Serbia        (Independent Serbia)
  1 LANG en
  1 TRAN Szerbia
    2 LANG hu
  1 TYPE COUNTRY, POLI, 7     (Serbia independant Federal State) 
  1 PERIOD FROM 27 APR 1992
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 27 APR 1992
    2 SPLAC @SP100@           link to the SPLAC: EARTH
      3 TYPE GEOG             HIERARCHICAL_RELATIONSHIP, can be POLI, RELI, GEOG, or CULT
 .....
CREA and CHAN
```
## SPLAC Country: Kingdom of Hungary TO 1526

```gedcom
0 @SP003@ SPLAC Kingdom of Hungary   (Kingdom of Hungary (1000-1526))
  1 LANG en
  1 TYPE COUNTRY, POLI, 31    (Kingdom) 
  1 PERIOD TO 1526
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE TO 1526
    2 SPLAC @SP100@           link to the SPLAC: EARTH
      3 TYPE GEOG             HIERARCHICAL_RELATIONSHIP, can be POLI, RELI, GEOG, or CULT
 .....
CREA and CHAN
```
## SPLAC Country: Ottoman Empire FROM 1526 TO 1686

```gedcom
0 @SP004@ SPLAC Ottoman Empire
  1 LANG en
  1 TYPE COUNTRY, POLI, 31    (Kingdom) 
  1 PERIOD FROM 1526 TO 1686
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 1526 TO 1686
    2 SPLAC @SP100@           link to the SPLAC: EARTH
      3 TYPE GEOG             HIERARCHICAL_RELATIONSHIP, can be POLI, RELI, GEOG, or CULT
 .....
CREA and CHAN
```
## SPLAC Country: Habsburg Monarchy - Royal Hungary FROM 1526 TO 1867

```gedcom
0 @SP005@ SPLAC Habsburg Monarchy   (Habsburg Monarchy - Royal Hungary, 1526-1867)
  1 LANG en
  1 TYPE COUNTRY, POLI, 31    (Kingdom) 
  1 PERIOD FROM 1686 TO 1799
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 1686 TO 1799
    2 SPLAC @SP100@           link to the SPLAC: EARTH
      3 TYPE GEOG             HIERARCHICAL_RELATIONSHIP, can be POLI, RELI, GEOG, or CULT
 .....
CREA and CHAN
```
## SPLAC Country: Austro-Hungarian Empire (Kingdom of Hungary) FROM 1867 TO 1918

```gedcom
0 @SP006@ SPLAC Habsburg Monarchy   (Habsburg Monarchy - Royal Hungary, 1526-1867)
  1 LANG en
  1 TYPE COUNTRY, POLI, 31    (Kingdom) 
  1 PERIOD FROM 1867 TO 1918
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 1867 TO 1918
    2 SPLAC @SP100@           link to the SPLAC: EARTH
      3 TYPE GEOG             HIERARCHICAL_RELATIONSHIP, can be POLI, RELI, GEOG, or CULT
 .....
CREA and CHAN
```

## SPLAC Country: Voivodeship of Serbia and Banat of Temeschwar FROM 1849 TO 1918
```gedcom
0 @SP007@ SPLAC Voivodeship of Serbia and Banat of Temeschwar
  1 LANG en
  1 TYPE COUNTRY, POLI, 7     (Federal State) 
  1 PERIOD FROM 1849 TO 1918
    2 TYPE SOURCE             (SOURCE=researcher perspective, USER= conclusion perspective
    2 DATE FROM 1849 TO 1918
    2 SPLAC @SP100@           link to the SPLAC: EARTH
      3 TYPE GEOG             HIERARCHICAL_RELATIONSHIP, can be POLI, RELI, GEOG, or CULT
 .....
CREA and CHAN
```
#### There are more but they are left out.

