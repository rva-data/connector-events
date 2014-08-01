from django.conf.urls import patterns, url

from .views import EventList, EventDetail
from .feeds import EventFeed


urlpatterns = patterns('',
    url(r'^$', view=EventList.as_view(), name="event_list"),
    url(r'^ical/$', view=EventFeed(), name="event_list_ical"),
    url(r'^(?P<slug>[\w\d-]+)-(?P<pk>\d+)/$', view=EventDetail.as_view(), name="event_detail"),
)
