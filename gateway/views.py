from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from fuel_service.services.geocoder import GeocoderService
from optimizer_service.services.trip_optimizer import TripOptimizer


class OptimizeRouteView(APIView):

    def post(self, request):

        try:

            start = request.data.get("start")
            destination = request.data.get("destination")

            if not start or not destination:
                return Response(
                    {
                        "error": "start and destination are required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            start_location = GeocoderService.geocode(
                start
            )

            destination_location = GeocoderService.geocode(
                destination
            )

            if not start_location:
                return Response(
                    {
                        "error": f"Could not geocode: {start}"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not destination_location:
                return Response(
                    {
                        "error": f"Could not geocode: {destination}"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            result = TripOptimizer.optimize(
                start_lon=start_location["longitude"],
                start_lat=start_location["latitude"],
                end_lon=destination_location["longitude"],
                end_lat=destination_location["latitude"]
            )

            return Response(result)

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )