from django.urls import path
from . import views



app_name = 'teachers'




urlpatterns = [


	path('list/',views.Teachers_manager_List_View.as_view(), name = 'list'),



]