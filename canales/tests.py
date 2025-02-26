from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Chat, Mensaje

class ChatModelTest(TestCase):
    def test_crear_chat(self):
        """Prueba la creación de un chat"""
        chat = Chat.objects.create(nombre="Test Chat")
        self.assertEqual(chat.nombre, "Test Chat")

class MensajeModelTest(TestCase):
    def setUp(self):
        """Configura un usuario y un chat antes de cada test"""
        self.user = User.objects.create(username="testuser")
        self.chat = Chat.objects.create(nombre="Test Chat")

    def test_crear_mensaje(self):
        """Prueba la creación de un mensaje"""
        mensaje = Mensaje.objects.create(user=self.user, chat=self.chat, contenido="Hola!")
        self.assertEqual(mensaje.contenido, "Hola!")
        self.assertEqual(mensaje.chat, self.chat)
        self.assertEqual(mensaje.user, self.user)
