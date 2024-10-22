from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', 'role']  # Specify which fields to include
        # Or use fields = '__all__' to include all fields
        
        # Optionally, add widgets or field customizations
        widgets = {
            'password1': forms.PasswordInput(),

        }
        
        
