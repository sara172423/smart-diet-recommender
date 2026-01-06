from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=100)
    calories = models.IntegerField()
    category = models.CharField(max_length=50)
