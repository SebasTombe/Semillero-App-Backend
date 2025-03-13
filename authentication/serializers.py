from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    document_number = serializers.CharField(required=True)  
    password = serializers.CharField(min_length=8,required=True)
    
    def validate_password(self, password):
        return make_password(password)
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'document_number', 'password')  