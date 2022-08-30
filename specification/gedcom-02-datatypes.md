# Data types {#datatypes}

Every line value (with any continuation pseudo-structures) is a string.
However, those strings can encode 1 of several conceptual data types.

## Text

A free-text string is text in a human language.
Conceptually, it may be either a user-generated string or a source-generated string.
Programmatically, both are treated as unconstrained sequences of characters with an associated language.

```abnf
anychar = %x09-10FFFF ; but not banned, as with all ABNF rules
Text    = *anychar
```

The URI for the `Text` data type is `xsd:string`.

## Integer

An integer is a non-empty sequence of ASCII decimal digits
and represents a non-negative integer in base-10.
Leading zeros have no semantic meaning and should be omitted.

```abnf
Integer = 1*digit
```

Negative integers are not supported by this specification.

The URI for the `Integer` data type is `xsd:nonNegativeInteger`.

## Enumeration

An enumeration is a selection from a set of options.
They are represented as a string matching the same production as a tag.

```abnf
Enum    = Tag
```

Each structure type with an enumeration payload also defines specific payload values it permits.
These permitted payloads match production `stdTag` and should each have a defined URI.
Payload values that match production `extTag` are always permitted in structures with an enumeration payload
and have their URI defined by the schema.

Each enumeration value has a distinct meaning
as identified by its corresponding URI.

The URI of a given tag in an enumeration payload is determined by the tag itself and by the structure type of the structure it is in the payload of.

:::example
The tag `HUSB` is used in this document to represent two enumeration values.
Which one is meant can be identified by the structure type it appears in as follows:

| Containing structure type | Enumeration value identified by tag `HUSB` |
|---------------------|---------------------|
| `g7:FAMC-ADOP`      | `g7:enum-ADOP-HUSB` |
| `g7:ROLE`           | `g7:enum-HUSB`      |

