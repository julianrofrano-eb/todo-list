from django.test import TestCase
from .utils import get_api_event_id, get_api_events, get_auth_token
import json
from unittest.mock import patch


# class TestApiUtils(TestCase):
    
#     @patch('events.utils.Eventbrite.get', return_value=data)    
#     def test_get_events(self, res):
#         events = get_api_events('sdkasopdkasod')
#         self.assertEqual(events, res)
