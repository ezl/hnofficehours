import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from officehours.forms import EventForm
from schedule.utils import check_event_permissions
from schedule.models import Calendar, Rule
from schedule.utils import coerce_date_dict
from schedule.views import get_next_url


def site_index(request, template_name='index.html'):
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
