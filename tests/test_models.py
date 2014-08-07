from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from django_dynamic_fixture import G
from events.models import Event


class ModelTests(TestCase):

    def setUp(self):
        today = timezone.now()
        self.past = G(Event, start=today - timedelta(days=2),
                      end=today - timedelta(days=1))
        self.inactive = G(Event, is_active=False)
        self.future = G(Event, start=today + timedelta(days=1),
                        end=today + timedelta(days=2))

    def test_event_uid(self):
        """Ensure the UID is created"""
        e = Event(name="Test")
        self.assertFalse(getattr(e, 'uid'))
        e.save()
        self.assertTrue(e.uid)

    def test_active_queryset(self):
        """Ensure only active events are returned"""
        self.assertEqual(3, Event.objects.all().count())
        self.assertEqual(2, Event.active.all().count())

    def test_current_events(self):
        """Ensure only active events in future are returned"""
        self.assertEqual(3, Event.objects.all().count())
        self.assertEqual(1, Event.current.all().count())
