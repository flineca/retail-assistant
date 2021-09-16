from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello! ")
 

def home(request):
    context = {}
    context['welcome_string'] = 'The project has been created successfully!'
    return render(request, 'home.html', context)


def control(request):
    control_context = {}
    control_context['welcome_string'] = 'The project has been created successfully!'
    return render(request, 'control.html', control_context)

def analyze(request):
    context = {}
    context['welcome_string'] = 'The project has been created successfully!'
    return render(request, 'analyze.html', context)

