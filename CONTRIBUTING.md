# How to contribute

We welcome all forms of contribution!

The "we" here is the GEDCOM Steering Committee,
a group of volunteers who meet online weekly
to review recent action on our three GitHub repositories
([GEDCOM](https://github.com/FamilySearch/GEDCOM), [GEDCOM.io](https://github.com/FamilySearch/GEDCOM.io), and [GEDCOM-registries](https://github.com/FamilySearch/GEDCOM-registries))
as well as to discuss future directions for the GEDCOM specification.
Our goal is to read, discuss, and respond to every discussion, issue, and pull request,
but there are weeks when we have enough going on that we miss something;
if too many such weeks occur back-to-back we sometimes lose track of what we've not responded to.
If your post hasn't been responded to by the steering committee after several weeks, posting a follow-up on the same thread can bring it back to our attention.

We always open our responses with some version of "discussed in steering committee"
to distinguish responses from the entire group
from responses from just one of its individual members.

Anyone may open issues, discussions and pull requests.
FamilySearch approves the members of the steering committee.
If you'd like to be considered for a position on the GEDCOM Steering Committee,
please email GEDCOM@FamilySearch.org.

- [Code of Conduct](#code-of-conduct)
- [Before you post](#before-you-post)
- [Questions about use](#questions-about-use)
- [Errors in the specification](#errors-in-the-specification)
  - [Did you find an error or ambiguity?](#did-you-find-an-error-or-ambiguity)
  - [Did you write a fix?](#did-you-write-a-fix)
- [New tools and features](#new-tools-and-features)
  - [Does a tool already do it?](#does-a-tool-already-do-it)
  - [Requesting a feature](#requesting-a-feature)
  - [Proposing the change yourself](#proposing-the-change-yourself)
- [License of contributions](#license-of-contributions)
- [Contributing changes to the specification](#contributing-changes-to-the-specification)
- [The gedcom.io website](#the-gedcomio-website)

Don't worry too much about where something goes: if you put it in the wrong place, we will move it for you.
If you're not sure, the [discussions](https://github.com/FamilySearch/GEDCOM/discussions) page is always a good option.

## Code of Conduct

Everyone taking part is expected to follow our [Code of Conduct](https://github.com/FamilySearch/GEDCOM/blob/main/CODE_OF_CONDUCT.md).

## Before you post

Before opening an issue or a discussion,
**search the existing [issues](https://github.com/FamilySearch/GEDCOM/issues?q=is%3Aissue) and [discussions](https://github.com/FamilySearch/GEDCOM/discussions)**, open and closed.
If one already covers your point, please add to that conversation rather than starting a new one.
Search with the specification's own terms (a tag such as `ASSO`, or a structure name) as well as in plain words,
since an earlier post may describe the same thing in different words.


## Questions about use

These are most helpful if provided as a [Q&A-type discussion](https://github.com/FamilySearch/GEDCOM/discussions).
And these are helpful! We want the specification to be clear,
so anything you find unclear is a potential space for improving the specification.

Sometimes we decide the best solution is to add the answer to the [Technical FAQs](https://gedcom.io/techfaqs/),
which will result in a [change on the GEDCOM.io repository](https://github.com/FamilySearch/GEDCOM.io/pulls).
That said, for consistency and to make it easier to search for discussions, the Q&A discussion is still housed in the GEDCOM repository even if the resulting change happens in the GEDCOM.io repository.

## Errors in the specification

### Did you find an error or ambiguity?

Report it in an [issue](https://github.com/FamilySearch/GEDCOM/issues/new).
Say where the specification has it (a section or a structure), what is wrong or unclear, and an example if you have one.

### Did you write a fix?

Submit it as a [pull request](https://github.com/FamilySearch/GEDCOM/pulls).
Its description should link the issue it addresses (for example, `Fixes #123`), so a reader can click through to it, and summarize the change. The problem itself is described in the issue, so it needn't be restated in the pull request.
Simple typo fixes can be accepted without a corresponding issue.
[Contributing changes to the specification](#contributing-changes-to-the-specification) lists what every pull request is expected to include.

## New tools and features

### Does a tool already do it?

Do you know of a tool that uses GEDCOM or will help others use GEDCOM?
Let us know as a [show-and-tell-type discussion](https://github.com/FamilySearch/GEDCOM/discussions).

Do you know of something a tool does that GEDCOM doesn't yet handle?
That's also very useful, as use is one of our criteria for inclusion in a future version of the specification!
Add it to the issue that discusses it, or put it in a [discussion](https://github.com/FamilySearch/GEDCOM/discussions).

If a tool includes the new feature as an extension tag in GEDCOM export,
registering an extension for that in the [GEDCOM-registries repository](https://github.com/FamilySearch/GEDCOM-registries/blob/main/tips.md) is welcome.
This can be done by the tool author, but doesn't need to be:
community-filed extension registry entries are welcome.

### Requesting a feature

If you wish that GEDCOM supported something it does not support,
report that in an [issue](https://github.com/FamilySearch/GEDCOM/issues/new).
In writing your issue, you might consider including answers to the following,
which follow the three criteria (valuable, absent, used) that the [README](https://github.com/FamilySearch/GEDCOM#branches) gives for adding to a minor version:

1. What is an example case where it would be valuable? Concrete examples are often helpful in focussing the conversation and informing the solution.
2. How absent is this feature? What's the closest GEDCOM seems to come to it now?
3. How much is this used by current applications? Knowing that there are tools that have this in their internal data model goes a long way in convincing other tool developers that it is worth the energy to support if it is added to the standard in the future.

We welcome all kinds of feature requests, from something simple like adding a new type of event
to something all-encompassing like proposing a complete redesign in a future major version of the specification.

The steering committee labels each feature request by the kind of change it would need:
one that only adds to the specification, which a minor version can hold,
or one that changes how something works now, which needs a major version.
That label is a classification of what kind of change the feature request presupposes,
not a promise to include it in the next version of the spec.
An "awaiting use" label means the committee is waiting for evidence that programs implement and use the feature.
The [labels page](https://github.com/FamilySearch/GEDCOM/labels) lists the labels we use.

### Proposing the change yourself

If you know how the spec should change based on your feature request,
you're also welcome to submit a [pull request](https://github.com/FamilySearch/GEDCOM/pulls)
showing that.
Such pull requests should still be paired with an issue:
we use the conversation on the issue to discuss the feature itself (its scope, need, value, use, relationship to other features, and so on),
while the conversation on the pull request focuses on how a specific candidate addition to the specification is presented.

## License of contributions

The FamilySearch GEDCOM Specification is © Intellectual Reserve, Inc.
and is published under the [Apache License 2.0](https://github.com/FamilySearch/GEDCOM/blob/main/LICENSE)
(see also the [NOTICE](https://github.com/FamilySearch/GEDCOM/blob/main/NOTICE) file).
Unless you say otherwise, anything you submit for inclusion is provided under that same license,
as section 5 of the license describes.

## Contributing changes to the specification

These are most helpful if provided as a [pull request](https://github.com/FamilySearch/GEDCOM/pulls).
Pull requests are harder to author than the other options here,
so you're also welcome to put them in an [issue](https://github.com/FamilySearch/GEDCOM/issues).

For all but the simplest changes, first open an [issue](https://github.com/FamilySearch/GEDCOM/issues/new) describing the purpose and rationale of the change,
so that the committee and the community can give feedback before the work is done.
The [README](https://github.com/FamilySearch/GEDCOM#branches) describes the branches:
`main` holds the current release, and `v7.1` the draft of the next minor version.
The committee usually reviews corrections to the current release first, then additions for the next minor version, then anything later.

For every pull request that changes the specification, the following apply:

- **The branch matches the kind of change** ([A Guide to Version Numbers](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html#a-guide-to-version-numbers)):
  - A pull request against `main` clarifies or corrects the text and makes no additions.
  - A pull request against `v7.1` may add, but every file that was valid stays valid. For example, it may add new structure types, allow current structures in new contexts, add enumerated values or calendars, or relax a cardinality such as `{0:1}` to `{0:M}`.
  - There is currently no branch for breaking changes. Propose one in an issue instead.
- **Test files come with any change to what a file can contain.** Any test file that uses something you changed is updated, and a new structure comes with a small example file. The test files are in the [GEDCOM.io repository](https://github.com/FamilySearch/GEDCOM.io/tree/main/testfiles), so this means a matching pull request there, linked from yours. A change to wording alone, such as a typo fix, needs none.
- **For an addition, the description quotes the three tests.** Quote the part of the issue (or its discussion) that shows the change is valuable, absent from the specification today, and used, or why use isn't needed.
- **Say a thing once.** Where the specification already says something in general (what `DATE` means, for example), a structure that uses it doesn't repeat it. Add text only for what is specific to that structure. When unsure, include it and say so in the description: reviewers would rather delete a sentence than ask for one.
- **Generated files are rebuilt.** Run the build in [`build/`](https://github.com/FamilySearch/GEDCOM/blob/main/build/README.md) so that `extracted-files/` matches the specification text. The build adds and updates files but never deletes them, so delete the file of any term you removed or renamed.
- **The changelog is written at release.** Leave `changelog.md` alone; it's updated when a release is prepared. If your change renames or removes something, say so in the description.

## The gedcom.io website

If you have feedback or suggestions about any of the non-specification content of <https://gedcom.io/>,
such as [technical FAQ](https://gedcom.io/techfaqs/) or [example files](https://gedcom.io/tools/#example-familysearch-gedcom-70-files),
you are welcome to file them as an [issue in the GEDCOM repository](https://github.com/FamilySearch/GEDCOM/issues)
or as an [issue in the GEDCOM.io repository](https://github.com/FamilySearch/GEDCOM.io/issues).
If it results in a change in the site, we'll handle that as a [pull request in the GEDCOM.io repository](https://github.com/FamilySearch/GEDCOM.io/pulls/),
so it is slightly more convenient for us if it is filed there,
but since portions of that site (such as the [YAML files](https://gedcom.io/terms/v7/HEAD)) are pulled from the GEDCOM repository,
that line is not crisp; using either repository is fine.
