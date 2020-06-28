#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brian Shaw'
SITENAME = 'sha.ws'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

DEFAULT_METADATA = {
    'lang': 'en',
    'translation': 'false',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

CUSTOM_CSS = 'static/custom.css'

# pelican-bootstrap3 - https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'yeti'

DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_DATE_MODIFIED = True

HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False

USE_OPEN_GRAPH = False

DIRECT_TEMPLATES = ['index', 'tags',
                   'categories', 'authors', 'archives', 'search']

# https://creativecommons.org/licenses/
CC_LICENSE = 'CC-BY'

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['i18n_subsites', 'tipue_search']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
