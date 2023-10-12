from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


FOOD_TYPE = (("fish", "fish"), ("meat", "meat"), ("vegan", "vegan"))
MEAL_TYPE = (("starter", "starter"), ("main", "main"), ("dessert", "dessert"))


class Booking(models.Model):
    name = models.CharField(max_length=100)
    geeks_field = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    num_of_guests = models.IntegerField()
    booked_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['booked_on']
        

class Meals(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    food_type = models.CharField(max_length=100, choices=FOOD_TYPE)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE)

    class Meta:
        ordering = ['price']

