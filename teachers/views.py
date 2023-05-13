from courses.models import Course, Learn, Requirement, Module, Lesson, Analytics
from django.views.generic import View, ListView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.urls import reverse
from .models import Teacher

from courses.core import minutos


#----------------------------------- Teachers Courses -----------------------------------------------------------

class Teachers_manager_List_View(LoginRequiredMixin, View):


	def get(self, request):

		courses = Course.objects.filter(owner_id = request.user.id )
		projetos = courses.filter(status__startswith = 'projeto').count()
		publicados = courses.filter(status__startswith = 'publicado').count()
		cancelados = courses.filter(status__startswith = 'cancelado').count()
		total = courses.count()

	

		return render(request, 'teachers/courses/list.html',{

			'courses':courses,
			'projetos':projetos,
			'publicados':publicados,
			'cancelados':cancelados,			
			'total':total,

			})

			
		




class Teachers_Course_Detail(LoginRequiredMixin, View):


	def get(self, request, course_id):
		course = get_object_or_404(Course, id = course_id)
		learn = Learn.objects.filter(course_id = course.id)
		requirements = Requirement.objects.filter(course_id = course.id)

		modules = Module.objects.filter(course_id = course.id)
		
		content = Module.objects.filter(course_id = course.id).aggregate(total_price=Sum('content'))["total_price"]

		course.duration = Module.objects.filter(course_id = course.id).aggregate(tempo=Sum('duration'))["tempo"]
		course.save()

		print(course)

		
		analytics = get_object_or_404(Analytics, course_id = course_id)

		print(analytics)
		
		lessons = Lesson.objects.all()	

		return render(request,'teachers/courses/detail.html',{

			'course':course,
			'learn':learn,
			'requirements':requirements,
			'modules':modules,
			'lessons':lessons,
			'analytics':analytics,


			})




class Teacher_Instructor_Create(LoginRequiredMixin, View):

	def post(self, request, teacher_id):
		print('criando')

		Teacher.objects.get_or_create(			
			name_id = teacher_ids,
			slug = slugify(request.user),
			expert = "",
			description = "",
			rating = 0, 
			reviews =  0,			
			is_active = True

			)
		return HttpResponseRedirect(reverse('teachers:list'))

#----------------------------------- End Teachers Courses -------------------------------------------------------