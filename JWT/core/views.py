from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView ,status
from core.serializers import NoteSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Note


class NoteListCreateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NoteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "status": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save(owner=request.user)

        return Response(
            {
                "status": True,
                "message": "Note created",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


    def get(self, request):
        notes = Note.objects.filter(owner=request.user)
        serializer = NoteSerializer(notes, many=True)

        return Response(
            {"status": True, "data": serializer.data},
            status=status.HTTP_200_OK
        )



class NoteDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return Note.objects.get(pk=pk, owner=user)

    # UPDATE NOTE
    def put(self, request, pk):
        note = self.get_object(pk, request.user)
        serializer = NoteSerializer(note, data=request.data)

        if not serializer.is_valid():
            return Response(
                {"status": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(
            {"status": True, "data": serializer.data},
            status=status.HTTP_200_OK
        )

    # DELETE NOTE
    def delete(self, request, pk):
        note = self.get_object(pk, request.user)
        note.delete()

        return Response(
            {"status": True, "message": "Note deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
