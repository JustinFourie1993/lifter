from .models import Booking
from django import forms

# Create a form class named MakeBooking based on the Booking model


class MakeBooking(forms.ModelForm):
    class Meta:
        # Base form off of booking model
        model = Booking

        # Name the fields from the Booking model that should be included in the form
        fields = ['date', 'time', 'party_of']

        # Add custom widgets for each form field
        widgets = {
            # Use a date input type in the HTML form
            'date': forms.DateInput(attrs={'type': 'date'}),
            # Use a time input type in the HTML form
            'time': forms.TimeInput(attrs={'type': 'time'}),
            # Use a number input type in the HTML form with a minimum value of 1
            'party_of': forms.NumberInput(attrs={'type': 'number', 'min': '1'})
        }
