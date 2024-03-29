# Generated by Django 4.2.6 on 2023-10-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid_serviceapp', '0004_alter_customer_register_c_birthdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_register',
            name='c_dbooking',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceman_register',
            name='s_dapp',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceman_register',
            name='s_idimg',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='serviceman_register',
            name='s_scity',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='serviceman_register',
            name='s_service',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='serviceman_register',
            name='s_typid',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='serviceman_register',
            name='s_wexp',
            field=models.IntegerField(null=True),
        ),
    ]
