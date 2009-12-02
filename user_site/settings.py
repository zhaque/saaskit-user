from saaskit.settings import *

SITE_ID = 2

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+*q3$z(d1@hi^p%645&636$n7r@=w!m)(z9@k9&9s9_7uh%a+s'

ROOT_URLCONF = 'user_site.urls'

MIDDLEWARE_CLASSES += (
        'muaccounts.middleware.MUAccountsMiddleware',
        'page_view_quotas.middleware.PageViewQuotasMiddleware',
)

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'user_site',
) + INSTALLED_APPS
