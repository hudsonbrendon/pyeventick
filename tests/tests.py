import unittest
from pyeventick import Eventick

class TestEventick(unittest.TestCase):

    def setUp(self):
        self.eventick = Eventick('pyeventick@gmail.com', 'pyeventick123')

    def test_get_token(self):
        self.assertEqual(self.eventick.get_token()[0], 'mrEtj_9SLF43eB5fWRw1pCfY6Gbrhr2C4g')

    def test_get_api_url(self):
        self.assertEqual(self.eventick.get_api_url('events.json'), 'https://www.eventick.com.br/api/v1/events.json')
        self.assertEqual(self.eventick.get_api_url('events/10.json'), 'https://www.eventick.com.br/api/v1/events/10.json')
        self.assertEqual(self.eventick.get_api_url('events/10/attendees.json'), 'https://www.eventick.com.br/api/v1/events/10/attendees.json')
        self.assertEqual(self.eventick.get_api_url('events/10/attendees/10.json'), 'https://www.eventick.com.br/api/v1/events/10/attendees/10.json')
        self.assertEqual(self.eventick.get_api_url('events/10/attendees/10.json'), 'https://www.eventick.com.br/api/v1/events/10/attendees/10.json')
        self.assertEqual(self.eventick.get_api_url('events/10/attendees/10.json?checked_at=2012-10-17T16:54:35-03:00'), 'https://www.eventick.com.br/api/v1/events/10/attendees/10.json?checked_at=2012-10-17T16:54:35-03:00')
        self.assertEqual(self.eventick.get_api_url('events/10/attendees/check_all.json'), 'https://www.eventick.com.br/api/v1/events/10/attendees/check_all.json')

if __name__ == '__main__':
    unittest.main()
