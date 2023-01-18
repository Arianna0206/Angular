from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import agendas
from .forms import AgendaForm
from django.template import RequestContext


def inicio(request):
    return render(request, 'paginas/inicio.html')

def pets(request):
    pets = agendas.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})

def crear(request):
    agenda = AgendaForm(request.POST or None, request.FILES or None)
    if agenda.is_valid():
        agenda.save()
        return redirect('pets')
    return render(request, 'pets/crear.html', {'agenda': agenda})

def editar(request):
    return render(request, 'pets/editar.html'),

def eliminar(request, id):
    mascotas = agendas.objects.get(id=id)
    mascotas.delete()
    return redirect('pets')


