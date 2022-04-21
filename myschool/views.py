from django.shortcuts import render

# Create your views here.
from email import message
from urllib import response
from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import Fee, Teacher, Student, Scores, Staff
from django.contrib.auth import login, authenticate
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeacherForm, ScoresForm, StudentForm, FeeForm, StaffForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def dashboard(request):

    return render(request, 'dashboard.html')

@login_required(login_url='/accounts/login/')
def teachers(request):
    teachers = Teacher.objects.all()

    return render(request,'teachers.html',{'teachers':teachers})

@login_required(login_url='/accounts/login/')
def students(request):
    students = Student.objects.all()

    return render(request,'studentss.html',{'students':students})

@login_required(login_url='/accounts/login/')
def staffs(request):
    staffs = Staff.objects.all()

    return render(request,'teachers.html',{'teachers':teachers})



       
       

@login_required(login_url='/accounts/login/')
def add_business(request):
    current_user = request.user
    if request.method =='POST':
        print('received')
        form = ScoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('saved successfully')
            return redirect()
        else:
            print('not not saved')
    
    else:
        print('get request')
        form = ScoresForm()
        return render(request, 'add_business.html', {'form':form})
    return redirect('home')

@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method =='POST':
        
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
            print('post saved successfully')
    
    else:
        form = StudentForm()

        return render(request, 'add_post.html', {'form':form})
    return redirect('single_neighbourhood')

@login_required(login_url='/accounts/login/')
def add_neighbourhood(request):
    if request.method =='POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect()
    
    else:
        form = TeacherForm()
        return render(request, 'add_neighbourhood.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        try:
            searched_result = Scores.search_business(search_term)
            message = f"Found searched business {search_term}"
        
        except Scores.DoesNotExist:
             message="No business with that name try a different name."
             return render(request, 'NotFound.html',{'message':message})


        return render(request, 'search.html',{'message':message,"search_result": searched_result})

    else:
        message = "You haven't searched for any Business"
        return render(request, 'search.html',{"message":message})

def single_neighbourhood(request, pk):
    
    print('searching....................')
    belonging=Teacher.objects.get(id=pk)
    print(belonging)

    return render(request, 'home.html',{'neighbourhood':belonging})



