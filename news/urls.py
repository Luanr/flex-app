from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news import views

urlpatterns = [
    path('news/', views.NewsList.as_view()),
    path('news/<int:pk>/', views.NewsDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)