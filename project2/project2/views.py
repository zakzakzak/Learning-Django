from django.http import HttpResponse

# method view index
def index(request):
    # buat terpisah biar enak dilihat
    judul = "<h1> ini adalah Home </h1>"
    subjudul = "<h2> selamat datang </h2>"

    output = judul + subjudul
    return HttpResponse(output)

def about(request):
    str_output = "<h1> ini adalah About </h1>"
    return HttpResponse(str_output)
