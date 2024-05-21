"""
URL configuration for DASSHBORD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.urls import path, include
from dash.views import DataListView,BarChartDataView,PieChartDataView
from .views import home

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/',DataListView.as_view(),name='data-list'),

# ]
# from django.contrib import admin
# from django.urls import path, include
# from dash.views import DataListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', DataListView.as_view(), name='data-list'),
    path('bar-chart-data/', BarChartDataView.as_view(), name='bar-chart-data'),
    path('pie-chart-data/', PieChartDataView.as_view(), name='pie-chart-data'),
    path('', home, name='home'),  # Define a root view
]
