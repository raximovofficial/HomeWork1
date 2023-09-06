from django.urls import path
from .views import ThemeLessonsView

urlpatterns = [
    path('', ThemeLessonsView.as_view(), name='mavzular')

]