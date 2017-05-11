from django.shortcuts import render

#log in required
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

# def room_sets(request):
# 	return HttpResponse("today vs tommorow will go here")

@login_required
def room_sets(request):
    

    return render(request,'todvstom_inner.html',{
        
        
        'nbar': 'room_sets',
        'have_jumbo': 'no',
        'jumbo_info': 'room sets'
    })
