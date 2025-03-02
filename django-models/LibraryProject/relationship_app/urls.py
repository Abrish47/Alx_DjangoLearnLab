from django.urls import path
from . import views
from .views import list_books

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: List all books
    path('books/', views.list_books, name='list_books'),
    # Class-based view: Library details by ID
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
