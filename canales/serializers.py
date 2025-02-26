from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chat, Mensaje

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'nombre']

class MensajeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Muestra el nombre de usuario en lugar del ID
    chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all()) 
    
    class Meta:
        model = Mensaje
        fields = ['id', 'user', 'chat', 'contenido', 'creado']
