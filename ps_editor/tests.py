from datetime import datetime  

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

import ps_editor_logic
from ps_editor.models import Pitchspot, IntroModule

## SET UP FOR TESTS
c = Client()    

## COMMON FUNCTIONS
def create_test_user(username, password):
    ''' Create and logs in a user, you must pass username and password. '''
    new_user_for_test = User.objects.create_user(username=username, password=password)
    new_user_for_test.save()
    c.login(username=username, password=password)            
        
class PsEditorTests(TestCase):
    def test_pitchspots(self):
        """
        Tests that pitchspots are created and retrieved correctly
        """
        def assert_that_x_pitchspots_exist(x):
            ''' Checks that x pitchspots exist '''
            number_of_pitchspots = Pitchspot.objects.all().count()
            self.assertEqual(number_of_pitchspots, x)


        ###Set up
        #Create user
        create_test_user(username='fred2', password='secret')        
        #Create pitchspot
        response = c.post('/pitchspot/create/', {   'title': 'testspot', 
                                                    'campaign_manager_firstname': 'Johnny',
                                                    'campaign_manager_lastname': 'Bravo',
                                                    })

        #Check that we get the proper responsecode, and that it worked
        self.assertEqual(response.status_code, 200)
        assert_that_x_pitchspots_exist(1)
        
        #Create another pitchspot
        response = c.post('/pitchspot/create/', {   'title': 'testspot2', 
                                                    'campaign_manager_firstname': 'Johnny2',
                                                    'campaign_manager_lastname': 'Bravo2',
                                                    })
        #Check that we get the proper responsecode, and that it worked
        self.assertEqual(response.status_code, 200)
        assert_that_x_pitchspots_exist(2)
        
        #Check that the types are correct
        p = Pitchspot.objects.get(id=1)
        
        self.assertIsInstance(p.title, unicode)
        self.assertIsInstance(p.owner, object)
        self.assertIsInstance(p.admin, object)
        self.assertIsInstance(p.is_published, bool)
        self.assertIsInstance(p.date_created, datetime)
        self.assertIsInstance(p.campaign_manager_firstname, unicode)
        self.assertIsInstance(p.campaign_manager_lastname, unicode)
        
        #Create intromodule
        test_intromodule = ps_editor_logic.create_intro_module(  pitchspot=Pitchspot.objects.get(id=1),
                                                            title="test_title", 
                                                            bodytext="test bodytext", 
                                                            ingress="ingress here"
                                                            )

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
                                            "owner", 
                                            "title", 
                                            "fred2",
                                            "testspot",
                                            "1",
                                            "intromodule_bodytext",
                                            "intromodule_ingress",
                                            "intromodule_title",
                                            "Johnny",
                                            "Bravo"
                                            ]
        for word in words_expected_to_be_in_response:
            self.assertIn(word, response.content)
 









