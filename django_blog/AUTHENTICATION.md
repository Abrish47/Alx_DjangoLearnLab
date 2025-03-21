# Django Blog Authentication System Documentation

This document explains the user authentication system implemented in the `django_blog` project, covering registration, login, logout, and profile management.

## Overview
The authentication system allows users to:
- Register with a username, email, and password.
- Log in and out securely.
- View and update their profile (email).
It uses Django’s built-in authentication framework with custom extensions for registration and profile management.

## Components

### 1. Models
- **User Model**: Uses Django’s built-in `User` model (`django.contrib.auth.models.User`) for authentication.
- **Post Model**: Links posts to users via `author = ForeignKey(User, on_delete=models.CASCADE)` (defined in Task 0).

### 2. Forms
- **CustomUserCreationForm** (`blog/forms.py`):
  - Extends `UserCreationForm` to add a required `email` field.
  - Fields: `username`, `email`, `password1`, `password2`.
  - Handles user registration with secure password hashing.
- **ProfileForm** (`blog/forms.py`):
  - A `ModelForm` for the `User` model.
  - Fields: `email` (editable by users).
  - Used for profile updates.

### 3. Views
- **register** (`blog/views.py`):
  - Handles GET (displays form) and POST (creates user, logs in, redirects to home).
  - Template: `blog/register.html`.
- **LoginView** (`django.contrib.auth.views.LoginView`):
  - Built-in view for login.
  - Template: `blog/login.html`.
  - Redirects to home (`/`) on success.
- **LogoutView** (`django.contrib.auth.views.LogoutView`):
  - Built-in view for logout.
  - Template: `blog/logout.html`.
- **profile** (`blog/views.py`):
  - Secured with `@login_required`.
  - Handles GET (shows current email) and POST (updates email).
  - Template: `blog/profile.html`.
- **home** (`blog/views.py`):
  - Simple view for the homepage.
  - Template: `blog/home.html`.

### 4. URLs
- Defined in `blog/urls.py`:
  - `/`: `home` (name='home')
  - `/login/`: `LoginView` (name='login')
  - `/logout/`: `LogoutView` (name='logout')
  - `/register/`: `register` (name='register')
  - `/profile/`: `profile` (name='profile')
- Included in `django_blog/urls.py` via `path('', include('blog.urls'))`.

### 5. Templates
- **base.html**: Base template with navigation (Home, Login, Register; “Blog Posts” commented out).
- **home.html**: Welcome page, shows user status.
- **login.html**: Login form with error feedback.
- **register.html**: Registration form with error feedback.
- **logout.html**: Logout confirmation.
- **profile.html**: Displays username/email and update form.

### 6. Security
- **CSRF Protection**: All forms include `{% csrf_token %}` to prevent CSRF attacks.
- **Password Hashing**: Handled by Django’s `UserCreationForm` (uses PBKDF2 with SHA256).
- **Access Control**: `@login_required` on `profile` ensures only authenticated users can access it.

## User Interaction Flow
1. **Registration**:
   - Visit `/register/`, fill out the form, submit.
   - Auto-logged in and redirected to `/`.
2. **Login**:
   - Visit `/login/`, enter credentials, submit.
   - Redirected to `/` on success, error message on failure.
3. **Logout**:
   - Visit `/logout/`, see confirmation, click to log in again.
4. **Profile**:
   - Visit `/profile/` (must be logged in), update email, submit.
   - Page refreshes with new email.

## Testing Instructions
1. **Start Server**:
   - Run `python manage.py runserver` in `django_blog/`.
   - Base URL: `http://127.0.0.1:8000/`.
2. **Register**:
   - Go to `/register/`, create a user (e.g., username: "testuser", email: "test@example.com", password: "test1234").
   - Verify redirect to home and “Hello, testuser!” message.
3. **Login**:
   - Log out via `/logout/`, then go to `/login/`.
   - Test with correct and incorrect credentials.
4. **Logout**:
   - Log in, then visit `/logout/`.
   - Confirm logout message and home page updates.
5. **Profile**:
   - Log in, go to `/profile/`, change email (e.g., to "new@example.com").
   - Verify update persists after logout/login.
6. **Security**:
   - Check `{% csrf_token %}` in form templates.
   - In shell (`python manage.py shell`):
     ```python
     from django.contrib.auth.models import User
     user = User.objects.get(username="testuser")
     print(user.password)  # Should be hashed
     ```

## Setup Instructions
- Ensure Django is installed (`pip install django`).
- Project structure, models, and static/templates from Task 0 are in place.
- No additional configuration needed beyond Task 1 steps.

## Notes
- “Blog Posts” link in `base.html` is commented out until Task 2.
- Profile can be extended with a custom model (e.g., bio) if needed.