from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views





urlpatterns =[

    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', views.loggin, name = 'login'),  
    path('register/',views.Register_User_View.as_view(), name = 'register'),


    path('profile/<usuario_id>/',views.Profile_View.as_view(), name = 'profile'),
    
]