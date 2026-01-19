# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'JCPenney Credit Card Activation Help'
copyright = '2026, JCPenney'
author = 'JCP Activation Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add more if required)
extensions = []

# Allow reStructuredText raw HTML (for buttons, custom UI elements)
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# Page titles
html_title = "Activate Your JCPenney Credit Card at Jcp.syf.com/activate"
html_short_title = "JCP Card Activation Guide"

# Favicon (place file in root or _static folder)
html_favicon = 'favicon.ico'

# Hide “View page source”
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (CSS, JS)
# html_static_path = ['_static']
