from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Nests Meta class to override the default fields."""
    class Meta(UserCreationForm):
        """Adds an age field to the default fields."""
        model = CustomUser
        fields = ('username', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):
    """Nests Meta clas to override the default fields."""
    class Meta(UserChangeForm):
        """Allows to modify default user fields."""
        model = CustomUser
        fields = ('username', 'email', 'age',)