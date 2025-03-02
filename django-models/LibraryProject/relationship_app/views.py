from django.shortcuts import render
from django.views.generic.detail import DetailView  
from .models import Book
from .models import Library
from .models import UserProfile
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginOut
from django.contrib.auth.decorators import user_passes_test


# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Function-based view: User registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect to book list after success
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Class-based view: Login
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True  # Redirect logged-in users

# Class-based view: Logout (using TemplateView for custom logout page)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
# Role check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Existing views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role-based views
@user_passes_test(is_admin, login_url='/relationship/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@user_passes_test(is_librarian, login_url='/relationship/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@user_passes_test(is_member, login_url='/relationship/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})
