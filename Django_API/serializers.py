from rest_framework import serializers

from base.models import Country
from base.models import CountryPopulation


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryPopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryPopulation
        fields = '__all__'
