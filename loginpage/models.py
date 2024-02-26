
from django.db import models

class login(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.user_name} ({self.id})"

class signin(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username

