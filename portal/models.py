from django.db import models
from django.contrib.auth.models import User

class UserExtension(models.Model):
	username = models.CharField(max_length=140, unique=True, null=False)
	dob = models.DateField(null=False)
	fb_id = models.CharField(max_length=140)
	image = models.ImageField(upload_to='user_image')
	
	def __str__(self):
		return self.username

class Subject(models.Model):
	name = models.CharField(max_length=140)

	def __str__(self):
		return self.name


class Topic(models.Model):
	name = models.CharField(max_length=140)
	subject = models.ForeignKey(Subject)

	def __str__(self):
		return self.name


class Option(models.Model):
	text = models.TextField(default="nooption")
	is_correct = models.BooleanField(default=False)
	image = models.ImageField(upload_to='option_image')

	def __str__(self):
		return self.text


class Question(models.Model):
	text = models.TextField()
	description = models.TextField(default="nodescription")
	review = models.TextField(default="noreview")
	options = models.ManyToManyField("Option")
	image = models.ImageField(upload_to='question_image')

	def __str__(self):
		return self.text


class Quiz(models.Model):
	name = models.CharField(max_length=140)
	is_graded = models.BooleanField(default=False)
	author = models.ForeignKey(UserExtension)
	topics = models.ManyToManyField(Topic)
	questions = models.ManyToManyField(Question)

	def __str__(self):
		return self.name


class Answer(models.Model):
	student = models.ForeignKey(UserExtension)
	question = models.ForeignKey(Question)
	quiz = models.ForeignKey(Quiz)
	option = models.ForeignKey(Option)

	def __str__(self):
		return self.option.__str__()


class Review(models.Model):
	student = models.ForeignKey(UserExtension)
	quiz = models.ForeignKey(Quiz)
	score = models.IntegerField(default=0)
	text = models.TextField()

	def __str__(self):
		return self.student.__str__() + ', {0}'.format(self.score)


class Attempted(models.Model):
	student = models.ForeignKey(UserExtension)
	quiz = models.ForeignKey(Quiz)
	no_of_q_attempted = models.IntegerField(default=0)
	is_complete = models.BooleanField(default=False)

	def __str__(self):
		return self.student.__str__() + ' has completed {0} questions in quiz '.format(self.number_attempted) + '.'
