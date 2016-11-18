# coding=utf-8
from django import forms
from .models import Usuario, Libro, Prestamo

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'dpi', 'libro')


def __init__ (self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        self.fields["libro"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["libro"].help_text = "Ingrese libros"
        self.fields["libro"].queryset = Libro.objects.all()
