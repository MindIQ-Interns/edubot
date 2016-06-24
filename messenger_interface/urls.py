from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^0802c8786a09ae44a56a072d9d9a5e5da3172747df3d39e915/', views.MessengerView.as_view(), name='messenger_view'),
]