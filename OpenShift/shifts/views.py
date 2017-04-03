from django.shortcuts import render

# below is my creation
from django.http import HttpResponse, Http404
from shifts.models import open_shift

# original per tutorial.
# def index(reauest):
# 	return HttpResponse ("open shifts will appear hear!")


def index(request):
    shifts = open_shift.objects.all()
    #form = TransfersForm()
    return render(request,'open_shifts.html',{
        'shifts': shifts,
        'nbar': '/'
    })

def parking_train(request):
	return render(request, 'parking_train.html',{
		'nbar': 'parking_train/',
		})

def hotel_location(request):
	return render(request, 'hotel_location.html',{
		'nbar': 'parking_train/',
		'jumbo_info': 'Where to find the hotel'
		})
def parking(request):
	return render(request, 'parking.html',{
		'nbar': 'parking_train/',
		'jumbo_info': 'Where to Park'
		})

def train(request):
	return render(request, 'train.html',{
		'nbar': 'parking_train/',
		'jumbo_info': 'Catch the Train'
		})

def each_shift(request,shift_id):
		id = shift_id
		each_shift_db = open_shift.objects.filter(pk = id)
		return render(request, 'each_shift.html',{
		'each_shift_db': each_shift_db,
		'jumbo_info': 'confirm this shift'
		})



