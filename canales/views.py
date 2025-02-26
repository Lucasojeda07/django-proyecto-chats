from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Chat, Mensaje
from .serializers import ChatSerializer, MensajeSerializer
from .pagination import CustomPagination  # Importamos la paginación personalizada

# Vista para gestionar los chats
class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination  # Aplicamos paginación

class ChatDetailView(generics.RetrieveUpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Vista para gestionar los mensajes
class MensajeListCreateView(generics.ListCreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination  # Aplicamos paginación

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Asigna el usuario autenticado

        

class MensajesPorChatView(generics.ListAPIView):
    serializer_class = MensajeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination  # Aplicamos paginación

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Mensaje.objects.filter(chat__id=chat_id)
