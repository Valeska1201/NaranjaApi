from django.db import models

# Create your models here.
class Postre(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    descripcion = models.CharField(max_length=150)
    

    def __str__(self):
        return str(self.id) + " " + self.nombre 

    def delete(self, using=None, keep_parents=False):
        if self.imagen:
            self.imagen.storage.delete(self.imagen.name)
        super().delete()