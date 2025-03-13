from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import Estudiante
from .serializers import EstudianteSerializer, InitialRegistrationSerializer, ProgressiveUpdateSerializer

class EstudianteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    
    @action(detail=False, methods=['get'])
    def search_by_id(self, request):
        id_number = request.query_params.get('NumeroIdentificacion')
        if not id_number:
            return Response({"error": "El parámetro NumeroIdentificacion es requerido"}, status=400)

        student = Estudiante.objects.filter(NumeroIdentificacion=id_number).first()
        if student:
            return Response(EstudianteSerializer(student).data, status=200)
        return Response({"message": "Estudiante no encontrado"}, status=404)

class InitialRegistrationView(generics.CreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = InitialRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class ProgressiveUpdateView(generics.UpdateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = ProgressiveUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        return generics.get_object_or_404(Estudiante, pk=pk)

