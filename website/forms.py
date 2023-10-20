from .models import Booking
from django import forms


class MakeBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'number_of_guests']
