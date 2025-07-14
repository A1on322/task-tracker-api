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

    def test_new_user_email_normalized(self):
        """Test email is normalized"""
        test_data = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in test_data:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email(self):
        """Test creating a new user with no email is raising error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'sample123')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'sample123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
