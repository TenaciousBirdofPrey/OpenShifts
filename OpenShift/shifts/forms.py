from django import forms
from .models import open_shift


class open_shiftForm(forms.ModelForm):
	class Meta:
		model = open_shift
		fields = ['is_filled']


# adds first and last name to sign up
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()