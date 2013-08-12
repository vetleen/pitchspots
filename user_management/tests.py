from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


c = Client()  

def create_test_user(username, password):
    ''' Create a user, you must pass username and password. '''
    new_user_for_test = User.objects.create_user(username=username, password=password)
    new_user_for_test.save()

def count_objects(object_to_count):
    return len(object_to_count.objects.all())

class SimpleTest(TestCase):        
    def test_createuserview(self):
        """
        Tests that createuserview acts like it should.
        """  
        #Create a user validly
        test_username = "johnnybravo"
        test_password = "godsgifttowomen"       
        response = c.post('/user/create/', {        'email': 'test@test.com', 
                                                    'password': 'test-password',
                                                    })
        #print response.content
        self.assertEqual(count_objects(User), 1)
        self.assertEqual(response.status_code, 200)
        self.assertIn("User was successfully created.", response.content)

        #Create a user whos username already exists
        test_username = "johnnybravo"
        test_password = "godsgifttowomen"       
        response = c.post('/user/create/', {        'email': 'test@test.com', 
                                                    'password': 'test-password',
                                                    })
        #print response.content
        self.assertEqual(count_objects(User), 1)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Username is unavailable, this may be because it is already in use.", response.content)
        
    def test_logoutview(self):
        """
        Tests that logoutview acts like it should.
        """    
        #Create a user
        test_username = "johnnybravo"
        test_password = "godsgifttowomen"
        u = create_test_user(test_username, test_password)
        test_username = "johnnybravo2"
        test_password = "godsgifttowomen"
        u = create_test_user(test_username, test_password)       
        
        response = c.login(username=test_username, password=test_password) 
        #u = User.objects.get(id=1)
        
        #Assert that there is now a logged in user PROBABLY OUT OF ORDER
        self.assertIn('_auth_user_id', c.session)
        #print c.session['_auth_user_id']
        
        #Try a valid logout
        response = c.post('/user/logout/')        
        
        #Assert that we get the proper responsecode
        self.assertEqual(response.status_code, 200)        
        
        #Assert that there are curretly no users logged in OUT OF ORDER
        #self.assertIn('_auth_user_id', c.session)
        #print dir(c.session)#['_auth_user_id']
        
    def test_loginview(self):
        """
        Tests that loginview acts like it should.
        """    
        #Create a user
        test_username = "johnnybravo"
        test_password = "godsgifttowomen"
        u = create_test_user(test_username, test_password)
        
        #Assert that one user object exists
        self.assertEqual (count_objects(User), 1)
        
        #Try a valid login
        response = c.post('/user/login/', { 'username': test_username, 
                                            'password': test_password,
                                                    })        
        
        #Check that we get the proper responsecode
        self.assertEqual(response.status_code, 200)   
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
             
