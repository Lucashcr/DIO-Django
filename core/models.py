from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(verbose_name="Título do evento", max_length=100)
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)
    event_date = models.DateTimeField(verbose_name="Data marcada", default=now)
    created_at = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title