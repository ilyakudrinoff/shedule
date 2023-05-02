from django.contrib import admin
from .models import Contacts, PreMeeting, Relationship, Facts, Sectors


class PremeetingAdmin(admin.TabularInline):
    model = PreMeeting


class RelationshipAdmin(admin.TabularInline):
    model = Relationship


class FactsAdmin(admin.TabularInline):
    model = Facts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'status', 'krug',)
    search_fields = ('last_name',)
    list_filter = ('status', 'krug',)
    empty_value_display = '-пусто-'
    inlines = [
        PremeetingAdmin,
        RelationshipAdmin,
        FactsAdmin,
    ]


admin.site.register(Sectors)
