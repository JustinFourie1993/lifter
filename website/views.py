from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Meal, Booking
from .forms import MakeBooking


# class MealList(generic.ListView):
#     model = Meal
#     queryset = Meal.objects.order_by('price')
#     template_name = 'menu.html'


# def index(request):
#     return render(request, 'index.html')


def make_booking(request):
    
    if request.method == 'POST':
        make_booking = MakeBooking(request.POST)

        if make_booking.is_valid():
            make_booking.save()
            
    make_booking = MakeBooking()        
    context = {'form': make_booking}

    return render(request, 'booking.html', context)