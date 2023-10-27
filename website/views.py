from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Meal, Booking
from .forms import MakeBooking
from django.views import generic
from django.http import JsonResponse


def check_availability(request):
    date = request.GET.get('date')
    time = request.GET.get('time')
    bookings_on_date = Booking.objects.filter(date=date, time=time)

    if bookings_on_date.exists():
        return JsonResponse({'available': False})
    return JsonResponse({'available': True})


def index(request):
    return render(request, 'index.html')


@login_required
def make_booking(request):

    booking_cancelled = False
    booking_success = False

    if request.method == 'POST':
        form = MakeBooking(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            existing_bookings = Booking.objects.filter(date=date, time=time)

            if not existing_bookings.exists():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.email = request.user.email
                booking.name = request.user.username
                booking.save()
                booking_success = True
            else:
                form.add_error(
                    None, "A booking with this date and time already exists.")
    else:
        form = MakeBooking()

    user_bookings = Booking.objects.filter(user=request.user)

    context = {
        'form': form,
        'booking_cancelled': booking_cancelled,
        'booking_success': booking_success,
        'user_bookings': user_bookings
    }

    return render(request, 'booking.html', context)


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = MakeBooking(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking')

    else:
        form = MakeBooking(instance=booking)

    return render(request, 'booking.html', {'form': form})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST":
        booking.delete()
        return redirect('booking')

    return render(request, 'booking.html', {'booking_cancelled': True})


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('price')
    template_name = 'menu.html'
