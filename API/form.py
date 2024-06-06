from django import forms
from django.forms import ModelForm
from .models import Producto,Stock,Tipo_Producto

class Tipo_Producto_Form(ModelForm):
    class meta:
        model= Tipo_Producto
        fields="__all__"
        widgets={
            'nombre_Tipo_Producto':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar nombre del tipo de produto',
                        'class':'form-control'
                        }
                    ),
        }

class Stock_Form(ModelForm):
    class meta:
        model= Stock
        fields="__all__"
        widgets={
            'Cantidad':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar cantidad del produto',
                        'class':'form-control'
                        }
                    ),
        }

class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields="__all__"
        widgets={
                'Codigo_Producto':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar codigo del produto',
                        'class':'form-control'
                        }
                    ),
                'Marca':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar marca',
                        'class':'form-control'
                        }
                    ),
                'Codigo':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar codigo',
                        'class':'form-control',
                        }
                    ),
                'Nombre':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar nombre',
                        'class':'form-control',
                        }
                    ),
                'precio':forms.TextInput(
                    attrs={
                        'placeholder':'Debe ingresar precio en dolares',
                        'class':'form-control',
                        'type':'number'
                        }
                    ),
                'Stock':forms.Select(
                    attrs={                   
                        'class':'form-control'
                        }
                    ),
                'Tipo_Producto':forms.Select(
                    attrs={                   
                        'class':'form-control'
                        }
                    )               
                }