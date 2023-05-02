from django.contrib import admin
from .models import Purposes


@admin.register(Purposes)
class PurposesAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'deadline', 'date_complete', 'what_is_do')
    search_fields = ('name',)
    list_filter = ('deadline', 'date_complete', 'user',)
    empty_value_display = '-пусто-'
