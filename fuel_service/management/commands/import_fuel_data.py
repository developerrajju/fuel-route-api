import pandas as pd

from django.core.management.base import BaseCommand

from fuel_service.models import FuelStation


class Command(BaseCommand):
    help = "Import fuel station data from CSV"

    def handle(self, *args, **kwargs):

        csv_file = "fuel-prices-for-be-assessment.csv"

        df = pd.read_csv(csv_file)

        original_count = len(df)

        # Remove duplicate stations
        df = df.drop_duplicates(
            subset=["OPIS Truckstop ID"]
        )

        unique_count = len(df)

        stations = []

        for _, row in df.iterrows():

            station = FuelStation(
                opis_id=row["OPIS Truckstop ID"],
                name=row["Truckstop Name"],
                address=row["Address"],
                city=row["City"],
                state=row["State"],
                rack_id=row["Rack ID"],
                retail_price=row["Retail Price"]
            )

            stations.append(station)

        FuelStation.objects.bulk_create(
            stations,
            batch_size=1000
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"""
Original rows: {original_count}
Unique stations: {unique_count}
Duplicates removed: {original_count - unique_count}
                """
            )
        )