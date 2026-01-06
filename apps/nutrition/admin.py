from django.contrib import admin
from .models.food import Food
from .models.user import User
from .models.reservation import Reservation

admin.site.register(Food)
admin.site.register(User)
admin.site.register(Reservation)
