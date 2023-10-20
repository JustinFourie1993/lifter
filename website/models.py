from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# ordering variables for Meal model
FOOD_TYPE = (("fish", "fish"), ("meat", "meat"), ("vegan", "vegan"))
MEAL_TYPE = (("starter", "starter"), ("main", "main"),
             ("dessert", "dessert"), ("drink", "drink"))

# Booking model
class Booking(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    party_of = models.IntegerField(null=False, blank=False)
    booked_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['booked_on']

    def __str__(self):
        return self.name

# Meal Model
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
