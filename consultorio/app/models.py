from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=40)
    rg = models.IntegerField()
    orgExp = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    endereco = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=40)
    crm = models.IntegerField()
    ufcrm = models.CharField(max_length=2)
    especialidade = models.CharField(max_length=40)
    rg = models.IntegerField()
    orgExp = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=40)
    bairro = models.CharField(max_length=40)
    endereco = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return self.nome + ' - ' + str(self.crm)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    datahora = models.DateTimeField()
    prontuario = models.TextField()

    def __str__(self):
        return self.paciente.nome + ' - ' + self.medico.nome + ' - ' + str(self.datahora) + ' - '
