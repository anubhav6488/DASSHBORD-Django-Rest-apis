from rest_framework import generics
from rest_framework import generics,status
from rest_framework.response import Response
from dashbrd.models import Data
from dashbrd.serializers import DataSerializer,BarChartSerializer,PieChartSerializer,IntensitySerializer

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
        print(Data.objects.all())
        
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
        
        for data in queryset:
            print(data.intensity)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class IntensityDataView(generics.ListAPIView):
    serializer_class = IntensitySerializer

    def get_queryset(self):
        return Data.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response({"message": "No data available"}, status=status.HTTP_202_ACCEPTED)
        
        for data in queryset:
            print(data.intensity)  # Print intensity for each record
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    