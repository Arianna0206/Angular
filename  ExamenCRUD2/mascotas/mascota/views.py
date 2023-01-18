from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import mascotas
from .forms import MascotaForm
from django.template import RequestContext


def inicio(request):
    return render(request, 'paginas/inicio.html')

def pets(request):
    pets = mascotas.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})

def crear(request):
    agenda = MascotaForm(request.POST or None, request.FILES or None)
    if agenda.is_valid():
        agenda.save()
        return redirect('pets')
    return render(request, 'pets/crear.html', {'agenda': agenda})

def editar(request):
    return render(request, 'pets/editar.html'),

def eliminar(request, id):
    mascotas = mascotas.objects.get(id=id)
    mascotas.delete()
    return redirect('pets')

