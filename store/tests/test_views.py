from unittest import skip

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from store.models import Category, Product


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
    
    def test_url_allowed_host(self):
        """
        TEST ALLOWED HOSTS
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
