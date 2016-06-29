from django.db import models
from django.contrib.auth.models import User as PortalUser

class BotUser(models.Model):
    first_name = models.CharField(max_length=200, default='*')
    last_name = models.CharField(max_length=200, default='*')
    username = models.CharField(max_length=200, default='*')
    fb_id = models.CharField(max_length=200)
    dob = models.DateField()
    portal_counterpart = models.ForeignKey(PortalUser, null=True, blank=True, default=None)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def has_first_name(self):
        return False if self.first_name == '*' else True

    def has_last_name(self):
        return False if self.last_name == '*' else True

    def has_username(self):
        return False if self.username == '*' else True


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return self.name


class Option(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to='problems')

    def __str__(self):
        return self.text


# To VTA: Please add comments to this model, slightly unclear as to what the attributes are for -NJ
class Question(models.Model):
    text = models.TextField()
    details = models.TextField()
    review = models.TextField()
    options = models.ManyToManyField(Option)
    image = models.ImageField(upload_to='problem')

    def __str__(self):
        return self.text


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    is_compulsory = models.BooleanField(default=False)
    author = models.ForeignKey(PortalUser)
    topics = models.ManyToManyField(Topic)
    questions = models.ManyToManyField(Question)
    length = models.IntegerField()

    def __str__(self):
        return self.name


class Answer(models.Model):
    student = models.ForeignKey(BotUser)
    quiz = models.ForeignKey(Quiz)
    question = models.ForeignKey(Question)
    option = models.ForeignKey(Option)

    def __str__(self):
        return self.option.__str__()


# To VTA: Add comments on this too.
class Review(models.Model):
    student = models.ForeignKey(BotUser)
    quiz = models.ForeignKey(Quiz)
    score = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.student.__str__() + ', {0}'.format(self.score)


class AttemptedData(models.Model):
    student = models.ForeignKey(BotUser)
    quiz = models.ForeignKey(Quiz)
    number_attempted = models.IntegerField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.student.__str__() + ' has completed {0} questions in quiz '.format(self.number_attempted) + '.'
