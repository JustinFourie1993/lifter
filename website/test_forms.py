from django.test import TestCase
from .forms import MakeBooking


class MakeBookingFormTest(TestCase):

    def test_make_booking_form_is_valid_(self):
        form = MakeBooking(data={
            'date': '2022-10-25',
            'time': '14:00',
            'party_of': 4
        })
        self.assertTrue(form.is_valid())
