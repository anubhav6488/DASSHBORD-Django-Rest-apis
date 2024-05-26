from django.db import models

# Create your models here.
class Data(models.Model):
    end_year=models.CharField(max_length=30) 
    intensity=models.FloatField(default='1')
    sector=models.CharField(max_length=30)
    topic=models.CharField(max_length=30) 
    insight=models.CharField(max_length=30)
    url=models.CharField(max_length=30)
    region=models.CharField(max_length=30)
    start_year=models.CharField(max_length=30)
    impact=models.CharField(max_length=30)
    added=models.CharField(max_length=30)
    published=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    relevance=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    pestle=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    likelihood=models.CharField(max_length=30)

    # class Meta:
    #     app_label = 'datass'
