# Generated by Django 2.1.4 on 2019-07-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_crm', '0002_auto_20190626_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='crm_clients',
            name='veh_body',
            field=models.CharField(default='empty', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='crm_clients',
            name='veh_budget',
            field=models.CharField(default='empty', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='crm_clients',
            name='veh_fuel',
            field=models.CharField(default='empty', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='crm_clients',
            name='veh_year1',
            field=models.CharField(default='empty', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='crm_clients',
            name='veh_year2',
            field=models.CharField(default='empty', max_length=10, null=True),
        ),
    ]
