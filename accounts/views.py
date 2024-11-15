from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm


def sign_in(request):
    return render(request, "accounts/sign-in.html")

def sign_up(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            # print(form)
            return redirect("/acc/sign-in")

    context = {"form": form}

    return render(request, "accounts/sign-up.html", context)