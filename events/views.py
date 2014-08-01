from django.views.generic import DetailView, ListView

from .models import Event


class EventDetail(DetailView):
    """
    A detail view for events which should fetch the event based on the passed
    ID.
    """
    queryset = Event.active.all()
    template_name = "events/event_detail.html"
    context_object_name = "event"


class EventList(ListView):
    """
    A list view for events.

    The view class provides basic filtering by date. This view should be able
    to return HTML, JSON, and iCalendar format.
    """
    queryset = Event.current.all()
    template_name = "events/event_list.html"
    context_object_name = "events_list"
