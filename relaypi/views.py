from django.shortcuts import render
from hardware.models import Relay

def home(request):
	relays = Relay.objects.all()
	
	return render(request, 'index.html', locals()) 
