from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# Custom Creation and Change forms because of the custom user model.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)
    password = None

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'bio')
