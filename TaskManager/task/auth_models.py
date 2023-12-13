from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    date_of_birth = models.DateField(null=True, blank=True)