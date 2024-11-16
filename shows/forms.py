from django import forms
from django.core.exceptions import ValidationError

from .models import Show


class NewShowForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=forms.TextInput(attrs={"placeholder": "YYYY-MM-DD HH:MM (24hr clock)"}))
    end_time = forms.DateTimeField(widget=forms.TextInput(attrs={"placeholder": "YYYY-MM-DD HH:MM (24hr clock)"}))
    class Meta:
        model = Show
        fields = ("movie", "start_time", "end_time")

        