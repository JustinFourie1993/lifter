from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.urls import reverse
from .models import Meal, Booking
from .forms import MakeBooking


# Displays home page
def index(request):
    return render(request, 'index.html')


# Displays booking page and post data from booking form
def make_booking(request):

    if request.method == 'POST':
        form = MakeBooking(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.email = request.user.email
            booking.name = request.user.username
            booking.save()
            # Redirect to a success page or the same page with a success message
            return redirect('booking_success')

    else:
        form = MakeBooking()

    return render(request, 'booking.html', {'form': form})


# Displays meal objects on menu page
class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('price')
    template_name = 'menu.html'