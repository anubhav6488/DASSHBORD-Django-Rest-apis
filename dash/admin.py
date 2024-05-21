from django.contrib import admin
from dash.models import Data
from import_export.admin import ImportExportModelAdmin
class datasadmin(ImportExportModelAdmin):
    list_display=('end_year','intensit','sector','topic','insight','url','region','start_year','impact','added','published','country','relevance','source','pestle','title','likelihood')
admin.site.register(Data,datasadmin)

