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

c = Client()    

def create_test_user(username='fred', password='secret'):
    ''' Create and logs in a user, you can pass username and password, or it will default to "fred" and "secret". '''
    new_user_for_test = User.objects.create_user(username=username, password=password)
    new_user_for_test.save()
    c.login(username=username, password=password)            
        
class CreatePitchspotTest(TestCase):
    def test_create_pitchspot(self):
        """
        Tests that new pitchspots are created correctly
        """
        def check_that_x_pitchspots_exist(x):
            ''' Checks that x pitchspots exist '''
            number_of_pitchspots = Pitchspot.objects.all().count()
            self.assertEqual(number_of_pitchspots, x)

        #Set up
      
        create_test_user(username='fred', password='secret')
        
        #Check that no pitchspots has been created yet
        check_that_x_pitchspots_exist(0)
               
        #try to create a Pitchspot
        response = c.post('/pitchspot/create/', {'title': 'testspot', 'is_published': 'False'})

        #Check that a pitchspot has been created
        check_that_x_pitchspots_exist(1)
        
        #title = "Test1"
        #owner = 
        #logic.create_pitchspot(title, owner, administrator, is_published, date_completed)
        #self.assertEqual("Hello World!", hello_var)
