from route_service.services.route_provider import RouteProvider
from route_service.services.route_parser import RouteParser

from fuel_service.services.station_locator import StationLocator

from optimizer_service.services.route_station_matcher import (
    RouteStationMatcher
)

from optimizer_service.services.route_progress import (
    RouteProgress
)

from optimizer_service.services.fuel_optimizer import (
    FuelOptimizer
)

from optimizer_service.services.fuel_stop_selector import (
    FuelStopSelector
)

from cost_service.services.cost_calculator import (
    CostCalculator
)


class TripOptimizer:

    @staticmethod
    def optimize(
        start_lon,
        start_lat,
        end_lon,
        end_lat
    ):

        # Step 1: Get route
        route = RouteProvider.get_route(
            start_lon=start_lon,
            start_lat=start_lat,
            end_lon=end_lon,
            end_lat=end_lat
        )

        # Step 2: Route coordinates
        coords = RouteParser.get_route_coordinates(
            route
        )

        # Step 3: Route distance
        distance = (
            RouteParser.get_route_distance_miles(
                route
            )
        )

        # Step 4: Stations in route bounding box
        candidate_stations = (
            StationLocator.get_stations_in_bbox(
                route["bbox"]
            )
        )

        # Step 5: Stations near route
        nearby_stations = (
            RouteStationMatcher.filter_near_route_stations(
                candidate_stations,
                coords
            )
        )

        # Step 6: Order stations along route
        progress = (
            RouteProgress.get_station_progress(
                coords,
                nearby_stations
            )
        )

        # Step 7: Fuel calculations
        trip = (
            FuelOptimizer.calculate_trip_requirements(
                distance
            )
        )

        # Step 8: Select best fuel stops
        selected_stops = (
            FuelStopSelector.select_stops(
                progress,
                trip["fuel_stops_needed"]
            )
        )

        # Step 9: Estimate fuel cost
        estimated_cost = (
            CostCalculator.estimate_fuel_cost(
                trip["fuel_required_gallons"],
                selected_stops
            )
        )

        # Step 10: Final response
        return {
            "distance_miles": trip[
                "route_distance"
            ],
            "fuel_needed": trip[
                "fuel_required_gallons"
            ],
            "fuel_stops_needed": trip[
                "fuel_stops_needed"
            ],
            "estimated_fuel_cost": estimated_cost,
            "recommended_stops": [
                {
                    "name": item[
                        "station"
                    ].name,
                    "city": item[
                        "station"
                    ].city.strip(),
                    "state": item[
                        "station"
                    ].state.strip(),
                    "price": item[
                        "station"
                    ].retail_price,
                }
                for item in selected_stops
            ]
        }