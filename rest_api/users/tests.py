from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, 
from users.models import User

class ClientTests(APITestCase):
    def test_create_user(self):
        url = reverse('users/create')
        data = {'name': 'ExampleUser', 'email': "example@mail.com", 'password':'123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'ExampleUser')

    def test_login_user(self):
        url = reverse('users/loging')
        data = {'name': 'ExampleUser', 'password':'123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_duplicate_emmail(self):

        url = reverse('users/create')
        data = {'name': 'ExampleUser', 'email': "example@mail.com", 'password':'123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertNotEqual(User.objects.count(), 1)



