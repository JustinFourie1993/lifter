from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

# Define choices for food types (used in Meal model)
FOOD_TYPE = (("fish", "fish"), ("meat", "meat"), ("vegan", "vegan"))

# Define choices for meal types (used in Meal model)
MEAL_TYPE = (("starter", "starter"), ("main", "main"),
             ("dessert", "dessert"), ("drink", "drink"))

# Booking model


class Booking(models.Model):
    # Define a foreign key relationship with the User model
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    # Define a field to store the name of the booking
    name = models.CharField(max_length=100, null=False, blank=False)

    # Define a field to store the email of the booking
    email = models.EmailField(max_length=200, null=False, blank=False)

    # Define a field to store the date of the booking
    date = models.DateField(null=False, blank=False, db_index=True)

    # Define a field to store the time of the booking
    time = models.TimeField(null=False, blank=False)

    # Define a field to store the party size of the booking, with a validator to ensure it's at least 1
    party_of = models.IntegerField(null=False, blank=False, validators=[
                                   MinValueValidator(1)])

    # Define a field to store the date and time when the booking was made
    booked_on = models.DateTimeField(auto_now_add=True)

    # Define a boolean field to indicate whether the booking is approved 
    approved = models.BooleanField(default=False)

    class Meta:
        # Set ordering of bookings to booked_on
        ordering = ['booked_on']

    def __str__(self):
        # Returns the name of the booker
        return self.name

# Meal model


class Meal(models.Model):
    # Define a field to store the title of the meal
    title = models.CharField(max_length=100)

    # Define a field to store the description of the meal
    description = models.TextField()

    # Define a field to store an excerpt of the meal (optional)
    excerpt = models.TextField(blank=True)

    # Define a field to store the price of the meal as a decimal
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Define a field to store the food type of the meal
    food_type = models.CharField(
        max_length=100, choices=FOOD_TYPE, db_index=True)

    # Define a field to store the meal type of the meal
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE)

    class Meta:
        # Set the ordering of meal objects to price
        ordering = ['price']

    def __str__(self):
        # Returns the meal title
        return self.title
