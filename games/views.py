from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, status, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Game, Publisher, Developer
from .permissions import IsOwnerOrReadOnly
from .serializers import GameSerializer

import django_filters
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
def api_root(request):
    return Response({
        'games': reverse('game-list', request=request),
        'publisher': reverse('publisher-list', request=request),
        'developer': reverse('developer-list', request=request),
        'release': reverse('release-list', request=request),
        'title': reverse('title-list', request=request),
    })


class TitleList(APIView):
    def get(self, request):
        title = sorted(list(set(Game.objects.values_list('title', flat=True))))
        return Response(title)


class ReleaseList(APIView):
    def get(self, request):
        release = sorted(list(set(Game.objects.values_list('release', flat=True))))
        return Response(release)


class PublisherList(APIView):
    def get(self, request):
        publishers = [i.publisher for i in Publisher.objects.all()]
        return Response(publishers)


class DeveloperList(APIView):
    def get(self, request):
        developers = [i.developer for i in Developer.objects.all()]
        return Response(developers)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class GameFilter(django_filters.FilterSet):
    publisher = django_filters.CharFilter("publisher__publisher")
    developer = django_filters.CharFilter("developer__developer")

    class Meta:
        model = Game
        fields = ['id', 'release', 'region', 'publisher', 'developer', 'title']


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    # filter_fields = ('id', 'release', 'region', 'publisher', 'developer', 'title')
    filter_class = GameFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request):
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
