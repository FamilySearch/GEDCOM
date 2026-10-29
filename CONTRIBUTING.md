# How to contribute

We welcome all forms of contribution!

The "we" here is the GEDCOM Steering Committee,
a group of volunteers who meet online weekly
to review recent action on this and our other two github repositories
([GEDCOM.io](https://github.com/FamilySearch/GEDCOM.io) and [GEDCOM-registries](https://github.com/FamilySearch/GEDCOM-registries))
as well as to discuss future directions for the GEDCOM specification.
Our goal is to read, discuss, and respond to every discussion, issue, and pull request,
but there are weeks when we have enough going on that we miss something;
if too many such weeks occur back-to-back we sometimes loose track of what we've not responded to.
If your post hasn't been responded to by the steering committee after several weeks, posting a follow-up on the same thread can bring it back to our attention.

We always open our responses with some version of "discussed in steering committee"
to distinguish responses from the entire group
from responses from just one of its individual members.

If you'd like to join the GEDCOM Steering Committee,
please email GEDCOM@FamilySearch.org.

# Kinds of contributions

We list several common forms of contribution below,
but don't worry too much about it: if you put something in the wrong place, we will move it for you.
If you're not sure where your contribution goes, the [discussions](https://github.com/FamilySearch/GEDCOM/discussions) is always a good option.

## Questions about use

These are most helpful if provided as a [Q&A-type discussion](https://github.com/FamilySearch/GEDCOM/discussion).
And these are helpful! We want the specification to be clear,
so anything you find unclear is a potential space for improving the specification.

Sometimes we decide the best solution is to add the answer to the [Technical FAQs](https://gedcom.io/techfaqs/),
which will result in a [change on the GEDCOM.io repository](https://github.com/FamilySearch/GEDCOM.io/pulls).
That said, for consistency we try to keep the discussion here, not there.

## Error or ambiguity in the specification

If you find an error or ambiguity in the specification,
please either report it in an [issue](https://github.com/FamilySearch/GEDCOM/issues)
or submit a proposed correction as a [pull request](https://github.com/FamilySearch/GEDCOM/pulls),
or both.

## Report of new tool or feature

Do you know of a tool that uses GEDCOM or will help others use GEDCOM?
Let us know as a [show-and-tell-type discussion](https://github.com/FamilySearch/GEDCOM/discussion).

Do you know of something a tool does that GEDCOM doesn't yet handle?
That's also very useful, as use is one of our criteria for inclusion in a future version of the specification!
You might search the [issues](https://github.com/FamilySearch/GEDCOM/issues) to see if there's a relevant conversation to add to,
or you can put this in a  [discussion](https://github.com/FamilySearch/GEDCOM/discussion).

If a tool includes the new feature as an extension tag in GEDCOM export,
registering an extension for that in the [GEDCOM-registies repository](https://github.com/FamilySearch/GEDCOM-registries/blob/main/tips.md) welcome.
This can be done by the tool author, but doesn't need to be:
community-filed extension registry entries welcome.

## Feature request

If you wish that GEDCOM supported something it does not support,
report that in an [issue](https://github.com/FamilySearch/GEDCOM/issues).
In writing your issue, you might consider including answers to the following:

1. What is an example case where it would be valuable? Concrete examples are often helpful in focussing the conversation and informing the solution.
2. How absent is this feature? What's the closest GEDCOM seems to come to it now?
3. How much is this used by current applications? Knowing that there are tools that have this in their internal data model goes a long way in convincing other tool developers that it is worth the energy to support if it is added to the standard in the future.

We welcome all kinds of feature requests, from something simple like adding a new type of event
to something all-encompassing like proposing a complete redesign in a future major version of the specification.

The steering committee will label each new feature as either [next-minor](https://github.com/FamilySearch/GEDCOM/issues?q=label%3A%22next+minor%22) or [next-major](https://github.com/FamilySearch/GEDCOM/issues?q=label%3A%22next+major%22), depending on whether it is proposing only adding to the spec (minor) or changing some aspect of how things work now (major).
That label is a classification of what kind of change the feature request presupposes,
not a promise to include it in the next version of the spec.

If you know how the spec should change based on your feature request,
you're also welcome to submit a [pull request](https://github.com/FamilySearch/GEDCOM/pulls)
showing that.
Such pull requests should still be paired with an issue:
we use the conversation on the issue to discuss the feature itself (its scope, need, value, use, relationship to other features, and so on),
while the conversation on the pull request focuses on how a specific candidate addition to the specification is presented.



## Changes to the specification

These are most helpful if provided as a [pull request](https://github.com/FamilySearch/GEDCOM/pulls).
Pull requests are harder to author that the other options here,
so you're also welcome to put them in an [issue](https://github.com/FamilySearch/GEDCOM/issues).

Changes should generally be preceded by an [issue](https://github.com/FamilySearch/GEDCOM/issues) describing the purpose and rationale of the change,
though some simple typo fixes can be accepted without a corresponding issue.


## Errors with or suggestions about the gedcom.io website

If you have feedback or suggestions about any of the non-specification content of <https://gedcom.io/>,
such as [technical FAQ](https://gedcom.io/techfaqs/) or [example files](https://gedcom.io/tools/#example-familysearch-gedcom-70-files),
you are welcome to file them as an [issue here](https://github.com/FamilySearch/GEDCOM/issues)
or as an [issue in the GEDCOM.io repository](https://github.com/FamilySearch/GEDCOM.io/issues).
If it results in a change in the site, we'll handle that as a [pull request in the GEDCOM.io repository](https://github.com/FamilySearch/GEDCOM.io/pulls/),
so it is slightly more convenient for us if it is filed there,
but since portions of that site (such as the [YAML files](https://gedcom.io/terms/v7/HEAD)) are pulled from this repository,
that line is not crisp; using either repository is fine.

