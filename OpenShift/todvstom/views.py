from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def room_sets(request):
	return HttpResponse("today vs tommorow will go here")
