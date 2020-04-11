from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as views2
from . import views
urlpatterns=[
    path('register/',views.register,name="nregister"),
    path('login/', views2.LoginView.as_view(template_name="login.html"), name="nlogin"),
    path('logout/', views2.LogoutView.as_view(template_name="logout.html"), name="nlogout"),
    path('profile/',views.profile,name="nprofile"),
]