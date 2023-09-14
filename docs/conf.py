#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# dcor documentation build configuration file, created by
# sphinx-quickstart on Thu Sep 14 14:53:09 2017.
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
# sys.path.insert(0, '/home/carlos/git/dcor/dcor')


import os
import sys

import pkg_resources
# Patch sphinx_gallery.binder.gen_binder_rst so as to point to .py file in
# repository
import sphinx_gallery.gen_rst
import sphinx_gallery.interactive_example

try:
    release = pkg_resources.get_distribution('dcor').version
except pkg_resources.DistributionNotFound:
    print(
        'To build the documentation, The distribution information of dcor\n'
        'Has to be available.  Either install the package into your\n'
        'development environment or run "setup.py develop" to setup the\n'
        'metadata.  A virtualenv is recommended!\n',
    )
    sys.exit(1)
del pkg_resources

version = '.'.join(release.split('.')[:2])

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinxcontrib.bibtex',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.intersphinx',
    'jupyter_sphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

rtd_version = os.environ.get("READTHEDOCS_VERSION", "latest")
branch = "master" if rtd_version == "stable" else "develop"

sphinx_gallery_conf = {
    'examples_dirs': '../examples',
    'gallery_dirs': 'auto_examples',
    'reference_url': {
        # The module you locally document uses None
        'dcor': None,
    },
    'backreferences_dir': 'backreferences',
    'doc_module': 'dcor',
    'binder': {
        'org': 'VNMabus',
        'repo': 'dcor',
        'branch': branch,
        'binderhub_url': 'https://mybinder.org',
        'dependencies': ['../binder/runtime.txt', '../binder/requirements.txt'],
        'notebooks_dir': '../examples',
    },
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(
        sys.version_info),
        None,
    ),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'dcor'
copyright = '2017, Carlos Ramos Carreño'
author = 'Carlos Ramos Carreño'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = ''
# The full version, including alpha/beta/rc tags.
# release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

add_module_names = False

autosummary_generate = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'dcordoc'

html_theme_options = {
    "use_edit_page_button": True,
    "github_url": "https://github.com/vnmabus/dcor",
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/dcor",
            "icon": "https://avatars.githubusercontent.com/u/2964877",
            "type": "url",
        },
        {
            "name": "Anaconda",
            "url": "https://anaconda.org/conda-forge/dcor",
            "icon": "https://avatars.githubusercontent.com/u/3571983",
            "type": "url",
        },
    ],
}

html_context = {
    "github_user": "vnmabus",
    "github_repo": "dcor",
    "github_version": "develop",
    "doc_path": "docs",
}

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
    (master_doc, 'dcor.tex', 'dcor Documentation',
     'Author', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dcor', 'dcor Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'dcor', 'dcor Documentation',
     author, 'dcor', 'One line description of project.',
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

bibtex_bibfiles = ['refs.bib']

autodoc_typehints = "description"

# Binder integration
# Taken from
# https://stanczakdominik.github.io/posts/simple-binder-usage-with-sphinx-gallery-through-jupytext/
original_gen_binder_rst = sphinx_gallery.interactive_example.gen_binder_rst


def patched_gen_binder_rst(*args, **kwargs):
    return original_gen_binder_rst(*args, **kwargs).replace(
        "../examples/auto_",
        "",
    ).replace(
        ".ipynb",
        ".py",
    )


#  # And then we finish our monkeypatching misdeed by redirecting

# sphinx-gallery to use our function:
sphinx_gallery.interactive_example.gen_binder_rst = patched_gen_binder_rst
sphinx_gallery.gen_rst.gen_binder_rst = patched_gen_binder_rst
