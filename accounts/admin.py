from django.contrib import admin
from .models import User, Newsletter
from import_export.admin import ImportExportModelAdmin

# Registre suas modelos aqui.

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ['id','username', 'name','date_of_birth']


@admin.register(Newsletter)
class NeewsletterAdmin(ImportExportModelAdmin):
    list_display = ['user', 'email']

