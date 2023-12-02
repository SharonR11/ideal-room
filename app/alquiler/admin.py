from django.contrib import admin
from .models import Usuario,Alumno,Alojamiento,Arrendador,Comentario,Reserva
admin.site.register(Usuario)
admin.site.register(Alumno)
admin.site.register(Alojamiento)
admin.site.register(Arrendador)
admin.site.register(Reserva)