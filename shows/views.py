from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/acc/sign-in")
def upcoming_shows(request):
    return render(request, "shows/upcoming-shows.html")

@login_required(login_url="/acc/sign-in")
def booked_shows(request):
    return render(request, "shows/booked-shows.html")