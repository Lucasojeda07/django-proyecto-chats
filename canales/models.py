from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Mensaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user.username}: {self.contenido[:20]}"