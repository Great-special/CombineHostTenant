from django.shortcuts import render

# Create your views here.



def tenant_data(request):
    return render(request, "tenant_dash.html")