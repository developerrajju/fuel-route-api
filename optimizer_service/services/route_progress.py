from optimizer_service.services.route_station_matcher import (
    RouteStationMatcher
)


class RouteProgress:

    @staticmethod
    def get_station_progress(
        route_coordinates,
        stations
    ):

        results = []

        sampled_route = route_coordinates[::25]

        for station in stations:

            closest_index = None
            closest_distance = float("inf")

            for idx, point in enumerate(sampled_route):

                lon, lat = point

                distance = (
                    RouteStationMatcher
                    .haversine_distance(
                        lat,
                        lon,
                        station.latitude,
                        station.longitude
                    )
                )

                if distance < closest_distance:
                    closest_distance = distance
                    closest_index = idx

            results.append({
                "station": station,
                "route_index": closest_index
            })

        return sorted(
            results,
            key=lambda x: x["route_index"]
        )