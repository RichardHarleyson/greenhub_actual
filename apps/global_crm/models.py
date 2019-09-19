from django.db import models

class GCrm_Client(models.Model):
    client_name = models.CharField(max_length=100, default="empty", null=True)
    client_contact = models.CharField(max_length=100, default="empty", null=True)
    client_goal = models.CharField(max_length=300, default="empty", null=True)
    client_comment = models.CharField(max_length=250, default="empty", null=True)
    client_income_date = models.CharField(max_length=14, default="empty", null=True)
    client_last_date = models.CharField(max_length=14, default="empty", null=True)
    client_last_event = models.CharField(max_length=30, default="empty", null=True)
    client_next_date = models.CharField(max_length=14, default="empty", null=True)
    client_next_event = models.CharField(max_length=30, default="empty", null=True)
    client_trashed_date = models.CharField(max_length=14, default="empty", null=True)
    client_status = models.CharField(max_length=20, default="emtpy", null=True)
    isvisible = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name

class GCrm_Event(models.Model):
    pass

class GCrm_files(models.Model):
    client = models.ForeignKey(GCrm_Client, on_delete=models.CASCADE, related_name="client_file")
    client_file = models.FileField(upload_to ='clients/%Y/%m_%d', blank=False)
    file_type = models.CharField(max_length=30, default="empty", blank=False)

class GCrm_Vehicle(models.Model):
    veh_client = models.ForeignKey(GCrm_Client, on_delete=models.CASCADE, related_name="veh_client")
    veh_track_num = models.CharField(max_length=30, default="empty")
    veh_w8_id = models.CharField(max_length=30, default="empty")
    veh_VIN = models.CharField(max_length=30, default="empty")
    veh_invoice_num = models.CharField(max_length=30, default="empty")
    veh_win_date = models.CharField(max_length=30, default="empty")
    veh_container_num = models.CharField(max_length=30, default="empty")
    veh_incomming_date = models.CharField(max_length=30, default="empty")
    veh_photo = models.CharField(max_length=30, default="empty")
    veh_payed = models.BooleanField(default=False)
