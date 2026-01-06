from .base import RecommendationStrategy

class EconomicStrategy(RecommendationStrategy):
    def recommend(self, user, foods):
        return sorted(foods, key=lambda f: f.price)[:3]
