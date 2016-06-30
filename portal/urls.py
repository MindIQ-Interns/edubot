from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='login'),
	url(r'^secure/$', views.secure, name='authentication'),
	url(r'^register/$', views.register_user, name='register'),
	url(r'^user_profile/$', views.user_profile, name='profile'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^my_quizzes/$', views.my_quizzes, name='my_quizzes'),
	url(r'^(?P<quiz_id>[0-9]+)/quizdetails/$', views.quizdetails, name="detail"),
	url(r'^create_quiz/$', views.create_quiz, name="main"),
	url(r'^logout/$', views.logout, name='logout'),
]