# games/models.py
from django.db import models


YEARS = (
    ("1991", "1991"), ("1992", "1992"), ("1993", "1993"), ("1994", "1994"), ("1995", "1995"), ("1996", "1996"), ("1997", "1997"), ("1998", "1998"), ("2017", "2017"),
)

REGIONS = (
	("PAL", "PAL"),
)

class Developer(models.Model):
    developer = models.CharField(max_length=200)

    class Meta:
        ordering = ('developer',)

    def __str__(self):
        return self.developer


class Publisher(models.Model):
    publisher = models.CharField(max_length=200)

    class Meta:
        ordering = ('publisher',)

    def __str__(self):
        return self.publisher


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='', default=None, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, default='')
    publisher = models.ForeignKey('Publisher', related_name='games', on_delete=models.CASCADE)
    developer = models.ForeignKey('Developer', related_name='games', on_delete=models.CASCADE)
    release = models.CharField(max_length=4, choices=YEARS)
    region = models.CharField(max_length=20, choices=REGIONS)
    owner = models.ForeignKey('auth.User', related_name='games', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title