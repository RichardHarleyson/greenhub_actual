from django.contrib import admin
from .models import GCrm_Client, GCrm_Event, GCrm_files, GCrm_Vehicle

class MainClient(admin.ModelAdmin):
    list_display = (
        'id',
        'client_name',
        'client_last_date',
        'isvisible',
    )

class MainFiles(admin.ModelAdmin):
    list_display = (
        'id',
        'client_file',
        'client',
        'file_type',
    )

class MainVehicle(admin.ModelAdmin):
    list_display = (
        'id',
        'veh_client',
        'veh_VIN',
    )

admin.site.register(GCrm_Client, MainClient)
admin.site.register(GCrm_files, MainFiles)
admin.site.register(GCrm_Vehicle, MainVehicle)
