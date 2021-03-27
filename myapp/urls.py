from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('add/', views.add_student),
    path('edit/<id>/', views.edit_student,name='edit'),
    path('delete/<id>/', views.delete_student, name='delete'),
    path('home/', views.home, name='home'),
]
