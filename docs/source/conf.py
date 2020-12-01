#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# JupyterLab documentation build configuration file, created by
# sphinx-quickstart on Thu Jan  4 15:10:23 2018.
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

# For conversion from markdown to html
from recommonmark.transform import AutoStructify


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The file extensions of source files.
# Sphinx considers the files with this suffix as sources.
# The value can be a dictionary mapping file extensions to file types.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'JupyterLab'
copyright = '2018, Project Jupyter'
author = 'Project Jupyter'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

import os
_version_py = os.path.join('..', '..', 'jupyterlab', '_version.py')
version_ns = {}

with open(_version_py, mode='r') as version_file:
    exec(version_file.read(), version_ns)

# The short X.Y version.
version = '%i.%i' % version_ns['version_info'][:2]
# The full version, including alpha/beta/rc tags.
release = version_ns['__version__']


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

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# build js docs and stage them to the build directory
import os
import shutil
from subprocess import check_call


def build_api_docs(out_dir):
    """build js api docs"""
    here = os.path.dirname(os.path.abspath(__file__))
    docs = os.path.join(here, os.pardir)
    root = os.path.join(docs, os.pardir)
    docs_api = os.path.join(docs, "api")
    api_index = os.path.join(docs_api, "index.html")
    # is this an okay way to specify jlpm
    # without installing jupyterlab first?
    jlpm = ["node", os.path.join(root, "jupyterlab", "staging", "yarn.js")]

    if os.path.exists(api_index):
        # avoid rebuilding docs because it takes forever
        # `make clean` to force a rebuild
        print(f"already have {api_index}")
    else:
        print("Building jupyterlab API docs")
        check_call(jlpm, cwd=root)
        check_call(jlpm + ["build:packages"], cwd=root)
        check_call(jlpm + ["docs"], cwd=root)

    dest_dir = os.path.join(out_dir, "api")
    print(f"Copying {docs_api} -> {dest_dir}")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(docs_api, dest_dir)


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

# Output for github to be used in links
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "jupyterlab",  # Username
    "github_repo": "jupyterlab",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/docs/source/",  # Path in the checkout to the docs root
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'JupyterLabdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'JupyterLab.tex', 'JupyterLab Documentation',
     'Project Jupyter', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'jupyterlab', 'JupyterLab Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'JupyterLab', 'JupyterLab Documentation',
     author, 'JupyterLab', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']



# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}


# autodoc configuration with AutoStructify
#
# See http://recommonmark.readthedocs.io/en/latest/auto_structify.html
# See the setup function in current conf.py file in the recommonmark repo
# https://github.com/rtfd/recommonmark/blob/master/docs/conf.py#L296
github_doc_root = 'https://github.com/jupyterlab/jupyterlab/tree/master/docs/'

# We can't rely on anchors because GitHub dynamically renders them for
# markdown documents.
linkcheck_anchors = False

def setup(app):
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
        'enable_auto_doc_ref': False,
    }, True)
    app.add_transform(AutoStructify)
    app.add_css_file('custom.css')  # may also be an URL
    build_api_docs(app.outdir)
