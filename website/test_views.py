from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking, Meal
from datetime import datetime

# Test class to test Index view


class IndexViewTest(TestCase):

    def test_index_view(self):
        # Test that the index view returns a status code of 200
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

# Test class to test Make booking view


class MakeBookingViewTest(TestCase):

    def setUp(self):
        # Set up a test client, URL, and user for making bookings
        self.client = Client()
        self.make_booking_url = reverse('booking')
        self.user = User.objects.create_user(
            'john', 'john@something.com', 'password')
        self.client.login(username='john', password='password')

    def test_make_booking(self):
        # Test making a booking and checking if it's created in the database
        response = self.client.post(self.make_booking_url, {
            'date': '2023-10-26',
            'time': '14:00',
            'party_of': 3
        })
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Booking.objects.filter(
            date="2023-10-26", time="14:00").exists())

    def test_make_booking_existing_time(self):
        # Test making a booking with an existing date and time
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

# Test class to test Edit booking view


class EditBookingViewTest(TestCase):
    def setUp(self):
        # Set up a test user and booking for editing
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.booking = Booking.objects.create(
            date="2023-10-25", time="14:00", user=self.user, party_of=2)
        self.client.login(username='testuser', password='testpassword')

    def test_edit_booking(self):
        # Test editing a booking and checking if it's redirected to the booking page
        response = self.client.post(reverse('edit_booking', args=[self.booking.id]), data={
            'date': '2023-10-26',
            'time': '15:00',
            'party_of': '4',
        })

        self.assertRedirects(response, reverse('booking'))

# Test class to test Cancel booking view


class CancelBookingViewTest(TestCase):

    def setUp(self):
        # Set up a test client, user, and booking for canceling
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'john@example.com', 'johnpassword')
        self.booking = Booking.objects.create(
            date="2023-10-25", time="14:00", user=self.user, party_of=2)
        self.client.login(username='john', password='johnpassword')

    def test_cancel_booking(self):
        # Test canceling a booking and checking if it's removed from the database
        response = self.client.post(
            reverse('cancel_booking', args=[self.booking.id]))
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())

# Test class to test Meal list view


class MealListViewTest(TestCase):

    def setUp(self):
        # Create test meals for listing
        Meal.objects.create(title='Meal A', price=20.00)
        Meal.objects.create(title='Meal B', price=10.00)

    def test_meals_ordered_by_price(self):
        # Test that meals are ordered by price in the meal list view
        response = self.client.get(reverse('menu'))
        meals = list(response.context['meal_list'])
        self.assertEquals(meals[0].title, 'Meal B')
        self.assertEquals(meals[1].title, 'Meal A')
        
