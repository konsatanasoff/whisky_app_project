from django.urls import path, include

from drink_api import views

urlpatterns = [
    path('', views.DrinkListCreate.as_view())
]
