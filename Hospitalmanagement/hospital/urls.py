from django.contrib import admin
from django.urls import path,include
from hospital import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home,name='home'),
    path('p_book_appointment/',views.book_appointment),
    path('about/',views.about),
    path('contactus/',views.contact),
    path('user_logout/',views.user_logout),
    path('update_profile/',views.update_profile),
]
