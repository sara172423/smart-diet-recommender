from django.contrib import admin
from .models.food import Food
from .models.user import SimpleUser
from .models.reservation import FoodReservation

admin.site.register(Food)
admin.site.register(SimpleUser)
admin.site.register(FoodReservation)
