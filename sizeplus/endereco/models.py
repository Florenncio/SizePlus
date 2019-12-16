from django.db import models

class Cidade(models.Model):

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

    nome_cid = models.CharField(max_length=45, blank=False, null=True)
    uf_cid = models.CharField(max_length=2, blank=False, null=True, choices=uf_CHOICES, default='PB', verbose_name='UF')
    
    #Controle de acesso
    id_cid = models.AutoField(primary_key=True)
    created_cid = models.DateTimeField(auto_now_add=True)
    updated_cid = models.DateTimeField(auto_now=True)

class Endereco(models.Model):
    class Meta:
        ordering = ['cep_endr', 'nome_endr']

    tipo_CHOICE = (
        ('Rua', 'Rua'),
        ('Av', 'Avenida'),
        ('Rod', 'Rodovia')
    )
    
    #Chaves estranjeiras
    cidade_to_endr = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    nome_endr = models.CharField(max_length=100, blank=False, null=True)
    num_endr = models.PositiveIntegerField(blank=False, null=True)
    cep_endr = models.CharField(max_length=9, blank=False, null=True, verbose_name ='CEP')
    bairro_endr = models.CharField(max_length=100, blank=False, null=True,verbose_name='Bairro')
    tipo_endr = models.CharField(max_length=3, blank=True, null=True, default='Rua', choices=tipo_CHOICE, verbose_name='Tipo')
    ref_endr = models.CharField(max_length=255, blank=False, null=True, verbose_name='Referência')

    #Controle de acesso
    id_endr = models.AutoField(primary_key=True)
    created_endr = models.DateTimeField(auto_now_add=True)
    updated_endr = models.DateTimeField(auto_now=True)