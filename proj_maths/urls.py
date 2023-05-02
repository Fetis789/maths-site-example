"""proj_maths URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('words-list', views.words_list),
    path('lesson-materials', views.lesson_list),
    path('add-word', views.add_word),
    path('add-lesson', views.add_lesson),
    path('delete-word', views.delete_word),
    path('delete-lesson', views.delete_lesson),
    path('send-word', views.send_word),
    path('send-lesson', views.send_lesson),
    path('project-info', views.info),
    path('stats', views.show_stats)
]
