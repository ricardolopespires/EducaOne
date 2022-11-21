from django.views.generic import View, ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.






#----------------------------------- Teachers Courses -----------------------------------------------------------

class Teachers_manager_List_View(LoginRequiredMixin, View):


	def get(self, request):
		return render(request, 'teachers/list.html')






#----------------------------------- End Teachers Courses -------------------------------------------------------