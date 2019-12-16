from django.urls import path
from .views import (
    CreateClienteFs,
    DetailClienteFs,
    ListClienteFs,
)

app_name = 'clientes'

urlpatterns = [
    path('novo/', CreateClienteFs.as_view(), name='create-cliente-fs'),
    path('<int:pk>/', DetailClienteFs.as_view(), name='detail-cliente-fs'),
    path('list/', ListClienteFs.as_view(), name='list-cliente-fs'),
]
