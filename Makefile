# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Custom target for GitHub Pages - build directly to docs folder
github:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "docs" $(SPHINXOPTS) $(O)

# Build directly to root directory for immediate GitHub Pages deployment
root:
	@echo "Building HTML files to root directory..."
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "_temp_build" $(SPHINXOPTS) $(O)
	@echo "Copying HTML files to root directory..."
	@cp -r _temp_build/* .
	@rm -rf _temp_build
	@echo "HTML files generated in root directory for GitHub Pages"

# Clean root directory HTML files (but preserve source files)
clean-root:
	@echo "Cleaning HTML files from root directory..."
	@rm -f *.html *.js objects.inv .buildinfo
	@rm -rf _images _sources _static/.doctrees
	@echo "Root directory cleaned"

# Build and deploy to root in one step
deploy: clean-root root
	@echo "Documentation built and ready for GitHub Pages!"

.PHONY: help Makefile github root clean-root deploy

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
