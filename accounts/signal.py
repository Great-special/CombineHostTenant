# signals.py
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Create groups
    admin_group, created = Group.objects.get_or_create(name='Admins')
    manager_group, created = Group.objects.get_or_create(name='Managers')
    regular_group, created = Group.objects.get_or_create(name='Regular Users')

    # Assign permissions to groups
    content_type = ContentType.objects.get_for_model(CustomUser)
    
    # Example: add 'view_user' permission to admins and managers
    view_user_permission = Permission.objects.get(codename='view_customuser', content_type=content_type)
    admin_group.permissions.add(view_user_permission)
    manager_group.permissions.add(view_user_permission)
    
    # Example: add 'change_user' permission to admins only
    change_user_permission = Permission.objects.get(codename='change_customuser', content_type=content_type)
    admin_group.permissions.add(change_user_permission)
    
    # Save groups
    admin_group.save()
    manager_group.save()
    regular_group.save()
