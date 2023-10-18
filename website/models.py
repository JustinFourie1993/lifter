from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


FOOD_TYPE = (("fish", "fish"), ("meat", "meat"), ("vegan", "vegan"))
MEAL_TYPE = (("starter", "starter"), ("main", "main"),
             ("dessert", "dessert"), ("drink", "drink"))


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    booked_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['booked_on']


class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    price = models.IntegerField()
    food_type = models.CharField(max_length=100, choices=FOOD_TYPE)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.title
