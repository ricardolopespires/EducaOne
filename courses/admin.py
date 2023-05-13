from .models import  Categorie, SubCategorie, Subject, Course, Module, Level, Analytics
from .models import  Promotion, Learn, Requirement, Lesson, Author
from .models import  Review, Visualizacao, Favorito, Like
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin





@admin.register(Categorie)

class AdminCategories(ImportExportModelAdmin):
	list_display = ['name','icon']


@admin.register(SubCategorie)

class AdminSubCategories(ImportExportModelAdmin):
	list_display = ['name','categorie']
	search_fields = ['name']


@admin.register(Subject)

class AdminSubCategories(ImportExportModelAdmin):
	list_display = ['title']


@admin.register(Level)
class LevelAdmin(ImportExportModelAdmin):
	list_display = ['title']


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
	list_display = ['name']



@admin.register(Course)
class AdminSubCategories(ImportExportModelAdmin):
	list_display = ['title','status','tipo','categorie','level']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('title',)}
	inlines = [ModuleInline]


@admin.register(Lesson)
class AdminLesson(ImportExportModelAdmin):
	list_display = ['id','module','order', 'title','concluded']
	list_filter = ['module']



@admin.register(Review)
class CategoriaAdmin(ImportExportModelAdmin):
    list_display = ['course','user','rate']
    search_fields =['course']



@admin.register(Visualizacao)
class CategoriaAdmin(ImportExportModelAdmin):
    list_display = ['course','ultimo','date','total']
    search_fields =['course']


@admin.register(Favorito)
class CategoriaAdmin(ImportExportModelAdmin):
    list_display = ['course','user']



@admin.register(Promotion)
class PromotionAdmin(ImportExportModelAdmin):
    list_display = ['course','inicio','termino','is_active']


@admin.register(Learn)
class AdminLearn(ImportExportModelAdmin):
	list_display = ['title','course']



@admin.register(Requirement)
class AdminLearn(ImportExportModelAdmin):
	list_display = ['title','course']



@admin.register(Analytics)
class AdminAnalytics(ImportExportModelAdmin):
	list_display = ['course','lesson', 'views','complete_per']

