# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os, sphinx_rtd_theme, time

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = '86Box'
copyright = f'2020-{time.strftime("%Y")}, 86Box Project'
author = '86Box Project'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx_rtd_theme',
	'sphinx.ext.autosectionlabel',
]
autosectionlabel_prefix_document = True
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

rst_prolog = ''
def generate_icons(app):
	for icon_dir in ('usage/images',):
		for icon in os.listdir(icon_dir):
			fn, ext = os.path.splitext(icon)
			if ext == '.png':
				if fn[-6:] != '_small' and 'html' not in app.builder.name: # use small icons in non-HTML applications
					small_icon = fn + '_small' + ext
					if os.path.exists(os.path.join(icon_dir, small_icon)):
						icon = small_icon
				app.config.rst_prolog += f'.. |{fn}| image:: /{icon_dir}/{icon}\n'

def setup(app):
	app.connect('builder-inited', generate_icons)


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
if os.path.isdir('_static'):
	html_static_path = ['_static']
html_favicon = 'favicon.ico'

latex_toplevel_sectioning = True
