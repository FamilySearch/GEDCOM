# Appendix A: Known Calendars and Dates {#A-calendars}

## Known Calendars

This specification defines 4 calendars: `GREGORIAN`, `JULIAN`, `FRENCH_R`, and `HEBREW`.
Previous versions also provided for, but did not define the meaning of, `ROMAN` and `UNKNOWN` calendars.

Extension calendars should use the usual rules for extensions, including using `_` as the leading character of the calendar name.

Each calendar must list its permitted epochs and their meaning.

All month tags must either be standard tags defined for the month name in some standard calendar or be extension tags.

Months with extension tags are permitted in standard calendars only when they are
documented extension tags with standard URIs defined by the calendar. This is intended
for future compatibility, to accommodate cases where an extension calendar later becomes
standardized without changing the URI, at which point the calendar name and month names
with `_` are acceptable with the now-standard URIs.

### `GREGORIAN`

The Gregorian calendar is the now-ubiquitous calendar introduced by Pope Gregory XIII in 1582 to correct the Julian calendar which was slowly drifting relative to the seasons.

Permitted months are

|`stdTag`| URI            | Name      |
|:-------|:---------------|:----------|
| `JAN`  | `g7:month-JAN` | January   |
| `FEB`  | `g7:month-FEB` | February  |
| `MAR`  | `g7:month-MAR` | March     |
| `APR`  | `g7:month-APR` | April     |
| `MAY`  | `g7:month-MAY` | May       |
| `JUN`  | `g7:month-JUN` | June      |
| `JUL`  | `g7:month-JUL` | July      |
| `AUG`  | `g7:month-AUG` | August    |
| `SEP`  | `g7:month-SEP` | September |
| `OCT`  | `g7:month-OCT` | October   |
| `NOV`  | `g7:month-NOV` | November  |
| `DEC`  | `g7:month-DEC` | December  |

The epoch marker `BCE` is permitted in this calendar;
year *y* BCE indicates a year *y* years before year 1.
Thus, there is no year 0; year 1 BCE was followed by year 1.

The URI for this calendar is `g7:cal-GREGORIAN`

### `JULIAN`

The Julian calendar was introduced by Julius Caesar in 45 BC and subsequently amended by Augustus in about 8 BC to correct an error in the application of its leap year rule during its first 3 decades. Years had been counted from various starting epochs during the Julian calendar's use; the version specified by this specification uses the same starting epoch as the Gregorian calendar.

This calendar uses the same months as the Gregorian calendar, differing only in which years February has 29 days.

The epoch marker `BCE` is permitted in this calendar;
year *y* BCE indicates a year *y* years before year 1.
Thus, there is no year 0; year 1 BCE was followed by year 1.

The URI for this calendar is `g7:cal-JULIAN`

### `FRENCH_R`

The French Republican calendar or French Revolutionary calendar are the names given to the new calendar adopted in 1794 by the French National Convention. This calendar was adopted on Gregorian day 22 September 1792, which was 1 Vendémiaire 1 in this calendar. It was abandoned 18 years later.

Permitted months are

|`stdTag`| URI             | Name               |
|:-------|:----------------|:-------------------|
|`VEND`  | `g7:month-VEND` |Vendémiaire         |
|`BRUM`  | `g7:month-BRUM` |Brumaire            |
|`FRIM`  | `g7:month-FRIM` |Frimaire            |
|`NIVO`  | `g7:month-NIVO` |Nivôse              |
|`PLUV`  | `g7:month-PLUV` |Pluviôse            |
|`VENT`  | `g7:month-VENT` |Ventôse             |
|`GERM`  | `g7:month-GERM` |Germinal            |
|`FLOR`  | `g7:month-FLOR` |Floréal             |
|`PRAI`  | `g7:month-PRAI` |Prairial            |
|`MESS`  | `g7:month-MESS` |Messidor            |
|`THER`  | `g7:month-THER` |Thermidor           |
|`FRUC`  | `g7:month-FRUC` |Fructidor           |
|`COMP`  | `g7:month-COMP` |Jour Complémentaires|

No epoch marker is permitted in this calendar.

The URI for this calendar is `g7:cal-FRENCH_R`

### `HEBREW`

The Hebrew calendar is the name given to the calendar used by Jewish peoples around the world which developed into its current form in the early ninth century. It traditionally marks new days at sunset, not midnight. Its first day (1 Tishrei 1) primarily overlapped with Gregorian 7 September 3761 BCE and Julian 7 October 3761 BCE (starting at sunset on the 6th day of those months).

