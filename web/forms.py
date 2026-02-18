from django import forms
from .models import Dato

class AgregarRegistroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}), label="")
    apellido = forms.CharField(max_length=100, required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}), label="")
    email = forms.EmailField(required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    telefono = forms.CharField(max_length=15, required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Telefono", "class": "form-control"}), label="")    
    direccion = forms.CharField(max_length=255, required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}), label="")
    ciudad = forms.CharField(max_length=100, required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}), label="")
    estado = forms.CharField(max_length=100, required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Estado", "class": "form-control"}), label="")
    codigo_postal = forms.CharField(max_length=20, required = True, widget=forms.widgets.TextInput(attrs={"placeholder": "Código Postal", "class": "form-control"}), label="")

    class Meta:
        model = Dato
        exclude = ("user",)