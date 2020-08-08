from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'kelas terbuka',
        'Kontributor':'zakiy',
    }
    return render(request, 'index.html', context)
