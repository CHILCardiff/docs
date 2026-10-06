# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CHIL Documentation'
copyright = '2026, M. R. Prior-Jones, L. Craw, J. D. Hawkins, S. F. Mann, J. Saade'
author = 'M. R. Prior-Jones, L. Craw, J. D. Hawkins, S. F. Mann, J. Saade'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_theme = 'sphinx_book_theme'
html_theme_options = {
    "navigation_depth" : 3,
    "collapse_navigation" : False
}
html_logo = '_static/logo.png'