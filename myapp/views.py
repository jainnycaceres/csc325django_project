from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the home page!</h1><p>This is a simple Django application.</p><p>Enjoy your stay!</p>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page of the simple Django application.</p>")