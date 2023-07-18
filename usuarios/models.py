from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    pnombre = models.CharField(max_length=40)
    snombre = models.CharField(max_length=40)
    appaterno = models.CharField(max_length=40)
    apmaterno = models.CharField(max_length=40)
    correo = models.EmailField(unique=True)
    nro_telefono = models.IntegerField()
    localizacion = models.CharField(max_length=100)
    dirreccion_envio = models.TextField()
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_activo = models.DateTimeField(null=True, blank=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar_usuario/', null=True, blank=True)

    def __str__(self):
        return f"{self.pnombre}-{self.appaterno}. Estado = {'Activo' if self.estado else 'Inactivo'}"