# Generated by Django 4.2.4 on 2023-08-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtherInfrastructure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherinfrastructure',
            name='Length',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='otherinfrastructure',
            name='Purchase_Amount',
            field=models.IntegerField(),
        ),
    ]
