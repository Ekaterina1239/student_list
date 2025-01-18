from django.contrib import admin
from django.urls import path, include

from app.views import student_list_view, student_view

urlpatterns = [
    path('', student_list_view, name='student_list'),
    path('student/<str:slug>/', student_view, name='student')
]
