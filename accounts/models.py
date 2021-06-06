from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """Defines custom user preferences."""
    age = models.PositiveIntegerField(null=True, blank=True)