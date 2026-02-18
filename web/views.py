from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dato
from .forms import AgregarRegistroForm

@login_required
def home(request):

    datos = Dato.objects.all()

    return render(request, 
                  'home.html', 
                  {'datos': datos})

@login_required
def registro_eliminar(request,pk):
    delete_dato = Dato.objects.get(id=pk)
    delete_dato.delete()
    return redirect('home')

@login_required
def registro_agregar(request):
    form = AgregarRegistroForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            nuevo_registro = form.save()
            return redirect('home')

    return render(request,
                  'registro_agregar.html',
                  {'form': form})

@login_required
def registro_editar(request, pk):
    try:
        dato = Dato.objects.get(id=pk)
        form = AgregarRegistroForm(request.POST or None, instance=dato)
        if form.is_valid():
            form.save()
            return redirect('home')
    except Dato.DoesNotExist:
        return redirect('home')
    return render(request, 
                  'registro_editar.html', 
                  {'form': form})