from django.urls import path
from app import views;

urlpatterns = [
    path('',views.register,name="register"), 
    path('home/',views.home,name="home"),
    path('login/',views.login, name="login"),  
    path('logout/',views.logout,name="logout"),
    path('query',views.query,name="query"),
    path('edit/<int:x>',views.edit,name="edit"),
    path('update/<int:x>',views.update,name="update" ),
    path('delete/<int:x>/<str:y>',views.delete,name="delete"),
    ]