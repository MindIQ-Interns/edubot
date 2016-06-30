from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portal/', include('portal.urls')),
    url(r'^messenger/', include('messenger_interface.urls')),
    url(r'^bot/', include('quiz_bot.urls')),
]
