from django import forms
from django.forms import ModelForm
from .models import Contact,Trick,Register

class ContactForm(ModelForm):
	class Meta:
		model=Contact
		fields = '__all__'

class TrickForm(ModelForm):
	class Meta:
		model=Trick
		fields = '__all__'

class RegisterForm(ModelForm):
	class Meta:
		model=Register
		fields='__all__'


