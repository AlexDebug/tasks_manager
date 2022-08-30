from rest_framework import routers
from users.views import CreateUser
from users import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('sing_up', CreateUser.as_view(), name='sing_up'),
]