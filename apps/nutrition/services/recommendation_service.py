from ..repositories.food_repository import FoodRepository


class RecommendationService:
    def __init__(self, strategy):
        self.strategy = strategy
        self.food_repo = FoodRepository()

    def recommend_food(self, user):
        foods = self.food_repo.get_all()
        return self.strategy.recommend(user, foods)