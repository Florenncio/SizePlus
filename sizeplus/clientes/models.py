from django.db import models
from endereco.models import Endereco


class Cliente(models.Model):

    uf_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

    sexo_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    estd_civil_CHOICES = (
        ('SL', 'Solteiro'),
        ('CS', 'Casado'),
        ('DV', 'Divorciado'),
        ('VV', 'Viúvo')
    )

    tipo_pessoa_CHOICES = (
        ('F', 'Física'),
        ('J', 'Jurídica'),
    )

    #Chaves estranjeiras
    endr_to_cliente = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    #Atributos p/ pessoa fisica
    nome_cliente = models.CharField(max_length=45, blank=False, null=True, verbose_name='Nome')
    cpf_cliente = models.CharField(max_length=18, blank=False, null=True, verbose_name='CPF')
    rg_cliente = models.CharField(max_length=18, blank=True, null=True, verbose_name='RG')
    estd_civil_cliente = models.CharField(max_length=10, blank=True, null=True, choices=estd_civil_CHOICES, verbose_name='Estado Civíl')
    sexo_cliente = models.CharField(max_length=9, blank=True, null=True, choices=sexo_CHOICES, verbose_name='Sexo')
    data_nasc_cliente = models.DateField(blank=True, null=True, verbose_name='Data de Nasc.')
    
    #Atributos p/ pessoas juridica
    razao_social_cliente = models.CharField(max_length=100, blank=False, null=True, verbose_name='Razão Social')
    nome_fant_cliente = models.CharField(max_length=100, blank=False, null=True, verbose_name='Nome Fantasia')
    cnpj_cliente = models.CharField(max_length=18, blank=False, null=True, verbose_name='CNPJ')
    insc_estd_cliente = models.CharField(max_length=18, blank=True, null=True, verbose_name='Insc. Estadual')
    insc_mun_cliente = models.CharField(max_length=18, blank=True, null=True, verbose_name='Insc. Municipal')

    #Atributos utilizados por ambos
    ativo_cliente = models.BooleanField(blank=True, default=True, verbose_name='Ativo')
    fone1_cliente = models.CharField(max_length=16, blank=False, null=True, verbose_name='Telefone(1)')
    fone2_cliente = models.CharField(max_length=16, blank=False, null=True, verbose_name='Telefone(2)')
    cell_cliente = models.CharField(max_length=16, blank=True, null=True, verbose_name='Celular')
    email_cliente = models.EmailField(max_length=100, blank=True, null=True, verbose_name='Email')

    #Controle de acesso
    id_cliente = models.AutoField(primary_key=True)
    created_cliente = models.DateTimeField(auto_now_add=True)
    updated_cliente = models.DateTimeField(auto_now=True)