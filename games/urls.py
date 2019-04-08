# games/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from games import views

schema_view = get_schema_view(title='SNES Database API')

urlpatterns = [
    path('schema/', schema_view),
    path('games/', views.GameList.as_view(), name='game-list'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('publisher/', views.PublisherList.as_view(), name='publisher-list'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)