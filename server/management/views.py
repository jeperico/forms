from django.shortcuts import render
from .models import User
from .serializers import UserReadSerializer
from rest_framework import viewsets


class UserView(viewsets.ModelViewSet):
  serializer_class = UserReadSerializer
  queryset = User.objects.all()


# class UserRegisterView(viewsets.ModelViewSet):
#   serializer_class = UserRegisterSerializer
#   queryset = User.objects.all()
