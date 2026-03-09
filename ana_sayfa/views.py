from django.shortcuts import render, redirect, get_object_or_404
from .models import TeknoProje
from .forms import TeknoProjeForm

def ana_sayfa(request):
    projeler = TeknoProje.objects.all()
    return render(request, 'anasayfa.html', {'projeler': projeler})

def proje_detay(request, id):
    proje = get_object_or_404(TeknoProje, id=id)
    return render(request, 'proje_detay.html', {'proje': proje})

def proje_ekle(request):
    if request.method == "POST":
        form = TeknoProjeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('anasayfa')
    else:
        form = TeknoProjeForm()
    return render(request, 'proje_ekle.html', {'form': form})