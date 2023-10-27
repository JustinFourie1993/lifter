from django.test import TestCase
from .forms import MakeBooking


class MakeBookingFormTest(TestCase):

    def test_make_booking_form_is_valid(self):
        form = MakeBooking(data={
            'date': '2022-10-25',
            'time': '14:00',
            'party_of': 4
        })
        self.assertTrue(form.is_valid())

    def test_make_booking_form_no_data(self):
        form = MakeBooking(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
