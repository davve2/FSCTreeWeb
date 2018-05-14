from django import forms

from .models import User

class UserCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'name',
			'email',
			'location'
		]