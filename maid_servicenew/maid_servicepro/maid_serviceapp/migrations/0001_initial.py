# Generated by Django 4.2.6 on 2023-10-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=10, null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
    ]
