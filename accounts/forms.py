from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    USERNAME_FIELD = "email"
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    # def clean_email(self):
    #     user_email = self.cleaned_data["email"]
    #     users = list(User.objects.raw(f"SELECT * FROM auth_user where email='{user_email}';"))

    #     if users != []:
    #         raise ValidationError("User with that email already exists.")