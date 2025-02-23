from django.urls import path  
from django.contrib.auth.views import LoginView, LogoutView  
from .views import admin_view
from . import views  
from .views import user_login, user_logout, register

urlpatterns = [
    path("register/", views.register, name="register"), 
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("login/", user_login, name="login"),
    path("admin-dashboard/", admin_view, name="admin_dashboard"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]
