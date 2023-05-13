from django.urls import path
from . import views



app_name = 'contact'




urlpatterns = [

		path('',views.Contact_Template_View.as_view(), name = 'form'),



]