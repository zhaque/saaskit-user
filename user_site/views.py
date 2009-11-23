### -*- coding: utf-8 -*- ####################################################

from django.http import HttpResponseRedirect
from django.utils.http import urlquote_plus
from django.conf import settings 
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from sso.views import sso

from muaccounts.views.decorators import public

def construct_main_site_url(location):
    return "http://%s%s%s" \
            % (Site.objects.get_current().domain, 
               (":%d" % settings.MAIN_SITE_PORT) if hasattr(settings, 'MAIN_SITE_PORT') else '', 
               location)

@public
def signin(request, redirect_field_name=REDIRECT_FIELD_NAME):
    
    redirect_to = request.REQUEST.get(redirect_field_name, settings.LOGIN_REDIRECT_URL)
    
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    else:
        sso_url = construct_main_site_url(getattr(settings, 'SSO_URL', '/sso/')) 
        return HttpResponseRedirect("%s?%s=%s" \
                % (sso_url, redirect_field_name, 
                   urlquote_plus(request.get_host() + request.get_full_path())))

@login_required
@public
def signout(request, redirect_field_name=REDIRECT_FIELD_NAME):
    """ log out then redirect to logout on main site """
    
    redirect_to = request.REQUEST.get(redirect_field_name, None)
    logout_url = "%s?%s=%s" \
                % (construct_main_site_url(getattr(settings, 'LOGOUT_URL', '/accounts/signout/')), 
                   redirect_field_name, 
                   urlquote_plus(request.build_absolute_uri(redirect_to)))
    
    data = request.GET.copy()
    data[redirect_field_name] = logout_url
    request.GET = data
    response = sso(request)
    
    logout(request)
    return response
    