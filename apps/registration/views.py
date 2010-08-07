from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from registration.forms import RegistrationForm

def register(request, template_name='registration/register.html'):
    if request.method == 'GET':
        profile_url = settings.USER_PROFILE_URL % 'username'
        form = RegistrationForm()
    else: # POST
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            # form validation checks that hn_username matches what's provided
            # and that the "key" (a url) is in the profile
            messages.success(request, 'Registration successful.')
            # TODO: this needs to redirect to the set password url
            return HttpResponseRedirect('/')
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
    