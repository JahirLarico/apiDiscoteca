from django.db import models
from django.utils import timezone
#Llamando a la clase para agregar campos
from django.contrib.auth.models import AbstractUser
# Create your models here.


#Crear una clase para albergar los campos de UserAdmin y agregar mas
class CustomUser(AbstractUser):
    UbicacionDiscoteca = models.CharField(max_length=100)

class Clientes(models.Model):
    #Relacion con la clase CustomUser y colocarle en nombre de relacion
    discoteca = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=9, unique=True)
    edad = models.IntegerField()
    estado = models.BooleanField(default=False)
    userFoto = models.ImageField(upload_to='usersImages', null=True)

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='historial')
    fechaEntrada = models.DateField(auto_now_add=True)
    horaEntrada = models.TimeField(auto_now_add=True)
    fechaSalida = models.DateField(null=True)
    horaSalida = models.TimeField(null=True)
