#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jason Reinhart'
SITENAME = u'Jason Reinhart'
SITESUBTITLE = u'Data Analysis, Visualization, and Machine Learning'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = u'en'

LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True

#Theme Settings
THEME = "/Users/jreinhart/Documents/pelican_blog/pelican_themes/pelican-clean"
MARKUP = ('md', 'ipynb')


#Plugin Settings
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
	'ipynb.markup'
	]

#ipynb plugin settings
IPYNB_USE_META_SUMMARY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
SOCIAL = (('github', 'https://github.com/JasonReinhart'),
          ('facebook','https://www.facebook.com/jason.reinhart.9'))

# Socials at bottom of posts
GITHUB_URL = 'https://github.com/JasonReinhart'
FACEBOOK_URL = 'https://www.facebook.com/jason.reinhart.9'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
