from .base import RecommendationStrategy
from ...repositories.food_repository import FoodRepository

class LowCalorieStrategy(RecommendationStrategy):

    def recommend(self, user):
        return FoodRepository.get_low_calorie_foods()
