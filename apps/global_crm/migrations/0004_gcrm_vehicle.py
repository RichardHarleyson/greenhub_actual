# Generated by Django 2.2.3 on 2019-09-13 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_crm', '0003_gcrm_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='GCrm_Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veh_track_num', models.CharField(default='empty', max_length=30)),
                ('veh_w8_id', models.CharField(default='empty', max_length=30)),
                ('veh_VIN', models.CharField(default='empty', max_length=30)),
                ('veh_invoice_num', models.CharField(default='empty', max_length=30)),
                ('veh_win_date', models.CharField(default='empty', max_length=30)),
                ('veh_container_num', models.CharField(default='empty', max_length=30)),
                ('veh_incomming_date', models.CharField(default='empty', max_length=30)),
                ('veh_photo', models.CharField(default='empty', max_length=30)),
                ('veh_payed', models.BooleanField(default=False)),
                ('veh_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veh_client', to='global_crm.GCrm_Client')),
            ],
        ),
    ]