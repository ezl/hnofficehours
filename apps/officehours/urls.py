from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.list_detail import object_list
from schedule.models import Calendar
from schedule.feeds import UpcomingEventsFeed
from schedule.feeds import CalendarICalendar
from schedule.periods import Year, Month, Week, Day

info_dict = {
    'queryset': Calendar.objects.all(),
}

global_calendar_slug = getattr(settings, 'GLOBAL_CALENDAR_SLUG', 'cal')

urlpatterns = patterns('',

# url(r'^$',
#     'schedule.views.calendar',
#     name = "calendar_home",
#     kwargs={'calendar_slug': global_calendar_slug}
#     ),
# 
# url(r'^year/$',
#     'schedule.views.calendar_by_periods',
#     name="year_calendar",
#     kwargs={'periods': [Year],
#             'calendar_slug': global_calendar_slug,
#             'template_name': 'schedule/calendar_year.html'}),
# 
# url(r'^tri_month/$',
#     'schedule.views.calendar_by_periods',
#     name="tri_month_calendar",
#     kwargs={'periods': [Month],
#             'calendar_slug': global_calendar_slug,
#             'template_name': 'schedule/calendar_tri_month.html'}),
# 
# url(r'^compact_month/$',
#     'schedule.views.calendar_by_periods',
#     name = "compact_calendar",
#     kwargs={'periods': [Month],
#             'calendar_slug': global_calendar_slug,
#             'template_name': 'schedule/calendar_compact_month.html'}),
# 
# url(r'^month/$',
#     'schedule.views.calendar_by_periods',
#     name = "month_calendar",
#     kwargs={'periods': [Month],
#             'calendar_slug': global_calendar_slug,
#             'template_name': 'schedule/calendar_month.html'}),
url(r'^$',
    'schedule.views.calendar_by_periods',
    name = "week_calendar",
    kwargs={'periods': [Week],
            'calendar_slug': global_calendar_slug,
            'template_name': 'schedule/calendar_week.html'}),

url(r'^daily/(?P<calendar_slug>\w+)?/$',
    'schedule.views.calendar_by_periods',
    name = "day_calendar",
    kwargs={'periods': [Day],
            # 'calendar_slug': global_calendar_slug,
            'template_name': 'schedule/calendar_day.html'}),

url(r'^event/create/$',
    'officehours.views.create_or_edit_event',
    name='calendar_create_event',
    kwargs={'calendar_slug': global_calendar_slug}),

url(r'^event/edit/(?P<event_id>\d+)/$',
    'officehours.views.create_or_edit_event',
    name='edit_event',
    kwargs={'calendar_slug': global_calendar_slug}),

url(r'^event/(?P<event_id>\d+)/$',
    'schedule.views.event',
    name="event"),
    
url(r'^event/delete/(?P<event_id>\d+)/$',
    'schedule.views.delete_event',
    name="delete_event"),

#urls for already persisted occurrences
url(r'^occurrence/(?P<event_id>\d+)/(?P<occurrence_id>\d+)/$',
    'schedule.views.occurrence',
    name="occurrence"), 
url(r'^occurrence/cancel/(?P<event_id>\d+)/(?P<occurrence_id>\d+)/$',
    'schedule.views.cancel_occurrence',
    name="cancel_occurrence"),
url(r'^occurrence/edit/(?P<event_id>\d+)/(?P<occurrence_id>\d+)/$',
    'schedule.views.edit_occurrence',
    name="edit_occurrence"),

#urls for unpersisted occurrences
url(r'^occurrence/(?P<event_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<second>\d+)/$',
    'schedule.views.occurrence', 
    name="occurrence_by_date"),
url(r'^occurrence/cancel/(?P<event_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<second>\d+)/$',
    'schedule.views.cancel_occurrence', 
    name="cancel_occurrence_by_date"),
url(r'^occurrence/edit/(?P<event_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<second>\d+)/$',
    'schedule.views.edit_occurrence', 
    name="edit_occurrence_by_date"),
    
url(r'^available_now/$',
    'officehours.views.new_event_now',
    kwargs={'calendar_slug': global_calendar_slug },
    name='available_now'),


#feed urls 
# url(r'^feed/calendar/(.*)/$',
#     'django.contrib.syndication.views.feed', 
#     { "feed_dict": { "upcoming": UpcomingEventsFeed } }),
#  
# (r'^ical/calendar/(.*)/$', CalendarICalendar()),

)
