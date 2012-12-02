# -*- coding: utf-8 -*- #
from __future__ import unicode_literals, print_function

AUTHOR = "Константин"
SITENAME = "Русские тут"
SITEURL = 'http://tehkonst.github.com'

TIMEZONE = 'Europe/Moscow'

STATIC_PATHS = ['images', 'sources', ]

DEFAULT_LANG = 'ru'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

'''DATE_FORMATS = {
    'en': ( str('rus'),'%d.%m.%Y' ),
	'ru': ( str('usa'),'%a, %d %b %Y' )
}'''

LOCALE = str('C')

#USE_FOLDER_AS_CATEGORY = False

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'