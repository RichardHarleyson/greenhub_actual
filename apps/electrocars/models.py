#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Vehicle(models.Model):
	veh_title = models.CharField(max_length=50)
	veh_comp = models.CharField(max_length=10, blank=True)
	veh_vin = models.CharField(max_length=30, unique=True)
	veh_year = models.CharField(max_length=12, blank=True)
	veh_mileage = models.CharField(max_length=20, blank=True)
	veh_color_in = models.CharField(max_length=30, blank=True)
	veh_color = models.CharField(max_length=30)
	veh_price = models.CharField(max_length=10)
	# Ссылка на сточник фоток
	veh_folder = models.URLField(max_length=500, blank=True)
	# Заглавное фото машины, всегда лежит на сервере
	veh_photo = models.FileField(upload_to='vehicles/%Y/%m_%d/', blank=True)
	veh_battery = models.CharField(max_length=10, blank=True)
	veh_info = models.CharField(max_length=100, blank=True)
	veh_type_choice = [('salon','салон'),('dealler','диллер')]
	veh_type = models.CharField(max_length=20, choices=veh_type_choice, default=veh_type_choice[0])
	veh_status = models.PositiveSmallIntegerField(default=0)
	add_date = models.DateTimeField(auto_now_add=True)

	def full_name(self):
		return self.veh_title

class Vehicle_new(models.Model):
	veh_model = models.CharField(max_length=100, default='empty')
	veh_photo = models.FileField(upload_to='vehicles_new/%Y/%m_%d/', blank=True)
	veh_year = models.CharField(max_length=10, default='0')
	veh_mileage = models.CharField(max_length=10, default='0')
	veh_color_in = models.CharField(max_length=20, default='empty')
	vah_color = models.CharField(max_length=20, default='empty')
	veh_price = models.CharField(max_length=10, default='0')
	veh_type = models.CharField(max_length=20, default='empty')
	veh_status = models.CharField(max_length=20, default='empty')
	record_status = models.BooleanField(default=True)
	veh_incomming_date = models.CharField(max_length=20, default='empty')
	add_date = models.DateTimeField(auto_now_add=True)


# Дополнительные фото машины, могут находится как на сервере так и на внешних ресурсах
class Vehicle_photos(models.Model):
	# Адрес фото хранимого локально на сервере
	veh_photo = models.FileField(upload_to='vehicles/%Y/%m_%d/', blank=False)
	# Ссылка на фото со внешних ресурсов
	veh_photo_url = models.URLField(max_length=300, blank=True)
	veh_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='photos')
	# Тип хранения фото(на сервере, гугл диск или внешний ресурс)
	type = models.PositiveSmallIntegerField(default=0, blank=False)
