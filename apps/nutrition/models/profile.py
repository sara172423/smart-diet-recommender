from django.db import models
from .user import SimpleUser

class Profile(models.Model):
    user = models.OneToOneField(SimpleUser, on_delete=models.CASCADE)
    wants_low_calorie = models.BooleanField(default=False)
    wants_high_protein = models.BooleanField(default=False)

