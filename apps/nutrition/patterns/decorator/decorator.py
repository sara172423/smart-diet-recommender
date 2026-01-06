from .base import FoodComponent

class FoodDecorator(FoodComponent):
    def __init__(self, food_component: FoodComponent):
        self.food_component = food_component

    def get_calories(self):
        return self.food_component.get_calories()

    def get_description(self):
        return self.food_component.get_description()
