from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
