import email
from users.models import Users
from users.serializers import UsersSerializer
from rest_framework import mixins, response, serializers, generics
from rest_framework import status
# Create your views here.


class CreateUser(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
