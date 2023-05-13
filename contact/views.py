from courses.models import Categorie, SubCategorie, Course
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from .core import calculo_entre_datas
from django.contrib import messages
from .forms import Contact_Form
from django.urls import reverse
from .models import Contact



# Create your views here.






class Contact_Template_View(View):


	def get(self, request):
		categories = Categorie.objects.all().order_by('id')
		subcategoria = SubCategorie.objects.all()

		return render(request,'contact/form.html',{
            
            'categories':categories,
            'subcategorias':subcategoria,            

            })


	def post(self, request):

		if request.method == 'POST':

			form = Contact_Form(request.POST)			
			if form.is_valid():
				form.save(commit = False)
				email = form.cleaned_data['email']

				if Contact.objects.filter( email = email).exists():

					dias = calculo_entre_datas()
					if dias.hours <= 0:
						form.save()
						messages.success(request,'Obrigado pelo seu Email, Entraremos em contato nas proxima 24 Horas')
						return HttpResponseRedirect(reverse('index'))
					else:
						messages.info(request,"Obs....., O seu email já  foi cadastrado no sistema, logo entraremos em contato.")
						return HttpResponseRedirect(reverse('index'))
				else:					
					form.save()
					messages.success(request,'Obrigado pelo seu Email, Entraremos em contato nas proxima 24 Horas')
					return HttpResponseRedirect(reverse('index'))
			else:
				messages.error("Obs....., Algum dos dados informado está errado, por favor verificar")
				return HttpResponseRedirect(reverse('contact:form'))



