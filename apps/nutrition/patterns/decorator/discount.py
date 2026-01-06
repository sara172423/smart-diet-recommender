from .decorator import FoodDecorator

class DiscountDecorator(FoodDecorator):

    def get_description(self):
        return self.food_component.get_description() + " (Discount)"
