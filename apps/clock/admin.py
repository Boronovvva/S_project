from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(clock)
class clockAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_filter = ['id', 'title', 'description', 'date']