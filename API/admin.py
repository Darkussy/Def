from django.contrib import admin
from .models import Tipo_Producto, Stock, Producto

# Register your models here.

admin.site.register(Tipo_Producto)
admin.site.register(Stock)
admin.site.register(Producto)
