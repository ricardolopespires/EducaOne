from courses.models import Promotion, Learn, Requirement, Module, Lesson, Review, Analytics
from courses.models import Categorie, SubCategorie, Subject, Level, Course
from django.views.generic.base import TemplateResponseMixin, View
from django.shortcuts import render, get_object_or_404, redirect
from .serializers import LessonSerializer, AnalyticsSerializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.forms.models import modelform_factory
from datetime import datetime, date, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .core import minutos, upload_file
from django.utils.text import slugify
from django.contrib import messages
from datetime import date, datetime
from django.shortcuts import render
from teachers.models import Teacher
from accounts.models import User
from django.urls import reverse
from .forms import  Lesson_Form
from django.apps import apps
from decimal import Decimal
from uuid import uuid4




#----------------------------------- Courses Index ---------------------------------------------------------------


class Courses_List_View(View):


	def get(self, request):

		courses = Course.objects.all()
		categories = Categorie.objects.all()
		subcategoria = SubCategorie.objects.all()
		level = Level.objects.all()
		gratis = Course.objects.filter(price = 0).count()
		pago = Course.objects.filter(price__gte = 1).count()

		return render(request, 'courses/course/list.html',{

			'courses':courses,
			'categories':categories,
			 'subcategorias':subcategoria,
			'level':level,
			'gratis':gratis,
			'pago':pago,

			})



class Courses_Detail_View(View):


	def get(self, request, course_id):

		course = get_object_or_404(Course, id = course_id)
		categories = Categorie.objects.all().order_by('id')		
		subcategoria = SubCategorie.objects.all()

		reviews = Review.objects.filter(course_id = course_id)
		analytics = Analytics.objects.filter(course_id = course.id).last()
		try:
			rating = float('{:.2f}'.format(reviews.aggregate(Avg("rate"))['rate__avg']))
		except:
			rating  = 0

		#Calculo das avaliações de 5 pontos
		rating_5 = reviews.filter(rate = 5).count()		

		#Calculo das avaliações de 4 e 4.5 pontos
		rating_4 = reviews.filter(rate = 4).count()		
		rating_45 = reviews.filter(rate = 4.5).count()
		rating_4 = rating_4 + rating_45

		#Calculo das avaliações de 3 e 3.5 pontos
		rating_3 = reviews.filter(rate = 3).count()		
		rating_35 = reviews.filter(rate = 3.5).count()
		rating_3 = rating_3 + rating_35

		#Calculo das avaliações de 2 e 2.5 pontos
		rating_2 = reviews.filter(rate = 2).count()		
		rating_25 = reviews.filter(rate = 2.5).count()
		rating_2 = rating_2 + rating_25


		#Calculo das avaliações de 1 e 1.5 pontos
		rating_1 = reviews.filter(rate = 1).count()		
		rating_15 = reviews.filter(rate = 1.5).count()
		rating_1 = rating_1 + rating_15
		


		#Se o curso tem promoção
		promotions = Promotion.objects.filter(Q(is_active = True),Q( course_id = course.id))



		#últimos cursos criados
		latest = Course.objects.filter(Q(created__gte=datetime.now())| Q(created__lte=datetime.now()))[:5]


		#itens em que os alunos vão aprender
		learn = Learn.objects.filter(course_id = course.id)

		#requisitos para aprender o curso
		requeriments = Requirement.objects.filter(course_id = course.id)


		#modulos do curso
		modules = Module.objects.filter(course_id = course.id)

		lessons = Lesson.objects.all()


		if Course.objects.filter(Q(id = course.id),Q(students = request.user.id)).exists():
			checkut_enroll = True
		else:
			checkut_enroll = None



		return render(request, 'courses/course/detail.html',{

			'checkut_enroll':checkut_enroll,
            'subcategorias':subcategoria,
            'requeriments':requeriments,
            'promotions':promotions,
            'categories':categories,
            'analytics':analytics,
            'rating_5':rating_5,
            'rating_4':rating_4,
            'rating_3':rating_3,
            'rating_2':rating_2,
            'rating_1':rating_1,
            'modules':modules,
            'lessons':lessons,
            'reviews':reviews,
            'rating':rating,
            'latest':latest,
            'course':course,
            'learn':learn,
            
                     		


			})




