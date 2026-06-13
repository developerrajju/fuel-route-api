from geopy.geocoders import ArcGIS


class GeocoderService:

    geolocator = ArcGIS()

    @classmethod
    def geocode(cls, address):

        try:

            location = cls.geolocator.geocode(address)

            if not location:
                return None

            return {
                "latitude": location.latitude,
                "longitude": location.longitude,
                "address": location.address
            }

        except Exception:
            return None