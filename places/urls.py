from django.urls import path
from . import views

urlpatterns = [
    path("<int:place_id>/", views.place_details, name="place_details"),
]
