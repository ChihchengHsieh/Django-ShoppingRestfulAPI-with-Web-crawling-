from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer

# Create your views here.


# 1. Only have to create the user here and add the
# 2. Set the URL
# 3. Create a custom permission.

## CreateAPIView vs ViewSet --> what's the difference 

class CreateUserView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
