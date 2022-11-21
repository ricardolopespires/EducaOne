from django.views.generic import View, ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.





#----------------------------------- Courses Index ---------------------------------------------------------------


class Courses_List_View(View):


	def get(self, request):
		return render(request, 'courses/index/list.html')



class Courses_Detail_View(View):


	def get(self, request):
		return render(request, 'courses/index/detail.html')




#----------------------------------- End Courses Index -----------------------------------------------------------
#----------------------------------- Courses Students ------------------------------------------------------------





#----------------------------------- End Courses Students ------------------------------------------------------------
#----------------------------------- Courses Management --------------------------------------------------------------

class Management_Course_List_View(LoginRequiredMixin, View):


	def get(self, request):

		return render(request, 'courses/management/list.html')



#----------------------------------- End Courses Management ------------------------------------------------------------