class Course_Review_Student(LoginRequiredMixin, View):

	def post(self, request, course_id):

		#informações do estudante
		student = get_object_or_404(User, id = request.user.id)

		#informações do course
		course = get_object_or_404(Course, id = course_id)

		#fazer requesições para buscar as demais informações da avaliação do estudante
		if request.method == 'POST':
			rating = request.POST.get('rating')
			title = request.POST.get('title')
			message = request.POST.get('message')

		

			#verificando se o estudante já fez a avaliação desse curso
			if Review.objects.filter(user_id = student.id).exists():

				messages.info(request, "Desculpe {}, mais você já fez avaliação de desse curso ")
				return HttpResponseRedirect(reverse('courses:detail', arg=[course_id]))
			else:

				Review.objects.get_or_create(

					user_id = student.id,
					course_id = course.id,
					title = title,
					message = message,
					rate = rating,


					)
				messages.success(request, "Obrigado {}, pela sua avaliação de desse curso ")
				return HttpResponseRedirect(reverse('courses:detail', args=[course_id]))








#----------------------------------- End Courses Index -----------------------------------------------------------
#----------------------------------- Courses Students ------------------------------------------------------------





#----------------------------------- End Courses Students ------------------------------------------------------------
#----------------------------------- Courses Management --------------------------------------------------------------

class Management_Course_List_View(LoginRequiredMixin, View):


	def get(self, request):

		return render(request, 'courses/manage/course/list.html')



class Create_Course_View(LoginRequiredMixin, View):


	def get(self, request):
		categorias = Categorie.objects.all()
		subjects = Subject.objects.all()
		niveis = Level.objects.all()

		return render(request, 'courses/manage/course/form.html', {

			'subjects':subjects,
			'categorias':categorias,
			'niveis':niveis,
			})



	def post(self, request):

		if request.method == 'POST':
			print('1º')

			codigo = str(uuid4())

			titulo = request.POST.get('titulo')
			categoria = request.POST.get('categoria')
			subjects = request.POST.getlist('subjects')
			descricao = request.POST.get('descricao')
			level = request.POST.get('level')
			linguagem = request.POST.get('linguagem')
			categoria = request.POST.get('categoria')
			capa = request.POST.get('image')			
			certificate = request.POST.get('certificate')
			price = str(request.POST.get('price')).replace(',','.')
			discount = str(request.POST.get('discount')).replace(',','.')

			if certificate == None:
				certificate = False
			else:
				certificate = True

			

			if Course.objects.filter(title = titulo).exists():
				messages.error(request, 'Ops...., O Curso com titulo {}, já foi adicionado no sistema'.format(titulo))
				return HttpResponseRedirect(reverse('courses:create_courses'))

			else:			
				usuario = get_object_or_404(User, id = request.user.id)

			
				
				c, create = Course.objects.get_or_create(

					
					owner_id = request.user.id, 
					title = titulo,
					categorie_id = categoria,
					info = descricao[:140],
					slug = slugify(titulo),
					overview = descricao,				
					publish = date.today(),
					status = "projeto",
					tipo = 'normal',
					level_id = level,
					popularity = 0,
					poster = capa,												
					linguagem = linguagem,    
					average_Rating = 0 ,				
					likes = 0,
					total_horas = '00:00:00',
					views =  0,
					price = Decimal(price),
					discount = Decimal(discount),
					certificate = certificate,
					)
				
				for x in subjects:
					subject = get_object_or_404(Subject, id = x)
					subject.course.add(c)
					c.subject.add(x)

				if usuario.teachers == False:
					usuario.teachers = True
					usuario.save()


				
				if Analytics.objects.filter(Q(course_id = c.id),Q(owner_id = request.user.id)).exists():
					print('Esse Curso já está adicionado')

				else:
					Analytics.objects.get_or_create(

						id = str(uuid4()),
						owner_id = request.user.id,
						course_id = c.id,					
						module = 0,
						lesson = 0,
						views = 0, 
						duration = timedelta(hours=int(0), minutes=int(0), seconds=int(0)),
						time = timedelta(hours=int(0), minutes=int(0), seconds=int(0)), 
						rating = 0 , 
						students = 0, 

						)
				messages.success(request, 'Parabéns, agora você está levando seu conhecimento para mais pessoas')					
				return HttpResponseRedirect(reverse('teachers:list'))



