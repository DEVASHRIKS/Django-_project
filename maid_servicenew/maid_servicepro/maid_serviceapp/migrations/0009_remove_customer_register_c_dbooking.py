# Generated by Django 4.2.6 on 2023-11-21 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maid_serviceapp', '0008_remove_customer_register_c_birthdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_register',
            name='c_dbooking',
        ),
    ]
