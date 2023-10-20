from . import views
from django.urls import path


urlpatterns = [
    # path('', views.MealList.as_view(), name='menu'),
    # path('', views.index, name='index'),
    path('', views.make_booking, name='booking'),
]