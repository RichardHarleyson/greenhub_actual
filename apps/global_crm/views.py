from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import GCrm_Client, GCrm_files, GCrm_Vehicle
from datetime import date, timedelta

def main_page(request):
    clients = GCrm_Client.objects.all();
    files = GCrm_files.objects.all();
    vehicles = GCrm_Vehicle.objects.all();
    return render(request, 'global_crm/global_crm_main.html', context={'clients': clients, 'files': files, 'vehicles': vehicles})

@csrf_exempt
def add_client(request):
    client_comment = date.today().strftime("%d/%m/%Y") + ":" + 'Клиент Добавлен' + "\r\n"
    if request.POST.get('client_comment') != '':
        client_comment += date.today().strftime("%d/%m/%Y") + ":" + request.POST.get('client_comment') + "\r\n"
    client = GCrm_Client.objects.create(
        client_name = request.POST.get('client_name'),
        client_contact = request.POST.get('client_contact'),
        client_goal = request.POST.get('client_goal'),
        client_comment = client_comment,
        client_income_date = date.today().strftime("%d/%m/%Y"),
        client_last_date = date.today().strftime("%d/%m/%Y"),
        client_last_event = 'Новый Клиент',
        client_next_date = (date.today() + timedelta(days=2)).strftime("%d/%m/%Y"),
        client_next_event = 'Перезвонить',
        client_status = 'В Работе',
        isvisible = True,
    )
    return HttpResponse("We're good")

@csrf_exempt
def add_vehicle(request):
    # if len(request.FILES) == 0:
    #     return HttpResponse('Shit!')
    # myfile = request.FILES.get(request.POST.get('veh_photo'))
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)

    # vehicle = GCrm_Vehicle.objects.create(
    #     veh_client = GCrm_Client.objects.get(id=int(request.POST.get('client_id'))),
    #     veh_track_num = request.POST.get('veh_track_num'),
    #     veh_w8_id = request.POST.get('veh_w8_id'),
    #     veh_VIN = request.POST.get('veh_VIN'),
    #     veh_invoice_num = request.POST.get('veh_invoice_num'),
    #     veh_win_date = request.POST.get('veh_win_date'),
    #     veh_container_num = request.POST.get('veh_container_num'),
    #     veh_incomming_date = request.POST.get('veh_incomming_date'),
    # )

        # veh_photo = fs.url(filename),
        # veh_payed = request.POST.get('veh_payed'),
    print('WTF')
    return HttpResponse('Vehicle Added')

@csrf_exempt
def upd_vehicle(request):
    return HttpResponse('Updated Vehicle')

@csrf_exempt
def del_vehicle(request):
    vehicle = GCrm_Vehicle.objects.get(id = int(request.POST.get('vehicle_id'))).delete()
    return HttpResponse('Vehicle deleted')

@csrf_exempt
def upd_client(request):
    client = GCrm_Client.objects.get(id = int(request.POST.get('client_id')))
    if(request.POST.get('client_comment') != ''):
        upd_client_comment = client.client_comment + date.today().strftime("%d/%m/%Y") + ':' + request.POST.get('client_comment') + "\r\n"
    else:
        upd_client_comment = client.client_comment
    upd_client_last_event = client.client_next_event
    print(request.POST.get('client_comment'))
    upd_client = GCrm_Client.objects.all().filter(id = int(request.POST.get('client_id'))).update(
        client_name = request.POST.get('client_name'),
        client_contact = request.POST.get('client_contact'),
        client_goal = request.POST.get('client_goal'),
        client_comment = upd_client_comment,
        client_status = request.POST.get('client_status'),
        client_last_date = date.today().strftime("%d/%m/%Y"),
        client_last_event = upd_client_last_event,
        client_next_date = (date.today() + timedelta(days=2)).strftime("%d/%m/%Y"),
        client_next_event = request.POST.get('client_next_event'),
    )
    return HttpResponse('We got in here')

@csrf_exempt
def del_client(request):
    client = GCrm_Client.objects.all().filter(id = int(request.POST.get('client_id'))).update(
        isvisible = False,
    )
    return HttpResponse('Deleted')

@csrf_exempt
def upload_client_file(request):
    if len(request.FILES) == 0:
        return HttpResponse('Shit!')
    myfile = request.FILES.get(request.POST.get('file_type'))
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    new_file = GCrm_files.objects.create(
        client = GCrm_Client.objects.get(id = int(request.POST.get('client_id'))),
        client_file = fs.url(filename),
        file_type = request.POST.get('file_type')
    )
    return HttpResponse('File Uploaded')

@csrf_exempt
def del_client_file(request):
    del_file = GCrm_files.objects.all().filter(id = int(request.POST.get('file_id'))).delete()
    return HttpResponse('File Deleted')
