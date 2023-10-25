from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

# Ordering variables for Meal model
FOOD_TYPE = (("fish", "fish"), ("meat", "meat"), ("vegan", "vegan"))
MEAL_TYPE = (("starter", "starter"), ("main", "main"),
             ("dessert", "dessert"), ("drink", "drink"))

# Booking model


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    date = models.DateField(null=False, blank=False, db_index=True)
    time = models.TimeField(null=False, blank=False)
    party_of = models.IntegerField(null=False, blank=False, validators=[
                                   MinValueValidator(1)])
    booked_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['booked_on']

    def __str__(self):
        return self.name

# Meal model


class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    food_type = models.CharField(
        max_length=100, choices=FOOD_TYPE, db_index=True)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.title
