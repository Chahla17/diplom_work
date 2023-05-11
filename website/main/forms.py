from .models import Task
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес:'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Меню заказа:'})}

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]   