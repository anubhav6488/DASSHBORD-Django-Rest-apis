# Generated by Django 5.0.6 on 2024-05-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(max_length=30)),
                ('intensity', models.FloatField()),
                ('sector', models.CharField(max_length=30)),
                ('topic', models.CharField(max_length=30)),
                ('insight', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('start_year', models.CharField(max_length=30)),
                ('impact', models.CharField(max_length=30)),
                ('added', models.CharField(max_length=30)),
                ('published', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('relevance', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('pestle', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('likelihood', models.CharField(max_length=30)),
            ],
        ),
    ]
