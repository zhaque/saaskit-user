from django.conf import settings
from django.conf.urls.defaults import *
from notification import views
from django.views.generic import simple
handler404 = 'perfect404.views.page_not_found'

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
       'template': 'index.html',
    }, name='notification_notices'),

    url(r'^sorry/$', 'django.views.generic.simple.direct_to_template', {
        'template': 'account_nam.html'
    }, name='muaccounts_not_a_member'),

    url(r'^sso/$', 'sso.views.sso', name="sso"),

    url(r'^admin/dashboard/$', views.notices, {
        'template': 'account/dashboard.html',
        'extra_context': {
            'buy_site_url': settings.BUY_SITE_URL,
        }
    }, name='account_dashboard'),

    url(r'^extend/users/$', simple.direct_to_template, {
        'template': 'manage_users.html',
    }),

    url(r'^extend/apps/$', simple.direct_to_template, {
        'template': 'manage_apps.html',
    }),

    url(r'^extend/dashboard/$', simple.direct_to_template, {
        'template': 'account_dashboard.html',
    }),

    url(r'^extend/profile/$', simple.direct_to_template, {
        'template': 'account_profile.html',
    }),

    url(r'^extend/password/$', simple.direct_to_template, {
        'template': 'account_password.html',
    }),

    url(r'^extend/plans/$', simple.direct_to_template, {
        'template': 'account_plans.html',
    }),

    url(r'^extend/invoice/$', simple.direct_to_template, {
        'template': 'account_invoice.html',
    }),

    (r'^accounts/', include('django_authopenid.urls')),
    (r'^admin/', include('muaccounts.urls')),
    (r'^profiles/', include('saaskit.urls.profiles_urls')),
    (r'^notices/', include('notification.urls')),
    (r'^subscription/', include('subscription.urls')),
)

# serve static files in debug mode
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )