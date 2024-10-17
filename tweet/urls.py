from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),  # Handles listing all tweets
    path('create/', views.tweet_create, name='tweet_create'),  # Handles creating a new tweet
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),  # Handles editing an existing tweet
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  # Handles deleting a tweet
    path('register/', views.register, name='register'), 
]
