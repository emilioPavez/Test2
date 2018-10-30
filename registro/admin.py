from django.contrib import admin

# Register your models here.
from .models import Postulante, Perro

class AdminPostulante(admin.ModelAdmin):
    list_display = ["nombre", "correo", "run"]
    class Meta:
        model = Postulante

# original o primera vista
# 
# admin.site.register(Usuario)
admin.site.register(Postulante, AdminPostulante)

class AdminPerro(admin.ModelAdmin):
    list_display = ["nombreperro", "Razaperro", "Descripción", "imagenperro"]
    class Meta:
        model = Perro

admin.site.register(Perro, AdminPerro)