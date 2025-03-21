# Django Blog Post Management Documentation

This document details the blog post management features in the `django_blog` project, enabling CRUD (Create, Read, Update, Delete) operations for the `Post` model.

## Overview
The blog post system allows:
- All users (authenticated or not) to view a list of posts and individual post details.
- Authenticated users to create new posts.
- Post authors to edit or delete their own posts.
Built using Django’s class-based views, forms, and templates.

## Components

### 1. Models
- **Post** (`blog/models.py`):
  - Fields: `title` (CharField), `content` (TextField), `published_date` (DateTimeField, auto-set), `author` (ForeignKey to `User`).
  - Defined in Task 0.

### 2. Forms
- **PostForm** (`blog/forms.py`):
  - A `ModelForm` for `Post`.
  - Fields: `title`, `content`.
  - Widgets: Adds placeholders for user-friendly input.
  - Author is set automatically in the view.

### 3. Views
- **PostListView** (`blog/views.py`):
  - Displays all posts.
  - Template: `blog/post_list.html`.
  - Accessible to all.
- **PostDetailView**:
  - Shows a single post’s details.
  - Template: `blog/post_detail.html`.
  - Accessible to all.
- **PostCreateView**:
  - Form to create posts (login required via `LoginRequiredMixin`).
  - Template: `blog/post_form.html`.
  - Sets `author` to the current user.
- **PostUpdateView**:
  - Form to edit posts (login required + author check via `UserPassesTestMixin`).
  - Template: `blog/post_form.html`.
- **PostDeleteView**:
  - Deletes a post (login required + author check).
  - Template: `blog/post_confirm_delete.html`.
  - Redirects to `/posts/`.

### 4. URLs
- Defined in `blog/urls.py`:
  - `/posts/`: `PostListView` (name='post_list')
  - `/posts/new/`: `PostCreateView` (name='post_create')
  - `/posts/<int:pk>/`: `PostDetailView` (name='post_detail')
  - `/posts/<int:pk>/edit/`: `PostUpdateView` (name='post_update')
  - `/posts/<int:pk>/delete/`: `PostDeleteView` (name='post_delete')

### 5. Templates
- **post_list.html**: Lists posts with titles, snippets, and author/date; “New Post” link for logged-in users.
- **post_detail.html**: Full post content with edit/delete links for the author.
- **post_form.html**: Form for creating/editing posts.
- **post_confirm_delete.html**: Deletion confirmation.

## Usage
1. **View Posts**:
   - Visit `/posts/` to see all posts.
   - Click a title to view details (e.g., `/posts/1/`).
2. **Create a Post**:
   - Log in, go to `/posts/new/`, fill out the form, submit.
3. **Edit a Post**:
   - As the author, go to `/posts/<pk>/edit/`, update, submit.
4. **Delete a Post**:
   - As the author, go to `/posts/<pk>/delete/`, confirm deletion.

## Permissions
- **Public Access**: `/posts/` and `/posts/<pk>/` are viewable by all.
- **Authenticated Only**: Creating posts requires login (`/posts/new/`).
- **Author Only**: Editing/deleting restricted to the post’s author via `UserPassesTestMixin`.
- **Redirect**: Unauthenticated users are sent to `/login/` (set in `settings.py`).

## Data Handling
- **Author**: Automatically set to the logged-in user on creation.
- **Published Date**: Auto-set to the current time (`auto_now_add=True`).