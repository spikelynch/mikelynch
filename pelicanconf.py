#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mike Lynch'
SITENAME = u'A Budget of Paradoxes'
SITEURL = 'http://mikelynch.org'

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = u'en'

DEFAULT_DATE = 'fs'

# themes and plugins

THEME='/Users/mike/Pelican/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME='europe'
BOOTSTRAP_NAVBAR_INVERSE=True
BOOTSTRAP_FLUID=True

FAVICON='images/ASCII.png'

#SITELOGO='images/ASCII.png'
#SITELOGO_SIZE=20


PLUGIN_PATHS = [ '/Users/mike/Pelican/pelican-plugins' ]
PLUGINS = [ 'tag_cloud' ]


# how URLs look (getting rid of the .html)

ARTICLE_URL      = '{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS  = '{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

PAGE_URL         = 'pages/{slug}/'
PAGE_SAVE_AS     = 'pages/{slug}/index.html'

AUTHOR_URL       = 'author/{slug}/'
AUTHOR_SAVE_AS   = 'author/{slug}/index.html'

CATEGORY_URL     = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL          = 'tag/{slug}/'
TAG_SAVE_AS      = 'tag/{slug}/index.html'

ARCHIVES_URL     = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

CATEGORIES_URL   = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'

TAGS_URL         = 'tags/'
TAGS_SAVE_AS     = 'tags/index.html'
INDEX_SAVE_AS    = 'index.html'





#DISQUS_SITENAME='mikelynch.disqus.com'
#DISQUS_SHORTNAME='mikelynch'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_RSS = None

CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('UTS eResearch', 'http://eresearch.uts.edu.au/'),
         ('Nannygoat Hill', 'http://nannygoathill.wordpress.com/'),
         ('DeepDreams', 'http://last-visible-dog.tumblr.com/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/spikelynch'),
          ('Google+', 'https://www.google.com/+MikeLynch0'),
          ('Pinboard', 'https://pinboard.in/u:mikelynch'),
          ('Tumblr', 'http://littleorangesuitcase.tumblr.com'),
          ('@spikelynch', 'https://twitter.com/spikelynch'),
          ('@FSVO', 'https://twitter.com/FSVO'),)

SHOW_ARTICLE_CATEGORY=True

DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_CATEGORIES_ON_SIDEBAR=True




DISPLAY_RECENT_POSTS_ON_SIDEBAR=True

DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
