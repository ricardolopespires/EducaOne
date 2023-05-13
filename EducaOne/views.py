from courses.models import Categorie, SubCategorie, Course, Review, Analytics
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from contact.forms import Newsletter_Form
from django.views.generic import View
from contact.models import Newsletter
from django.http import JsonResponse
from django.contrib import messages
from contact.models import Contact
from teachers.models import Teacher
from django.urls import reverse




class Index_View(View):

    def get(self, request):

        destaques = Categorie.objects.filter(featured = True).order_by('id')[0:10]
        categories = Categorie.objects.all().order_by('id')
        courses = Course.objects.filter( status = 'aprovado').order_by('id')[0:10]
        subcategoria = SubCategorie.objects.all()

        instrutores = Teacher.objects.all()

        reviews = Review.objects.all()
        analytics = Analytics.objects.all()

        return render(request,'initial/index.html',{

         
            'subcategorias':subcategoria,            
            'instrutores':instrutores,
            'categories':categories,
            'destaques':destaques,
            'analytics':analytics,
            'reviews':reviews,
            'courses':courses,

            })



    def post(self, request):

        if request.method == 'POST':

            form = Newsletter_Form(request.POST)           
            if form.is_valid():
                form.save(commit = False)
                email = form.cleaned_data['email']

                if Newsletter.objects.filter( email = email).exists():

                    if Contact.objects.filter(email = email).exists():
                        contact = Contact.objects.filter(email = email).last()

                        if Newsletter.objects.filter(name = contact.name ).exists():
                            pass

                        else:
                            newsletter = Newsletter.objects.filter(email = email).last()
                            newsletter.name = contact.name.title()
                            newsletter.save()

                    messages.success(request,'Obrigado, mais seu email já está cadastrado.')
                    return HttpResponseRedirect(reverse('index'))
                
                else:
                    form.save()

                    if Contact.objects.filter(email = email).exists():
                        contact = Contact.objects.filter(email = email).last()

                        

                        newsletter = Newsletter.objects.filter(email = email).last()
                        newsletter.name = contact.name.title()
                        newsletter.save()                    

                    messages.success(request,'Obrigado por cadastra na nossa Newsletter')
                    return HttpResponseRedirect(reverse('index'))
            else:
                messages.error("Obs....., Algum dos dados informado está errado, por favor verificar")
                return HttpResponseRedirect(reverse('index'))



def filter_data(request):
    categories = request.GET.getlist('categories[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
   
    if price == ['pricefree']:
       course = Course.objects.filter(price=0)
    elif price == ['pricepaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['priceall']:
       course = Course.objects.all()
    elif categories:
       course = Course.objects.filter(categorie__id__in=categories).order_by('-id')      
    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Course.objects.all().order_by('-id')

    print(course)

    t = render_to_string('ajax/course.html', {'courses': course})

    return JsonResponse({'data': t})


class About_Template_View(View):

    def get(self, request):
        categories = Categorie.objects.all().order_by('id')
        subcategoria = SubCategorie.objects.all()
        return render(request, 'initial/about.html',{
            
            'categories':categories,
            'subcategorias':subcategoria,            

            })



    def post(self, request):

        if request.method == 'POST':

            form = Newsletter_Form(request.POST)           
            if form.is_valid():
                form.save(commit = False)
                email = form.cleaned_data['email']

                if Newsletter.objects.filter( email = email).exists():

                    if Contact.objects.filter(email = email).exists():
                        contact = Contact.objects.filter(email = email).last()

                        if Newsletter.objects.filter(name = contact.name ).exists():
                            pass

                        else:
                            newsletter = Newsletter.objects.filter(email = email).last()
                            newsletter.name = contact.name.title()
                            newsletter.save()

                    messages.success(request,'Obrigado, mais seu email já está cadastrado.')
                    return HttpResponseRedirect(reverse('about'))
                
                else:                   
                    form.save()

                    if Contact.objects.filter(email = email).exists():
                        contact = Contact.objects.filter(email = email).last()             

                        newsletter = Newsletter.objects.filter(email = email).last()
                        newsletter.name = contact.name.title()
                        newsletter.save()

                    messages.success(request,'Obrigado por cadastra na nossa Newsletter')
                    return HttpResponseRedirect(reverse('about'))

            else:
                messages.error("Obs....., Algum dos dados informado está errado, por favor verificar")
                return HttpResponseRedirect(reverse('about'))

