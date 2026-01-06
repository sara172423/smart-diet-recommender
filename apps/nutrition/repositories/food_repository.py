from ..models.food import Food

class FoodRepository:

    def get_all(self):
        return Food.objects.all()

    def get_by_id(self, food_id):
        return Food.objects.filter(id=food_id).first()

    def filter_by_type(self, food_type):
        return Food.objects.filter(type=food_type)

    def create(self, **data):
        return Food.objects.create(**data)
