from django.urls import path
from .views.user_views import create_user_view
from .views.food_views import recommend_food_view
from .views.reservation_views import reserve_food_view

urlpatterns = [
    path('user/create/', create_user_view),
    path('recommend/<int:user_id>/', recommend_food_view),
    path('reserve/<int:food_id>/<int:user_id>/', reserve_food_view, name='reserve_food'),
]
