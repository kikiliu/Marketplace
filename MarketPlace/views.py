# Create your views here.
#from django.contrib.localflavor.us.forms import USStateField
from django.shortcuts import render
from django.http import HttpResponse
from models import Event

def eventlist(request):
    # 1. prepare data
    events = Event.objects.all()

    # 2. put into context dictionary
    context = { 'events' : events}
    
    # 3. render specified page using context
    return render(request, "eventlist.html", context)

def main(request):
	events = Event.objects.all()
	profiles = []
	for event in events:
		if event.profile.first_name == 'Derek':
			profiles.append(event.profile)
	context = {'events' : events, 'profiles': profiles}

	return render(request, 'main.html', context)
