# This file defines all of your app's urls
# Without this file you site won't work
from django.urls import path
# A . references the app
from . import views

# Before using this file, register this file settings.py( A Must )

urlpatterns = [
    path('', views.grey_index, name='grey_index'),
    path('file_class/<int:file_class_id>/', views.show_file_class, name='show_file_class'),
    path('upload_file/', views.upload_file, name='upload_file')
    ]

# name -> An alias for the route or link
# views. -> register the view function name
