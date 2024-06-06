from django.shortcuts import render,redirect
from API.models import Producto
from API.form import ProductoForm
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions, IntegrationCommerceCodes, IntegrationApiKeys
from transbank.common.integration_type import IntegrationType

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


def Pagar(request):
    precio = request.POST["valor"]
    return render(request,"htmls/Pagar.html", {'precio': precio})

def Webpay(request):
    return render(request,"htmls/Webpay.html")


#Api Webpay
def procesar_pago(request):
    token = request.GET.get('token_ws')

    transaction = Transaction(WebpayOptions(
        IntegrationCommerceCodes.WEBPAY_PLUS, 
        IntegrationApiKeys.WEBPAY, 
        IntegrationType.TEST))

    response = transaction.commit(token)

    status = response['status']
    amount = response['amount']
    buy_order = response['buy_order']

    context = {
        'status': status,
        'amount': amount,
        'buy_order': buy_order,
    }

    return render(request, 'htmls/Webpay.html', context)

def pago(request):
    buy_order = request.POST["ordenCompra"]
    session_id = request.POST["idSesion"]
    amount = request.POST["monto"]
    return_url = 'http://127.0.0.1:8000/Pagar/procesar_pago'

    transaction = Transaction(WebpayOptions(
        IntegrationCommerceCodes.WEBPAY_PLUS, 
        IntegrationApiKeys.WEBPAY, 
        IntegrationType.TEST))

    response = transaction.create(buy_order, session_id, amount, return_url)
    print (response)
    token = response['token']
    url = response['url']
    print(token,url)
    context = {
        'token': token,
        'url': url,
        'response': response  # Agrega response al contexto
    }
    
    return render(request, 'htmls/Pagar.html', context)
