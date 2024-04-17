from django.urls import path, include
from rest_framework import routers
from .viewsets import PacienteViewSet, MedicoViewSet, ConsultaViewSet
from .views import home, createmedico, createpaciente, \
    createconsulta, readmedico, readpaciente, readconsulta, \
    updatemedico, updateconsulta, updatepaciente, \
    deletemedico, deleteconsulta, deletepaciente

router = routers.DefaultRouter()
router.register(r'paciente', PacienteViewSet, basename="Paciente")
router.register(r'medico', MedicoViewSet, basename="Medico")
router.register(r'consulta', ConsultaViewSet, basename="Consulta")


urlpatterns = [
    path('', home, name='home'),
    path('createmedico', createmedico, name='createmedico'),
    path('createpaciente', createpaciente, name='createpaciente'),
    path('createconsulta', createconsulta, name='createconsulta'),
    path('readmedico', readmedico, name='readmedico'),
    path('readpaciente', readpaciente, name='readpaciente'),
    path('readconsulta', readconsulta, name='readconsulta'),
    path('updatemedico/<int:id>', updatemedico, name='updatemedico'),
    path('updatepaciente/<int:id>', updatepaciente, name='updatepaciente'),
    path('updateconsulta/<int:id>', updateconsulta, name='updateconsulta'),
    path('deletemedico/<int:id>', deletemedico, name='deletemedico'),
    path('deleteconsulta/<int:id>', deleteconsulta, name='deleteconsulta'),
    path('deletepaciente/<int:id>', deletepaciente, name='deletepaciente'),
    path('api/', include(router.urls)),
]