# Generated by Django 4.2.4 on 2023-08-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Railway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=200)),
                ('RailwayID', models.CharField(max_length=200)),
                ('Length', models.IntegerField()),
                ('DateOfCommissioning', models.DateField(max_length=200)),
                ('TypeOfRail', models.CharField(max_length=200)),
                ('AmenitiesAvailable', models.CharField(max_length=200)),
                ('LandRegistryID', models.CharField(max_length=200)),
                ('UsefulLife', models.CharField(max_length=200)),
                ('Cost', models.CharField(max_length=200)),
                ('AnnualDepreciation', models.IntegerField()),
                ('Remarks', models.TextField(max_length=200)),
            ],
        ),
    ]
