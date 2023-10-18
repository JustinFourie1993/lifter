from django.shortcuts import render
from django.views import generic
from .models import Meal


class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.order_by('price')
    template_name = 'menu.html'


def index(request):
    return render(request, 'index.html')