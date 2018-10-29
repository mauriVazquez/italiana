from django.conf.urls import url, include

urlpatterns = [
    url(r'^adminactions/', include('adminactions.urls')),
]