class Released_Course_View(LoginRequiredMixin, View):

	def get(self, request, course_id):

		if request.method == 'GET':
			
			course = get_object_or_404(Course, id = course_id)
			course.status = 'aprovado'
			course.save()

			messages.success(request, 'O curso {} foi liberado com sucesso'.format(course))
			return HttpResponseRedirect(reverse('teachers:list'))
		else:
			return render(request,'teachers/courses/list.html',{

				'courses':courses,

				})





class Module_Create_Course(LoginRequiredMixin, View):

	def get(self, request, course_id):
		course = get_object_or_404(Course, id = course_id)

		return render(request, 'courses/manage/module/form.html',{'course':course})


	def post(self, request, course_id):
		course = get_object_or_404(Course, id = course_id)

		if request.method == 'POST':
			#buscando os dados que foram digitado pelo usuário
			title = request.POST.get('title')
			description = request.POST.get('description')
			is_active = request.POST.get('is_active')

			if is_active == 'true':
				is_active = True
			else:
				is_active =  False


			if Module.objects.filter(Q(course_id = course.id), Q(title = title)).exists():
				messages.info(request, 'Obs...., {} o title para o course {} já foi cadastrado'.format(title, course.title))
				return HttpResponseRedirect(reverse('courses:module', args=[course_id]))

			else:
				#buscando o numero total de modulos criados para adicionar mais um (+1)
				order = Module.objects.filter(course_id = course.id).count() + 1

				Module.objects.get_or_create(


					id = str(uuid4()),
					course_id = course.id,
					title = title,
					order = order,
					description = description,
					is_active = is_active,

					)
				
				#pegando os dados de criação do modulo do curso
				analytics = get_object_or_404(Analytics, course_id = course.id)
				analytics.module += 1
				analytics.save()

				messages.success(request, 'O module {} foi adicionado com sucesso, você está pronto para criar as aulas desse modulo'.format(title))
				return HttpResponseRedirect(reverse('teachers:detail', args=[course_id]))



class Course_Module_Lesson(LoginRequiredMixin, View):

	def get(self, request, module_id):

		module = get_object_or_404(Module, id = module_id)
		course = get_object_or_404(Course, id = module.course.id)
		return render(request, 'courses/manage/list.html',{

			'module':module,
			'course':course,
			})


class Course_Module_Delete(LoginRequiredMixin, View):

	def get(self, request, module_id):

		module = get_object_or_404(Module, id = module_id)
		course = get_object_or_404(Course, id = module.course.id)

		return render(request, 'courses/manage/module/delete.html',{

			'module':module,
			'course':course,
			})


	def post(self, request, module_id):

		module = get_object_or_404(Module, id = module_id)
		course = get_object_or_404(Course, id = module.course.id)

		module.delete()

		messages.success(request, 'O module {}, foi excluido com success'.format(module))
		return HttpResponseRedirect(reverse('teachers:detail', args=[course.id]))


class Lesson_Module_Course(LoginRequiredMixin, View):

	def get(self, request, module_id):

		module = get_object_or_404(Module, id = module_id)
		course = get_object_or_404(Course, id = module.course.id)

		return render(request, 'courses/manage/module/lesson/list.html',{

			'module':module,
			'course':course,
			})



