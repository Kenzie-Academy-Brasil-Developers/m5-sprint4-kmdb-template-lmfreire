from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField()
    bio = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    is_critic = serializers.BooleanField(default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        
        return user  
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    