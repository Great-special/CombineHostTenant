from django.db import models

# Create your models here.


class UnitModel(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self) -> str:
        return self.title
    



class ClientUsers(models.Model):
    MANAGER = 'property_manager'
    AGENT = 'leasing_agent'
    SUPERVISOR = 'maintenance_supervisor'
    TECHNICIAN = 'maintenance_technician'
    
    
    USER_TYPE_CHOICES = [
        (MANAGER, 'Property Manager'),
        (AGENT, 'Leasing Agent'),
        (SUPERVISOR, 'Maintenance Supervisor'),
        (TECHNICIAN, 'Maintenance Technician')
    ]
    
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default=MANAGER)