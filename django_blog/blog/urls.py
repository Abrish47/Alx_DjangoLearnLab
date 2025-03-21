from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:post_id>/comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('post/<int:post_id>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]