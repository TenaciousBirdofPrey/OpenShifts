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


@login_required
def seven_day(request):
	#get the 7 dates to be viewed	
	one_date_is =  date.today()#.strftime("%Y-%m-%d")
	two_date_is = date.today() + timedelta(1)	
	three_date_is = date.today() + timedelta(2)
	four_date_is = date.today() + timedelta(3)
	five_date_is = date.today() + timedelta(4)
	six_date_is = date.today() + timedelta(5)
	seven_date_is = date.today() + timedelta(6)

	# get queries with it
	one_set = Room.objects.filter(set_date = one_date_is.strftime("%Y-%m-%d"))
	two_set = Room.objects.filter(set_date = two_date_is.strftime("%Y-%m-%d"))
	three_set = Room.objects.filter(set_date = three_date_is.strftime("%Y-%m-%d"))
	four_set = Room.objects.filter(set_date = four_date_is.strftime("%Y-%m-%d"))
	five_set = Room.objects.filter(set_date = five_date_is.strftime("%Y-%m-%d"))
	six_set = Room.objects.filter(set_date = six_date_is.strftime("%Y-%m-%d"))
	seven_set = Room.objects.filter(set_date = seven_date_is.strftime("%Y-%m-%d"))

	return render(request,'seven_day_inner.html',{ 
		#pass the dates
		'one_date_is':one_date_is,
		'two_date_is': two_date_is,
		'three_date_is': three_date_is,
		'four_date_is': four_date_is,
		'five_date_is': five_date_is,
		'six_date_is':six_date_is,
		'seven_date_is':seven_date_is,

		#pass queries
		'one_set': one_set,
		'two_set':two_set,
		'three_set': three_set,
		'four_set': four_set,
		'five_set': five_set,
		'six_set': six_set,
		'seven_set': seven_set,

        # template stuff
        'nbar': 'seven_day',
        'have_jumbo': 'no',
        'jumbo_info': 'seven_day'
    })