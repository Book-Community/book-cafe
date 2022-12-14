# Generated by Django 4.0.6 on 2022-07-23 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('findBookCafe', '0003_alter_shop_facebook_alter_shop_googlemaps_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='shop',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]
