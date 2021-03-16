from rest_framework import serializers
from .models import Tables,Legs,Feet

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = '__all__'

class LegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legs
        fields = '__all__'

class FeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feet
        fields = '__all__'