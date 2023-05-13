from django.urls import path
from . import views



app_name = 'blog'




urlpatterns = [

	path('list/post/',views.Blog_List_View.as_view(), name = 'list'),





]