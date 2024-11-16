from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import CreateUserForm


def sign_in(request):
    return render(request, "accounts/sign-in.html")

def sign_up(request):
    form = CreateUserForm()

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        form = CreateUserForm(data=request.POST)

        if password != confirm_password:
            form.add_error("password", "Passwords do not match.")
        
        if form.is_valid():
            user = User.objects.create_user(username=email, password=password, email=email)
            user.save()
            return redirect("/acc/sign-in")

    context = {"form": form}

    return render(request, "accounts/sign-up.html", context)