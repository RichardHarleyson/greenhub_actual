# Generated by Django 2.1.4 on 2019-02-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0009_auto_20190226_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='veh_title',
            field=models.CharField(max_length=50),
        ),
    ]
