from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

from .forms import SignupForm, SigninForm
from .models import Wallet
from .decorators import unauthenticated_user


@unauthenticated_user
def sign_in(request):
    form = SigninForm()

    credentials_are_valid = True
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return redirect("/")

        else:
            credentials_are_valid = False

    context = {"form": form, "credentials_are_valid": credentials_are_valid}
    return render(request, "accounts/sign-in.html", context)

@unauthenticated_user
def sign_up(request):
    form = SignupForm()

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        form = SignupForm(data=request.POST)

        if password != confirm_password:
            form.add_error("password", "Passwords do not match.")
        
        if form.is_valid():
            user = User.objects.create_user(username=email, password=password, email=email)
            user.save()
            user_wallet = Wallet(user=user, balance=0)
            user_wallet.save()
            return redirect("/acc/sign-in")

    context = {"form": form}

    return render(request, "accounts/sign-up.html", context)

def sign_out(request):
    logout(request)
    return redirect("/")