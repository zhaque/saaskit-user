from django.conf import settings
from django.conf.urls.defaults import *
from notification import views
from django.views.generic import simple
from django.views.generic.simple import direct_to_template
handler404 = 'perfect404.views.page_not_found'

import frontendadmin.views
from django_authopenid import views as oid_views
from registration import views as reg_views

from muaccounts.views.decorators import public
from muaccount_content.forms import MuFlatpageAddForm, MuFlatpageChangeForm

def mu_initial(func):
    def wrapped(request, initial=None, *args, **kwargs):
        if initial is None: initial = {}
        initial['muaccount'] = request.muaccount.id
        return func(request, initial=initial, *args, **kwargs)
    
    return wrapped


urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
       'template': 'index.html',
    }, name='notification_notices'),

    url(r'^sorry/$', public(direct_to_template), {
        'template': 'account_nam.html'
    }, name='muaccounts_not_a_member'),

    url(r'^sso/$', 'sso.views.sso', name="sso"),

    url(r'^admin/dashboard/$', views.notices, {
        'template': 'account/dashboard.html',
    }, name='account_dashboard'),

    url(r'^extend/plans/$', simple.direct_to_template, {
        'template': 'account_plans.html',
    }, name='account_plans'),

    url(r'^extend/invoice/$', simple.direct_to_template, {
        'template': 'account_invoice.html',
    }, name='account_invoice'),
    
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 
        'muaccounts.views.members.mu_activate', name='registration_activate'),

    url(r'^accounts/register/$', public(oid_views.register), 
        name='user_register'),
    url(r'^accounts/signin/complete/$', public(oid_views.complete_signin), 
        name='user_complete_signin'),
    url(r'^accounts/signin/$', public(oid_views.signin), name='user_signin'),
    url(r'^accounts/signup/complete/$',public(direct_to_template), 
        {'template': 'registration/registration_complete.html'},
        name='registration_complete'),
    
    (r'^accounts/', include('django_authopenid.urls')),
    (r'^admin/', include('muaccounts.urls')),
    (r'^profiles/', include('saaskit_profile.urls')),
    (r'^notices/', include('notification.urls')),
    (r'^subscription/', include('subscription.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    
    #Manage content
    url(r'^admin/apps/$', 'muaccount_content.views.mu_listing', name='app_settings'),
    
    url(r'^content/add/(?P<app_label>muaccount_content)/(?P<model_name>muflatpage)/$', 
        mu_initial(frontendadmin.views.add),
        {'form_exclude': ('enable_comments', 'template_name', 'use_default', 'active'),
         'form_class': MuFlatpageAddForm,
         'initial': {'sites': [settings.SITE_ID,]},
         'template_name': 'muaccounts/frontendadmin_form.html',
         },
        name='frontendadmin_add'
    ),
    
    url(r'^content/change/(?P<app_label>muaccount_content)/(?P<model_name>muflatpage)/(?P<instance_id>[\d]+)/$', 
        mu_initial(frontendadmin.views.change),
        {'form_exclude': ('enable_comments', 'template_name'),
         'form_class': MuFlatpageChangeForm,
         'template_name': 'muaccounts/frontendadmin_form.html',
         },
        name='frontendadmin_change'
    ),
    
    (r'^content/', include('frontendadmin.urls')),
)

# serve static files in debug mode
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
