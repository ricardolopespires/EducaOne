from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Contact, Newsletter

# Register your models here.





@admin.register(Contact)
class AdminContact(ImportExportModelAdmin):
	list_display = ['name','email','dias','resposta']
	search_fields = ['name']



@admin.register(Newsletter)
class AdminContact(ImportExportModelAdmin):
	list_display = ['name','email']
	search_fields = ['name', 'email']
