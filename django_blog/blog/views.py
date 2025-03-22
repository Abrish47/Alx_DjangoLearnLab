from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .models import Comment
from django.db.models import Q

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

def home(request):
    return render(request, "blog/home.html")

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm  # Use PostForm instead of fields

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm  # Use PostForm instead of fields

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/post/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])  # Changed from post_id to pk
        return super().form_valid(form)
    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
class PostByTagListView(ListView): 
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    def get_queryset(self):
        tag = self.kwargs["tag_slug"] 
        return Post.objects.filter(tags__name__in=[tag])
    
def search(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    return render(request, "blog/search_results.html",{"posts": posts, "query": query})
