from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Meal, Booking
from .forms import MakeBooking


# Displays home page
def index(request):
    return render(request, 'index.html')


# Displays booking page and post data from booking form
def make_booking(request):

    if request.method == 'POST':
        make_booking = MakeBooking(request.POST)

        if make_booking.is_valid():
            make_booking.instance.email = request.user.email
            make_booking.instance.name = request.user.username
            make_booking.save()
            context = {'form': make_booking, 'booked': True}
            return render(request, 'booking.html', context)

    make_booking = MakeBooking()
    context = {'form': make_booking, 'booked': False, }
    return render(request, 'booking.html', context)


# Displays meal objects on menu page
class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('price')
    template_name = 'menu.html'