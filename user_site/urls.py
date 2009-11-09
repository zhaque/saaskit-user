from django.conf import settings
from django.conf.urls.defaults import *
from notification import views
#from django.views.generic import simple
from django.views.generic.simple import direct_to_template
#from django.views.generic.list_detail import object_list
#from django.contrib.auth.decorators import login_required

import frontendadmin.views
from django_authopenid import views as oid_views
#from registration import views as reg_views

from saaskit.urls import handler404, urlpatterns as saaskit_patterns
from muaccounts.views.decorators import public
from muaccount_content.forms import MuFlatpageAddForm, MuFlatpageChangeForm
from muaccounts.urls import mu_initial

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
       'template': 'index.html',
    }, name='notification_notices'),

    url(r'^sorry/$', public(direct_to_template), {
        'template': 'account_nam.html'
    }, name='muaccounts_not_a_member'),

    url(r'^admin/dashboard/$', views.notices, {
        'template': 'account/dashboard.html',
    }, name='account_dashboard'),

    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 
        'muaccounts.views.members.mu_activate', name='registration_activate'),

    url(r'^accounts/register/$', 'muaccounts.views.members.mu_register', 
        name='user_register'),
    url(r'^accounts/signin/complete/$', public(oid_views.complete_signin), 
        name='user_complete_signin'),
    url(r'^accounts/signin/$', public(oid_views.signin), name='user_signin'),
    
    url(r'^accounts/signup/complete/$',public(direct_to_template), 
        {'template': 'registration/registration_complete.html'},
        name='registration_complete'),
    
    (r'^admin/', include('muaccounts.urls')),
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
)

#apply saaskit-core url mapping
urlpatterns += saaskit_patterns
