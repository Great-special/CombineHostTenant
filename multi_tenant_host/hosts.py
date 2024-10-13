from django_hosts import patterns, host


host_patterns = patterns(
    '', 
    host('', 'core.urls', name='app'), # main domain
    host('blog', 'blogs.urls', name='blog'), # blog subdomain
    host('account', 'accounts.urls', name='account'), # accounts subdomain
    host(r'(?!account|blog)\w+', 'multi_tenant_host.urls', name='tenant') # tenants subdomain by checking if is NOT "accounts" or "blog"
)