An [extension](#extensions) could also place either of these enumeration values in an extension structure type; the extension authors should document which one they permit.

The `HUSB` tag is also used to identify two different structure types, `g7:FAM-HUSB` and `g7:HUSB`.
:::

The URI for the `Enum` data type is `g7:type-Enum`.

## Date

The date formats defined in this specification
include the ability to store approximate dates, date periods, and dates expressed in different calendars.

Technically, there are 3 distinct date data types:

- `DateValue` is a generic type that can express many kinds of dates.
- `DateExact` is used for timestamps and other fully-known dates.
- `DatePeriod` is used to express time intervals that span multiple days.


```abnf
DateValue   = date / DatePeriod / dateRange / dateApprox / ""
DateExact   = day D month D year  ; in Gregorian calendar
DatePeriod  = %s"FROM" D date [D %s"TO" D date]
            / %s"TO" D date
            / ""

date        = [calendar D] [[day D] month D] year [D epoch]
dateRange   = %s"BET" D date D %s"AND" D date
            / %s"AFT" D date
            / %s"BEF" D date
dateApprox  = (%s"ABT" / %s"CAL" / %s"EST") D date

dateRestrict = %s"FROM" / %s"TO" / %s"BET" / %s"AND" / %s"BEF"
            / %s"AFT" / %s"ABT" / %s"CAL" / %s"EST" / %s"BCE"

calendar = %s"GREGORIAN" / %s"JULIAN" / %s"FRENCH_R" / %s"HEBREW"
         / extTag

day     = Integer
year    = Integer
month   = stdTag / extTag  ; constrained by calendar
epoch   = %s"BCE" / extTag ; constrained by calendar
```

In addition to the constraints above:

- The allowable `day`s, `month`s, `year`s, and `epoch`s are determined by the `calendar`.
    All known calendars restrict `day` to be between 1 and a month-specific maximum.
    The largest known maximum is 36, and most months in most calendars have a lower maximum.
- No calendar names, months, or epochs match `dateRestrict`.
- Extension calendars (those with `extTag` for their `calendar`) must use `extTag`, not `stdTag`, for months.

An absent `calendar` is equivalent to the calendar `GREGORIAN`.

The grammar above allows for `date`s to be preceded by various words. The meaning of these words is given as follows:

|Production| Meaning                                    |
|:---------|:-------------------------------------------|
|`FROM` *x*|Lasted for multiple days, beginning on *x*. |
|`TO` *x*  |Lasted for multiple days, ending on *x*.    |
|`BET` *x*<br/>`AFT` *x*|Exact date unknown, but no earlier than *x*.|
|`AND` *x*<br/>`BEF` *x*|Exact date unknown, but no later than *x*.  |
|`ABT` *x* |Exact date unknown, but near *x*.           |
|`CAL` *x* |*x* is calculated from other data.          |
|`EST` *x* |Exact date unknown, but near *x*; and *x* is calculated from other data.|

Known calendars and tips for handling dual dating and extension calendars are given in [Appendix A: Calendars and Dates](#A-calendars).

`DateValue` and `DatePeriod` payloads may also be the empty string if no suitable form is known but a substructure (such as a `PHRASE` or `TIME`) is desired.

:::note
Versions 5.3 through 5.5.1 allowed phrases inside `DateValue` payloads.
Date phrases were moved to the `PHRASE` substructure in version 7.0.
A current limitation, however, is that a phrase in the `PHRASE` substructure 
cannot specify a language, so if a non-default language is needed to correctly
interpret the phrase two options exist:

- `PHRASE` can be used with a documented extension tag for the language, as discussed in `g7:LANG`.
  
- `<<EVENT_DETAIL>>.SOUR.DATA.TEXT` can be used instead along with a `LANG` substructure;
  this loses the connection with the date, but includes the language with a standard tag.
:::

:::note
As defined by the grammar above, every date must have a year.
If no year is known, the entire date may be omitted.

:::example
The following is an appropriate way to handle a missing year

```gedcom
2 DATE
3 PHRASE 5 January (year unknown)
```
:::
:::

The URI for the `DateValue` data type is `g7:type-Date`.

The URI for the `DateExact` data type is `g7:type-Date#exact`.

The URI for the `DatePeriod` data type is `g7:type-Date#period`.

## Time

Time is represented on a 24-hour clock (for example, 23:00 rather than 11:00 PM).
It may be represented either in event-local time or in Coordinated Universal Time (UTC).
UTC is indicated by including a `Z` (U+005A) after the time value; event-local time is indicated by its absence.

```abnf
Time     =  hour ":" minute [":" second ["." fraction]] [%s"Z"]

hour     = digit / ("0" / "1") digit / "2" ("0" / "1" / "2" / "3")
minute   = ("0" / "1" / "2" / "3" / "4" / "5") digit
second   = ("0" / "1" / "2" / "3" / "4" / "5") digit
fraction = 1*digit
```

:::note
The above grammar prohibits end-of-day instant `24:00:00` and leap-seconds. It allows both `02:50` and `2:50` as the same time.
:::

The URI for the `Time` data type is `g7:type-Time`.

## Age

Ages are represented by counts of years, months, weeks, and days.

```abnf
Age         = [ageBound D] ageDuration

ageBound    = "<" / ">"
ageDuration = years [D months] [D weeks] [D days]
            / months [D weeks] [D days]
            / weeks [D days]
            / days

years   = Integer %x79    ; 35y
months  = Integer %x6D    ; 11m
weeks   = Integer %x77    ; 8w
days    = Integer %x64    ; 21d
```

Where

|Production |Meaning                                           |
|:----------|:-------------------------------------------------|
|`<`        | The real age was less than the provided age      |
|`>`        | The real age was greater than the provided age   |
|`years`    | a number of years                                |
|`months`   | a number of months                               |
|`weeks`    | a number of weeks                                |
|`days`     | a number of days                                 |

Non-integer numbers should be rounded down to an integer. Thus, if someone has lived for 363.5 days, their age might be written as `363d`, `51w 6d`, `51w`, `0y`, etc.

Because numbers are rounded down, `>` effectively includes its endpoint; that is, the age `> 8d` includes people who have lived 8 days + a few seconds.

Different cultures count ages differently. Some increment years on the anniversary of birth and others at particular seasons. Some round to the nearest year, others round years down, others round years up. Because users may be unaware of these traditions or may fail to convert them to the round-down convention, errors in age of up to a year are common.

Age payloads may also be omitted entirely if no suitable form is known but a substructure (such as a `PHRASE`) is desired.

:::note
Versions 5.5 and 5.5.1 allowed a few specific phrases inside `Age` payloads.
Age phrases were moved to the `PHRASE` substructure in 7.0.
:::

The URI for the `Age` data type is `g7:type-Age`.


## List

A list is a meta-syntax representing a sequence of values with another data type.
Two list data types are used in this document: List:Text and List:Enum.
Lists are serialized in a comma-separated form, delimited by a comma (U+002C `,`) and any number of spaces (U+0020) between each item.
It is recommended that a comma-space pair (U+002C U+0020) be used as the delimiter.

```abnf
List      = listItem *(listDelim listItem)
listItem  = "" / nocommasp / nocommasp *nocomma nocommasp
listDelim = *D "," *D
nocomma   = %x09-2B / %x2D-10FFFF
nocommasp = %x09-1D / %x21-2B / %x2D-10FFFF

List-Text = List
List-Enum = Enum *(listDelim Enum)
```

If valid for the underlying type, empty strings may be included in a list by having no characters between delimiters.

:::example
A `List:Text` with value "`, , one, more,`" has 5 `Text`-type values: 2 empty strings, the string "`one`", the string "`more`", and 1 more empty string.
:::

There is no escaping mechanism to allow lists of entries that begin or end with spaces or that contain comma characters.

The URI for the `List:Text` data type is `g7:type-List#Text`.

The URI for the `List:Enum` data type is `g7:type-List#Enum`.


## Personal Name

A personal name is mostly free-text. It should be the name as written in the culture of the individual and should not contain line breaks, repeated spaces, or characters not part of the written form of a name (except for U+002F as explained below).

```abnf
PersonalName = nameStr
             / [nameStr] "/" [nameStr] "/" [nameStr]

nameChar     = %x20-2E / %x30-10FFFF  ; any but '/' and '\t'
nameStr      = 1*nameChar
```

The character U+002F (`/`, slash or solidus) has special meaning in a personal name, being used to delimit the portion of the name that most closely matches the concept of a surname, family name, or the like.
This specification does not provide any standard way of representing names that contain U+002F.

The URI for the `PersonalName` data type is `g7:type-Name`.

## Language

The language data type represents a human language or family of related languages, as defined in [BCP 46](https://www.rfc-editor.org/info/bcp47).
It consists of a sequence of language subtags separated by hyphens,
where language subtags are [registered by the IANA](https://www.iana.org/assignments/language-subtag-registry).

The ABNF grammar for language tags is given in BCP 47, section 2.1, production `Language-Tag`.

The URI for the `Language` data type is `xsd:Language`.

## Media Type

The media type data type represents the encoding of information in bytes or characters, as defined in [RFC 2045](https://www.rfc-editor.org/info/rfc2045) and [registered by the IANA](http://www.iana.org/assignments/media-types/).

The official grammar for media type is given in RFC 2045, section 5.1.
However, that document does not give stand-alone ABNF, instead referring to registration rules and describing some components in English.
The programmatic parts of the media type grammar can be summarized as follows:

```abnf
MediaType    = mt-type "/" mt-subtype *(";" mt-parameter)

mt-type      = mt-token
mt-subtype   = mt-token
mt-parameter = mt-attribute "=" mt-value
mt-token     = 1*mt-char
mt-attribute = mt-token
mt-value     = mt-token / quoted-string
mt-char      = %x20-21 / %x23-27 / %x2A-2B / %x2D-2E ; not "(),/
             / %x30-39 / %x41-5A / %x5E-7E           ; not :;<=>?@[\]

mt-qstring   = %x22 *(mt-qtext / mt-qpair) %x22
mt-qtext     = %x09-0A / %x20-21 / %x23-5B / %x5D-7E ; not CR "\
mt-qpair     = "\" %x09-7E
```

The URI for the `MediaType` data type is `dcat:mediaType`.

## Special

The special data type is a string conforming to a case-specific standard or constraints. The constraints on each special data type instance are either unique to that structure type or are not simply expressed.
For example, the payload of an `IDNO` structure may obey different rules for each possible `TYPE` substructure.

Each special data type is distinct.
The URI for the generic data type subsuming all `Special` data types is `xsd:string` (the same as the `Text` data type).

```abnf
Special = Text
```

