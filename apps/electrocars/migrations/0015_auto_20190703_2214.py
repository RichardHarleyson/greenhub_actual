# Generated by Django 2.1.4 on 2019-07-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0014_vehicle_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_new',
            name='veh_photo',
            field=models.FileField(blank=True, upload_to='vehicles_new/%Y/%m_%d/'),
        ),
    ]
