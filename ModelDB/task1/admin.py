from django.contrib import admin

# Register your models here.
from .models import Buyer, Game

admin.site.register(Buyer)
admin.site.register(Game)