#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fletcher Foti'
SITENAME = u'OaklandAnalytics'
SITEURL = ''

THEME="./medius"

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Homepage', 'http://fletcherfoti.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True


MEDIUS_CATEGORIES = {
    'Category': {
        'description': 'A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas and dust, and dark matter.',
        #'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/GalacticRotation2.svg/250px-GalacticRotation2.svg.png',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/NGC_3923_Elliptical_Shell_Galaxy.jpg/220px-NGC_3923_Elliptical_Shell_Galaxy.jpg'
    }
}


MEDIUS_AUTHORS = {
    'Onur Aslan': {
        'description': """
            And where does the newborn go from here? The net is vast and infinite.
        """,
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
        'links': (('github-square', 'https://github.com/onuraslan'),
                  ('twitter-square', 'https://twitter.com/oasln'),
                  ('envelope-square', '#')),
    }
}
