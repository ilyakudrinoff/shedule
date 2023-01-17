from django.contrib import admin
from .models import Purposes, Tasks, Friends


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('purpose', 'name', 'description', 'deadline', 'date_complete',)
    search_fields = ('name', 'purpose')
    list_filter = ('deadline', 'date_complete', 'purpose',)
    empty_value_display = '-пусто-'


@admin.register(Purposes)
class PurposesAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'deadline', 'date_complete',)
    search_fields = ('name',)
    list_filter = ('deadline', 'date_complete', 'user',)
    empty_value_display = '-пусто-'


@admin.register(Friends)
class FriendsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'link',)
    search_fields = ('name',)
