This directory is used to convert the `specifications/gedcom.md` source file into fully-hyperlinked HTML and PDF.

# Building -- quick-start guide

1. Install dependencies:

    - [python 3](https://python.org)
    - [pandoc](https://pandoc.org)
    - [weasyprint](https://weasyprint.org) installed by running `python3 -mpip install --user --upgrade weasyprint`
    - [git](https://git-scm.com/)
    - `make`-compatible executable

2. From the directory containing this README, run `make`

# Pushing to [gedcom.io](https://gedcom.io)

A script is provided to assist in uploading tag definitions and rendered specifiations to gedcom.io. To use it

1. Clone <https://github.com/FamilySearch/GEDCOM.io/> into a local diretory
2. From the directory containing this README, run

    ````sh
    make
    python3 path/to/GEDCOM.io
    ````
3. From the GEDCOM.io directory
    
    1. `git add _pages/tag-def/*.md`
    2. `git commit` and `git push`

# Building -- how it works

Getting from `gedcom.md` to `gedcom.pdf` is a multi-step process, all of which is handled by the `Makefile`:

1. `hyperlink.py` reads `gedcom.md` and adds hyperlinks into `gedcom-tmp.md`. It is somewhat dependent on the internal formatting of `gedcom.md` and may need adjustment if, e.g., tables are switched to a different markdown table format.

2. `pandoc` converts `gedcom-tmp.md` into `gedcom-tmp.html`.
    It uses `template.html` for structure,
    `pandoc.css` for styling,
    and `gedcom.xml`, `gedstruct.xml`, and `abnf.xml` for syntax highlighting.
    
    Pandoc's command-line options include
    
    - syntax highlighting options:
        - `--syntax-definition=gedcom.xml`
        - `--syntax-definition=gedstruct.xml`
        - `--syntax-definition=abnf.xml`
        - `--highlight-style=kate`
    - general formatting options
        - `--from=markdown+smart`
        - `--standalone`
        - `--toc`
        - `--number-sections`
        - `--self-contained`
        - `--metadata="date:`date you want on the cover page`"`
    - stylistic options
        - `--css=pandoc.css`
        - `--template=template.html`
    - input/output options
        - `--wrap=none`
        - `--to=html5`
        - `--output=gedcom-tmo.html`
        - `gedcom-tmp.md`

3. `hyperlink-code.py` converts `gedcom-tmp.html` into `gedcom.html` by
    
    - removing all `col` and `colgroup` elements, which are incorrectly handled by some versions of the webkit rendering engine used by weasyprint.
    - adding hyperlinks inside code blocks (which markdown cannot do)
    
    This is dependent on the code environment classes created by syntax highlighting, and may need adjusting if pandoc changes these class names or of the syntax highlighting definition files XML are edited.

4. `python3 -mweasyprint gedcom.html gedcom.pdf` turns the HTML into PDF
    
    Note that a relatively recent version of `weasyprint` (published in 2020 or later) is needed to correctly handle syntax-highlighted code blocks.
    Also note that it is expected that this will emit a variety of warning messages based on CSS rules intended for screen, not print. If it emits any error messages, those should be resolved whether they impede the creation of the PDF or not.
