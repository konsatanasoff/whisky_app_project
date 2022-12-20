from rest_framework import serializers

from drink_api.models import DrinkModel


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkModel
        fields = '__all__'
