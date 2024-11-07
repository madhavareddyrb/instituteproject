from django.shortcuts import render, redirect
#forms import ContactForm
#from .forms import CommentForm
#from .models import Comment
#from .models import CourseDetails
from .forms import RegistraionForm
from .models import *
from .forms import *
from django.contrib import admin
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Register your models here.

def mainpage(request):
    return render(request, 'mainPage.html')

def home(request):
  return render(request, 'home.html')

def services(request):
  courses = CourseDetails.objects.all()
  return render(request,'services.html' ,{'courses':courses})

@login_required
def feedback(request):
  return render(request,'feedback.html')

def contact(request):
  return render(request, 'contact.html')


def gallery(request):
  return render(request,'gallery.html')

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contact_success')
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form})

def contact_success(request):
  return render(request, 'contact_success.html')


def feedback(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = CommentForm()
    
    comments = Comment.objects.all()
    return render(request, 'feedback.html', {'form': form, 'comments': comments})


""" def register_view(request):
   if request.method == "POST":
    form = RegistraionForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return render("request, 'register.html")
    else:
      return render(request, "register.html", {"form":form})
   else:
    form = RegistraionForm()
   return render(request, "register.html", {"form":form}) """


def register_view(request):
  if request.method == "POST":
    form = RegistraionForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return render(request, "registraion_success.html")
    else:
      return render(request, "register.html", {"form": form})
  else:
    form = RegistraionForm()
    return render(request, "register.html", {"form": form})
def registraion_success(request):
  return render(request, 'registraion_success.html')

def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get("password")
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('mainpage')
  else:
      form = AuthenticationForm()
  return render(request, "login.html", {"form" : form})

def logout_view(request):
  logout(request)

  return redirect("login")



