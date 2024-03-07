from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def createdoctor(request):
    return render(request, 'createdoctor.html')

def createpaciente(request):
    return render(request, 'createpaciente.html')