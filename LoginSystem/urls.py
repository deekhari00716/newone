from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = {
    path('', home, name='home Page'),
    path('login/', loginView, name='login Page'),
    path('register/', register, name='register Page'),
    path('logout/', logoutView, name='logout Page'),

    # path('moreAboutuser/',moreAboutuser,name='moreAboutuserPage')
}