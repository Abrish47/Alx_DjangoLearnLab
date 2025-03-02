from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