class Lesson_List_View(LoginRequiredMixin, View):

	def get(self, request, module_id):
		
		module = get_object_or_404(Module, id = module_id)
		course = get_object_or_404(Course, id = module.course.id)
		lessons = Lesson.objects.filter(Q(module_id = module.id))

	
		module.duration = Lesson.objects.filter(module_id = module.id).aggregate(tempo=Sum('duration'))["tempo"]
		module.save()
	
		released = Lesson.objects.filter(Q(module_id = module.id ), Q(is_active = True)).count()

		total = Lesson.objects.filter(module_id = module.id).count()

		if released == total:
			module.is_active = True
			module.save()
		else:
			module.is_active = False
			module.save()


		return render(request, 'courses/manage/module/list.html',{

			'course':course,
			'lessons':lessons,
			'module':module,
					 
			})


class Released_Lesson_Video(LoginRequiredMixin, View):

	def get(self, request, lesson_id):

		
		lesson = get_object_or_404(Lesson, id = lesson_id)
		lesson.is_active = True
		lesson.save()

		course = get_object_or_404(Course, id = lesson.module.course.id)
		module = get_object_or_404(Module, id = lesson.module.id)
		lessons = Lesson.objects.filter(module_id = module.id)

		return render(request,'courses/manage/module/list.html',{

				'course':course,
				'module':module,
				'lessons':lessons,

				})



class Delete_Lesson_Video(LoginRequiredMixin, View):

	def get(self, request, lesson_id):

		lesson = get_object_or_404(Lesson, id = lesson_id)
		course = get_object_or_404(Course, id = lesson.module.course.id)
		module = get_object_or_404(Module, id = lesson.module.id)
		lessons = Lesson.objects.filter(module_id = module.id)

		
		return render(request,'courses/manage/module/delete.html',{

			'course':course,
			'module':module,
			'lessons':lessons,

			})






class Lesson_Create_Content(LoginRequiredMixin, View):   


    def get(self, request, module_id,):
    	module = get_object_or_404(Module, id = module_id)
    	return render(request,'courses/manage/content/form.html',{'module':module})

    def post(self, request, module_id):
    	module = get_object_or_404(Module, id = module_id)

    	if request.method == 'POST':
    		form =Lesson_Form(request.POST, request.FILES)
    		if form.is_valid():
    			form.save(commit = False)
    			title = form.cleaned_data['title']
    			duration = form.cleaned_data['duration']   			

    			if Lesson.objects.filter(Q(module_id = module.id),Q(title = title)).exists():
    				messages.info(request, 'A video aula {}, do modulo {}, já foi adicionado no sistema'.format(title,  module.title))
    				return HttpResponseRedirect(reverse('courses:list_lesson', args=[module.id]))
    			else:
    				    				
    				#module.content.add(lesson_id)

    				analytics = get_object_or_404(Analytics, course_id = module.course.id )
    				analytics.lesson += 1
    				analytics.duration = minutos(analytics.duration, duration)
    				analytics.save()
    				form.save()

    				#adicionando mais uma lesson no modulo
    				lesson = Lesson.objects.filter(Q(module_id = module.id),Q(title = title)).last()
    				lesson.order =  Lesson.objects.filter(module_id = module.id).count() + 1
    				lesson.save()

    				if  Lesson.objects.filter(module_id = module.id).count() > 10:
    					module.course.status = 'analizando'
    					module.course.save()

    				module.content.add(lesson.id)


    				
    				messages.success(request, 'Parabéns. A video  aula {} foi adicionado com sucesso'.format(title))
    				return HttpResponseRedirect(reverse('courses:list_lesson', args=[module.id]))
    		else:
    			return HttpResponseRedirect(reverse('courses:list_lesson', args=[module.id]))


        




