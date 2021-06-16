from django.contrib import admin
from .models import *

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'level')