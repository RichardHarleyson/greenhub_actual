# Generated by Django 2.1.4 on 2019-02-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gdrive_vehicles',
            name='veh_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
