from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.utils import timezone


class NameSerialisationTest(APITestCase):
  def test_full_name(self):
    time_format_out = "%Y-%m-%d %H:%M"
    client = APIClient()
    url = reverse('serial.full_name')
    data = {
      "first_name": "Sam", 
      "last_name":"McSammy",
      "start_date": timezone.now().strftime(time_format_out),
      "end_date": timezone.now().strftime(time_format_out)
    }
    response = client.post(url, data=data)
    print(response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
