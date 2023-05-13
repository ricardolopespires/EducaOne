from courses.models import Course, Categorie, Module, Lesson, Visualizacao, Analytics, Review
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from datetime import datetime, date
from accounts.models import User
from django.urls import reverse
from .models import Learning
from uuid import uuid4

data_atual = date.today()
today = datetime.now().date()


class Students_Template_View(View, LoginRequiredMixin):


    def get(self, request, student_id):
        student = get_object_or_404(User, id = request.user.id)
        courses = Course.objects.all()
        suggestion = Course.objects.filter(suggestion = True)
        categorias = Categorie.objects.all()[:7]
        return render(request, 'students/course/learning.html', {

            'student':student,
            'courses':courses,
            'categorias':categorias,
            'suggestion':suggestion,

            })




class Student_Course_List_View(View, LoginRequiredMixin):


    def get(self, request):
        student = get_object_or_404(User, id = request.user.id)
        courses = Course.objects.all()        
        categorias = Categorie.objects.all()[:7]
        students = Course.objects.filter( students = student.id)
        print(students)

        analytics = Analytics.objects.all()      

        try:
            learning = Learning.objects.all().last()

        except Learning.DoesNotExist:
            learning = None

        reviews = Review.objects.filter(user_id = request.user.id)        

        return render(request, 'students/course/list.html', {

            'student':student,
            'courses':courses,
            'categorias':categorias,            
            'students':students,
            'learning':learning,
            'analytics':analytics,
            'reviews':reviews,

       

            })



class Student_Course_Detail_View(View, LoginRequiredMixin):


    def get(self, request, course_id):
        course = get_object_or_404(Course, id = course_id)
        modulos = Module.objects.filter(course_id = course.id)
        lessons = Lesson.objects.all()

        views = Analytics.objects.filter(course_id  = course.id).aggregate(total=Sum('views'))['total']

        


        leacture = request.GET.get('leacture')

        if leacture == None:
            module = Module.objects.filter(course_id = course.id).first()
            video = Lesson.objects.filter(module_id = module.id ).first()
            concluded = Lesson.objects.filter(Q(module_id = video.module.id),Q(concluded = True)).count()


        else:
            video = Lesson.objects.filter(id = leacture).last()

            if video.is_active == False:
                module = Module.objects.filter(course_id = course.id).first()
                video = Lesson.objects.filter(module_id = module.id ).first()                
                messages.info(request, 'A video aula {} do modulo {}, ainda não está liberada'.format(video.title, video.module))
                return HttpResponseRedirect(reverse('students:detail', args =[course_id]))

        if Learning.objects.all().count() > 0:

            for learning in Learning.objects.all():

                Learning.objects.filter(id = learning.id).update(

                    course_id = course.id,
                    student_id = request.user.id, 
                    date = date.today(),  

                    )             

           
        else:

            Learning.objects.get_or_create(

                id = str(uuid4()),
                course_id = course.id,
                student_id = request.user.id, 
                date = date.today(),                  

                )

        


        if Course.objects.filter(id = course.id).exists():
            course =Course.objects.filter(id = course.id).last()
        else:
            return redirect('404')


        reviews = Review.objects.filter(course_id = course.id)
        
        return render (request, 'students/course/detail.html',{

            'course':course,
            'modulos':modulos,
            'lessons':lessons,
            'video':video,
            'reviews':reviews,

            })



class Checkout_Course_Student(View):

    def get(self, request, course_id):

        course = get_object_or_404(Course, id = course_id)        

        if course.price == 0:
            if request.user.is_authenticated:

                course.students.add(request.user.id)
                messages.success(request,'Parabéns você está matriculado no curso {}'.format(course.title))
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('index'))

        return render(request, 'students/checkout/documentation.html')



'''

class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super(StudentCourseDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.all()
        return context
'''