from django.contrib import admin
from .models import Meal, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    list_filter = ('price', 'food_type', 'meal_type')
    search_fields = ['title', 'price', 'food_type', 'meal_type']
    list_display = ('title', 'meal_type', 'price', 'food_type')
    


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'date', 'time', 'party_of', 'approved')
    list_filter = ('date', 'time', 'party_of', 'approved')
    search_fields = ('name', 'email', 'date', 'time')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)