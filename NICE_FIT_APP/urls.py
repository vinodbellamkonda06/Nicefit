from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home', views.home),
    url(r'singup/', views.singup),
    url(r'user/', views.list_of_users),

]