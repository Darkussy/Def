from django.shortcuts import render,redirect
from API.models import Producto
from API.form import ProductoForm
# Create your views here.

def Index(request):
    return render(request,'htmls/Index.html')

def Productos(request):
    return render(request,'htmls/Productos.html')

def Prod_1(request):
    return render(request,'htmls/Prod_1.html')

def Admin(request):
    Productos= Producto.objects.all()
    return render(request,'admin/Index_Admin.html',{"Productos":Productos})

def Registrar(request):
    form =ProductoForm
    mensaje = ""
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = request.POST.get('Codigo_Producto', None)
            if nombre in Producto.objects.values_list('Codigo_Producto', flat=True):
                mensaje="Este nombre de Producto ya está registrado"
            else:
                form.save()
                mensaje="Datos Guardados Correctamente"    

    return render(request,"admin/Save_Prod_Admin.html", {"form":form,"mensaje":mensaje})

def Modificar(request, id):
    Product = Producto.objects.get(idProducto=id)
    mensaje=""
    if request.method == 'POST':
        form =ProductoForm(request.POST, request.FILES, instance=Product)
        if form.is_valid():
            form.save()
            mensaje = "Datos Modificado Correctamente"
            return redirect(to="Admin")
    else:
        return render(request, "admin/Mod_Prod_Admin.html", {"form":ProductoForm(instance=Product), "mensaje":mensaje})



def delete_Producto(request, id):
    Product = Producto.objects.get(idProducto=id)
    Product.delete()
    return redirect(to="Admin")