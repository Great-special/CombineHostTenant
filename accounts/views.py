from django.shortcuts import render

# Create your views here.


def index_account(request):
    return render(request, 'accounts.html')

