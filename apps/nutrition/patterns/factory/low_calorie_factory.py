from .food_factory import FoodFactory
from ...models.food import Food

class LowCalorieFoodFactory(FoodFactory):
    def create_food(self, data):
        return Food(
            name=data["name"],
            calories=data["calories"],
            category="LOW_CALORIE"
        )
