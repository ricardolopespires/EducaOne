from django.views.generic import View, ListView, TemplateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from datetime import date
from .models import User

# Create your views here.




def loggin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                if user.groups.filter(name='Administrador').exists() == True:
                    login(request,user)
                    #Redirect to success page.
                    form = LoginForm()                
                    return redirect('management:manager')                
                else:
                    login(request,user)
                    #Redirect to success page.
                    form = LoginForm()                
                    return redirect('index')
                    

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


User = get_user_model()



class Register_User_View( View):


    def post(self, request):
        if request.method == 'POST':
        
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('pass1')

            print(username)
            print(email)
            print(password)

            new_user = User.objects.create_user(username, email, password)
            messages.success(request,'O seu usuário foi criado com sucesso!!!!')
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'registration/register.html',{'form':form})



   
def profile_users(request):
    profiles = User.objects.all()    
    
    return render(request, 'profile/profile.html',{'profiles':profiles})


def profile_details(request, pk):
    user_profile = get_object_or_404(User, id = pk)     

    return render(request, 'profile/details.html',{'user_profile':user_profile, })












#---------------------------------------- PROFILE ----------------------------------------------------


class Profile_View(LoginRequiredMixin, View):

    def get(self, request, usuario_id):
        return render(request, 'profile/index.html')