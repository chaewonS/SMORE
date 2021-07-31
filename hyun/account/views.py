from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, UserPaper
from django.contrib import auth

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        
        if user is not None :
            login(request, user)
            return redirect('home') 
        else: 
            return render(request, 'login.html', {'error' : '아이디와 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username = request.POST["username"],
            password = request.POST["password"],
            company_name = request.POST["company_name"],
            company_number = request.POST["company_number"],
            company_location = request.POST["company_location"],
        )
        user.save()
        for papers in request.FILES.getlist('company_paper'):
            paper = UserPaper()
            paper.companyFK = user
            paper.papers = papers
            paper.save()
        auth.login(request, user)
        return redirect('home')
    else:
        return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('home')

