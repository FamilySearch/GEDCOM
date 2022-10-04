SPECDIR = ../specification/
EXTDIR = ../extracted-files/
MD_FILES = $(sort $(wildcard $(SPECDIR)gedcom*.md))
TERMS_FILES = $(sort $(wildcard $(SPECDIR)/terms/*))
HTML_FILE = $(SPECDIR)gedcom.html
PDF_FILE = $(SPECDIR)gedcom.pdf
GRAMMARS = $(EXTDIR)grammar.abnf $(EXTDIR)grammar.gedstruct
TAGDEFS = $(EXTDIR)tags

MODTIME := $(shell git log -1 --date="format:%_d %B %Y" --format="%ad" -- $(SPECDIR))
PDARGS := --syntax-definition=gedcom.xml --syntax-definition=gedstruct.xml --syntax-definition=abnf.xml --from=markdown+smart --standalone --css=pandoc.css --template=template.html --toc --number-sections --self-contained --highlight-style=kate  --metadata="date:$(MODTIME)" --wrap=none

.phony: all clean distclean

all:	$(PDF_FILE) $(PDF_FILE) $(TAGDEFS) $(GRAMMARS)

$(PDF_FILE): $(HTML_FILE)
	python3 -mweasyprint $(HTML_FILE) $(PDF_FILE)

$(HTML_FILE): hyperlink-code.py GEDCOM-tmp.html
	python3 hyperlink-code.py GEDCOM-tmp.html $(HTML_FILE)

$(TAGDEFS): $(MD_FILES) $(TERMS_FILES) uri-def.py
	python3 uri-def.py $(MD_FILES) $(TAGDEFS)
	touch $(TAGDEFS)

$(EXTDIR)grammar.abnf: $(MD_FILES) extract-grammars.py
	python3 extract-grammars.py $(MD_FILES) $(EXTDIR)

$(EXTDIR)grammar.gedstruct: $(MD_FILES) extract-grammars.py
	python3 extract-grammars.py $(MD_FILES) $(EXTDIR)

GEDCOM-tmp.html: GEDCOM-tmp.md gedcom.xml gedstruct.xml abnf.xml template.html pandoc.css
	pandoc $(PDARGS) --to=html5 --output GEDCOM-tmp.html GEDCOM-tmp.md

GEDCOM-tmp.md: $(MD_FILES) hyperlink.py
	python3 hyperlink.py $(MD_FILES) GEDCOM-tmp.md

clean:
	rm -f GEDCOM-tmp.html GEDCOM-tmp.md

distclean: clean
	rm -f $(HTML_FILE) $(PDF_FILE) $(GRAMMARS)
	rm -fr $(TAGDEFS)/

