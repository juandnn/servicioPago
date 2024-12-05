from django.db import models

# Create your models here.
class Pago(models.Model):
    monto = models.IntegerField()
    usuario = models.CharField(max_length=100)
    pagado = models.BooleanField(default=False)

    
    def __str__(self):
        return self.usuario 