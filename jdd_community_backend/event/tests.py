from django.test import TestCase
from event.models import Event
from datetime import datetime
import random

class EventTestCase(TestCase):
    def setUp(self):
        pass
    
    """
    case 1 : create simple event
    containing title, desc and date.
    """
    def test_event_creation(self):
        sample_input = {
            'title': 'Event Perdana #1 JDD',
            'description': 'event <i>percobaan</i>',
            'start_date': datetime(2020,10,30),
        }
        sample_event = Event.objects.create(**sample_input)

        self.assertEqual(str(sample_event), sample_input['title'])
        self.assertEqual(sample_event.start_date, datetime.strptime('30 October 2020', '%d %B %Y'))


    """
    case 2 : create many event
    containing title, desc and date.
    then query.
    """
    def test_event_ordering(self):
        def randsample_event():
            communities = ['LinuxBunulrejo', 'PolehanDev', 'NgemplakFrontEnd']
            yield Event.objects.create(**{
                'title': '#{} Meetup {}'.format(random.randrange(1,99), random.choice(communities)),
                'description': '',
                'start_date': datetime(2020,10,random.randrange(1,30)),
            })

        # create 20 entry in database...
        sample_events = [next(randsample_event()) for _ in range(20)]
        # ... then sort sample 
        sample_events.sort(key=lambda k: k.start_date)

        # query database
        db_events = Event.objects.all()

        #TODO : sample event was not timezone adjusted (+17)
        for a, b in zip(db_events, sample_events):
            self.assertEqual(a.start_date.timestamp(), b.start_date.timestamp())
            self.assertEqual(a.title, b.title)
            # print('{} = \n{}'.format(a.title, b.title))
        
