from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services.reservation_service import ReservationService


class ReservationAPIView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        food_id = request.data.get("food_id")

        service = ReservationService()
        reservation = service.reserve_food(user_id, food_id)

        return Response(
            {
                "reservation_id": reservation.id,
                "status": "reserved"
            },
            status=status.HTTP_201_CREATED
        )
