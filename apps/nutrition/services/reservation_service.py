from ..models.reservation import Reservation
from ..patterns.observer.subject import Subject


class ReservationService(Subject):
    def __init__(self):
        super().__init__()

    def reserve_food(self, user, food):
        reservation = Reservation.objects.create(
            user=user,
            food=food
        )

        # Observer Pattern
        self.notify_observers(
            event="food_reserved",
            user=user,
            food=food
        )

        return reservation
