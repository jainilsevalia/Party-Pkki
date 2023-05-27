# Generated by Django 4.0.3 on 2022-04-23 12:55

import api.account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_booking_admin_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=api.account.models.profile_pic_path),
        ),
    ]
