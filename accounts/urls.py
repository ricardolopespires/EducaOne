from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views





urlpatterns =[

   
    path('logout/',auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', views.loggin, name = 'login'),  
    path('register/',views.Register_User_View.as_view(), name = 'register'),


    path('profile/habilidades/<usuario_id>/',views.Profile_Habilidades_View.as_view(), name = 'habilidades'),
    path('profile/conquista/<usuario_id>/',views.Profile_Conquistas_View.as_view(), name = 'conquistas'),
    
]