# Generated by Django 4.2.6 on 2023-11-21 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maid_serviceapp', '0006_service_category_service_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceman_register',
            name='s_birthdate',
        ),
    ]
