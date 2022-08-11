# Generated by Django 4.0.6 on 2022-08-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findBookCafe', '0007_alter_shop_type_delete_cafetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='internetQuality',
            field=models.CharField(choices=[(0, 'none'), (1, 'bad'), (2, 'normal'), (3, 'good')], default=2, max_length=1),
        ),
    ]