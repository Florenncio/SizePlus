# -*- coding: utf-8 -*-
from django import forms
from .models import Endereco, Cidade
from django.forms import Textarea


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = [
            'nome_endr',
            'cep_endr',
            'num_endr',
            'bairro_endr',
            'tipo_endr',
            'ref_endr',
        ]
class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        fields = [
            'nome_cid',
            'uf_cid',
        ]