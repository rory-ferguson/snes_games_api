from django.contrib.auth.models import User
from rest_framework import serializers
from games.models import Game, Publisher, Developer


class GameSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    publisher = serializers.SlugRelatedField(queryset=Publisher.objects.all(), slug_field='publisher')
    developer = serializers.SlugRelatedField(queryset=Developer.objects.all(), slug_field='developer')

    class Meta:
        model = Game
        depth = 1
        fields = ('url', 'title', 'image', 'publisher', 'developer', 'release', 'region',)
