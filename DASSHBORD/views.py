from rest_framework import generics,status
from rest_framework.response import Response
from dashbrd.models import Data
from dashbrd.serializers import DataSerializer
from django.http import HttpResponse



def home(request):
    return HttpResponse("Welcome to the Data API. Go to /api/ to see the data.")
