from .observer import Observer

class DietChangeObserver(Observer):

    def update(self, data):
        print(f"Diet changed for user {data['user_id']}")
