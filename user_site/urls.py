from django.conf import settings
from django.conf.urls.defaults import *
#from django.views.generic import simple
from django.views.generic.simple import direct_to_template

import frontendadmin.views

from saaskit.urls import handler404, urlpatterns as saaskit_patterns
from muaccounts.views.decorators import public
from muaccount_content.forms import MuFlatpageAddForm, MuFlatpageChangeForm
from muaccounts.urls import mu_initial

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
       'template': 'index.html',
    }, name='notification_notices'),

    url(r'^suspended/$', public(direct_to_template), {
        'template': 'suspended.html'
    }, name='muaccount_suspended'),
    
    url(r'^accounts/signin/$', 'user_site.views.signin', name='user_signin'),
    url(r'^accounts/signout/$', 'user_site.views.signout', name='user_signout'),
    
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
    
    (r'^count/', include('django_counter.urls')),
)

#apply saaskit-core url mapping
urlpatterns += saaskit_patterns
