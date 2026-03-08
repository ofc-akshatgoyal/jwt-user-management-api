from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists")

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")

        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username=data['username']
        password=data['password']
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            raise serializers.ValidationError("Invalid Username or Password")

        data['user'] = user
        return data