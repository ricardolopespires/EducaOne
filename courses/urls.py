from django.urls import path
from . import views



app_name = 'courses'




urlpatterns = [



	#----------------------------------- Courses Index ----------------------------------

	path('list/',views.Courses_List_View.as_view(), name = 'list'),
	path('detail/',views.Courses_Detail_View.as_view(), name = 'detail'),



	#----------------------------------- Courses Students ---------------------------------






	#----------------------------------- Courses Management -------------------------------

	path('management/list/',views.Management_Course_List_View.as_view(), name = 'management_list')





]