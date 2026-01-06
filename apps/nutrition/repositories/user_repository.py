from ..models import SimpleUser

class UserRepository:

    @staticmethod
    def get_by_id(user_id):
        return SimpleUser.objects.get(id=user_id)

    @staticmethod
    def create(**kwargs):
        return SimpleUser.objects.create(**kwargs)
