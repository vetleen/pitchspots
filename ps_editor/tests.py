"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

import logic

class CreatePitchspotTest(TestCase):
    def test_create_pitchspot(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        hello_var = logic.edit_pitchspot()
        self.assertEqual("Hello World!", hello_var)
