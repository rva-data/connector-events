import calendar
from django import template

register = template.Library()


@register.filter
def month_name(month_number):
    """
    Returns the full name of a month based on the integer order.

    Straight from http://stackoverflow.com/a/7385976/122291
    """
    return calendar.month_name[month_number]
