# Generated by Django 4.2.6 on 2023-10-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid_serviceapp', '0003_serviceman_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_register',
            name='c_birthdate',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='serviceman_register',
            name='s_birthdate',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
