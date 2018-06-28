from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from serial import views

urlpatterns = [
    url(r'^serial/$', views.SerialList.as_view(), name="serial.full_name"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
