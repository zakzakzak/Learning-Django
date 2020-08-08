from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Judul':'Kelas Terbuka',
        'Subjudul':'Blog',
        'nav':[
            ["/", "Home"],
            ["/blog/cerita", "Cerita"],
            ["/blog/news", "News"],
        ],
    }
    return render(request, 'index.html', context)
