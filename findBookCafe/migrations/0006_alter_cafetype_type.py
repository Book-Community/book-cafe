# Generated by Django 4.0.6 on 2022-08-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findBookCafe', '0005_alter_shop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafetype',
            name='type',
            field=models.CharField(choices=[('CAF', 'Καφετέρια'), ('LIB', 'Βιβλιοθήκη')], max_length=200, primary_key=True, serialize=False),
        ),
    ]