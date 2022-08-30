from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer, Serializer
from users.models import Users

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'password']