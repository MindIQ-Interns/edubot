from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import *

class MyRegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')


class MyRegistrationExtensionForm(forms.ModelForm):

	class Meta:
		model = UserExtension
		fields = ('dob', 'image', 'fb_id')

class QuizForm(forms.ModelForm):

	class Meta:
		model = Quiz
		fields = ('topics',)