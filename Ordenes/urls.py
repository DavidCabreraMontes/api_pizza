from django.urls import path, re_path
from django.conf.urls import include
from Ordenes import views

urlpatterns = [
    re_path(r'^$', views.OrdenesList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.OrdenesListAuthor.as_view()),
]