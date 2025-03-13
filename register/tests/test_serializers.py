import pytest
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.contrib.auth import get_user_model
from register.models import Estudiante
from register.serializers import InitialRegistrationSerializer, ProgressiveUpdateSerializer, EstudianteSerializer

User = get_user_model()

@pytest.mark.django_db
def test_serializador_registro_inicial():
    data = {
        'Nombre': 'Juan',
        'Apellidos': 'Pérez',
        'NumeroIdentificacion': '1234567890'
    }
    serializer = InitialRegistrationSerializer(data=data)
    assert serializer.is_valid()
    estudiante = serializer.save()
    assert estudiante.Nombre == 'Juan'
    assert estudiante.Apellidos == 'Pérez'
    assert estudiante.NumeroIdentificacion == '1234567890'
    assert estudiante.user.document_number == '1234567890'

    # Verificar que se lanza una ValidationError si el NumeroIdentificacion ya está en uso
    with pytest.raises(DRFValidationError):
        serializer = InitialRegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)

@pytest.mark.django_db
def test_serializador_actualizacion_progresiva():
    user = User.objects.create_user(
        document_number='1234567890',
        email='juan.perez@example.com',
        password='password123'
    )
    estudiante = Estudiante.objects.create(
        user=user,
        Nombre='Juan',
        Apellidos='Pérez',
        NumeroIdentificacion='1234567890'
    )
    data = {
        'CorreoElectronico': 'nuevo.correo@example.com',
        'CiudadNacimiento': 'Ciudad Nueva'
    }
    serializer = ProgressiveUpdateSerializer(estudiante, data=data, partial=True)
    assert serializer.is_valid()
    estudiante = serializer.save()
    assert estudiante.CorreoElectronico == 'nuevo.correo@example.com'
    assert estudiante.CiudadNacimiento == 'Ciudad Nueva'
    assert estudiante.user.email == 'nuevo.correo@example.com'

