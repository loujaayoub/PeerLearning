from django.shortcuts import redirect, render
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm,UserForm
from .models import User
from django.contrib.auth.decorators import login_required

def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist, please sign up ')
            return render(request,'login.html')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home") 
        else:
            messages.error(request, 'Email OR password is not correct')

    return render(request,'login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')



def register_page(request):

    if request.method == 'POST':

        email = request.POST.get('email').lower()
        try:
            user = User.objects.get(email=email)
        except:
            form = MyUserCreationForm(request.POST,request.FILES)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.email.lower()
                user.save()
                messages.success(request, 'Congrats, account has been created successfully :) log in Now ')
                return render(request,'login.html')
            else:
                messages.error(request, 'An error occurred during registration, please verify if you have retyped the same password !')
                return render(request,'signUp.html')

        messages.error(request, 'user with this email already exists , please use another email ')
        return render(request,'signUp.html')

    return render(request, 'signUp.html')

def forget_password(request):
    return render(request,'forgetPassword.html')




