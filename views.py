from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from schedule.models import Event
from schedule.periods import Period


def site_index(request, template_name='index.html'):
    users_available_now = User.objects.filter(profile__is_available=True)
    events = Event.objects.all()
    now = Period(events=events, start=datetime.now(),
                                end=datetime.now() + timedelta(minutes=1))
    occurences = now.get_occurrences()
    users_holding_office_hours_now = map(lambda x: x.event.creator, occurences)
    users = set(list(users_available_now) + users_holding_office_hours_now)
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
