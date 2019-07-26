# Generated by Django 2.1.4 on 2019-06-26 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crm_Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='empty', max_length=70, null=True)),
                ('client_type', models.CharField(default='empty', max_length=50)),
                ('client_phone', models.CharField(default='empty', max_length=12, null=True)),
                ('client_email', models.CharField(default='empty', max_length=50, null=True)),
                ('client_comment', models.CharField(default='empty', max_length=500, null=True)),
                ('client_status', models.BooleanField()),
                ('client_join_date', models.CharField(default='empty', max_length=30)),
                ('trashed_date', models.CharField(default='empty', max_length=30)),
                ('isvisible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Crm_Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(default='empty', max_length=20)),
                ('event_date', models.CharField(default='empty', max_length=20)),
                ('event_status', models.CharField(default='empty', max_length=20)),
                ('event_creator', models.CharField(default='empty', max_length=20)),
                ('event_curator', models.CharField(default='empty', max_length=20)),
                ('event_comment', models.CharField(default='empty', max_length=500)),
                ('event_state', models.BooleanField(default=True)),
                ('isvisible', models.BooleanField(default=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_client', to='gh_crm.Crm_Clients')),
            ],
        ),
    ]
