from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import User, UserSerializer
from datetime import datetime, timedelta
import jwt
from django.conf import settings

# Create your views here.
class RegisterUserView(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({'message': 'Registration Succesfull'}, status=status.HTTP_201_CREATED)
        

class LoginUserView(APIView):
    def poast(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied()
        
        if not user.check_password(password):
            raise PermissionDenied()

        expiry_time = datetime.now() + timedelta(days=7)

        token = jwt.encode(
            {'sub': user.id, 'exp': int(expiry_time.strftime(f'%s'))},
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return Response(
            {'token': token, 'message': f'Welcome back {user.username}'}
        )
