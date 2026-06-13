# cost_service/services/cost_calculator.py

class CostCalculator:

    @staticmethod
    def estimate_fuel_cost(
        fuel_needed,
        selected_stops
    ):

        if not selected_stops:
            return 0

        average_price = (
            sum(
                item["station"].retail_price
                for item in selected_stops
            )
            /
            len(selected_stops)
        )

        return round(
            fuel_needed * average_price,
            2
        )