from .base import RecommendationStrategy
from ...repositories.food_repository import FoodRepository

class HighProteinStrategy(RecommendationStrategy):

    def recommend(self, user):
        return FoodRepository.get_high_protein_foods()
