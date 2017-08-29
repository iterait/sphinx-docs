#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# cxflow-tensorflow documentation build configuration file, created by
# sphinx-quickstart on Mon Aug 21 13:06:39 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

import os, sys

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_bootstrap_theme

extensions = \
    ['sphinx.ext.autodoc',
     'sphinxarg.ext',
     'autoapi.sphinx',
     'sphinx.ext.inheritance_diagram',
     'sphinx.ext.intersphinx',
     'sphinx.ext.todo',
     'sphinx.ext.coverage',
     'sphinx.ext.ifconfig',
     'sphinx.ext.mathjax',
     'sphinx.ext.viewcode',
     'sphinx_autodoc_typehints']

# Add any paths that contain templates here, relative to this directory.
templates_path = [os.path.join(os.path.dirname(__file__), '_templates')]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = [os.path.join(os.path.dirname(__file__), '_static')]
html_sidebars = {'**': ['relations_side.html', 'localtoc.html', 'searchbox.html', 'related.html']}
html_theme_options = {
    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 0,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nope",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "cosmo" or "sandstone".
    'bootswatch_theme': "united",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3.6', None),
                       'cxflow': ('https://cxflow.org', None),
                       'cxflow_tensorflow': ('https://tensorflow.cxflow.org', None)}

def setup(app):
    app.add_stylesheet("highlight.css")

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../..'))
