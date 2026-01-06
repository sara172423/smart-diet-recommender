from ..repositories.food_repository import FoodRepository
from ..patterns.decorator.food_base import BaseFood
from ..patterns.decorator.low_calorie import LowCalorieDecorator
from ..patterns.decorator.discount import DiscountDecorator
from .ai_model_singleton import AIModelSingleton



class RecommendationService:
    def __init__(self, strategy):
        self.strategy = strategy
        self.food_repository = FoodRepository()
        self.ai_engine = AIModelSingleton()

    def recommend_food(self, user):
        foods = self.food_repository.get_all_foods()

        # Strategy Pattern
        recommended_foods = self.strategy.recommend(user, foods)

        decorated_results = []

        for food in recommended_foods:
            food_component = BaseFood(food)

            # Decorator Pattern (بر اساس شرایط کاربر)
            if user.is_on_diet:
                food_component = LowCalorieDecorator(food_component)

            if user.is_student:
                food_component = DiscountDecorator(food_component)

            decorated_results.append(food_component)

        return decorated_results

    def feedback(self, accepted: bool):
        """
        Adaptive learning based on user behavior
        """
        strategy_name = self.strategy.__class__.__name__.lower()

        if accepted:
            self.ai_engine.reward(strategy_name)
        else:
            self.ai_engine.penalize(strategy_name)
