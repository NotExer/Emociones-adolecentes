from apps.cliente.models import Cliente
from apps.cliente.form import ClienteForm
from django.views.generic import CreateView, ListView, DeleteView,UpdateView
from django.urls import reverse_lazy




class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente.html'
    context_object_name = 'cliente'
    login_url = "iniciar"

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear_cliente.html'
    success_url = reverse_lazy('lista_cliente')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/editar_cliente.html'
    success_url = reverse_lazy('lista_cliente')
    context_object_name = 'cliente'  # <--- Este es el correcto

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar_cliente.html'
    context_object_name = 'cliente'  # <--- También aquí
    success_url = reverse_lazy('lista_cliente')
