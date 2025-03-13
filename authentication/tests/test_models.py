# authentication/tests/test_models.py
import pytest
from authentication.models import AdminUser

@pytest.mark.django_db
def test_crear_usuario_admin():
    user = AdminUser.objects.create_user(
        document_number='1234567890',
        email='test@example.com',
        password='password123'
    )
    assert user.document_number == '1234567890'
    assert user.email == 'test@example.com'
    assert user.check_password('password123')

@pytest.mark.django_db
def test_crear_superusuario():
    superuser = AdminUser.objects.create_superuser(
        document_number='0987654321',
        email='superuser@example.com',
        password='superpassword123'
    )
    assert superuser.document_number == '0987654321'
    assert superuser.email == 'superuser@example.com'
    assert superuser.check_password('superpassword123')
    assert superuser.is_staff
    assert superuser.is_superuser

@pytest.mark.django_db
def test_campos_unicos():
    AdminUser.objects.create_user(
        document_number='1234567890',
        email='test@example.com',
        password='password123'
    )
    with pytest.raises(Exception):
        AdminUser.objects.create_user(
            document_number='1234567890',
            email='another@example.com',
            password='password123'
        )
    with pytest.raises(Exception):
        AdminUser.objects.create_user(
            document_number='0987654321',
            email='test@example.com',
            password='password123'
        )

@pytest.mark.django_db
def test_representacion_str():
    user = AdminUser.objects.create_user(
        document_number='1234567890',
        email='test@example.com',
        password='password123'
    )
    assert str(user) == '1234567890'