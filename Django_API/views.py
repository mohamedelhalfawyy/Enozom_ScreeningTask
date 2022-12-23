from rest_framework.response import Response
from rest_framework.decorators import api_view
from Django_API.serializers import ItemSerializer
from base.models import Country

@api_view(['GET'])
def getData(request):
    countries = Country.objects.all()
    serializer = ItemSerializer(countries, many=True)
    return Response(serializer.data)
