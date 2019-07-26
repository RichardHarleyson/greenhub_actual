# Generated by Django 2.1.4 on 2019-02-05 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0002_vehicle_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veh_photo', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='veh_photo',
            field=models.FileField(blank=True, upload_to='veh_photo'),
        ),
        migrations.AddField(
            model_name='vehicle_photos',
            name='veh_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electrocars.Vehicle'),
        ),
    ]
