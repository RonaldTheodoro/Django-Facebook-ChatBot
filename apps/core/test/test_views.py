from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class TestSpotifyBotView(TestCase):

    def setUp(self):
        self.url = reverse('core:spotify')
        self.client = Client()

    def test_get_token_is_invalid(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.content, b'Error, invalid token')
        