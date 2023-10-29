from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Meal, Booking
from .forms import MakeBooking
from django.views import generic
from django.http import JsonResponse

# Check the availability of a date and time for booking


def check_availability(request):
    # Get the date and time from the GET request
    date = request.GET.get('date')
    time = request.GET.get('time')

    # Query the database for bookings on the given date and time
    bookings_on_date = Booking.objects.filter(date=date, time=time)

    # Return a JSON response indicating whether the date and time are available
    if bookings_on_date.exists():
        return JsonResponse({'available': False})
    return JsonResponse({'available': True})

# Render the index page


def index(request):
    return render(request, 'index.html')


@login_required
def make_booking(request):
    # Initialize flags for booking status
    booking_cancelled = False
    booking_success = False

    if request.method == 'POST':
        # Handle form submission
        form = MakeBooking(request.POST)
        if form.is_valid():
            # If the form is valid, extract data
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Check if a booking already exists for the selected date and time
            existing_bookings = Booking.objects.filter(date=date, time=time)

            if not existing_bookings.exists():
                # Create a new booking if no conflicts exist
                booking = form.save(commit=False)
                booking.user = request.user
                booking.email = request.user.email
                booking.name = request.user.username
                booking.save()
                booking_success = True
            else:
                # Report an error if a booking already exists
                form.add_error(
                    None, "A booking with this date and time already exists.")
    else:
        # Create a new booking form
        form = MakeBooking()

    # Retrieve the bookings of the logged-in user
    user_bookings = Booking.objects.filter(user=request.user)

    context = {
        'form': form,
        'booking_cancelled': booking_cancelled,
        'booking_success': booking_success,
        'user_bookings': user_bookings
    }

    # Render the booking.html template with the booking form and user's bookings
    return render(request, 'booking.html', context)


@login_required
def edit_booking(request, booking_id):
    # Get the booking to edit
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        # Handle form submission for editing
        form = MakeBooking(request.POST, instance=booking)
        if form.is_valid():
            # Save the edited booking
            form.save()
            return redirect('booking')
    else:
        # Create a form pre-populated with the booking's data
        form = MakeBooking(instance=booking)

    # Render the booking.html template with the booking edit form
    return render(request, 'booking.html', {'form': form})


@login_required
def cancel_booking(request, booking_id):
    # Get the booking to cancel
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST":
        # Delete the booking if the request method is POST
        booking.delete()
        return redirect('booking')

    # Render the booking.html template with a flag indicating the booking was canceled
    return render(request, 'booking.html', {'booking_cancelled': True})


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('price')
    template_name = 'menu.html'
