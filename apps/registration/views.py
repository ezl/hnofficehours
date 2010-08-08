import string, random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from registration.forms import RegistrationForm

from retrieve_hn_user_data import retrieve_hn_user_data


def register(request, template_name='registration/register.html'):
    if request.method == 'GET':
        profile_url = settings.USER_PROFILE_URL % 'username'
        form = RegistrationForm()
    else: # POST
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            hn_username = form.cleaned_data['hn_username']
            # user_data is a dict containing the users HN account creation
            # date, karma at query time, and HN profile
            user_data = retrieve_hn_user_data(hn_username)
            # form validation checks that hn_username matches what's provided
            # and that the "key" (a url) is in the profile
            temp_password = ''.join(random.sample(string.letters, 16))
            new_user = User.objects.create_user(username=hn_username,
                                                email='',
                                                password=temp_password)
            user = authenticate(username=new_user.username,
                                password=temp_password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'That worked. Please provide a password.')
                return HttpResponseRedirect(reverse('set_password'))
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


@login_required
def set_password(request, template_name='registration/set_password.html'):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password set.')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SetPasswordForm(user=request.user)
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
