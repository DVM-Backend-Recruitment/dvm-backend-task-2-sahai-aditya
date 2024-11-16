from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django import forms


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ("email", "password", "confirm_password")

    def clean_email(self):
        user_email = self.cleaned_data["email"]
        users = list(User.objects.raw(f"SELECT * FROM auth_user where email='{user_email}';"))

        if users != []:
            raise ValidationError("User with that email already exists.")