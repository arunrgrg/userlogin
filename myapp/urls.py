
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
   path('',views.Reg,name='reg'),
   path('signin/',views.Signin,name='signin'),
   path('user/',views.User,name='user'),

   path('deleteuser/<int:userid>/',views.DeleteUser,name='deleteuser'),
   path('logout',views.logout,name='logout'),
   
]



