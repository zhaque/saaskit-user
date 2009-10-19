from saaskit.settings import *

import os.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_ID = 2

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
APP_MEDIA_ROOT = MEDIA_ROOT

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+*q3$z(d1@hi^p%645&636$n7r@=w!m)(z9@k9&9s9_7uh%a+s'

ROOT_URLCONF = 'user_site.urls'

MIDDLEWARE_CLASSES += ('muaccounts.middleware.MUAccountsMiddleware',)

TEMPLATE_DIRS = (
    os.path.join(KIT_ROOT, 'templates/user_sites'),
) + TEMPLATE_DIRS
