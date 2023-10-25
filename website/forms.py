from .models import Booking
from django import forms

# form created from booking model


class MakeBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'party_of']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'party_of': forms.NumberInput(attrs={'type': 'number', 'min': '1'})
        }
