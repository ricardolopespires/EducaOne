from django.urls import path
from django.views.decorators.cache import cache_page
from . import views



app_name = 'students'




urlpatterns = [     
     path('learning/aula/<course_id>/detail/',views.Student_Course_Detail_View.as_view(), name = 'detail'),
     path('courses/', views.Student_Course_List_View.as_view(), name='student_course_list'),
     path('<course_id>/checkout/',views.Checkout_Course_Student.as_view(), name = 'checkout'),
    
    
    
]
