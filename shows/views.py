from django.shortcuts import render


def upcoming_shows(request):
    return render(request, "shows/upcoming-shows.html")

def booked_shows(request):
    return render(request, "shows/booked-shows.html")