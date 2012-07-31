HEADER = src/header.html
FOOTER = src/footer.html
SIDEBAR = src/sidebar.html
CSS = src/main.css
PANDOC_OPTS = --mathml -t HTML5 -B $(HEADER) -B $(SIDEBAR) -A $(FOOTER) -c $(CSS)

all: description plandecours

description: src/description.rst $(HEADER) $(FOOTER) $(SIDEBAR)
	pandoc $(PANDOC_OPTS) -o description.html src/description.rst

plandecours: src/Compl_mathematiques_201-GGF-SH_LSC_A10.tex \
	$(HEADER) $(FOOTER) $(SIDEBAR)
	pandoc $(PANDOC_OPTS) -o syllabus.html src/Compl_mathematiques_201-GGF-SH_LSC_A10.tex

