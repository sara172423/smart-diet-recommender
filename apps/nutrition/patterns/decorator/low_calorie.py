from .decorator import FoodDecorator

class LowCalorieDecorator(FoodDecorator):

    def get_calories(self):
        return self.food_component.get_calories() * 0.8

    def get_description(self):
        return self.food_component.get_description() + " (Low Calorie)"
