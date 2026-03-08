from django.urls import path, include
from accounts.views import SignupAPI, LoginAPI
from core.views import NoteListCreateAPI, NoteDetailAPI
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'people', PersonViewSet, basename='people')

urlpatterns = [
    path('signup/', SignupAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('notes/', NoteListCreateAPI.as_view()),
    path('notes/<int:pk>/', NoteDetailAPI.as_view()),
]