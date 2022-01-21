
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
   path('',views.Reg,name='reg'),
   path('signin/',views.Signin,name='signin'),
   path('user/',views.User,name='user'),

   path('deleteuser/<int:userid>/',views.DeleteUser,name='deleteuser'),
   path('logout',views.logout,name='logout'),

   path('college/',views.clgreg,name='clg'),
   path('collegesign/',views.ClgSign,name='ClgSign'),
   path('collegede/',views.clgde,name='clgde'),      
   
   path('cldeleteuser/<int:userid>/',views.ClDeleteUser,name='cldeleteuser'),
   path('cllogout',views.cllogout,name='cllogout'),

   path('admin/',views.admin,name='admin'),
   path('deleteuserad/<int:userid>/',views.Deuser,name='deuser'),
   path('deleteclgad/<int:clgid>/',views.Declg,name='deuser'),

   
]



