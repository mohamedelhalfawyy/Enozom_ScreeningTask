from rest_framework import serializers

from base.models import Country


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
