import RPi.GPIO as GPIO
from time import sleep

from django.shortcuts import render, redirect
from django.contrib import messages

from models import Relay

def control(request, relay_id):
	relay = Relay.objects.get(pk=relay_id)
	print relay.name
	
	#set up GPIO using BCM numbering
	GPIO.setmode(GPIO.BCM)
	#trigger relay
	GPIO.setup(relay.gpio_id,GPIO.OUT)
	#nessesary to simulate a button push(?)
	sleep(1)
	#return relay to orginial state
	GPIO.cleanup()
	
	#send success message
	messages.add_message(request, messages.SUCCESS, '%s was triggered successfully' % relay.name)
	
	return redirect('/')
