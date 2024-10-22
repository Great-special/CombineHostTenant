from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
from .forms import UserForm
from .models import CustomUser

def index_account(request):
    return render(request, 'accounts.html')



def user_register(request):
    template_name = 'forms.html'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, template_name=template_name, context={'form':form})
    
    return render(request, template_name=template_name, context={'form':form})



def login_user(request):
    template_name = 'login_form.html'
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('account_index')
    
    return render(request, template_name)

