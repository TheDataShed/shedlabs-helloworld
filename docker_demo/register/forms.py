from django import forms

from .models import Attendee

class RegisterForm(forms.ModelForm):

	class Meta:
		model = Attendee
		fields = ('first_name', 'surname', 'company', 'email_address')