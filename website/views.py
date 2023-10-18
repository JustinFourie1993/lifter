from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Meal


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('price')
    template_name = 'menu.html'


def index(request):
    return render(request, 'index.html')


# class Booking(View):

#     def get(self)