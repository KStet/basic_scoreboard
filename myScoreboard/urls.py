from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='user_login'),
    path('scoreboard', views.scoreboard, name='scoreboard'),    
    path('submit_flag', views.submit_flag, name='submit_flag'),
    path('signup', views.signup, name='signup'),
    path('teamcreation', views.teamcreation, name='teamcreation'),
]
