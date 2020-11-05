from django.test import TestCase
from event.models import Event
from datetime import datetime, MAXYEAR, timedelta
from django.utils.timezone import make_aware, get_default_timezone
from django.core.exceptions import ValidationError
import random

class EventTestCase(TestCase):

    """
    case : create event
    containing title, desc, date,
    """
    def test_event_creation(self):
        sample_input = {
            'title': 'Event Perdana #1 JDD',
            'description': 'event <i>percobaan</i>',
            'start_at': datetime(2020,10,30), # will raise warning since using naive datetime
            'end_at': datetime(2020,10,30) + timedelta(hours=1), # will raise warning since using naive datetime
        }
        sample_event = Event.objects.create(**sample_input)

        # test : str(model)
        self.assertEqual(str(sample_event), sample_input['title'])
        # test : date saved
        self.assertEqual(sample_event.start_at, datetime.strptime('30 October 2020', '%d %B %Y'))


    """
    case : create many event
    containing title, desc, date,
    then query.
    """
    def test_event_ordering(self):
        def mock_event():
            mock_title = '#{} Meetup {}'.format(random.randrange(1,99), random.choice(['LinuxBunulrejo', 'PolehanDev', 'NgemplakFrontEnd']))
            mock_date = make_aware(datetime(2020,10,random.randrange(1,30)))
            yield Event.objects.create(**{
                'title': mock_title,
                'description': '',
                'start_at': mock_date,
                'end_at': mock_date + timedelta(hours=1),
            })

        # create 20 entry in database...
        sample_events = [next(mock_event()) for _ in range(20)]
        # ... then sort sample 
        sample_events.sort(key=lambda k: k.start_at)

        # query database
        db_events = Event.objects.all()

        # test : check if each created model and database entry match
        for a, b in zip(db_events, sample_events):
            self.assertEqual(a.start_at.timestamp(), b.start_at.timestamp())
            self.assertEqual(a.title, b.title)
            # print('{} = \n{}'.format(a.title, b.title))


    """
    case : create event with invalid date range
    containing title, desc, date,
    """
    def test_event_valid_date(self):
        sample_input = {
            'title': 'Event Perdana #1 JDD',
            'description': 'event <i>percobaan</i>',
            'start_at': make_aware(datetime.strptime('30 October 2020, 18:00', '%d %B %Y, %H:%M')), 
            'end_at': make_aware(datetime.strptime('30 October 2020, 17:00', '%d %B %Y, %H:%M')), 
        }
        
        # test : error when end_date is before start_date
        with self.assertRaises(ValidationError):
            Event.objects.create(**sample_input)


    """
    case : create event
    containing title, desc, date, published date,
    """
    def test_event_status(self):
        # create new input, published
        sample_input = {
            'title': 'Event Perdana #1 JDD',
            'description': 'event <i>percobaan</i>',
            'start_at': make_aware(datetime.strptime('30 October 2020, 18:00', '%d %B %Y, %H:%M')), 
            'end_at': make_aware(datetime.strptime('30 October 2020, 19:00', '%d %B %Y, %H:%M')), 
            'is_published': True
        }
        sample_event = Event.objects.create(**sample_input)

        published_events = Event.objects.published()
        # test : event above is 'published'
        [self.assertTrue(ev.is_published) for ev in published_events]
        
        # create new input, default is unpublished
        sample_input.pop('is_published')
        sample_event_2 = Event.objects.create(**sample_input)
        
        draft_events = Event.objects.draft()
        # test : event above is 'draft'
        [self.assertFalse(ev.is_published) for ev in draft_events]
        