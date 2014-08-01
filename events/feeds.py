from django.conf import settings
from django.template.defaultfilters import striptags
from django_ical.views import ICalFeed
from .models import Event


class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//rvaconnect.com//RVA Events//EN'
    timezone = settings.TIME_ZONE

    def items(self):
        return Event.current.all().order_by('-start')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return striptags(item.description)

    def item_start_datetime(self, item):
        return item.start

    def item_end_datetime(self, item):
        return item.end

    def item_location(self, item):
        return item.location

    def item_link(self, item):
        return item.url
