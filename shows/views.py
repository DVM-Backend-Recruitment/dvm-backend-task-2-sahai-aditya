from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import datetime
import pytz

from .models import Movie, Show, TheatreAdmin, Theatre
from .forms import NewShowForm


@login_required(login_url="/acc/sign-in")
def upcoming_shows(request):
    return render(request, "shows/upcoming-shows.html")

@login_required(login_url="/acc/sign-in")
def booked_shows(request):
    return render(request, "shows/booked-shows.html")

@login_required(login_url="/acc/sign-in")
def new_show(request):
    form = NewShowForm()

    if request.method == "POST":
        form = NewShowForm(data=request.POST)
        movie = request.POST.get("movie")

        if form.is_valid():
            start_time = datetime.strptime(request.POST.get("start_time"), "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(request.POST.get("end_time"), "%Y-%m-%d %H:%M")

            if start_time > end_time:
                form.add_error("start_time", "Start time cannot be after end time.")
                form.add_error("end_time", "Start time cannot be after end time.")

                context = {"form": form}
                return render(request, "shows/new-show.html", context)

            movie = Movie.objects.get(pk=int(movie))
            theatre_id = list(TheatreAdmin.objects.raw(f"SELECT * FROM shows_theatreadmin where user_id={request.user.id}"))[0].theatre_id
            theatre = Theatre.objects.get(pk=theatre_id)

            show = Show(movie=movie, theatre=theatre, start_time=start_time, end_time=end_time, vacant_seats=theatre.total_seats)
            show.save()

            return redirect("/")

    context = {"form": form}
    return render(request, "shows/new-show.html", context)