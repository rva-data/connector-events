from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTests(TestCase):

    def test_ical_format(self):
        """Ensure that iCal format is returned"""
        response = self.client.get((reverse('event_list_ical')))
        self.assertEqual(response['Content-Type'],
                'text/calendar; charset=utf8')
