from django.shortcuts import render

#log in required
from django.contrib.auth.decorators import login_required

# Create your views here.
from todvstom.models import Room
from django.http import HttpResponse
import time
import datetime
from datetime import timedelta,date


@login_required
def room_sets(request):
	#get yesterdays,today, tommorow dates
	yesterday_date_is = date.today() - timedelta(1)
	today_date_is =  date.today()
	tommorow_date_is = date.today() + timedelta(1)


	# format strings for query
	yesterday_date_query = yesterday_date_is.strftime("%Y-%m-%d")
	today_date_query = time.strftime("%Y-%m-%d")
	tommorow_date_query = tommorow_date_is.strftime("%Y-%m-%d")

	#query
	yesterday_set = Room.objects.filter(set_date = yesterday_date_query)
	today_set = Room.objects.filter(set_date = today_date_query)
	tommorow_set = Room.objects.filter(set_date = tommorow_date_query)	

	return render(request,'todvstom_inner.html',{ 

		#pass query results to template
        'yesterday_set':yesterday_set,
        'today_set': today_set,
        'tommorow_set': tommorow_set,

        #pass dates for columm headers
        'yesterday_date_is': yesterday_date_is,
        'today_date_is': today_date_is,
        'tommorow_date_is': tommorow_date_is,

        # template stuff
        'nbar': 'room_sets',
        'have_jumbo': 'no',
        'jumbo_info': 'room sets'
    })

