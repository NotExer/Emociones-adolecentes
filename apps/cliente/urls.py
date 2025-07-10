from cliente.views import ClienteListView, ClienteCreateView, ClienteDeleteView, ClienteDetailView, ClienteUpdateView
from django.urls import path


urlpatterns = [
    path('cliente/', ClienteListView.as_view(), name='lista_cliente'),
    path('cliente/crear/', ClienteCreateView.as_view(), name='crear_cliente'),# urls.py
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='eliminar_cliente'),

    path('clientes/detalle/<int:ClienteID>/', ClienteDetailView.as_view(), name='detalle_cliente'),
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar_cliente')







]
