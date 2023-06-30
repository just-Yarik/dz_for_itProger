from django.shortcuts import render
from django.http import HttpResponse
data = {
    'title': 'Головна сторінка'
}

def golovna (request):
    return render(request, 'main/main.html', data)

def kontakty (request):
    return render(request, 'main/kontakt.html', {'title': 'Сторінка з контактами'})

def register (request):
    form = UserForm()
    return render(request, 'register/registretion.html', {'title': 'Сторінка регистрації', 'form':form})