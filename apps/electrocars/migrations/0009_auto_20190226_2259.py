# Generated by Django 2.1.4 on 2019-02-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0008_auto_20190213_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='veh_folder',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='vehicle_photos',
            name='veh_photo_url',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='veh_photo',
            field=models.FileField(blank=True, upload_to='vehicles/%Y/%m_%d/'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='veh_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicle_photos',
            name='veh_photo',
            field=models.FileField(upload_to='vehicles/%Y/%m_%d/'),
        ),
    ]