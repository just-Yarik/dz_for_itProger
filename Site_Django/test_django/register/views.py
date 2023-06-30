from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
# Create your views here.

def register (request):
    form = UserForm()
    return render(request, 'register/registretion.html', {'title': 'Сторінка регистрації', 'form':form})

