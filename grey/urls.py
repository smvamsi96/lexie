from django.urls import path
from . import views

urlpatterns = [
    path('', views.grey_index, name='grey_index'),
    path('file_class/<int:file_class_id>/', views.show_file_class, name='show_file_class'),
    ]
