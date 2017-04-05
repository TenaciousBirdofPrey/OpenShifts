from django import forms
from .models import open_shift


class open_shiftForm(forms.ModelForm):
	class Meta:
		model = open_shift
		fields = ['is_filled']