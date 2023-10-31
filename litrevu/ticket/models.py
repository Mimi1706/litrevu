from django.db import models
from django.conf import settings


# Create your models here.
class Ticket(models.Model):
    # Your Ticket model definition goes here
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
