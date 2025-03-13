import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import AdminUser

@pytest.mark.django_db
def test_inicio_sesion_exitoso():
    client = APIClient()
    user = AdminUser.objects.create_user(
        document_number='1234567890',
        email='test@example.com',
        password='password123'
    )
    url = reverse('login')
    data = {'document_number': '1234567890', 'password': 'password123'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

@pytest.mark.django_db
def test_inicio_sesion_fallido():
    client = APIClient()
    url = reverse('login')
    data = {'document_number': '1234567890', 'password': 'wrongpassword'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data['detail'] == 'Invalid credentials'

@pytest.mark.django_db
def test_cerrar_sesion():
    client = APIClient()
    user = AdminUser.objects.create_user(
        document_number='1234567890',
        email='test@example.com',
        password='password123'
    )
    client.force_authenticate(user=user)
    url = reverse('logout')
    response = client.post(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_registro():
    client = APIClient()
    url = reverse('signup')
    data = {
        'email': 'newuser@example.com',
        'document_number': '0987654321',
        'password': 'newpassword123'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert AdminUser.objects.filter(email='newuser@example.com').exists()