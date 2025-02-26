from django.urls import path
from .views import ChatListCreateView, ChatDetailView, MensajeListCreateView, MensajesPorChatView

urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chat-list-create'),  # Listar y crear chats
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),  # Ver o actualizar un chat
    path('mensajes/', MensajeListCreateView.as_view(), name='mensaje-list-create'),  # Listar y crear mensajes
    path('chats/<int:chat_id>/mensajes/', MensajesPorChatView.as_view(), name='mensajes-por-chat'),  # Mensajes de un chat específico
]
