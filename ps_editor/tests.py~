"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

from django.contrib.auth.models import User

import ps_editor.logic
from ps_editor.models import Pitchspot
class CreateUser(TestCase):
    def create_user(self):
        
        #Set up client
        c = Client()
            
        #create and log in a user
        new_user_for_test = User.objects.create_user(username='fred', password='secret')
        new_user_for_test.save()
        c.login(username='fred', password='secret')
        
        
class CreatePitchspotTest(TestCase):
    def test_create_pitchspot(self):
        """
        Tests that new pitchspots are created correctly
        """
        #Check that no pitchspots has been created yet
        number_of_pitchspots = Pitchspot.objects.all().count()
        self.assertEqual(number_of_pitchspots, 0)
        
        #Set up client
        c = Client()
        

        
        #try to create a Pitchspot
        response = c.post('/pitchspot/create/', {'title': 'testspot', 'is_published': 'False'})

        #Check that a pitchspot has been created
        number_of_pitchspots = Pitchspot.objects.all().count()
        self.assertEqual(number_of_pitchspots, 1)
        
        #title = "Test1"
        #owner = 
        #logic.create_pitchspot(title, owner, administrator, is_published, date_completed)
        #self.assertEqual("Hello World!", hello_var)
