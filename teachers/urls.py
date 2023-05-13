from django.urls import path
from . import views



app_name = 'teachers'




urlpatterns = [


	path('courses/list/',views.Teachers_manager_List_View.as_view(), name = 'list'),
    path('courses/<course_id>/detail/', views.Teachers_Course_Detail.as_view(), name ='detail'),
    path('teachers/<teacher_id>create/',views.Teacher_Instructor_Create.as_view(), name = 'create_teachers'),
 



]