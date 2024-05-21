from rest_framework import generics
from rest_framework import generics,status
from rest_framework.response import Response
from dash.models import Data
from dash.serializers import DataSerializer,BarChartSerializer,PieChartSerializer
from django.http import HttpResponse

class DataListView(generics.ListAPIView):
    serializer_class = DataSerializer

    def get_queryset(self):
        return Data.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response({"message": "No data available"}, status=status.HTTP_202_ACCEPTED)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BarChartDataView(generics.ListAPIView):
    serializer_class = BarChartSerializer
    def get_queryset(self):
        return Data.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response({"message": "No data available"}, status=status.HTTP_202_ACCEPTED)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PieChartDataView(generics.ListAPIView):
    serializer_class = PieChartSerializer    
    def get_queryset(self):
        return Data.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response({"message": "No data available"}, status=status.HTTP_202_ACCEPTED)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)