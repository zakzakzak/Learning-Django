from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Kelas Terbuka',
        'Subjudul':'SELAMAT DATANG',
        'nav' : [
            ['/',        'Home'],
            ['/blog',    'Blog'],
            ['/about',   'About'],
            ['/contact', 'Contact']
        ],
    }
    return render(request,'index.html', context)
