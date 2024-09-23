from django.urls import path
from app import views;

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"), 
    path('login/',views.login, name="login"),  
    path('rdata/',views.rdata,name="rdata"),    
]