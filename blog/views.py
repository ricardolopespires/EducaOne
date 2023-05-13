from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.utils.text import slugify
from django.contrib import messages
from datetime import date, datetime
from teachers.models import Teacher
from accounts.models import User
from django.urls import reverse
from decimal import Decimal
from uuid import uuid4

# Create your views here.







class Blog_List_View(LoginRequiredMixin, View):

	def get(self, request):
		return render(request, 'blog/list.html')