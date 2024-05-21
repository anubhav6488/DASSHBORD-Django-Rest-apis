from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['intensit', 'likelihood', 'relevance', 'end_year','start_year', 'country', 'topic', 'region',]


class BarChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['intensit', 'likelihood', 'relevance', 'end_year','start_year', 'country', 'topic', 'region',]

class PieChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['intensit', 'likelihood', 'relevance', 'end_year','start_year', 'country', 'topic', 'region',]