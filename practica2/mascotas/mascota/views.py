from django.shortcuts import render
from django.http import HttpResponse
from .models import mascotas
# Create your views here.

def incio(request):
        return render(request, 'paginas/inicio.html')


def presupuesto(request):
    return render(request, 'paginas/presupuesto.html')

def pets(request):
    pets = mascotas.objects.all()
    print(pets)
    return render(request, 'pets/index.html', {'pets': pets})