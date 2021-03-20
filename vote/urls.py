from django.contrib import admin
from django.urls import path, include
from vote import views

app_name = 'vote'

urlpatterns = [
    path('home', views.home, name='home'),
    path('vote', views.home, name='vote'),
    path('result', views.home, name='result'),
    path('answer', views.save_answer, name='save_answer'),
    path('api/get/quiz-list', views.get_quiz_list, name='get_quiz_list'),
    path("", views.user_info, name="user_info"),
]
