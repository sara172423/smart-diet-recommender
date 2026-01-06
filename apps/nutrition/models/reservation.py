from django.db import models
from .user import User
from .food import Food

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
