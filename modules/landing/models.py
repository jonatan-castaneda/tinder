from django.db import models
#from django.contrib.auth.models import User #For django auth
from django.contrib.postgres.fields import ArrayField
from modules.users.models import User #For custom auth

# Create your models here.
class Images(models.Model):
    GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    )
    id = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(User, 
        on_delete = models.CASCADE) #Borrar toda la info del user cuando sea eliminado
    descripcion = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    tags = ArrayField(
        models.CharField(max_length = 50),
        null = True
    )
    imagen = models.ImageField(upload_to = "images/")#Se crea dentro de media automáticamente
    genero = models.CharField(max_length=1, choices=GENERO, null=True, blank="true")
