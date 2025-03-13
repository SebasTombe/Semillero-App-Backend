from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModuloViewset

router = DefaultRouter()
router.register(r'registro-modulos',ModuloViewset)

urlpatterns = [
    path('', include(router.urls)),
]