import random
from unittest import mock

import pytz
from datetime import datetime, MAXYEAR, timedelta
from django.utils import timezone

from django.test import TestCase
from django.core.exceptions import ValidationError

from event.models import Event


class EventTestCase(TestCase):

    def _mock_inputs(self, set_published=None):
        mock_title = '#{} Meetup {}'.format(random.randrange(1,99), random.choice(['LinuxBunulrejo', 'PolehanDev', 'NgemplakFrontEnd']))
        mock_date = timezone.make_aware(datetime(2020,10,random.randrange(1,30)))
        inputs = {
            'title': mock_title,
            'description': '',
            'start_at': mock_date,
            'end_at': mock_date + timedelta(hours=1),
        }
        if set_published is not None:
            inputs['is_published'] = set_published
        return inputs

    """
    case : create event
    containing title, desc, date,
    """
    def test_event_creation(self):
        def aware_datetime(*args, **kwargs):
            return timezone.make_aware(datetime(*args, **kwargs))

        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=aware_datetime(2020,1,1))):
            # will raise warning if using naive datetime
            sample_inputs = {
                'title': 'Event Perdana #1 JDD',
                'description': 'event <i>percobaan</i>',
                'start_at': aware_datetime(2020,10,30), 
                'end_at': aware_datetime(2020,10,30) + timedelta(hours=1),
            }
            event = Event.objects.create(**sample_inputs)
            
            # inputs test
            self.assertEqual(event.title, sample_inputs['title'])
            self.assertEqual(event.start_at, aware_datetime(2020,10,30))
            # default value test
            self.assertFalse(event.is_published)
            self.assertEqual(event.created_at, aware_datetime(2020,1,1))
            # print / str(model) test
            self.assertEqual(str(event), sample_inputs['title'])
        
        # required test
        with self.assertRaises(TypeError):
            Event.objects.create()
        with self.assertRaises(TypeError):
            Event.objects.create(title='')
        with self.assertRaises(TypeError):
            Event.objects.create(start_at='')
        with self.assertRaises(TypeError):
            Event.objects.create(end_at='')

        # validation test
        with self.assertRaises(ValidationError):
            Event.objects.create(start_at=aware_datetime(2020,2,2), end_at=aware_datetime(2020,2,2) - timedelta(hours=1))


    """
    case : create many event
    containing title, desc, date,
    then query.
    """
    def test_event_many(self):
        # create 20 entry
        events = [Event.objects.create(**self._mock_inputs()) for _ in range(20)]

        ## Test :: All orderings
        unsorted_event_ids = [event.id for event in events]
        
        events.sort(key=lambda k: k.start_at)
        sorted_event_ids = [event.id for event in events]
        
        db_events = Event.objects.all()
        db_event_ids = [event.id for event in db_events]
        
        assert not all([ p == q for p,q in zip(unsorted_event_ids, db_event_ids)])
        assert all([ p == q for p,q in zip(sorted_event_ids, db_event_ids)])
        for a, b in zip(db_events, events):
            self.assertEqual(a.start_at.timestamp(), b.start_at.timestamp())
            self.assertEqual(a.title, b.title)
        
        
    """
    case : create event
    containing title, desc, date, published date,
    """
    def test_event_status(self):
        # create pub/unpub events
        pub_events = [Event.objects.create(**self._mock_inputs(set_published=True)) for _ in range(20)]
        unpub_events = [Event.objects.create(**self._mock_inputs()) for _ in range(30)]

        
        ## Test :: Published/Draft status        

        # test : events is 'published'
        pub_db_events = Event.objects.published()
        self.assertEqual(len(pub_db_events), len(pub_events))
        assert all([ ev.is_published for ev in pub_db_events])
        
        # test : events is 'draft'
        unpub_db_events = Event.objects.draft()
        self.assertEqual(len(unpub_db_events), len(unpub_events))
        assert all([ not ev.is_published for ev in unpub_db_events])
        
        



        
        