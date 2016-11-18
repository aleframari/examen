from django.db import models
from django.contrib import admin

class Libro(models.Model):
    isbn    = models.CharField(max_length=60)
    titutlo      = models.CharField(max_length=200)
    #portada = models.ImageField(upload_to='albun/images/')
    autor   = models.CharField(max_length=200)
    editorial   = models.CharField(max_length=200)
    pais      = models.CharField(max_length=200)
    anio      = models.IntegerField()

    def __str__(self):
        return self.isbn

class Usuario(models.Model):
    nombre  =   models.CharField(max_length=30)
    dpi = models.TextField()
    libro   = models.ManyToManyField(Libro, through='Prestamo')

    def __str__(self):
        return self.nombre



class Prestamo (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo=models.DateTimeField(auto_now=True, null=True)
    fecha_devolulcion=models.DateTimeField(null=False,max_length=50)
    fecha_devolucionreal=models.DateTimeField(null=False,max_length=50)


class PrestamoInLine(admin.TabularInline):
    model = Prestamo
    extra = 1


class UsuarioAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)


class LibroAdmin (admin.ModelAdmin):
    inlines = (PrestamoInLine,)
