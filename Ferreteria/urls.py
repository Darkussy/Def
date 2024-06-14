from django.urls import path
from .views import Index, Productos, Prod_1 , Admin,Registrar,delete_Producto, Modificar,Pagar ,pago,procesar_pago,Webpay,agregar_producto,eliminar_producto,limpiar_carrito,restar_producto

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
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),


]