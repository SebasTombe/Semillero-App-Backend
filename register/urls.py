from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, InitialRegistrationView, ProgressiveUpdateView

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)

urlpatterns = [
    path('initial/', InitialRegistrationView.as_view(), name='initial-register'),
    path('update/<int:pk>/', ProgressiveUpdateView.as_view(), name='progressive-update'),
]

urlpatterns += router.urls