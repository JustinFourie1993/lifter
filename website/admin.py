from django.contrib import admin
from .models import Meal, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register the Meal model in the Django admin site


@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):
    # Enable Summernote for the 'description' field
    summernote_fields = ('description',)

    # Filter options on the admin list page
    list_filter = ('price', 'food_type', 'meal_type')

    # Add search functionality for these fields
    search_fields = ['title', 'price', 'food_type', 'meal_type']

    # Display these fields in the admin list view
    list_display = ('title', 'meal_type', 'price', 'food_type')


# Register the Booking model in the Django admin site

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    # Display these fields in the admin list view
    list_display = ('name', 'date', 'time', 'party_of', 'approved')

    # Filter options on the admin list page
    list_filter = ('date', 'time', 'party_of', 'approved')

    # Add search functionality for these fields
    search_fields = ('name', 'email', 'date', 'time')

    # Define custom admin actions
    actions = ['approve_bookings']

    # Custom admin action to approve bookings
    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
