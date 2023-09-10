from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class PasswordEntry(models.Model):
    length = models.IntegerField(default=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Letter = models.BooleanField()
    Number = models.BooleanField()
    Symbols = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title