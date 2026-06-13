class RouteParser:

    @staticmethod
    def get_route_coordinates(route_data):

        return (
            route_data["features"][0]
            ["geometry"]
            ["coordinates"]
        )

    @staticmethod
    def get_route_distance_miles(route_data):

        meters = (
            route_data["features"][0]
            ["properties"]
            ["summary"]
            ["distance"]
        )

        return meters * 0.000621371