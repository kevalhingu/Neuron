from django.contrib import admin
from .models import Game, Therapy, Story, Doctor

# Register your models here.
admin.site.register(Game)
admin.site.register(Therapy)
admin.site.register(Story)
admin.site.register(Doctor)