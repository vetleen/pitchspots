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

## SET UP FOR TESTS
c = Client()    

## COMMON FUNCTIONS
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
               
        #Create a Pitchspot
        response = c.post('/pitchspot/create/', {'title': 'testspot', 'is_published': 'False'})

        #Check that a pitchspot has been created
        check_that_x_pitchspots_exist(1)
        
        #Check that the types are correct
        NewP = Pitchspot.objects.get(id=1)
        print "owner is type: %s" % (type(NewP.owner))
        print "admin is type: %s" % (type(NewP.admin))
        self.assertIsInstance(NewP.title, str)
        self.assertIsInstance(NewP.owner, class)
        self.assertIsInstance(NewP.admin, class)
        self.assertIsInstance(NewP.is_published, bool)













