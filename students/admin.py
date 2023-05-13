from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Learning
# Register your models here.



@admin.register(Learning)
class AdminSubCategories(ImportExportModelAdmin):
	list_display = ['id','student','course','date']
	search_fields = ['course', 'date','student']