class Lesson_Create_View(LoginRequiredMixin, View):

	def get(self, request, module_id):

		modules = Module.objects.filter(id = module_id)
		module = get_object_or_404(Module, id = module_id)
		course = get_object_or_404(Course, id = module.course.id)
		return render(request, 'courses/management/module/lesson/create.html',{

			'modules':modules,
			'module':module,
			'course':course,
			})

	def post(self, request, module_id):

		module = get_object_or_404(Module, id = module_id)
		course = get_object_or_404(Course, id = module.course.id)

		if request.method == 'POST':

			title = request.POST.get('title')
			is_active = request.POST.get('is_active')

			if Lesson.objects.filter(Q(module_id = module_id),Q(title = title)).exists():
				messages.error(request, 'Obs... esse titulo ja foi adicionado')
				return HttpResponseRedirect(reverse('courses:create_lesson', args=[module.id]))

			else:

				if is_active == 'true':
					is_active = True
				else:
					is_active = False


				order = Lesson.objects.filter(Q(module_id = module_id),Q(title = title)).count() + 1

				Lesson.objects.get_or_create(

					module_id = module.id,
					title = title,
					order = order,					
					is_active = is_active,

					)
				messages.success(request, 'A nova aula do {} foi adicionado com sucesso'.format(module.title))
				return HttpResponseRedirect(reverse('teachers:detail', args=[course.id]))



class Lesson_Video_List(LoginRequiredMixin,View):

	def get(self, request, lesson_id):
		lesson = get_object_or_404(Lesson, id = lesson_id)

		return render(request, 'courses/manage/module/lesson/arquivos/video.html',{

			'lesson':lesson,
			

			})





class Learn_Create_Course(LoginRequiredMixin, View):


	def get(self, request, course_id):
		course = get_object_or_404(Course, id = course_id)

		return render(request, 'courses/manage/course/learn.html',{'course':course,})


	def post(self, request, course_id):
		course = get_object_or_404(Course, id = course_id)

		if request.method == 'POST':

			title = request.POST.get('title')

			if Learn.objects.filter(title = title).exists():
				
				messages.error(request, 'Obs... esse conhecimento já foi adicionado!!!!')
				return HttpResponseRedirect(reverse('teachers:detail', args=[course.id]))

			else:
				print('2º')
				Learn.objects.get_or_create(

					id = str(uuid4()),
					course_id = course_id,
					title = title,

					)
				messages.success(request, 'O novo conhecimento sobre o curso foi adicionado com sucesso')
				return HttpResponseRedirect(reverse('teachers:detail', args=[course_id]))








class Requirement_Create_Course(LoginRequiredMixin, View):


	def get(self, request, course_id):
		course = get_object_or_404(Course, id = course_id)

		return render(request, 'courses/manage/course/requeriments.html',{'course':course,})


	def post(self, request, course_id):
		course = get_object_or_404(Course, id = course_id)

		if request.method == 'POST':

			title = request.POST.get('title')

			if Requirement.objects.filter(title = title).exists():
				print('1º')
				messages.error(request, 'Obs... esse conhecimento já foi adicionado!!!!')
				return HttpResponseRedirect(reverse('teachers:detail', args=[course.id]))

			else:
				print('2º')
				Requirement.objects.get_or_create(

					id = str(uuid4()),
					course_id = course_id,
					title = title,

					)
				messages.success(request, 'O novo requisito sobre o curso foi adicionado com sucesso')
				return HttpResponseRedirect(reverse('teachers:detail', args=[course_id]))










#----------------------------------- End Courses Management ------------------------------------------------------------




#------------------------------------------------------- API COURSE ------------------------------------------------------




@api_view(['GET'])
def lessonList(request):
    lesson = Lesson.objects.all()
    serializer = LessonSerializer(lesson, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def lessonDetail(request, pk):
	lessons = Lesson.objects.get(id = pk)
	serializer = LessonSerializer(lessons, many=False)
	return Response(serializer.data)



@api_view(['POST'])
def lessonUpdate(request, pk):
	lesson = Lesson.objects.get(id=pk)
	serializer = LessonSerializer(instance=lesson, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)




@api_view(['GET'])
def analyticsList(request):
    analytics = Analytics.objects.all()
    serializer = AnalyticsSerializers(analytics, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def analyticsUpdate(request, pk):
	analytics = Analytics.objects.get(id = pk)
	serializer = AnalyticsSerializers(instance=analytics, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)