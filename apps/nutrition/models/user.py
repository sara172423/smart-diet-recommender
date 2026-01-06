
from django.db import models

class SimpleUser(models.Model):
    STRATEGY_CHOICES = [
        ('low_calorie', 'کم‌کالری'),
        ('high_protein', 'پروتئینی'),
        ('economic', 'اقتصادی'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.CharField(max_length=20, unique=True)

    strategy_type = models.CharField(
        max_length=20,
        choices=STRATEGY_CHOICES,
        default='low_calorie'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
