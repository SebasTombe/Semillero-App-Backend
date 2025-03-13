import pytest
from django.core.exceptions import ValidationError
from register.models import Estudiante
from curse.models import Modulo
from django.conf import settings

@pytest.mark.django_db
def test_crear_estudiante():
    estudiante = Estudiante.objects.create(
        Nombre='Juan',
        Apellidos='Pérez',
        NumeroIdentificacion='1234567890',
        CorreoElectronico='juan.perez@example.com',
        password='password123'
    )
    assert estudiante.Nombre == 'Juan'
    assert estudiante.Apellidos == 'Pérez'
    assert estudiante.NumeroIdentificacion == '1234567890'
    assert estudiante.CorreoElectronico == 'juan.perez@example.com'
    assert estudiante.password == 'password123'

@pytest.mark.django_db
def test_estudiante_numero_identificacion_unico():
    Estudiante.objects.create(
        Nombre='Juan',
        Apellidos='Pérez',
        NumeroIdentificacion='1234567890',
        CorreoElectronico='juan.perez@example.com',
        password='password123'
    )
    with pytest.raises(ValidationError):
        estudiante = Estudiante(
            Nombre='Ana',
            Apellidos='Gómez',
            NumeroIdentificacion='1234567890',
            CorreoElectronico='ana.gomez@example.com',
            password='password123'
        )
        estudiante.full_clean()  # This will raise the ValidationError
        estudiante.save()

@pytest.mark.django_db
def test_estudiante_modulo_matricular():
    modulo = Modulo.objects.create(NombreModulo='Modulo 1')
    estudiante = Estudiante.objects.create(
        Nombre='Juan',
        Apellidos='Pérez',
        NumeroIdentificacion='1234567890',
        CorreoElectronico='juan.perez@example.com',
        ModuloMatricular=modulo,
        password='password123'
    )
    assert estudiante.ModuloMatricular == modulo

@pytest.mark.django_db
def test_estudiante_informacion_pago():
    estudiante = Estudiante.objects.create(
        Nombre='Juan',
        Apellidos='Pérez',
        NumeroIdentificacion='1234567890',
        CorreoElectronico='juan.perez@example.com',
        ValorConsignado=100000,
        NumeroRecibo='12345',
        password='password123'
    )
    assert estudiante.ValorConsignado == 100000
    assert estudiante.NumeroRecibo == '12345'