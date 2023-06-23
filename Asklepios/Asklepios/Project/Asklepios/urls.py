from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('upload_page',views.upload_page, name='upload_page'),
    path('register',views.register,name='register')
    
] 