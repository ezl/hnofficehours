from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from schedule.models import Event
from schedule.periods import Period


def site_index(request, template_name='index.html'):
    # most future office hours to show
    MAX_FUTURE_OFFICE_HOURS = 30
    # furthest into the future to display office hours
    MAX_FUTURE_DAYS = 30
    users_available_now = User.objects.filter(profile__is_available=True)
    events = Event.objects.all()
    now = Period(events=events, start=datetime.now(),
                 end=datetime.now() + timedelta(minutes=1))
    occurences = now.get_occurrences()
    users_holding_office_hours_now = map(lambda x: x.event.creator, occurences)
    users = set(list(users_available_now) + users_holding_office_hours_now)
    future = Period(events=events, start=datetime.now(),
                    end=datetime.now() + timedelta(days=MAX_FUTURE_DAYS))
    upcoming_office_hours = future.get_occurrences()
    upcoming_office_hours = upcoming_office_hours[:MAX_FUTURE_OFFICE_HOURS]
    return direct_to_template(request, template_name, locals())

def about(request):
    return direct_to_template(request, 'about.html')
