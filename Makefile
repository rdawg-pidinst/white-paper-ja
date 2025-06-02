PYTHON        = python3
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = PIDINST
SOURCEDIR     = .
BUILDDIR      = _build
BUILDERS      = html dirhtml singlehtml epub latex latexpdf linkcheck	\
                xml json pickle

# Subdirectories of the source directory that are supposed to be there
# but that may be empty and may thus be missing after a git checkout.
STATIC_SOURCEDIRS = $(SOURCEDIR)/_static $(SOURCEDIR)/_templates


help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(BUILDERS): $(STATIC_SOURCEDIRS) _meta.py
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

_meta.py:
	$(PYTHON) setup.py meta

clean:
	rm -rf __pycache__

distclean: clean
	rm -rf $(BUILDDIR)
	rm -f _meta.py

$(STATIC_SOURCEDIRS):
	mkdir $@

.PHONY: help _meta.py clean distclean $(BUILDERS)
