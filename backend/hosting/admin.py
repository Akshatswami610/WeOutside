from django.contrib import admin
from .models import *


class PartyPosterInline(admin.TabularInline):
    model = PartyPoster
    extra = 1


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = (
        "party_name",
        "user",
        "party_category",
        "party_date",
        "party_time",
        "max_members",
        "fee",
        "gender",
    )

    list_filter = (
        "party_category",
        "gender",
        "party_date",
    )

    search_fields = (
        "party_name",
        "location",
        "description",
        "user__username",
    )

    ordering = (
        "party_date",
        "party_time",
    )

    inlines = [PartyPosterInline]


@admin.register(PartyPoster)
class PartyPosterAdmin(admin.ModelAdmin):
    list_display = (
        "poster_id",
        "party",
    )