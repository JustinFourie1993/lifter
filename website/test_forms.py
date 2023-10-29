from django.test import TestCase
from .forms import MakeBooking

# Create a test class for the MakeBooking form


class MakeBookingFormTest(TestCase):

    # Test when the form is valid
    def test_make_booking_form_is_valid(self):
        form = MakeBooking(data={
            'date': '2022-10-25',
            'time': '14:00',
            'party_of': 4
        })
        self.assertTrue(form.is_valid())  # Check that the form is valid

    # Test when the form has no data (empty form)
    def test_make_booking_form_no_data(self):
        form = MakeBooking(data={})  # Create an empty form
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        # Check that it has three errors
        self.assertEquals(len(form.errors), 3)

    # Test when the form has invalid 'party_of' data (party size is 0)
    def test_make_booking_form_invalid_party_of_data(self):
        form = MakeBooking(data={
            'date': '2022-10-25',
            'time': '14:00',
            'party_of': 0  
        })
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        # Check that 'party_of' is in the list of errors
        self.assertIn('party_of', form.errors)
