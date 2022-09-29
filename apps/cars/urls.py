from django.urls import path
from . import views

urlpatterns = [
    path("cars/create/", views.CarCreateView.as_view()),
    path("cars/", views.CarsListView.as_view()),
    path("cars/<int:pk>/", views.CarView.as_view()),
]