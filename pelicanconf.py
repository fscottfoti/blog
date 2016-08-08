#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fletcher Foti'
SITENAME = u'OaklandAnalytics'
SITEURL = 'http://localhost:8000'
SITEURL = "https://oaklandanalytics.com"

THEME="./medius"

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('github-square', 'https://github.com/fscottfoti'),
         ('twitter-square', 'https://twitter.com/fscottfoti'),
         ('linkedin-square', 'https://linkedin.com/in/fletcherfoti'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

MEDIUS_CATEGORIES = {
    'Web Tools': {
        'description': 'Ways to understand cities via interactive websites.',
        'thumbnail': SITEURL + '/images/webcities.jpg'
    }
}


MEDIUS_AUTHORS = {
    'Fletcher Foti': {
        'description': """
            PhD in City Planning from Berkeley, now modeling for the Bay Area regional gov't and making web apps to build better cities.
        """,
        'cover': SITEURL + '/images/montreal.jpg',
        'image': SITEURL + '/images/ffoti.png',
        'links': (('github-square', 'https://github.com/fscottfoti'),
                  ('twitter-square', 'https://twitter.com/fscottfoti'),
                  ('linkedin-square', 'https://linkedin.com/in/fletcherfoti'),
                  ('envelope-square', 'mailto:oaklandanalytics@gmail.com'),),
    }
}


EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}
