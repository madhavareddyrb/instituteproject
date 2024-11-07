from django import forms
from .models import contact
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
  class Meta:
    model = contact
    fields = [
      'name','email','message']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')

""" class RegistraionForm(UserCreationForm):
   email = forms.EmailField(required=True)

   class Meta:
      model = User
      fields = ['username',"email",'password','password2'] """

class RegistraionForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']