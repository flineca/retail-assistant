from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello! ")

from django.shortcuts import render
 
def home(request):
    context = {}
    context['welcome_string'] = 'The project has been created successfully!'
    return render(request, 'home.html', context)

def dashboard(request):
    context = {}
    context['welcome_string'] = 'The project has been created successfully!'
    return render(request, 'dashboard.html', context)

def control(request):
    context = {}
    context['welcome_string'] = 'The project has been created successfully!'
    return render(request, 'control.html', context)
    