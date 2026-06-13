MAX_RANGE_MILES = 500


class FuelStopSelector:

    @staticmethod
    def select_stops(
        ordered_stations,
        stops_needed
    ):

        if stops_needed <= 0:
            return []

        total_stations = len(
            ordered_stations
        )

        if total_stations == 0:
            return []

        selected = []

        step = max(
            1,
            total_stations // (
                stops_needed + 1
            )
        )

        for i in range(
            step,
            total_stations,
            step
        ):

            window = ordered_stations[
                max(0, i - 3):
                min(
                    total_stations,
                    i + 3
                )
            ]

            cheapest = min(
                window,
                key=lambda x:
                x["station"].retail_price
            )

            selected.append(
                cheapest
            )

            if len(selected) == stops_needed:
                break

        return selected