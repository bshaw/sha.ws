#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brian Shaw'
SITENAME = 'sha.ws'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

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

# pelican-bootstrap3 - https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'yeti'
HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False

# https://creativecommons.org/licenses/
CC_LICENSE = 'CC-BY'

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
