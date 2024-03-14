from django.forms import ModelForm
from .models import Paciente, Medico, Consulta

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome','rg','orgExp',
        'cpf','cep', 'estado', 'bairro',
        'endereco', 'email', 'telefone',
                  'celular']


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'ufcrm', 'especialidade',
                  'rg','orgExp', 'cpf','cep', 'estado',
                  'bairro','endereco', 'email', 'telefone',
                  'celular']

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'datahora',
                  'prontuario']