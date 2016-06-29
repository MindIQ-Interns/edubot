from django.contrib import admin
from models import *
from django.contrib.auth.models import User

admin.site.register(UserExtension)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(Review)
admin.site.register(Attempted)