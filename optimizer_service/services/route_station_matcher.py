import math


class RouteStationMatcher:

    EARTH_RADIUS_MILES = 3958.8

    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):

        # convert degrees → radians
        lat1, lon1, lat2, lon2 = map(
            math.radians,
            [lat1, lon1, lat2, lon2]
        )

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1)
            * math.cos(lat2)
            * math.sin(dlon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return RouteStationMatcher.EARTH_RADIUS_MILES * c

    @staticmethod
    def is_station_near_route(
        station_lat,
        station_lon,
        route_coords,
        max_distance_miles=5
    ):
        """
        Checks if station is within X miles of ANY route point
        """

        for lon, lat in route_coords:

            distance = RouteStationMatcher.haversine_distance(
                lat,
                lon,
                station_lat,
                station_lon
            )

            if distance <= max_distance_miles:
                return True

        return False

    @staticmethod
    def filter_near_route_stations(
        stations,
        route_coords,
        max_distance_miles=5
    ):

        nearby = []

        for station in stations:

            if RouteStationMatcher.is_station_near_route(
                station.latitude,
                station.longitude,
                route_coords,
                max_distance_miles
            ):
                nearby.append(station)

        return nearby