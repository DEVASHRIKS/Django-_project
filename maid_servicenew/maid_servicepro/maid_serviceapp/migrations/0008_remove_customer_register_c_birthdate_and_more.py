# Generated by Django 4.2.6 on 2023-11-21 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maid_serviceapp', '0007_remove_serviceman_register_s_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_register',
            name='c_birthdate',
        ),
        migrations.RemoveField(
            model_name='serviceman_register',
            name='s_dapp',
        ),
    ]
