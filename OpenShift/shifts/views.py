from django.shortcuts import render

# below is my creation
from django.http import HttpResponse, Http404
from shifts.models import open_shift

#import form for is_filled
from .forms import open_shiftForm

#log in required
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    shifts = open_shift.objects.filter(is_filled = False)
    #form = TransfersForm()
    return render(request,'open_shifts.html',{
        'shifts': shifts,
        'nbar': '/',
        'jumbo_info': 'Available Shifts'
    })
@login_required
def profile(request):
    #shifts = open_shift.objects.filter(is_filled = False)
    
    return render(request,'profile.html',{
        #'shifts': shifts,
        'nbar': '/',
        'jumbo_info': 'Available Shifts'
    })


@login_required
def parking_train(request):
	return render(request, 'parking_train.html',{
		'nbar': 'parking_train/',
		})

@login_required
def hotel_location(request):
	return render(request, 'hotel_location.html',{
		'nbar': 'parking_train/',
		'jumbo_info': 'Where to find the hotel'
		})

@login_required	
def parking(request):
	return render(request, 'parking.html',{
		'nbar': 'parking_train/',
		'jumbo_info': 'Where to Park'
		})

@login_required
def train(request):
	return render(request, 'train.html',{
		'nbar': 'parking_train/',
		'jumbo_info': 'Catch the Train'
		})

@login_required
def each_shift(request,shift_id):
		# form = open_shiftForm(request.POST)
		# if form.is_valid():
		# 	form.save(commit = True)
		id = shift_id
		each_shift_db = open_shift.objects.filter(pk = id)
		return render(request, 'each_shift.html',{
		'each_shift_db': each_shift_db,
		'jumbo_info': 'confirm this shift'
		})
		
@login_required
def post_confirm(request, shift_id):
	form = open_shiftForm(request.POST)
	id = shift_id
	fill_db = open_shift.objects.filter(pk = id)
	fill_db.update(is_filled = True)

	
	
	
	return render(request, 'confirmed.html',{
		'fill_db': fill_db,
		'jumbo_info': 'This shift is Confirmed'
		})

# filter(pk=object_id).update(is_inprocess=True)