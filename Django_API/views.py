from rest_framework.decorators import api_view
from rest_framework.response import Response

from Django_API.serializers import CountrySerializer
from Django_API.serializers import CountryPopulationSerializer

from base.models import Country
from base.models import CountryPopulation


@api_view(['GET'])
def getData(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


# Here we get the specific country population depending on the country code
@api_view(['GET'])
def get_specific_country(request, countryCode):
    countryName = Country.objects.get(country_code=countryCode)
    countryInfo = CountryPopulation.objects.filter(country_code=countryCode)
    populationSerializer = CountryPopulationSerializer(countryInfo, many=True)
    nameSerializer = CountrySerializer(countryName, many=False)

    return Response([nameSerializer.data, populationSerializer.data])
