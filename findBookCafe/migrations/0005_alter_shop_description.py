# Generated by Django 4.0.6 on 2022-07-23 20:02

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('findBookCafe', '0004_shop_created_date_shop_description_shop_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
    ]
