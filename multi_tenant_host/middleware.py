from django.conf import settings
from django.http import Http404
from django_tenants.middleware.main import TenantMainMiddleware
from django.db.models.functions import Substr, StrIndex
from django.db.models import Value
from core.models import Client, Domain


class CustomTenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        # Getting the host or domain
        host = request.get_host().lower()
        base_domain = host.split(':')[0]  # Strip out any port number

        print(f"Processing request for host: {host}")

        # Skip tenant processing for accounts and blog subdomains
        if base_domain.startswith(('account.', 'blog.')):
            print(f"Skipping tenant processing for {base_domain}")
            return None
        
        try:
            # Get the public schema (should always exist)
            public_tenant = Client.objects.get(schema_name='public')
            print(f"Public tenant domain: {public_tenant.domains.first().domain}")
            
            # Query domains directly and get a set of subdomains
            available_tenant_subdomains = set(
                Domain.objects.exclude(tenant__schema_name='public')
                              .values_list('domain', flat=True)
                              .annotate(subdomain=Substr('domain', 1, StrIndex('domain', Value('.')) - 1))
                              .distinct()
            )

            request_subdomain = base_domain.split('.')[0]
            print(f"Request subdomain: {request_subdomain}")
            
            available_tenant_subdomains.add(public_tenant.domains.first().domain)
            print(available_tenant_subdomains)
            if request_subdomain in available_tenant_subdomains:
                print(f"Subdomain '{request_subdomain}' matched a tenant.")
                return super().process_request(request)
            else:
                print(f"Subdomain '{request_subdomain}' not matched. Raising Http404.")
                raise Http404("No tenant for this subdomain")

        except Client.DoesNotExist:
            print("Public tenant not found in the database.")
            raise Http404("Public tenant not found")

        except Http404 as e:
            # Handle cases where the subdomain doesn't match a tenant
            if base_domain.startswith(('app.', '')):
                print(f"Skipping tenant processing for www or no subdomain in {base_domain}")
                return super().process_request(request)
            print("Http404 raised during tenant matching")
            raise

        except Exception as e:
            # Catch any other exceptions that occur and log them
            print(f"Unexpected error during tenant processing for {base_domain}: {e}")
            raise Http404("Error during tenant processing")
