from django.shortcuts import render, redirect,get_object_or_404
#forms import ContactForm
#from .models import CourseDetails
from .forms import RegistraionForm, FeedbackForm
from .models import *
from .forms import *
from django.contrib import admin
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Register your models here.

def mainpage(request):
  pages = [
        {'name': 'Home', 'template': 'home.html'},
        {'name': 'Contact', 'template': 'contact.html'},
        {'name': 'Services', 'template': 'services.html'},
        {'name': 'Feedback', 'template': 'feedback.html'},
        {'name': 'Gallery', 'template': 'gallery.html'},
        {'name': 'Register', 'template': 'register.html'},
        {'name': 'Login', 'template': 'login.html'},
    ]
  template = request.GET.get('template', 'mainPage.html')  
  return render(request, template, {'pages' : pages})

def home(request):
  return render(request, 'home.html')

def services(request):
  courses = CourseDetails.objects.all()
  return render(request,'services.html' ,{'courses':courses})

""" @login_required
def .html(request):
  retu.htmlrn render(request,'.html.html')
 .html.html"""
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
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('feedback')
    else:
        form = FeedbackForm() 
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})


@login_required
def update_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)  # Retrieve the feedback object or return 404
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback')  # Redirect to the feedback page
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'update_feedback.html', {'form': form})

@login_required
def delete_feedback(request, pk):
    feedback = Feedback.objects.get(pk=pk)
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback')
    return render(request, 'delete_feedback.html', {'feedback': feedback})

def register_view(request):
  if request.method == "POST":
    form = RegistraionForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return render(request, 'registraion_success.html')
    else:
      return render(request, "register.html", {"form":form})
  else:
    form = RegistraionForm()
    return render(request, "register.html", {"form":form})


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
        return render(request, "login.html", {"form" : form, "error": "Invalid username or password"})
  else:
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
  logout(request)
  return redirect("login")



