from django.shortcuts import redirect
from ..models.reservation import FoodReservation
from ..models.food import Food
from ..models.user import SimpleUser


def reserve_food_view(request, user_id, food_id):
    user = SimpleUser.objects.get(id=user_id)
    food = Food.objects.get(id=food_id)

    FoodReservation.objects.create(
        user=user,
        food=food
    )

    return redirect(f'/recommend/{user_id}/')
