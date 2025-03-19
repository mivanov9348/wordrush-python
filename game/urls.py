from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('play/', views.play, name='play'),
    path('check-word/', views.check_word, name='check_word'),
    path('high-scores/', views.high_scores, name='high_scores'),
    path('clear-scores/', views.clear_scores, name='clear_scores'),
]
