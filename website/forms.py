from .models import Booking
from django import forms

# form created from booking model

class MakeBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date','time','party_of']