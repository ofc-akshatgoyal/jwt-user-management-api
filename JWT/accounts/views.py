from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView ,status
from accounts.serializers import SignupSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class SignupAPI(APIView):
    
    def post(self , request):
        data = request.data
        serializer = SignupSerializer(data = data)
        
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            } , status.HTTP_400_BAD_REQUEST)
            
        serializer.save()
        
        return Response({'status':True , 'message': 'user created'}, status=status.HTTP_201_CREATED)
    
    
    
    
class LoginAPI(APIView):
    
    def post(self , request):
        data = request.data
        serializer = LoginSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            } , status.HTTP_400_BAD_REQUEST)
            
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "status": True,
                "message": "Login successful",
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            },
            status=status.HTTP_200_OK
        )