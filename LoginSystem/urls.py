from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = {
    path('', home, name='home'),
    path('login/', loginView, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutView, name='logout'),

    # path('moreAboutuser/',moreAboutuser,name='moreAboutuserPage')
}
