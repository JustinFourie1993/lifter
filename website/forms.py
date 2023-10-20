from .models import Booking
from django import forms


class MakeBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'date', 'time', 'party_of']
        
