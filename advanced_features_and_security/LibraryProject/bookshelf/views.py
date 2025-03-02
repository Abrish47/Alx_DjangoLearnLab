from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from .models import CustomUser
from .models import Book
from .forms import BookForm 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookshelf:login')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

# Permission-protected views
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):  
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Book.objects.create(title=title)
        return redirect('bookshelf:book_list') 
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('bookshelf:book_list')  
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshelf:book_list')  
    return render(request, 'bookshelf/delete_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def example_form_view(request):
    if request.method == 'POST':
        input_data = request.POST.get('example_input', '').strip()
        # Example safe handling (no direct SQL, just logging for demo)
        print(f"User input: {input_data}")  # Replace with actual logic
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/form_example.html')
