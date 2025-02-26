from django.urls import path
from .views import ChatListCreateView, ChatDetailView, MensajeListCreateView, MensajesPorChatView

urlpatterns = [
    path('api/canales/chats/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('api/canales/chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),
    path('api/canales/mensajes/', MensajeListCreateView.as_view(), name='mensaje-list-create'),
    path('api/canales/chats/<int:chat_id>/mensajes/', MensajesPorChatView.as_view(), name='mensajes-por-chat'),
]
