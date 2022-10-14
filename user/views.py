from django.shortcuts import render, redirect
from django.contrib import auth
from .models import UserModel

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        phonenumber = request.POST.get('phonenumber', None)
        adress = request.POST.get('adress', None)
        
        if password != password2:
            return render(request, 'signup.html')
        else:
            exist_user = UserModel.objects.filter(username=username)
            
            if exist_user:
                return render(request, 'signup.html') 
            else:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.phonenumber = phonenumber
                new_user.adress = adress                
                new_user.save()
                return redirect('/signin/')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password) 
        if me is not None:  
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/signin/') 
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:  
            return render(request, 'signin.html')


def home(request):
    return render (request, 'home.html')