from django.shortcuts import render

# below is my creation
from django.http import HttpResponse, Http404
from shifts.models import open_shift

#import form for is_filled
from .forms import open_shiftForm

#log in required
from django.contrib.auth.decorators import login_required

#imprt for email
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage



@login_required
def index(request):
    shifts = open_shift.objects.filter(is_filled = False)
    #form = TransfersForm()

    #get the shifts user has already confirmed --can change to user id later
    current_user = request.user
    first_name = current_user.first_name
    last_name = current_user.last_name
    confirmed_user = open_shift.objects.filter(filled_by =first_name+' '+last_name )
    return render(request,'open_shifts.html',{
        'shifts': shifts,
        'confirmed_by_user': confirmed_user,
        'nbar': '/',
        'have_jumbo': 'yes',
        'jumbo_info': 'Available Shifts'
    })
@login_required
def profile(request):
    #shifts = open_shift.objects.filter(is_filled = False)
    
    return render(request,'profile.html',{
        #'shifts': shifts,
        'nbar': '/',
        'have_jumbo': 'yes',
        'jumbo_info': 'Available Shifts'
    })


@login_required
def parking_train(request):
	return render(request, 'parking_train.html',{
		'nbar': 'parking_train/',
		'have_jumbo': 'yes',
		})

@login_required
def hotel_location(request):
	return render(request, 'hotel_location.html',{
		'nbar': 'parking_train/',
		'have_jumbo': 'yes',
		'jumbo_info': 'Where to find the hotel'
		})

@login_required	
def parking(request):
	return render(request, 'parking.html',{
		'nbar': 'parking_train/',
		'have_jumbo': 'yes',
		'jumbo_info': 'Where to Park'
		})

@login_required
def train(request):
	return render(request, 'train.html',{
		'nbar': 'parking_train/',
		'have_jumbo': 'yes',
		'jumbo_info': 'Catch the Train'
		})

@login_required
def each_shift(request,shift_id):
		# get available shifts
		id = shift_id
		each_shift_db = open_shift.objects.filter(pk = id, is_filled= False)
		
		#get the shifts user has already confirmed --can change to user id later
		current_user = request.user
		first_name = current_user.first_name
		last_name = current_user.last_name
		confirmed_by_user = open_shift.objects.filter(filled_by =first_name+' '+last_name )


		return render(request, 'each_shift.html',{
		'each_shift_db': each_shift_db,
		'have_jumbo': 'yes',
		'confirmed_by_user': confirmed_by_user,
		'jumbo_info': 'confirm this shift'
		})
		
@login_required
def post_confirm(request, shift_id):
		form = open_shiftForm(request.POST)
		id = shift_id
		current_user = request.user
		#get_full_name only return object so we are piecing it together.
		first_name = current_user.first_name
		last_name = current_user.last_name
		fill_db = open_shift.objects.filter(pk = id)
		

		#send confirm email
		subject = "Confirmed Shift " 
		to = [current_user.email, 'bodonnell@psav.com']
		from_email = 'bodonnellpsav@gmail.com'
		ctx = {
		        'user_first': first_name,
		        'user_last'  : last_name,
		        'fill_db': fill_db,
		     }
		message = get_template('EMAIL_shift_taken.html').render(Context(ctx))
		msg = EmailMessage(subject, message, to=to, from_email=from_email)
		msg.content_subtype = 'html'
		msg.send()

		
		fill_db.update(is_filled = True , filled_by = first_name+' '+last_name)
		
		return render(request, 'confirmed.html',{
			'fill_db': fill_db,
			'have_jumbo': 'yes',
			'jumbo_info': 'This shift is Confirmed'
			})

# filter(pk=object_id).update(is_inprocess=True)

@login_required
def blast_shifts(request):
	#get all shifts that are not emailed.
	unblasted_db = open_shift.objects.filter(is_sent = False, is_filled=False)
	return render(request, 'blast_shifts.html',{
		'nbar': 'blast_shifts',
		'have_jumbo': 'yes',
		'jumbo_info': 'Send out Emails',
		'unblasted_db': unblasted_db,
		})

@login_required
def blast_confirm(request):
	#get all shifts that are not emailed.
	unblasted_db = open_shift.objects.filter(is_sent = False, is_filled = False)

	# send all techs and email alerting creation of new shifts
	techs = User.objects.filter(groups__name='techs')
	for u in techs:
		subject = "New shifts are available at the Renaissance Providence"
		to = [u.email]
		from_email = 'bodonnellpsav@gmail.com'
		ctx = {
	        'user': u.first_name,
	        'unblasted_db': unblasted_db,
	     }
		message = get_template('EMAIL_available_shifts.html').render(Context(ctx))
		msg = EmailMessage(subject, message, to=to, from_email=from_email)
		msg.content_subtype = 'html'
		msg.send()

	# mark each shift as sent to avoid duplicate sendings.	
	
	unblasted_db.update(is_sent = True)

	return render(request, 'blast_confirm.html',{
		'nbar': 'blast_confirm',
		'have_jumbo': 'yes',

		
		
		})	

