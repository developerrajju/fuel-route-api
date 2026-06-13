import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "backend.settings"
)

django.setup()

from fuel_service.models import FuelStation
from fuel_service.services.geocoder import GeocoderService

stations = FuelStation.objects.all()[:10]

for station in stations:

    search_text = (
        f"{station.address}, "
        f"{station.city}, "
        f"{station.state}"
    )

    result = GeocoderService.geocode(search_text)

    print("\n" + "=" * 50)
    print(search_text)
    print(result)