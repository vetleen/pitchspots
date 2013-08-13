from datetime import datetime  

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

import ps_editor_logic
from ps_editor.models import Pitchspot, IntroModule



## SET UP FOR TESTS
c = Client()    

def count_objects(object_to_count):
    return len(object_to_count.objects.all())


## COMMON FUNCTIONS
def create_test_user(username, password):
    ''' Create and logs in a user, you must pass username and password. '''
    new_user_for_test = User.objects.create_user(username=username, password=password)
    new_user_for_test.save()
    
        
class PsEditorTests(TestCase):
    def test_create_pitchspots(self):
        """
        Tests that pitchspots are created and retrieved correctly
        """
        ###Set up
        #Create and log in user
        create_test_user(username='fred2', password='secret')
        c.login(username="fred2", password="secret")
        
        #Create pitchspot
        response = c.post('/pitchspot/create/', {   'title': 'testspot', 
                                                    'campaign_manager_firstname': 'Johnny',
                                                    'campaign_manager_lastname': 'Bravo',
                                                    })

        #Assert that we get the proper responsecode, and that it worked
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_objects(Pitchspot), 1)
        
        p1 = Pitchspot.objects.get(id=1)
        self.assertEqual(p1.title, 'testspot')
        self.assertEqual(p1.campaign_manager_firstname, 'Johnny')
        self.assertEqual(p1.campaign_manager_lastname, 'Bravo')
        
        #Create another pitchspot
        response = c.post('/pitchspot/create/', {   'title': 'testspot2', 
                                                    'campaign_manager_firstname': 'Johnny2',
                                                    'campaign_manager_lastname': 'Bravo2',
                                                    })
        #Assert that we get the proper responsecode, and that it worked
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_objects(Pitchspot), 2)

        p2 = Pitchspot.objects.get(id=2)
        self.assertEqual(p2.title, 'testspot2')
        self.assertEqual(p2.campaign_manager_firstname, 'Johnny2')
        self.assertEqual(p2.campaign_manager_lastname, 'Bravo2')
        
        #Assert that nothing else is affected
        p1 = Pitchspot.objects.get(id=1)
        self.assertEqual(p1.title, 'testspot')
        self.assertEqual(p1.campaign_manager_firstname, 'Johnny')
        self.assertEqual(p1.campaign_manager_lastname, 'Bravo')
                
        #Check that the types are correct
       
        self.assertIsInstance(p1.title, unicode)
        self.assertIsInstance(p1.owner, object)
        self.assertIsInstance(p1.admin, object)
        self.assertIsInstance(p1.is_published, bool)
        self.assertIsInstance(p1.date_created, datetime)
        self.assertIsInstance(p1.campaign_manager_firstname, unicode)
        self.assertIsInstance(p1.campaign_manager_lastname, unicode)

        self.assertIsInstance(p2.title, unicode)
        self.assertIsInstance(p2.owner, object)
        self.assertIsInstance(p2.admin, object)
        self.assertIsInstance(p2.is_published, bool)
        self.assertIsInstance(p2.date_created, datetime)
        self.assertIsInstance(p2.campaign_manager_firstname, unicode)
        self.assertIsInstance(p2.campaign_manager_lastname, unicode)

    def test_create_intromodule(self):
        """
        Tests that intromodules are created and retrieved correctly
        """
        ###Set up
        #Create and log in user
        create_test_user(username='fred2', password='secret')
        c.login(username="fred2", password="secret")
        
        #Create pitchspot
        response = c.post('/pitchspot/create/', {   'title': 'testspot', 
                                                    'campaign_manager_firstname': 'Johnny',
                                                    'campaign_manager_lastname': 'Bravo',
                                                    })

        #Assert that we get the proper responsecode, and that it worked
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_objects(Pitchspot), 1)
        
        p1 = Pitchspot.objects.get(id=1)
        self.assertEqual(p1.title, 'testspot')
        self.assertEqual(p1.campaign_manager_firstname, 'Johnny')
        self.assertEqual(p1.campaign_manager_lastname, 'Bravo')
        
        #Create intromodule
        test_intromodule = ps_editor_logic.create_intro_module(  pitchspot=p1,
                                                            title="test_title", 
                                                            bodytext="test_bodytext", 
                                                            
                                                            )

        #Check that we get what we expect
        response = c.get('/pitchspot/1/')
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
                                            "test_bodytext",
                                            "intromodule_title",
                                            "test_title",
                                            "Johnny",
                                            "Bravo"
                                            ]
        for word in words_expected_to_be_in_response:
            self.assertIn(word, response.content)
 









