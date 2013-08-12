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
        #
        self.assertEqual(count_objects(User), 1)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Your acount was created successfully.", response.content)

        #Create a user whos username already exists
        test_username = "johnnybravo"
        test_password = "godsgifttowomen"       
        response = c.post('/user/create/', {        'email': 'test@test.com', 
                                                    'password': 'test-password',
                                                    })
        #
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
        
        response = c.login(username=test_username, password=test_password) 
        
        #Assert that there is now a logged in user
        self.assertIn('_auth_user_id', c.session)
        
        #Logout
        response = c.post('/user/logout/')        
        
        #Assert that we get the proper response
        self.assertEqual(response.status_code, 200)
        self.assertIn("You were logged out successfully.", response.content)
        
        #Assert that there are curretly no users logged in
        self.assertNotIn('_auth_user_id', c.session)
        
    def test_loginview_test_valid_login(self):
        """
        Tests that loginview acts like it should.
        """    
        #Create a user
        test_username = "johnnybravo"
        test_password = "godsgifttowomen"
        u = create_test_user(test_username, test_password)
        
        #Assert that one user object exists
        self.assertEqual (count_objects(User), 1)
        
        #Assert that there are curretly no users logged in
        self.assertNotIn('_auth_user_id', c.session)
        
        #Log in
        response = c.post('/user/login/', { 'username': test_username, 
                                            'password': test_password,
                                                    })        
        
        #Assert that we get the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("You were logged in successfully.", response.content)        
            
        #Assert that there is now a logged in user
        self.assertIn('_auth_user_id', c.session)
        
    def test_loginview_test_invalid_login(self):
        """
        Tests that loginview acts like it should.
        """    
        #Create a user
        test_username = "johnnybravo"
        test_password = "godsgifttowomen"
        u = create_test_user(test_username, test_password)
        
        #Assert that one user object exists
        self.assertEqual (count_objects(User), 1)

        #Assert that there are curretly no users logged in
        self.assertNotIn('_auth_user_id', c.session)
        
        #Try a login with the wrong password
        response = c.post('/user/login/', { 'username': test_username, 
                                            'password': "test_password",
                                                    })        
        
        #Check that we get the proper response code and response
        self.assertEqual(response.status_code, 200)
        self.assertIn("The username and password that you provided do not match. Please try again.", response.content)        
            
        #Assert that there is no logged in user at this point
        self.assertNotIn('_auth_user_id', c.session)        
        
    def test_edituser_view(self):
        """
        Tests that loginview acts like it should.
        """    
        #Create a user
        test_username = "johnnybravo@gphone.com"
        test_password = "godsgifttowomen"
        u = create_test_user(test_username, test_password)

        #Assert that the user object was created with the correct attributes
        u = User.objects.get(id=1)
        self.assertEqual(u.username, test_username)

        #Try to update user while logged out
        response = c.post('/user/edit/', { 'email': "test@test.com", 
                                           'first_name': "Jack",
                                           'last_name': "Sparrow"
                                                    })        

        #Assert that user is redirected to login-page
        self.assertEqual(response.status_code, 302)  

        #Assert that the user object was not updated
        self.assertNotEqual(u.username, "test@test.com")
        self.assertNotEqual(u.first_name, "Jack")
        self.assertNotEqual(u.last_name, "Sparrow")

        #Try to update user while logged in
        response = c.login(username=test_username, password=test_password)
        response = c.post('/user/edit/', { 'email': "test@test.com", 
                                           'first_name': "Jack",
                                           'last_name': "Sparrow"
                                                    })

        #Assert that user gets the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("Username successfully updated.", response.content)
        self.assertIn("First name successfully updated.", response.content)
        self.assertIn("Last name successfully updated.", response.content)
        
        #Assert that the user object was changed
        u = User.objects.get(id=1)
        self.assertEqual(u.username, "test@test.com")
        self.assertEqual(u.first_name, "Jack")
        self.assertEqual(u.last_name, "Sparrow")                
        
        #Try to update single items
        response = c.post('/user/edit/', { 'email': "test2@test.com", 
                                           'first_name': "",
                                           'last_name': ""
                                                    })
                                                    
        #Assert that user gets the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("Username successfully updated.", response.content)
        self.assertNotIn("First name successfully updated.", response.content)        
        self.assertNotIn("Last name successfully updated.", response.content)

        #Assert that the user object was changed
        u = User.objects.get(id=1)
        self.assertEqual(u.username, "test2@test.com")
        
        #Try to update single items
        response = c.post('/user/edit/', { 'email': "", 
                                           'first_name': "Peter",
                                           'last_name': ""
                                                    })
                                                    
        #Assert that user gets the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("First name successfully updated.", response.content)
        self.assertNotIn("Username successfully updated.", response.content)        
        self.assertNotIn("Last name successfully updated.", response.content)

        #Assert that the user object was changed
        u = User.objects.get(id=1)
        self.assertEqual(u.first_name, "Peter")

        #Try to update single items
        response = c.post('/user/edit/', { 'email': "", 
                                           'first_name': "",
                                           'last_name': "Griffin"
                                                    })
                                                    
        #Assert that user gets the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("Last name successfully updated.", response.content)
        self.assertNotIn("Username successfully updated.", response.content)        
        self.assertNotIn("First name successfully updated.", response.content)        

        #Assert that the user object was changed
        u = User.objects.get(id=1)
        self.assertEqual(u.last_name, "Griffin")

    def test_changepasswordview(self):
        """
        Tests that loginview acts like it should.
        """    
        #Create a user
        test_username = "johnnybravo@thistest.com"
        test_password = "godsgifttowomen"
        u = create_test_user(test_username, test_password)
        
        #Check that the password works
        u = User.objects.get(id=1)
        self.assertTrue(u.check_password(test_password))
        
        response = c.login(username=test_username, password=test_password)
        #Try to change password properly
        response = c.post('/user/changepassword/', {    'old_password': test_password, 
                                                        'new_password1': "Jackinabox",
                                                        'new_password2': "Jackinabox"
                                                    })        

        #Assert that user gets the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("Your password was successfully changed.", response.content)

        #Check that the new password works
        u = User.objects.get(id=1)
        self.assertTrue(u.check_password("Jackinabox"))
        
        #Try to change password with new password mismatch
        response = c.post('/user/changepassword/', {    'old_password': "Jackinabox", 
                                                        'new_password1': "Jackinabox2",
                                                        'new_password2': "Jackinabox3"
                                                    })        

        #Assert that user gets the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("The new passwords you provided did not match. Your password was not changed.", response.content)

        #Check that the old password works
        u = User.objects.get(id=1)
        self.assertTrue(u.check_password("Jackinabox"))
        
        #Try to change password while providing wrong old password
        response = c.post('/user/changepassword/', {    'old_password': "Jackinabox4", 
                                                        'new_password1': "Jackinabox5",
                                                        'new_password2': "Jackinabox5"
                                                    })        

        #Assert that user gets the correct response
        self.assertEqual(response.status_code, 200)
        self.assertIn("The password you provided was incorrect. Your password was not changed.", response.content)

        #Check that the old password works
        u = User.objects.get(id=1)
        self.assertTrue(u.check_password("Jackinabox"))

