# -*- coding: utf-8 -*-
from django import forms
from .models import Cliente
from django.forms import Textarea


class ClienteFsForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'ativo_cliente', 
            'fone1_cliente', 
            'fone2_cliente', 
            'cell_cliente', 
            'email_cliente', 
            'nome_cliente', 
            'cpf_cliente', 
            'rg_cliente', 
            'estd_civil_cliente', 
            'sexo_cliente', 
            'data_nasc_cliente'
        ]