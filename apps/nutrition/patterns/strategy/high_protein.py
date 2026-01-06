from .base import RecommendationStrategy

class HighProteinStrategy(RecommendationStrategy):
    def recommend(self, user, foods):
        return sorted(foods, key=lambda f: f.protein, reverse=True)[:3]
