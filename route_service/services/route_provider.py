import requests
from django.conf import settings


class RouteProvider:

    @staticmethod
    def get_route(
        start_lon,
        start_lat,
        end_lon,
        end_lat
    ):

        url = (
            "https://api.openrouteservice.org/v2/"
            "directions/driving-car/geojson"
        )

        headers = {
            "Authorization": settings.ORS_API_KEY,
            "Content-Type": "application/json"
        }

        body = {
            "coordinates": [
                [start_lon, start_lat],
                [end_lon, end_lat]
            ]
        }

        response = requests.post(
            url,
            json=body,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()