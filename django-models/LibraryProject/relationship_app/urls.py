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
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
     # Add book path
    path('add_book/', views.add_book, name='add_book'),

    # Edit book path with primary key (pk) as a dynamic part of the URL
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),

    # Delete book path with primary key (pk)
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
