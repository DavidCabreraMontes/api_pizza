from django.urls import path, re_path
from django.conf.urls import include
from Pizzas import views

urlpatterns = [
    re_path(r'^$', views.PizzasList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.PizzasDetails.as_view()),
]