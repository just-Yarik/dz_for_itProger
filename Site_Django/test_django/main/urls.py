from django.urls import path
from . import views 
urlpatterns = [
    path('', views.golovna, name='golovna'),
    path('konta', views.kontakty, name='kontakty'),
    path('regist', views.register, name='register')
]