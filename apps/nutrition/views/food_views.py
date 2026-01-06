# nutrition/views/food_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.recommendation_service import RecommendationService
from ..patterns.strategy.low_calorie import LowCalorieStrategy
from ..patterns.strategy.economic import EconomicStrategy
from ..patterns.strategy.high_protein import HighProteinStrategy
from ..repositories.user_repository import UserRepository
class RecommendFoodAPIView(APIView):
    def get(self, request, user_id):
        user = UserRepository.get_by_id(user_id)

        strategy_type = request.query_params.get("type", "low_calorie")

        if strategy_type == "high_protein":
            strategy = HighProteinStrategy()
        elif strategy_type == "economic":
            strategy = EconomicStrategy()
        else:
            strategy = LowCalorieStrategy()

        service = RecommendationService(strategy)
        foods = service.recommend_food(user)

        data = [
            {
                "id": food.id,
                "name": food.name,
                "calories": food.calories,
                "price": food.price,
            }
            for food in foods
        ]

        return Response(data, status=status.HTTP_200_OK)