from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.

class Country(models.Model):
    country_code = models.CharField(max_length=45, null=False, primary_key=True)
    country_name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "country"


class CountryPopulation(models.Model):
    country_code = models.CharField(max_length=45, null=False, primary_key=True)
    year = models.CharField(max_length=45, null=False)
    value = models.IntegerField(null=False)

    class Meta:
        db_table = "country_population"
