from django.urls import path
from . import views



app_name = 'courses'




urlpatterns = [



	#----------------------------------- Courses Index ----------------------------------

	path('list/',views.Courses_List_View.as_view(), name = 'list'),
	path('<course_id>/detail/',views.Courses_Detail_View.as_view(), name = 'detail'),
	path('<course_id>/released/',views.Released_Course_View.as_view(), name = 'released_course'),
	path('<course_id>/review/',views.Course_Review_Student.as_view(), name = 'review'),
	path('course/<course_id>/learn/create/',views.Learn_Create_Course.as_view(), name = 'learn'),
	path('course/<course_id>/requirement/create/',views.Requirement_Create_Course.as_view(), name = 'requirement'),
	path('lesson/list/',views.lessonList, name = 'lesson_list'),
	path('lesson/<int:pk>/update/',views.lessonUpdate, name = 'lesson_update'),
	path('lesson/<int:pk>/detail/',views.lessonDetail, name = 'lesson_detail'),
	path('lesson/analytics/list/',views.analyticsList, name = 'lesson_analytics'),
	path('lesson/analytics/<int:pk>/update/',views.analyticsUpdate, name = 'analytics_update'),




	#----------------------------------- Courses Students ---------------------------------






	#----------------------------------- Courses Management -------------------------------

	path('dashboard/list/courses/',views.Management_Course_List_View.as_view(), name = 'list_courses'),
	path('dashboard/create/courses/',views.Create_Course_View.as_view(), name = 'create_courses'),

	path('dashboard/create/<course_id>/module/',views.Module_Create_Course.as_view(), name = 'module'),
	path('dashboard/module/<module_id>/list/',views.Course_Module_Lesson.as_view(), name = 'list_module'),
	path('dashboard/module/<module_id>/delete/',views.Course_Module_Delete.as_view(), name = 'delete_module'),
	path('dashboard/module/<module_id>/lesson/',views.Lesson_List_View.as_view(), name = 'list_lesson'),
	path('dashboard/lesson/<module_id>/create/',views.Lesson_Create_View.as_view(), name = 'create_lesson'),
	path('dashboard/lesson/<lesson_id>/videos/',views.Lesson_Video_List.as_view(), name = 'video_lesson'),
	path('lesson/<lesson_id>/release/videos',views.Released_Lesson_Video.as_view(), name = 'release_lesson'),
	path('dashboard/lesson/<lesson_id>/delete/',views.Delete_Lesson_Video.as_view(), name = 'delete_lesson'),

	path('lesson/<module_id>/content/create/',
            views.Lesson_Create_Content.as_view(), name='lesson_content_create'),









]