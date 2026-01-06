from .base import RecommendationStrategy
from ...repositories.food_repository import FoodRepository

class EconomicStrategy(RecommendationStrategy):

    def recommend(self, user):
        return FoodRepository.get_economic_foods()
