from django.urls import path,include
from rest_framework import routers
from API import views

routers= routers.DefaultRouter()
routers.register(r'Tipo_Producto',views.Tipo_ProductoViewSet)
routers.register(r'Stock',views.StockViewSet)
routers.register(r'Producto',views.ProductoViewSet)

urlpatterns = [
    path('',include(routers.urls))
]