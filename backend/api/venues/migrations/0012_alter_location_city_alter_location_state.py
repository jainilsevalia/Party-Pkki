# Generated by Django 4.0.3 on 2022-03-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0011_remove_venue_city_remove_venue_state_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]