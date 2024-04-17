from .models import Paciente, Medico, Consulta
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome','rg','orgExp','cpf','cep',
        'estado','bairro','endereco','email','telefone',
                  'celular']


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['nome','crm', 'ufcrm', 'especialidade','rg','orgExp','cpf','cep',
                  'estado','bairro','endereco','email','telefone',
                  'celular']

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['paciente','medico','datahora','prontuario']
