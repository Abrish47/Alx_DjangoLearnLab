from django.shortcuts import render  
from django.contrib.auth.decorators import user_passes_test  

# Function to check if the user is an Admin  
def is_admin(user):  
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"  

@user_passes_test(is_admin)  
def admin_view(request):  
    return render(request, "relationship_app/admin_dashboard.html")  # ✅ Create this template  
