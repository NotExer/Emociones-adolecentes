
from django.contrib import admin
from django.urls import path
from apps.cliente.views import ClienteListView, ClienteCreateView, ClienteDeleteView, ClienteUpdateView
from apps.accounts.views import register_view, login_view, logout_view
from apps.main.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('cliente/', ClienteListView.as_view(), name='lista_cliente'),
    path('cliente/crear/', ClienteCreateView.as_view(), name='crear_cliente'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar_cliente')

]
