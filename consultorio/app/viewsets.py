from rest_framework import viewsets
from .serializers import PacienteSerializer, MedicoSerializer, ConsultaSerializer
from .models import Paciente, Medico, Consulta

class PacienteViewSet(viewsets.ModelViewSet):
    model = Paciente
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()
    filter_fields = ('nome','rg','orgExp','cpf','cep',
                     'estado','bairro','endereco','email','telefone',
                     'celular')

class MedicoViewSet(viewsets.ModelViewSet):
    model = Medico
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()
    filter_fields = ('nome','crm', 'ufcrm', 'especialidade','rg','orgExp','cpf','cep',
                     'estado','bairro','endereco','email','telefone',
                     'celular')

class ConsultaViewSet(viewsets.ModelViewSet):
    model = Consulta
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
    filter_fields = ('paciente','medico','datahora','prontuario')