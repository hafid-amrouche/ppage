from django.db import models

# Create your models here.

class Message(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    email = models.TextField(max_length=100)
    text = models.TextField()