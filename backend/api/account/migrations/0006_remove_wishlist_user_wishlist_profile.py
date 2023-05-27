# Generated by Django 4.0.3 on 2022-04-01 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_wishlist_wishlistitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='profile',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
            preserve_default=False,
        ),
    ]
