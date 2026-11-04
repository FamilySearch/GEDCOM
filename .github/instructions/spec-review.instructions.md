---
applyTo: "specification/**,extracted-files/**,build/**,changelog.md"
---

# Reviewing a change to the GEDCOM specification

The steering committee decides whether a change is valuable, absent and used. Your job is narrower: flag what can be checked from the change, quote the line you mean, and ask rather than decide. If nothing is wrong, say so in one line. Don't restate the change, and don't suggest wording you merely prefer.

## Every change

- **Which kind is it?** A typo, a clarification, an addition, or a change of meaning. Say which you think it is.
- **The branch.** `main` takes fixes and clarifications. Additions go to `v7.1`. Anything that would make a valid 7.0 file invalid, or change what it means, needs a major version: say so plainly.
- **The changelog.** A change to the data needs a line in `changelog.md`. If a term is renamed or removed, check that the changelog doesn't still list the old one.
- **Generated files.** The files in `extracted-files/` must match the specification text. Check that the PR changes them only as rebuilding would.

## A renamed or removed term

- **Leftover files.** The build adds term files to `extracted-files/tags` and never deletes them. A rename must delete the old term's file in the same PR, or validators built from the tables keep accepting the old term.
- **Everywhere else.** Look for the old tag in the specification text, its examples and the changelog.
- **Test files.** The test files are in the GEDCOM.io repository (`testfiles/gedcom70`, `testfiles/gedcom71`). Ask whether any of them uses the old term, and whether a GEDCOM.io PR goes with this one. A GEDZIP (`.gdz`) copy of a test file needs the same change.

## A new structure, value or calendar

- **The URI rule.** A 7.0 structure that gains a substructure in 7.1 gets a new `g7.1:` URI, and so does every structure that holds it. An enumeration set that gains a `g7.1:` value becomes a `g7.1:` set.
- **An example.** Ask for a small GEDCOM file that uses the change, and say where the maximal test file should use it.
- **Is there already a way?** If the specification already has a structure that records this, name it.

## Wording

- Keep the definition. Where programs use something differently, a note that describes the difference is usually the fix.
- Match the style of the surrounding text, and change the specification, never generated files by hand.

## How this file grows

When a reviewer catches something this file didn't ask about, add a line here, in the same PR or the next one, so the same miss isn't made twice.
