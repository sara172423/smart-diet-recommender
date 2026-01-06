from ..models.user import User

class UserRepository:

    def get_by_id(self, user_id):
        return User.objects.filter(id=user_id).first()

    def create(self, **data):
        return User.objects.create(**data)
