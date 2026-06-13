import math

MAX_RANGE_MILES = 500
MPG = 10


class FuelOptimizer:

    @staticmethod
    def calculate_trip_requirements(route_distance):

        fuel_required = route_distance / MPG

        segments = math.ceil(
            route_distance / MAX_RANGE_MILES
        )

        fuel_stops_needed = max(
            0,
            segments - 1
        )

        return {
            "route_distance": round(route_distance, 2),
            "fuel_required_gallons": round(
                fuel_required,
                2
            ),
            "segments": segments,
            "fuel_stops_needed": fuel_stops_needed,
        }

    @staticmethod
    def optimize(route_distance, stations):

        stations = list(stations)

        trip = FuelOptimizer.calculate_trip_requirements(
            route_distance
        )

        if trip["fuel_stops_needed"] == 0:
            return {
                "stops": [],
                "message": "No fuel stop needed"
            }

        stations_sorted = sorted(
            stations,
            key=lambda x: x.retail_price
        )

        selected = stations_sorted[
            :trip["fuel_stops_needed"]
        ]

        return {
            "route_distance": trip["route_distance"],
            "fuel_required_gallons": trip[
                "fuel_required_gallons"
            ],
            "fuel_stops_needed": trip[
                "fuel_stops_needed"
            ],
            "fuel_stops": [
                {
                    "name": station.name,
                    "city": station.city,
                    "state": station.state,
                    "price": station.retail_price,
                }
                for station in selected
            ]
        }