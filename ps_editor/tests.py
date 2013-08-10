from datetime import datetime  

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

import ps_editor_logic
from ps_editor.models import Pitchspot

## SET UP FOR TESTS
c = Client()    

## COMMON FUNCTIONS
def create_test_user(username, password):
    ''' Create and logs in a user, you must pass username and password. '''
    new_user_for_test = User.objects.create_user(username=username, password=password)
    new_user_for_test.save()
    c.login(username=username, password=password)            
        
class PsEditorTests(TestCase):
    def test_create_pitchspot(self):
        """
        Tests that new pitchspots are created correctly
        """
        def assert_that_x_pitchspots_exist(x):
            ''' Checks that x pitchspots exist '''
            number_of_pitchspots = Pitchspot.objects.all().count()
            self.assertEqual(number_of_pitchspots, x)

        #Set up
        create_test_user(username='fred', password='secret')
        
        #Check that no pitchspots has been created yet
        assert_that_x_pitchspots_exist(0)
               
        #Create a Pitchspot
        response = c.post('/pitchspot/create/', {'title': 'testspot', 'is_published': 'False'})

        #Check that we get the proper responsecode
        self.assertEqual(response.status_code, 200)
        
        #Check that a pitchspot has been created
        assert_that_x_pitchspots_exist(1)
        
        #Check that the types are correct
        NewP = Pitchspot.objects.get(id=1)
        
        #print "date_created is type: %s, and is: %s" % (type(NewP.date_created), NewP.date_created)
        self.assertIsInstance(NewP.title, unicode)
        self.assertIsInstance(NewP.owner, object)
        self.assertIsInstance(NewP.admin, object)
        self.assertIsInstance(NewP.is_published, bool)
        self.assertIsInstance(NewP.date_created, datetime)

    def test_retrieve_pitchspot(self):
        """
        Tests that pitchspots are retrieved correctly
        """
        ###Set up
        #Create user
        create_test_user(username='fred2', password='secret')        
        #Create pitchspot
        response = c.post('/pitchspot/create/', {'title': 'testspot', 'is_published': 'False'})
        #Check that we get the proper responsecode
        self.assertEqual(response.status_code, 200)
        
        #Check that we get what we expect
        response = c.get('/pitchspot/1/')
        #Check that we get the proper responsecode
        self.assertEqual(response.status_code, 200)
        #Check that content is as expected
        self.assertIsInstance(response.content, str)
        words_expected_to_be_in_response = ["admin", 
                                            "date_created",
                                            "day", 
                                            "hour", 
                                            "minute", 
                                            "month", 
                                            "second", 
                                            "year", 
                                            "is_published", 
                                            "owner", 
                                            "title", 
                                            "fred2",
                                            "true", 
                                            "testspot",
                                            ]
        for word in words_expected_to_be_in_response:
            self.assertIn(word, response.content)
 
    def test_create_module(self):
        """
        Tests that pitchspots are retrieved correctly
        """
        ###Set up
        #Create user
        create_test_user(username='fred2', password='secret')        
        #Create pitchspot
        response = c.post('/pitchspot/create/', {'title': 'testspot', 'is_published': 'False'})
        #Check that we get the proper responsecode
        self.assertEqual(response.status_code, 200)          









