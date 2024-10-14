from django.shortcuts import render
from django_tenants.utils import schema_context
from django.apps import apps
from .models import Client
# Create your views here.
UnitModel = apps.get_model('tenants', 'UnitModel')

def index_view(request):
    tenants_set = set()
    # Switch to the tenant's schema
    tenants = Client.objects.all().exclude(schema_name='public')
    print(tenants)
    # Switch to the tenant's schema
    for tenant in tenants:
        with schema_context(tenant.schema_name):
            # Perform queries on tenant-specific models
            tenants_set.update(UnitModel.objects.all())
    print(tenants_set)
    return render(request, 'core.html', {'tenants_data':tenants_set})






