import os
import unittest
from pyeventick import Eventick


class TestEventick(unittest.TestCase):

    def setUp(self):
        self.eventick = Eventick(os.environ.get('EMAIL'),
                                 os.environ.get('PASSWORD'))

    def test_get_token(self):
        self.assertEqual(self.eventick.get_token()[0],
                         os.environ.get('TOKEN'))

    def test_get_api_url(self):
        self.assertEqual(self.eventick
                         .get_api_url('events.json'),
                         'https://www.eventick.com.br/api/v1/events.json')

        self.assertEqual(self.eventick
                         .get_api_url('events/10.json'),
                         'https://www.eventick.com.br/api/v1/events/10.json')

        self.assertEqual(self.eventick
                         .get_api_url('events/10/attendees.json'),
                         'https://www.eventick.com.br/'
                         'api/v1/events/10/attendees.json')

        self.assertEqual(self.eventick.get_api_url(
                         'events/10/attendees/10.json'),
                         'https://www.eventick.com.br/'
                         'api/v1/events/10/attendees/10.json')

        self.assertEqual(self.eventick.get_api_url(
                         'events/10/attendees/10.json'),
                         'https://www.eventick.com.br/'
                         'api/v1/events/10/attendees/10.json')

        self.assertEqual(self.eventick.get_api_url(
                         'events/10/attendees/10.json?'
                         'checked_at=2012-10-17T16:54:35-03:00'),
                         'https://www.eventick.com.br/'
                         'api/v1/events/10/attendees/10.json?'
                         'checked_at=2012-10-17T16:54:35-03:00')

        self.assertEqual(self.eventick.get_api_url(
                         'events/10/attendees/check_all.json'),
                         'https://www.eventick.com.br/'
                         'api/v1/events/10/attendees/check_all.json')

    def test_events(self):
        self.assertEqual(self.eventick.events()
                         ['events'][0]['title'], 'Event test')

    def test_event(self):
        self.assertEqual(self.eventick.event(21091)
                         ['events'][0]['title'], 'Event test')

    def test_attendee(self):
        self.assertEqual(self.eventick.attendee(21091, 911536)
                         ['attendees'][0]['code'], 'XWD2I1LH')

    def test_checkin(self):
        self.assertEqual(self.eventick.checkin(
                         21091, 'XWD2I1LH',
                         '2012-10-17T16:54:35-03:00'),
                         204)

        self.assertEqual(self.eventick.attendee(21091, 911536)
                         ['attendees'][0]['checked_at'],
                         '2012-10-17 16:54:35 -0300')

    def test_checkin_all(self):
        self.assertEqual(self.eventick.checkin_all(
                         21091,
                         {"attendees": [{"id": 911697,
                          "checked_at": "2012-10-17T16:54:35-03:00"},
                                        {"id": 911536,
                                         "checked_at":
                                         "2012-10-17T16:54:35-03:00"}]}), 200)

        self.assertEqual(self.eventick.attendee(21091, 911697)
                         ['attendees'][0]['checked_at'],
                         '2012-10-17 16:54:35 -0300')

        self.assertEqual(self.eventick.attendee(21091, 911536)
                         ['attendees'][0]['checked_at'],
                         '2012-10-17 16:54:35 -0300')


if __name__ == '__main__':
    unittest.main()
