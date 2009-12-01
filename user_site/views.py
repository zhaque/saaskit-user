### -*- coding: utf-8 -*- ####################################################

from django.http import HttpResponseRedirect
from django.utils.http import urlquote_plus
from django.conf import settings 
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.contrib.auth.decorators import login_required

from sso.views import sso

from muaccounts.views.decorators import public
from muaccounts.utils import construct_main_site_url

@public
def signin(request, redirect_field_name=REDIRECT_FIELD_NAME):
    
    redirect_to = request.REQUEST.get(redirect_field_name, settings.LOGIN_REDIRECT_URL)
    
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    else:
        sso_url = "%s?%s=%s" \
                % (getattr(settings, 'SSO_URL', '/sso/'), 
                   redirect_field_name, 
                   urlquote_plus(request.get_host() + request.get_full_path()),
                   )
        
        return HttpResponseRedirect("%s?%s=%s&muaccount=%d" \
                % (construct_main_site_url(getattr(settings, 'LOGIN_URL', '/accounts/signin/'), False), 
                   redirect_field_name, 
                   urlquote_plus(sso_url),
                   request.muaccount.pk))

@login_required
@public
def signout(request, redirect_field_name=REDIRECT_FIELD_NAME):
    """ log out then redirect to logout on main site """
    
    redirect_to = request.REQUEST.get(redirect_field_name, None)
    logout_url = "%s?%s=%s" \
                % (construct_main_site_url(getattr(settings, 'LOGOUT_URL', '/accounts/signout/'), False), 
                   redirect_field_name, 
                   urlquote_plus(request.build_absolute_uri(redirect_to)))
    
    data = request.GET.copy()
    data[redirect_field_name] = logout_url
    request.GET = data
    response = sso(request)
    
    logout(request)
    return response
    