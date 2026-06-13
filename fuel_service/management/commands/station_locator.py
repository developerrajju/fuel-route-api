from fuel_service.models import FuelStation


class StationLocator:

    @staticmethod
    def get_stations_in_bbox(bbox):

        min_lon, min_lat, max_lon, max_lat = bbox

        stations = FuelStation.objects.filter(
            latitude__isnull=False,
            longitude__isnull=False,
            latitude__gte=min_lat,
            latitude__lte=max_lat,
            longitude__gte=min_lon,
            longitude__lte=max_lon,
        )

        return stations