from django.db import models

# Create your models here.

class Postulante(models.Model):
    run = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    correo = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    vivienda = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    def __str__(self):
        #return "run: " + self.run + " nombre: " + self.nombre + " fecha: " + self.fecha + " correo: " + self.correo
        var = """
            run: {} nombre: {} fecha: {} correo: {} 
          """.format(self.run, self.nombre, self.fecha, self.correo)
        return var

class Perro(models.Model):
    #foto = models.ImageField(upload_to='fotos/') 
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=30)

    def __str__(self):
        return "PERRO"