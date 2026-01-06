from .base import RecommendationStrategy

class LowCalorieStrategy(RecommendationStrategy):
    def recommend(self, user, foods):
        return sorted(foods, key=lambda f: f.calories)[:3]
