# Security Measures in LibraryProject

## Settings (settings.py)
- `DEBUG = False`: Prevents detailed error leaks in production.
- `SECURE_BROWSER_XSS_FILTER`: Enables browser XSS protection.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Stops MIME-type sniffing.
- `CSRF_COOKIE_SECURE` & `SESSION_COOKIE_SECURE`: Ensures HTTPS-only cookies.
- CSP via `django-csp`: Limits content sources to reduce XSS risk.

## CSRF Protection
- All forms (e.g., `create_book.html`, `form_example.html`) include `{% csrf_token %}` to prevent CSRF attacks.

## Views (views.py)
- Uses Django ORM (`Book.objects.all()`, `get_object_or_404`) to prevent SQL injection.
- Inputs validated and sanitized via `BookForm` (e.g., `clean_title` strips whitespace).

## Testing
- Test with DEBUG=False and HTTPS (local proxy if needed).
- Submit invalid inputs (e.g., `<script>`) to `create_book` to verify XSS protection.
- Attempt form submission without CSRF token to confirm rejection.
