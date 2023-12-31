# Generated by Django 4.2.4 on 2023-08-09 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Biological',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssetDescription', models.CharField(max_length=200)),
                ('CategoryOfAsset', models.CharField(max_length=200)),
                ('UnitOfMeasurement', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Unitcost', models.IntegerField()),
                ('FairValue', models.IntegerField()),
                ('UsefulLife', models.IntegerField()),
                ('AnnualDepreciation', models.IntegerField()),
                ('Department', models.CharField(choices=[('CPSB', 'CPSB'), ('REVENUE', 'REVENUE SERVICES')], max_length=200)),
                ('Status', models.CharField(max_length=200)),
                ('Remarks', models.TextField(max_length=200)),
                ('Responsible_officer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
