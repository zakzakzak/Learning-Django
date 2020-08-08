from django.http import HttpResponse
# buat template
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h1>Hello World!</h1>")
