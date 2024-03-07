from django.urls import path
from .views import home, createdoctor, createpaciente

urlpatterns = [
    path('', home, name='home'),
    path('createdoctor', createdoctor, name='createdoctor'),
    path('createpaciente', createpaciente, name='createpaciente'),
]