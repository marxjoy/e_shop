from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.urls import resolve, reverse


class TestAccount(TestCase):
    sample_user = {'username': 'Jan123',
                  'password': 'baba1234',
                  'first_name': 'John',
                  'last_name': 'Smith',
                  'email': 'john@smith.org',
                       }
    
    def setUp(self):
        User.objects.create(username=self.sample_user['username'],
                            password=self.sample_user['password'])
        user = User.objects.get(username=self.sample_user['username'])
        user.first_name = self.sample_user['first_name']
        user.last_name = self.sample_user['last_name']
        user.email = self.sample_user['email']
        user.save()
        self.client = Client()

    def tearDown(self):
        pass

    def test_sample_user_exist(self):
        user = User.objects.get(username=self.sample_user['username'])
        self.assertEqual(user.username, self.sample_user['username'])
        self.assertEqual(user.last_name, self.sample_user['last_name'])
        self.assertEqual(user.first_name, self.sample_user['first_name'])


