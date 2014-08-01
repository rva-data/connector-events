from django.test import TestCase
from django.core.urlresolvers import reverse

from events.models import Event


class ModelTests(TestCase):

    def test_event_uid(self):
        """Ensure the UID is created"""
        e = Event(name="Test")
        self.assertFalse(getattr(e, 'uid'))
        e.save()
        self.assertTrue(e.uid)
