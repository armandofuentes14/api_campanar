from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.get_users, name='get_users'),
    path('requests/', views.get_requests, name='get_requests'),
    path('news/', views.get_news, name='get_news'),
    path('activities/', views.get_activities, name='get_activities'),
    path('predict/', views.get_prediction, name='get_prediction'),
     path('sentiment/', views.get_sentiment, name='get_sentiment'),
]