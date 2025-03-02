from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Author, Book, Library, Librarian, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
