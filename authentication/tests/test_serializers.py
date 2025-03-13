import pytest
from authentication.serializers import UserSerializer
from authentication.models import AdminUser

@pytest.mark.django_db
def test_serializador_usuario_datos_validos():
    data = {
        'email': 'test@example.com',
        'document_number': '1234567890',
        'password': 'password123'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.email == 'test@example.com'
    assert user.document_number == '1234567890'
    assert user.check_password('password123')

@pytest.mark.django_db
def test_serializador_usuario_datos_invalidos():
    data = {
        'email': 'invalid-email',
        'document_number': '',
        'password': 'short'
    }
    serializer = UserSerializer(data=data)
    assert not serializer.is_valid()
    assert 'email' in serializer.errors
    assert 'document_number' in serializer.errors
    assert 'password' in serializer.errors

@pytest.mark.django_db
def test_serializador_usuario_encriptacion_contrasena():
    data = {
        'email': 'test@example.com',
        'document_number': '1234567890',
        'password': 'password123'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.check_password('password123')
    assert user.password != 'password123'  # Ensure the password is encrypted