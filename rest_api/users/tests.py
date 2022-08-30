from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import Users

class ClientTests(APITestCase):
    def test_create_user(self):
        url = reverse('users:sing_up')
        data = {'name': 'ExampleUser', 'email': "example@mail.com", 'password':'123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 1)
        self.assertEqual(Users.objects.get().name, 'ExampleUser')

    def test_duplicate_emmail(self):

        url = reverse('users:sing_up')
        data = {'name': 'ExampleUser', 'email': "example@mail.com", 'password':'123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Users.objects.count(), 1)
        self.assertNotEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_login_user(self):
        url = reverse('users/login')
        data = {'name': 'ExampleUser', 'password':'123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)




