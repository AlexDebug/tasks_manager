from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer, Serializer
from users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']