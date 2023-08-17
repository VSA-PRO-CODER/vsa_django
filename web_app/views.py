# appname/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import authenticate
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from .models import Reg_Data, Salary 
from .forms import Reg_Data_Form
from django.conf import settings
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        context = {}
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context = {'error':'invalid username and password'}
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        cpassword = request.POST.get('Cpassword')
        if password == cpassword:
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('home')
        else :
            context = {'error':'incorrect username and password'}
            return render(request,'login.html',context)
    else :
        return render(request,'login.html')
def logoutPage(request):
    logout(request)
    return redirect('home')
def home(request):
    context = {}
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('msg')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        subject = f'a user "{name}" tryna contact'
        send_mail(subject,message,from_email,recipient_list)
        return redirect('home')
    return render(request,'contact.html')
@login_required(login_url='Login')
def user_register(request):
    if request.method == 'POST':
        form = Reg_Data_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = Reg_Data_Form()
    
    return render(request, 'regsiter.html', {'form': form})
def UpdateUser(request,pk):
    data = Reg_Data.objects.get(ID=pk)
    form = Reg_Data_Form(instance=data)
    if request.method == 'POST':
        form = Reg_Data_Form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'regsiter.html',context)
    
@login_required(login_url='Login')
def Usalary(request):
    context = {}
    if request.method == 'POST':
        ID = request.POST.get('ID')
        salary = request.POST.get('salary')
        Salary.objects.create(ID=ID,salary=salary)
        return redirect('home')
    return render(request,'salary.html',context)
@login_required(login_url='Login')
def feed(request):
    data = Salary.objects.all()
    context = {'data':data}
    return render(request,'resent.html',context)

def users(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    Data = Reg_Data.objects.filter(
        Q(name__icontains=q) |
        Q(ID__icontains=q) 
        )
    context = {'Data':Data}
    return render(request,'users.html',context)
@login_required(login_url='Login')
def profile(request,pk):
    data = Reg_Data.objects.get(ID=pk)
    context = {'data':data}
    return render(request,'profile.html',context)
def deluser(request,pk):
    Reg_Data.objects.get(ID=pk).delete()
    return HttpResponse("objects deleted successfully.")
def delsalary(request,pk):
    Salary.objects.get(ID=pk).delete()
    return HttpResponse("objects deleted successfully.")
    
