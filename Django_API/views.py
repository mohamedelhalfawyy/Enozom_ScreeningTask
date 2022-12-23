from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from Django_API.pagination import CustomPagination
from Django_API.serializers import CountryPopulationSerializer
from Django_API.serializers import CountrySerializer
from base.models import Country
from base.models import CountryPopulation


class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = CustomPagination


# Here we get the specific country population depending on the country code
@api_view(['GET'])
def get_specific_country(request, countryCode):
    countryName = Country.objects.get(country_code=countryCode)
    countryInfo = CountryPopulation.objects.filter(country_code=countryCode)
    populationSerializer = CountryPopulationSerializer(countryInfo, many=True)
    nameSerializer = CountrySerializer(countryName, many=False)

    return Response([nameSerializer.data, populationSerializer.data])
