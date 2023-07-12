# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ClimateSocialPolicy'
copyright = '2023, Bin Cheng'
author = 'Bin Cheng'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.bibtex',
    'sphinx.ext.intersphinx',
    'sphinx_togglebutton',
]

templates_path = ['_templates']
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_material
html_context = sphinx_material.get_html_context()
html_theme_path = sphinx_material.html_theme_path()
html_theme = 'sphinx_material'
html_theme_options = {
    'navigation_with_keys': True,
    'nav_title': 'UncertaintySocialPolicy',
    'color_primary': 'blue-grey',
    'color_accent': 'indigo',
    'repo_url': 'https://github.com/binchengecon/TwoCapital_Shrink',
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

html_static_path = ['_static']

bibtex_bibfiles = ['climate.bib']


nbsphinx_allow_errors = True
nbsphinx_kernel_name = "python"
mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"