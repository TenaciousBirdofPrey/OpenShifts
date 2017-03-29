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
    })

