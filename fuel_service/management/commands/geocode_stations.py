"""
Management Command:
Geocode fuel stations using ArcGIS and save coordinates.

Purpose:
- Convert truck stop addresses into latitude/longitude
- Store coordinates in the database
- Skip already geocoded stations
- Support resumable execution
"""

import time

from django.core.management.base import BaseCommand

from fuel_service.models import FuelStation
from fuel_service.services.geocoder import GeocoderService


class Command(BaseCommand):
    help = "Geocode fuel stations and save coordinates"

    def add_arguments(self, parser):
        parser.add_argument(
            "--limit",
            type=int,
            default=200,
            help="Number of stations to process"
        )

    def handle(self, *args, **options):

        limit = options["limit"]

        stations = FuelStation.objects.filter(
            latitude__isnull=True,
            longitude__isnull=True
        )[:limit]

        total = stations.count()

        success_count = 0
        failure_count = 0

        self.stdout.write(
            self.style.SUCCESS(
                f"Found {total} stations to geocode"
            )
        )

        for index, station in enumerate(
            stations,
            start=1
        ):

            search_text = (
                f"{station.address}, "
                f"{station.city}, "
                f"{station.state}"
            )

            try:

                result = GeocoderService.geocode(
                    search_text
                )

                if result:

                    station.latitude = result["latitude"]
                    station.longitude = result["longitude"]

                    station.save(
                        update_fields=[
                            "latitude",
                            "longitude"
                        ]
                    )

                    success_count += 1

                    self.stdout.write(
                        self.style.SUCCESS(
                            f"[{index}/{total}] "
                            f"SUCCESS: {search_text}"
                        )
                    )

                else:

                    failure_count += 1

                    self.stdout.write(
                        self.style.WARNING(
                            f"[{index}/{total}] "
                            f"NOT FOUND: {search_text}"
                        )
                    )

            except Exception as e:

                failure_count += 1

                self.stdout.write(
                    self.style.ERROR(
                        f"[{index}/{total}] "
                        f"ERROR: {e}"
                    )
                )

            # avoid rate limiting
            time.sleep(1)

        self.stdout.write("")
        self.stdout.write("=" * 60)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully geocoded: {success_count}"
            )
        )

        self.stdout.write(
            self.style.WARNING(
                f"Failed: {failure_count}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Geocoding completed."
            )
        )