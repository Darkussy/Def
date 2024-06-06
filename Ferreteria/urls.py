from django.urls import path
from .views import Index, Productos, Prod_1 , Admin,Registrar,delete_Producto, Modificar,Pagar ,pago,procesar_pago,Webpay

urlpatterns = [
    path('', Index, name="Index"),
    path('Productos/',Productos,name='Productos'),
    path('Prod_1/',Prod_1,name='Prod_1'),
    path('Admin/',Admin,name='Admin'),
    path('Registrar/',Registrar,name='Registrar'),
    path('Modificar/<id>',Modificar,name='Modificar'),
    path('delete_Producto/<id>',delete_Producto,name='delete_Producto'),
    path('Pagar/', Pagar, name='Pagar'),
    path('pago/', pago, name='pago'),
    path('Pagar/procesar_pago', procesar_pago, name='procesar_pago'),  # Nueva ruta para procesar_pago
    path('Webpay/', Webpay, name='Webpay'),
    

]