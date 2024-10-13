from django.urls import path
from .views import tenant_data

urlpatterns = [
    path('', tenant_data, name="tenant_dashboard"),
    path('settings', tenant_data, name="tenant_settings")
]

