from django.shortcuts import render
from django.contrib import messages
from .forms import UsuarioForm
from blog.models import Usuario, Prestamo

def usuario_nueva(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = Usuario.objects.create(nombre=formulario.cleaned_data['nombre'], dpi = formulario.cleaned_data['dpi'])
            for libro_id in request.POST.getlist('libro'):
               prestamo = Prestamo(libro_id=libro_id, usuario_id = Usuario.id)
               prestamo.save()
            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = UsuarioForm()
    return render(request, 'blog/usuario_editar.html', {'formulario': formulario})
