# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

# setup documentation metadata
project = 'Synaptics Astra SR SDK User Guide'
copyright = '2023 - 2025, Synaptics'
author = 'Synaptics'
release = 'SRSDK 1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

exclude_patterns = [
        "README.rst",
        "org-docs/**"
        "_build",
        "Thumbs.db",
        ".DS_Store"
]

templates_path = ['_templates']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'



html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_logo = "images/logo_full_white.png"

html_theme_options = {
  'logo_only': True,
  'style_nav_header_background': '#007dc3'
}

html_context = {
  'display_github': True,
  'github_repo': 'syna-astra-mcu-dev.github.io',
  'github_version': 'main',
  'conf_py_path': '/',
  'version': release
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Allow HTML files to be included
html_extra_path = ['Synatoolkit_User_Guide.pdf', 'Astra_MCU_SDK_MIPI_Sensor_Integration_Guide.pdf', 'TI_design.pdf']

# MyST parser configuration
myst_enable_extensions = [
    "strikethrough",
    "tasklist",
]

# Allow cross-references to work properly
myst_heading_anchors = 6

#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