|`stdTag`| URI             |Name                                                   |
|:-------|:----------------|:------------------------------------------------------|
|`TSH`   | `g7:month-TSH` | Tishrei (תִּשְׁרֵי) |
|`CSH`   | `g7:month-CSH` | Marcheshvan (מַרְחֶשְׁוָן) or Cheshvan (חֶשְׁוָן) |
|`KSL`   | `g7:month-KSL` | Kislev (כִּסְלֵו) |
|`TVT`   | `g7:month-TVT` | Tevet (טֵבֵת) |
|`SHV`   | `g7:month-SHV` | Shevat (שְׁבָט) |
|`ADR`   | `g7:month-ADR` | Adar I, Adar Rishon, First Adar, or Adar Aleph (אדר א׳) |
|`ADS`   | `g7:month-ADS` | Adar (אֲדָר); or Adar II, Adar Sheni, Second Adar, or Adar Bet (אדר ב׳) |
|`NSN`   | `g7:month-NSN` | Nisan (נִיסָן) |
|`IYR`   | `g7:month-IYR` | Iyar (אִייָר) |
|`SVN`   | `g7:month-SVN` | Sivan (סִיוָן) |
|`TMZ`   | `g7:month-TMZ` | Tammuz (תַּמּוּז) |
|`AAV`   | `g7:month-AAV` | Av (אָב) |
|`ELL`   | `g7:month-ELL` | Elul (אֱלוּל) |

To keep the lunar-based months synchronized with the solar-based years, some years have Adar I and others do not, instead proceeding from Shevat directly to Adar II. However, in common (non-leap) years, it is common to simply write "Adar" not "Adar II", which users not aware of the distinction might incorrectly encode as `ADR` instead of `ADS`. It is recommended that systems knowing which years had Adar I and which did not replace `ADR` in common years with `ADS`.

No epoch marker is permitted in this calendar.

The URI for this calendar is `g7:cal-HEBREW`

## Dual dates

The day on which a new year began and the year number increased varied at different times and places during the use of the Gregorian and Julian calendars. For example, England measured the new year as 25 March until 1752, when it switched to 1 January as the new year. In periods of transition, or when writing after a change about dates occurring before a change, it was sometimes common to indicate 2 years with a slash, for example, "30 January 1648/49" meaning "1648 if you count the new year as coming after 30 January, 1649 if you count it as coming before 30 January". Other notations, such as abbreviations for phrases like "new style" and "old style", were also sometimes employed.

```gedcom
2 DATE 30 JAN 1649
3 PHRASE 30 January 1648/49
```

Many nations transitioned from using the Julian calendar to using the Gregorian calendar. This transition caused a change in dates by several days, which (depending on the date in question) could change the month and year as well. In periods of transition, or when writing after a change about dates occurring before a change, it was sometimes common to indicate 2 dates with slashes, for example "23/6 November/December 1907" meaning "Julian 23 November 1907, Gregorian 6 December 1907". Other notations, such as abbreviations for phrases like "new style" and "old style", were also sometimes employed.

```gedcom
2 DATE 6 DEC 1907
3 PHRASE 23/6 November/December 1907
```

Some documents also used slashes to indicate approximate dates, such as writing a birth year as "1903/4" when it was computed from a year-granularity age at a given date.

```gedcom
2 DATE BET 1903 AND 1904
3 PHRASE 1903/4
```


Versions 5.3 through 5.5.1 had special syntax for recording the first of these 3 concepts with a slash in the year. However, because slashes appear in historical documents with all 3 of the above meanings, some users misused this notation to record the other 2 situations as well. The result is ambiguity in the intended meaning of the resulting data. Version 7.0 removed the year slash notation; a `PHRASE` substructure should be used instead to clarify meaning.


## Calendars in date ranges and date periods

Calendars apply to the subsequent `date` production, not to the entire `DateValue`.
Hence,

- `DATE FROM 1670 TO 1800` means `DATE FROM GREGORIAN 1670 TO GREGORIAN 1800`
- `DATE FROM 1670 TO JULIAN 1800` means `DATE FROM GREGORIAN 1670 TO JULIAN 1800`
- `DATE FROM JULIAN 1670 TO 1800` means `DATE FROM JULIAN 1670 TO GREGORIAN 1800`

Because some systems may show dates as-is to users and because not all users understand the above rule, it is recommended that `calendar` tags be included if any `date` is non-`GREGORIAN`. It is recommended that the `calendar` tag be omitted if all `date`s in a payload are in the Gregorian calendar. Hence, the recommended forms of the previous 3 dates are

- `DATE FROM 1670 TO 1800`
- `DATE FROM GREGORIAN 1670 TO JULIAN 1800`
- `DATE FROM JULIAN 1670 TO GREGORIAN 1800`
