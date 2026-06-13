from geopy.geocoders import Nominatim
from geopy.geocoders import ArcGIS


TEST_ADDRESSES = [
    "I-44, EXIT 283 & US-69, Big Cabin, OK",
    "I-8, EXIT 119 & SR-85, Gila Bend, AZ",
    "I-94, EXIT 143 & US-12 & SR-21, Tomah, WI",
]


def test_nominatim():

    print("\n===== NOMINATIM =====")

    geolocator = Nominatim(
        user_agent="fuel_optimizer"
    )

    for address in TEST_ADDRESSES:

        try:

            location = geolocator.geocode(
                address,
                timeout=10
            )

            print("\nAddress:", address)
            print("Result:", location)

        except Exception as e:

            print(address, e)


def test_arcgis():

    print("\n===== ARCGIS =====")

    geolocator = ArcGIS()

    for address in TEST_ADDRESSES:

        try:

            location = geolocator.geocode(
                address
            )

            print("\nAddress:", address)
            print("Result:", location)

        except Exception as e:

            print(address, e)


if __name__ == "__main__":

    test_nominatim()

    test_arcgis()