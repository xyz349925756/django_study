from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from webapi.apps.user.models import User
from webapi.utils.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
