from django.urls import path

from . import views


urlpatterns = [
    path("upcoming", views.upcoming_shows, name="upcoming_shows"),
    path("booked", views.booked_shows, name="booked_shows"),
    path("new-show", views.new_show, name="new_show"),
]
