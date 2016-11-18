from django.contrib import admin
from blog.models import Usuario, UsuarioAdmin, Libro, LibroAdmin

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Libro, LibroAdmin)
