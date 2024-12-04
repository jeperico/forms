from .models import User
from django.db import transaction
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password



class UserReadSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['name', 'password', 'created_at', 'updated_at']


# class UserRegisterSerializer(serializers.ModelSerializer):
#   password = serializers.CharField(
#     write_only=True, required=True, validators=[validate_password]
#   )

#   class Meta:
#     model = User
#     fields = ['name', 'password']
#     extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#       with transaction.atomic():
#         password = validated_data.pop("password")
#         user = User.objects.create(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user
