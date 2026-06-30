from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','is_staff')
    search_fields = ('name', 'email', 'phone_number','is_staff')
    list_filter = ('name', 'email', 'phone_number','is_staff')
