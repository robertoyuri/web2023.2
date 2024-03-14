from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm, MedicoForm, ConsultaForm
from . models import Paciente, Medico, Consulta

# Create your views here.

def home(request):
    return render(request, 'home.html')

def createmedico(request):
    medicoForm = MedicoForm(request.POST or None)
    if(medicoForm.is_valid()):
        medico = medicoForm.save(commit=False)
        medico.save()
        return redirect("readmedico")
    return render(request, 'createmedico.html', {'medicoForm':medicoForm})

def createpaciente(request):
    pacienteForm = PacienteForm(request.POST or None)
    if(pacienteForm.is_valid()):
        paciente = pacienteForm.save(commit=False)
        paciente.save()
        return redirect("readpaciente")
    return render(request, 'createpaciente.html', {'pacienteForm':pacienteForm})

def createconsulta(request):
    consultaForm = ConsultaForm(request.POST or None)
    if(consultaForm.is_valid()):
        consulta = consultaForm.save(commit=False)
        consulta.save()
        return redirect("readconsulta")
    return render(request, 'createconsulta.html', {'consultaForm':consultaForm})

def readpaciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'readpaciente.html',
                  {'pacientes':pacientes})


def readmedico(request):
    medicos = Medico.objects.all()
    return render(request, 'readmedico.html',
                  {'medicos':medicos})


def readconsulta(request):
    consultas = Consulta.objects.all()
    return render(request, 'readconsulta.html',
                  {'consultas':consultas})


def updatemedico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    medicoForm = MedicoForm(request.POST or None,
                            instance=medico)
    if(medicoForm.is_valid()):
        medico = medicoForm.save(commit=False)
        medico.save()
        return redirect("readmedico")
    return render(request, 'createmedico.html', {'medicoForm':medicoForm})


def updatepaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    pacienteForm = PacienteForm(request.POST or None,
                                instance=paciente)
    if(pacienteForm.is_valid()):
        paciente = pacienteForm.save(commit=False)
        paciente.save()
        return redirect("readpaciente")
    return render(request, 'createpaciente.html', {'pacienteForm':pacienteForm})

def updateconsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    consultaForm = ConsultaForm(request.POST or None,
                                instance=consulta)
    if(consultaForm.is_valid()):
        consulta = consultaForm.save(commit=False)
        consulta.save()
        return redirect("readconsulta")
    return render(request, 'createconsulta.html', {'consultaForm':consultaForm})

def deletemedico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    medico.delete()
    return redirect("readmedico")

def deletepaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    paciente.delete()
    return redirect("readpaciente")

def deleteconsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    consulta.delete()
    return redirect("readconsulta")
