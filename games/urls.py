from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from games import views

schema_view = get_schema_view(title='SNES Database API')

urlpatterns = [
    path('schema/', schema_view),
    path('games/', views.GameList.as_view(), name='game-list'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('developers/', views.DeveloperList.as_view(), name='developer-list'),
    path('release/', views.ReleaseList.as_view(), name='release-list'),
    path('title/', views.TitleList.as_view(), name='title-list'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)