from django.urls import path
from .views.food_views import RecommendFoodAPIView
from .views.reservation_views import ReservationAPIView
urlpatterns = [
    path("recommend/<int:user_id>/", RecommendFoodAPIView.as_view()),
    path("reserve/", ReservationAPIView.as_view()),
]
