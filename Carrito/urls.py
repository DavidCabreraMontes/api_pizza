from django.urls import path, re_path
from django.conf.urls import include
from Carrito import views

urlpatterns = [
    re_path(r'^$', views.CarritoList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.CarritoListUser.as_view()),
]