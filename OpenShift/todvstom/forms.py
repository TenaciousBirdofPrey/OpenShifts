from django import forms
from django.forms import ModelForm
from todvstom.models import Room


class DateInput(forms.DateInput):
    input_type = 'date'

class RoomForm(ModelForm):
	class Meta:
		model = Room
		fields = ['set_date', 'symph_a','symph_b','ballroom',
				  'mozart','beethoven','haydn','handel','thirty_third',
				  	'capitol','other'	

					]
		widgets = {
            'set_date': DateInput(),
        }