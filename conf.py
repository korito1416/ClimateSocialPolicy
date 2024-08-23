# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))


import sphinx_material
project = 'ClimateSocialPolicy'
copyright = '2024, Michael Barnett, William Brock, Lars Peter Hansen and Hong Zhang'
author = 'Haoyang Sun'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.mathjax',
              'sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinxcontrib.bibtex',
              'sphinx.ext.intersphinx',
              'sphinx_togglebutton', 
              "nbsphinx"]

mathjax3_config = {
    'tex': {'tags': 'ams', 'useLabelIds': True},
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_context = sphinx_material.get_html_context()
html_theme_path = sphinx_material.html_theme_path()
html_theme = 'sphinx_material'
html_theme_options = {
    'navigation_with_keys': True,
    'nav_title': 'UncertaintySocialPolicy',
    'color_primary': 'blue-grey',
    'color_accent': 'indigo',
    'repo_url': 'https://github.com/binchengecon/ClimateSocialPolicy',
    'repo_name': 'Uncertainty Social Policy',
    'repo_type': 'github',
    'globaltoc_depth': 3,
    'globaltoc_collapse': True,
    'master_doc': True,
    'logo_icon': '&#xe55d',
}
html_show_sourcelink = False
html_sidebars = {
    '**': [
        'globaltoc.html',
        'localtoc.html',
        'searchbox.html',
        'logo-text.html',
        "mfr.png",
    ]
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

bibtex_bibfiles = ['climate.bib']


nbsphinx_allow_errors = True
nbsphinx_kernel_name = "python"
mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"
