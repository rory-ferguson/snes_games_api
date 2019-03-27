# games/admin.py
from django.contrib import admin
from . models import Game, Publisher, Developer


class GameAdmin(admin.ModelAdmin):
	pass
    # readonly_fields = ('highlighted',)


admin.site.register(Game, GameAdmin)
admin.site.register(Publisher)
admin.site.register(Developer)
