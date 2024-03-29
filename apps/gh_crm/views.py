from django.shortcuts import render
from django.http import HttpResponse
from .models import Crm_Clients, Crm_Events, Client_file
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import datetime

def events_page(request):
	clients = Crm_Clients.objects.all().filter(isvisible = True)
	events = Crm_Events.objects.all().filter(isvisible = True)
	counts = {'client_count': clients.count(), 'event_count': events.count()}
	return render(request, 'gh_crm/crm_events.html', context={'clients': clients, 'events': events, 'content': counts,})


def clients_page(request):
	clients = Crm_Clients.objects.all().filter(isvisible = True)
	events = Crm_Events.objects.all().filter(isvisible = True)
	files = Client_file.objects.all().filter(photo_status = True)
	counts = {'client_count': clients.count(), 'event_count': events.count()}
	return render(request, 'gh_crm/crm_clients.html', context={'clients': clients, 'content': counts, 'files': files})


@csrf_exempt
def load_file(request):
	if len(request.FILES) == 0:
		return HttpResponse('Shit!')
	myfile = request.FILES.get('client_file')
	fs = FileSystemStorage()
	filename = fs.save(myfile.name, myfile)
	new_file = Client_file.objects.create(
		client_file = fs.url(filename),
		client_id = Crm_Clients.objects.get(
			id = int(request.POST.get('client_id'))),
		photo_status = True,
	)
	return HttpResponse('File Added');


@csrf_exempt
def del_file(request):
	del_file = Client_file.objects.all().filter(id = int(request.POST.get('file_id'))).update(
		photo_status = False,
	)
	return HttpResponse('File deleted');


def add_client(request):
	now = datetime.datetime.now()
	try:
		if(request.POST.get('isactive') == 'on'):
			isactive = True
		else:
			isactive = False
		new_client = Crm_Clients.objects.create(
			client_name = request.POST.get('client_name'),
			client_type = request.POST.get('client_type'),
			veh_body = request.POST.get('veh_body'),
			veh_budget = request.POST.get('veh_budget'),
			client_phone = request.POST.get('client_phone'),
			client_email = request.POST.get('client_email'),
			client_comment = request.POST.get('comment'),
			client_join_date = now.strftime("%d/%m/%Y"),
			client_status = isactive,
		)
		return HttpResponse(True)
	except Exception as ex:
		return HttpResponse(False)

def add_event(request):
	try:
		new_event = Crm_Events.objects.create(
			client_id = Crm_Clients.objects.get(id = request.POST.get('client_id')),
			event_type = request.POST.get('event_type'),
			event_date = request.POST.get('event_date'),
			event_status = 'Не Выполнено',
			event_creator = 'Анатолий',
			event_curator = request.POST.get('responsible'),
			event_comment = request.POST.get('comment'),
			event_state = True,
		)
		return HttpResponse(True)
	except:
		return HttpResponse(False)

def update_event(request):
	try:
		get_event = Crm_Events.objects.all().filter(id = int(request.POST.get('event_id'))).update(
			client_id = Crm_Clients.objects.get(id = request.POST.get('client_id')),
			event_type = request.POST.get('event_type'),
			event_date = request.POST.get('event_date'),
			event_status = 'Не Выполнено',
			event_creator = 'Анатолий',
			event_curator = request.POST.get('responsible'),
			event_comment = request.POST.get('comment'),
			event_state = True,
		)
		return HttpResponse(True)
	except:
		return HttpResponse(False)

def update_client(request):
	try:
		if(request.POST.get('isactive') == 'on'):
			isactive = True
		else:
			isactive = False
		get_client = Crm_Clients.objects.all().filter(id = int(request.POST.get('client_id'))).update(
			client_name = request.POST.get('client_name'),
			veh_body = request.POST.get('veh_body'),
			veh_budget = request.POST.get('veh_budget'),
			client_type = request.POST.get('client_type'),
			client_phone = request.POST.get('client_phone'),
			client_email = request.POST.get('client_email'),
			client_comment = request.POST.get('comment'),
			client_status = isactive,
		)
		return HttpResponse(True)
	except:
		return HttpResponse(False)

@csrf_exempt
def remove_event(request):
	try:
		get_event = Crm_Events.objects.all().filter(id = int(request.POST.get('event_id'))).update(
			isvisible = False
		)
		return HttpResponse(True)
	except:
		return HttpResponse(False)

@csrf_exempt
def remove_client(request):
	try:
		now = datetime.datetime.now()
		get_client = Crm_Clients.objects.all().filter(id = int(request.POST.get('client_id'))).update(
			isvisible = False,
			client_status = False,
			trashed_date = now.strftime("%d/%m/%Y")
		)
		get_event = Crm_Events.objects.all().filter(client_id__id = int(request.POST.get('client_id'))).update(
			isvisible = False
		)
		return HttpResponse(True)
	except:
		return HttpResponse(False)

@csrf_exempt
def update_event_status(request):
	try:
		get_event = Crm_Events.objects.all().filter(id = int(request.POST.get('event_id'))).update(
			event_status = request.POST.get('event_status'),
		)
		return HttpResponse(True)
	except:
		return HttpResponse(False)

@csrf_exempt
def update_client_status(request):
	try:
		savior = lambda a: a == '1'
		get_client = Crm_Clients.objects.all().filter(id = int(request.POST.get('client_id'))).update(
			# client_status = bool(request.POST.get('client_status')),
			client_status = savior(request.POST.get('client_status'))
		)
		return HttpResponse(True)
	except:
		return HttpResponse(False)

@csrf_exempt
def event_page(request):
	clients = Crm_Clients.objects.all()
	events = Crm_Events.objects.all()
	return render(request, 'gh_crm/core_gh_crm.html', context={'clients': clients, 'events': events})
