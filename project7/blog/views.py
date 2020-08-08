from django.shortcuts import render

# Create your views here.

def index(request):
    context ={
        'Judul':'Blog',
        'Kontributor' : 'Fuad',
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context ={
        'Judul':'news',
        'Kontributor' : 'Rims',
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context ={
        'Judul':'cerita',
        'Kontributor' : 'limi',
    }
    return render(request, 'blog/index.html', context)
