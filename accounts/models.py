from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    REGULAR = 'regular'
    
    USER_TYPE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (REGULAR, 'Regular'),
    ]
    email = models.EmailField("email address", unique=True, help_text="Required.",
        error_messages={
            "unique": "A user with that email already exists.",
        },)
    role = models.CharField(max_length=15, choices=USER_TYPE_CHOICES, default=REGULAR)
    
    def is_admin(self):
        return self.role == self.ADMIN
    
    def is_manager(self):
        return self.role == self.MANAGER
    
    def is_regular(self):
        return self.role == self.REGULAR


class AdminProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="admin_profile")
    