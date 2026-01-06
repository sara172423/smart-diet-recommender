from ..models import FoodReservation

class ReservationService:

    def reserve(self, user, food):
        return FoodReservation.objects.create(user=user, food=food)
