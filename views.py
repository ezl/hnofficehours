from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from schedule.models import Event


def site_index(request, template_name='index.html'):
    available_users = User.objects.filter(profile__is_available=True)
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
