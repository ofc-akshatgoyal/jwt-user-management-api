from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'owner']