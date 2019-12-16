from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView, 
    UpdateView, 
    DeleteView, 
    ListView,
    DetailView,
    FormView
    )
from .forms import ClienteFsForm
from endereco.forms import EnderecoForm, CidadeForm
from multi_form_view import MultiFormView
from .models import Cliente
from django.urls import reverse_lazy

class CreateClienteFs(MultiFormView):
    form_classes = {
        'cliente_form' : ClienteFsForm,
        'endr_form' : EnderecoForm,
        'cid_form' : CidadeForm,
    }
    
    record_id = None
    template_name = 'create_cliente_fs.html'
    success_url = reverse_lazy('clientes:list-cliente-fs')



class DetailClienteFs(DetailView):
    context_object_name = 'detail_cliente'
    form_classes = ClienteFsForm
    template_name = 'detail_cliente_fs.html'

class ListClienteFs(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'list_cliente_fs.html'
    context_object_name = 'clientes'