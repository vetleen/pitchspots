"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

from django.contrib.auth.models import User

import logic

class CreatePitchspotTest(TestCase):
    def test_create_pitchspot(self):
        """
        Tests that new pitchspots are created correctly
        """
        #Log in a user
        c = Client()
        c.login(username='fred', password='secret')

        assertTrue(request.user.is_authenticated())
        #title = "Test1"
        #owner = 
        #logic.create_pitchspot(title, owner, administrator, is_published, date_completed)
        #self.assertEqual("Hello World!", hello_var)
