from datetime import datetime

from django.contrib import admin

from .models import Event
from .forms import EventAdminForm


class PastOrCurrent(admin.SimpleListFilter):
    title = 'Current event'

    parameter_name = 'current'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('yes', 'current events'),
            ('no', 'past events'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'yes':
            return queryset.filter(start__gte=datetime.now())
        if self.value() == 'no':
            return queryset.filter(start__lte=datetime.now())


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'description')
    list_display = ('name', 'start')
    list_filter = ('is_active', PastOrCurrent)


admin.site.register(Event, EventAdmin)
