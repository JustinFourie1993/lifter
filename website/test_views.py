from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking, Meal
from datetime import datetime


class IndexViewTest(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)


class MakeBookingViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.make_booking_url = reverse('booking')
        self.user = User.objects.create_user(
            'john', 'john@something.com', 'password')
        self.client.login(username='john', password='password')

    def test_make_booking(self):
        response = self.client.post(self.make_booking_url, {
            'date': '2023-10-26',
            'time': '14:00',
            'party_of': 3
        })
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Booking.objects.filter(
            date="2023-10-26", time="14:00").exists())

    def test_make_booking_existing_time(self):
        Booking.objects.create(
            date="2023-10-25", time="14:00", user=self.user, party_of=2)
        response = self.client.post(self.make_booking_url, {
            'date': '2023-10-25',
            'time': '14:00',
            'party_of': 4
        })
        self.assertEquals(response.status_code, 200)
        self.assertTrue(
            'A booking with this date and time already exists.' in response.content.decode())
