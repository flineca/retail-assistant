from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello! ")

from django.shortcuts import render
 
def home(request):
    context          = {}
    context['welcome'] = 'The project has been created successfully!'
    return render(request, 'home.html', context)
    