from .base import FoodComponent

class BaseFood(FoodComponent):
    def __init__(self, food):
        self.food = food

    def get_calories(self):
        return self.food.calories

    def get_description(self):
        return self.food.name
