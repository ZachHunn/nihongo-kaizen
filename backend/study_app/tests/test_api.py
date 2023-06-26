from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class StudyAppApiTestCase(APITestCase):
    def setup(self):
        self.client = Client()

    def test_get_endpoint(self):
        url = reverse('api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'OK'} )