from django.db import models

# Create your models here.

class Tipo_Producto(models.Model):
    id_Tipo_Producto =models.AutoField(primary_key=True)
    nombre_Tipo_Producto = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_Tipo_Producto
    
class Stock(models.Model):
    id_Stock = models.AutoField(primary_key=True) 
    Cantidad = models.IntegerField()

    def __str__(self):
        Texto = " Stock Disponible: " + str(self.Cantidad)
        return Texto
    

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    Codigo_Producto = models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    Stock = models.ForeignKey(Stock,on_delete=models.CASCADE)
    Tipo_Producto = models.ForeignKey(Tipo_Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre
    
