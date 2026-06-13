from django.db import models

# Create your models here.



class FuelStation(models.Model):

    opis_id = models.IntegerField()

    name = models.CharField(max_length=255)

    address = models.CharField(max_length=255)

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=20)

    rack_id = models.IntegerField()

    retail_price = models.FloatField()

    latitude = models.FloatField(
        null=True,
        blank=True
    )

    longitude = models.FloatField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name