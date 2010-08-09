from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from officehours.forms import EventForm
from schedule.utils import check_event_permissions
from schedule.models import Calendar, Rule, Event
from schedule.utils import coerce_date_dict
from schedule.views import get_next_url


@check_event_permissions
@login_required
def create_or_edit_event(request, calendar_slug, event_id=None, next=None,
    template_name='schedule/create_event.html', form_class = EventForm):
    """
    This function, if it receives a GET request or if given an invalid form in a
    POST request it will generate the following response

    Template:
        schedule/create_event.html

    Context Variables:

    form:
        an instance of EventForm

    calendar:
        a Calendar with id=calendar_id

    if this function gets a GET request with ``year``, ``month``, ``day``,
    ``hour``, ``minute``, and ``second`` it will auto fill the form, with
    the date specifed in the GET being the start and 30 minutes from that
    being the end.

    If this form receives an event_id it will edit the event with that id, if it
    recieves a calendar_id and it is creating a new event it will add that event
    to the calendar with the id calendar_id

    If it is given a valid form in a POST request it will redirect with one of
    three options, in this order

    # Try to find a 'next' GET variable
    # If the key word argument redirect is set
    # Lastly redirect to the event detail of the recently create event
    """
    date = coerce_date_dict(request.GET)
    initial_data = None
    if date:
        try:
            start = datetime(**date)
            initial_data = {
                "start": start,
                "end": start + timedelta(minutes=30)
            }
        except TypeError:
            raise Http404
        except ValueError:
            raise Http404

    instance = None
    if event_id is not None:
        instance = get_object_or_404(Event, id=event_id)

    calendar = get_object_or_404(Calendar, slug=calendar_slug)

    form = form_class(data=request.POST or None, instance=instance,
        hour24=True, creator=request.user, initial=initial_data)

    if form.is_valid():
        event = form.save(commit=False)
        if instance is None:
            event.creator = request.user
            event.calendar = calendar
            event.title = request.user.username

        (repeats, repeats_on, repeats_until) = [form.cleaned_data.get(x) for x
                                                in ('repeats', 'repeats_on',
                                                    'end_recurring_period',)]
        if repeats:
            params = "byweekday:%s;" % ','.join(repeats_on)
            from officehours.forms import WEEKDAY_CHOICES
            weekdays = dict(WEEKDAY_CHOICES)
            name = "Weekly on " + ", ".join(weekdays[int(daynumchar)][:3]+'.' for daynumchar in repeats_on)
            rule, created = Rule.objects.get_or_create(name=name,
                                                       description=name,
                                                       frequency='WEEKLY',
                                                       params=params)
            event.rule = rule

        event.save()
        next = next or reverse('event', args=[event.id])
        next = get_next_url(request, next)
        return HttpResponseRedirect(next)

    next = get_next_url(request, next)
    return render_to_response(template_name, {
        "form": form,
        "calendar": calendar,
        "next":next
    }, context_instance=RequestContext(request))


@login_required
def new_event_now(request, calendar_slug, duration=30):
    start = datetime.now()
    end = start + timedelta(minutes=60-start.minute)
    calendar = Calendar.objects.get(name=getattr(settings, 'GLOBAL_CALENDAR_SLUG', 'cal'))
    Event.objects.create(start=start, end=end, title=request.user.username,
                         creator=request.user, calendar=calendar)
    end_time = end.strftime('%I %p')
    end_time = end_time[1:] if end_time[0] == '0' else end_time
    messages.success(request, 'You are now marked as available until %s.' % end_time)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
