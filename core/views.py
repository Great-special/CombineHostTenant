from django.shortcuts import render

# Create your views here.


def index_view(request):
    print()
    return render(request, 'core.html')

