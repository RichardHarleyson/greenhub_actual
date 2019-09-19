from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='global_crm_main_page'),
    path('add_client', views.add_client, name='global_crm_add_client'),
    path('add_vehicle', views.add_vehicle, name='global_crm_add_vehicle'),
    path('upd_vehicle', views.upd_vehicle, name='global_crm_upd_vehicle'),
    path('upd_client', views.upd_client, name="global_crm_upd_client"),
    path('del_client', views.del_client, name="global_crm_del_client"),
    path('upload_client_file', views.upload_client_file, name="global_crm_upload_client_file"),
    path('del_client_file', views.del_client_file, name="global_crm_del_client_file"),
]
