# games/models.py
from django.db import models


class Developer(models.Model):
    developer = models.CharField(max_length=200)

    def __str__(self):
        return self.developer


class Publisher(models.Model):
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.publisher


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    publisher = models.ForeignKey('Publisher', related_name='games', on_delete=models.CASCADE)
    developer = models.ForeignKey('Developer', related_name='games', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='games', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title