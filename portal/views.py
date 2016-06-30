from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from forms import *
from models import *
from django.contrib.auth.models import User
from datetime import date
import datetime

def login(request):
	return render(request, 'portal/login.html')

def signin(request):
	context = {}
	context.update(csrf(request))
	context.update({'enter': 'entering'})
	return render(request, 'portal/signin.html', context)

def secure(request):
	username = request.POST.get('username', '')	
	password = request.POST.get('pwd', '')
	user = auth.authenticatinge(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return render(request, 'portal/home.html')
	else:
		context = {}
		return render(request, 'portal/signin.html', context = {
			'enter': 'doesnotexist'
			})

def register_user(request):
	if request.method == 'POST':
		userextension = UserExtension()
		form1 = MyRegistrationForm(request.POST)
		user = form1.save(commit=False)
		userextension.username = request.POST['username']
		userextension.image = request.POST['image']
		userextension.dob = request.POST['dob']
		userextension.fb_id = request.POST['fb_id']
		# checking validity before saving
		user.full_clean()
		userextension.full_clean()
		# saving
		userextension.save()
		user.save()
		# authenticating and logging in
		curr_user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
		if (curr_user.is_anonymous() == False):
			auth.login(request, curr_user)
		return render(request, 'portal/home.html')
	args = {}
	args.update(csrf(request))
	args['form1'] = MyRegistrationForm()
	args['form2'] = MyRegistrationExtensionForm()
	return render(request, 'portal/register.html', args)

def home(request):
	if request.user.is_authenticated():
		return render(request, 'portal/home.html')
	else:
		return render(request, 'portal/login.html')

def create_quiz(request):
	if request.method == 'POST':
		list_of_options = {}
		data = request.POST
		new_quiz = Quiz()
		new_quiz.name = data['quiz.name']
		if 'quiz.is_graded' in data.keys():
			new_quiz.is_graded=True
		curr_user_extension = UserExtension.objects.get(username=request.user.username)
		new_quiz.author = curr_user_extension

		for fields in data:
			field = fields.split(".")
			if(field[0]=='option'):
				question_number = field[1]
				option_number = field[2]
				new_option = Option()
				new_option.text = data[fields]
				if question_number in list_of_options.keys():
					list_of_options[question_number][option_number]=new_option
				else:
					list_of_options[question_number] = {}
					list_of_options[question_number][option_number]=new_option
		for fields in data:
			field = fields.split(".")
			if(field[0]=='optioncheck'):
				question_number = field[1]
				option_number = field[2]
				list_of_options[question_number][option_number].is_correct = True

		# checking validity before saving
		for question in list_of_options:
			for option in list_of_options[question]:
				list_of_options[question][option].full_clean()
		new_quiz.full_clean()

		# saving all the options :
		for question in list_of_options:
			for option in list_of_options[question]:
				list_of_options[question][option].save()

		new_quiz.save()
		for topic in data['topics']:
			new_quiz.topics.add(topic)

		# saving all the questions :
		for fields in data:
			field = fields.split(".")
			if(field[0]=='q'):
				question_number = field[1]
				new_question = Question()
				new_question.text = data[fields]
				new_question.save()
				for option in list_of_options[question_number]:
					new_question.options.add(list_of_options[question_number][option])
				new_question.save()
				new_quiz.questions.add(new_question)
		return render(request, 'portal/new.html')
	quizform = QuizForm()
	args = {}
	args.update(csrf(request))
	args['quizform'] = quizform
	return render(request, 'portal/new.html', args)

def quizdetails(request, quiz_id):
	if request.user.is_authenticated():		
		args = {}
		args['quiz'] = Quiz.objects.get(pk=quiz_id)
		return render(request, 'portal/detail.html', args)
	else:
		return render(request, 'portal/login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'portal/login.html')	

def user_profile(request):
	args = {}
	args.update(csrf(request))
	args['userextension'] = UserExtension.objects.get(username=request.user.username)
	return render(request, 'portal/user_profile.html', args)

def my_quizzes(request):
	args = {}
	args.update(csrf(request))
	curr_user_extension = UserExtension.objects.get(username=request.user.username)
	args['quiz'] = Quiz.objects.filter(author=curr_user_extension)
	return render(request, 'portal/my_quizzes.html', args)