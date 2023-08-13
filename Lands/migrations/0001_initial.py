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
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ModeOfAcquisition', models.CharField(choices=[('Purchase', 'Purchase'), ('Transfer', 'Transfer'), ('Donation', 'Donation')], max_length=200)),
                ('CategoryOfLand', models.CharField(choices=[('Land', 'Land'), ('Investment', 'Investment')], max_length=200)),
                ('County', models.CharField(max_length=200)),
                ('Nearest_Location', models.CharField(max_length=200)),
                ('GPS', models.CharField(max_length=200)),
                ('Polygon', models.CharField(max_length=200)),
                ('LRCertifcateNo', models.CharField(max_length=200)),
                ('DocumentOfOwnership', models.CharField(choices=[('Title Deed', 'Title Deed'), ('Certificate', 'Certificate'), ('Allotment Letter', 'Allotment Letter')], max_length=200)),
                ('OwnershipDetails', models.CharField(max_length=200)),
                ('Size', models.IntegerField()),
                ('OwnershipStatus', models.CharField(choices=[('Freehold', 'Freehold'), ('Leasehold', 'Leasehold')], max_length=200)),
                ('AcquisitionDate', models.DateField(max_length=200)),
                ('RegistrationDate', models.DateField(max_length=200)),
                ('Status', models.CharField(choices=[('Disputed', 'Disputed'), ('Undisputed', 'Undisputed')], max_length=200)),
                ('Encumberances', models.CharField(max_length=200)),
                ('PlanningStatus', models.CharField(choices=[('Planned', 'Planned'), ('Unplanned', 'Unplanned')], max_length=200)),
                ('UseOfLand', models.CharField(max_length=200)),
                ('SurveyStatus', models.CharField(choices=[('Surveyed', 'Surveyed')], max_length=200)),
                ('AcquisitionAmount', models.IntegerField()),
                ('LandIndex', models.CharField(choices=[('Fair_Value', 'Fair Value'), ('Ministry_Zonal_Map', 'Ministry Zonal Map'), ('Land_Index', 'Land Index')], max_length=200)),
                ('DisposalDate', models.DateField(max_length=200)),
                ('ChangeOfUseDate', models.DateField(max_length=200)),
                ('DisposalValue', models.IntegerField()),
                ('AnnualRentalIncome', models.IntegerField()),
                ('DescriptionOfLand', models.TextField(max_length=200)),
                ('Department', models.CharField(choices=[('CPSB', 'CPSB'), ('REVENUE', 'REVENUE SERVICES')], max_length=200)),
                ('Remarks', models.TextField(max_length=200)),
                ('Responsible_officer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
