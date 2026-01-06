from django.db import models
from .user import SimpleUser
from .food import Food

class FoodReservation(models.Model):
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
