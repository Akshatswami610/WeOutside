from django.contrib import admin
from .models import *

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('party_id', 'party_name')
    search_fields = ('party_id', 'party_name')

@admin.register(Partyposter)
class PartyposterAdmin(admin.ModelAdmin):
    list_display = ('poster_id', 'party')
    search_fields = ('poster_id', 'party')
