from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import plantas
from . forms import MacetaForm

from . models import Categoria

#PAGINAS SECUENDARIAS
def inicio_def(request):
    categorias_consulta = Categoria.objects.all()
    return render(request, 'paginas_secundarias/inicio.html', {'categorias_consulta_vr': categorias_consulta})

def nosotros_def(request):
    return render(request, 'paginas_secundarias/nosotros.html')

#CRUD DE PLANTAS
def plantas_def(request):
    plantas_consulta = plantas.objects.all()
    return render(request, 'plantas/index.html', {'plantas_consulta_vr': plantas_consulta})

def crear_planta_def(request):
    formulario = MacetaForm(request.POST or None, request.FILES  or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ver_planta_def_path')
    return render(request, 'plantas/crear.html', {'formulario': formulario})

def editar_planta_def(request, id):
    plantas_datos = plantas.objects.get(id=id)
    formulario = MacetaForm(request.POST or None, request.FILES  or None, instance=plantas_datos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('ver_planta_def_path')
    return render(request, 'plantas/editar.html', {'formulario': formulario})

def eliminar_planta_def(request, id):
    maceta = plantas.objects.get(id=id)
    maceta.delete()
    return redirect('ver_planta_def_path')