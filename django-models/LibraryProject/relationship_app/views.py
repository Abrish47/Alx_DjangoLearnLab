from django.contrib.auth.forms import UserCreationForm  # ✅ Ensure this is included!
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test 
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # ✅ Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})
    
def is_admin(user):  
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"  

@user_passes_test(is_admin)  
def admin_view(request):  
    return render(request, "relationship_app/admin_dashboard.html")

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # ✅ Uses Django's built-in form
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Automatically logs in the user
            return redirect("home")  # ✅ Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View to edit an existing book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})
