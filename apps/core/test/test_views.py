from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class TestSpotifyBotView(TestCase):

    def setUp(self):
        self.url = reverse('core:spotify')
        self.client = Client()

    def test_get(self):
        """GET / must return status code 200"""
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.content, b'Hello World')
