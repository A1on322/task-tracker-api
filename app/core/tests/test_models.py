"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models functions"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        test_data = {
            'email': 'test@example.com',
            'password': 'testpass123',
        }
        user = get_user_model().objects.create_user(**test_data)

        self.assertEqual(user.email, test_data['email'])
        self.assertTrue(user.check_password(test_data['password']))
