from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)', BotUserData.as_view()),
]