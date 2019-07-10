from django.urls import path, re_path
from django.conf.urls import include
from Usuarios import views

urlpatterns = [
    re_path(r'^$', views.UsuariosList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.UsuariosDetails.as_view()),
]