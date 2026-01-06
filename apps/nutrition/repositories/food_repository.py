from ..models.food import Food


class FoodRepository:
    def get_all(self):
        return Food.objects.all()
