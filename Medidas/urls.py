from django.urls import path, re_path
from django.conf.urls import include
from Medidas import views

urlpatterns = [
    re_path(r'^$', views.MedidasList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.MedidasListDetails.as_view()),
]