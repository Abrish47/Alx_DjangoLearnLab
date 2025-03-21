from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]

class PostForm(forms.ModelForm):
    tags_widget_instance = TagWidget()
    class Meta:
        model = Post
        fields = ["title", "content","tags"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter post title"}),
            "content": forms.Textarea(attrs={"placeholder": "Write your post here"}),
            "tags": TagWidget(attrs={"placeholder": "e.g., python, django, blog"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"placeholder": "Add your comment here", "rows": 4}),
        }