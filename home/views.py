from django.shortcuts import render, render_to_response
from event_details.models import Event_details
# Create your views here.
def index(request):
	return render_to_response('home/home.html', {'content ': Event_details.objects.all()})
