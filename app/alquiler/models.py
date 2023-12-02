from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=20)

class Alumno(models.Model):
    idAlumno = models.AutoField(primary_key=True, auto_created=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()
    fecha_nac= models.DateField()
    foto= models.ImageField(upload_to='fotos')
    password = models.CharField(max_length=100)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Arrendador(models.Model):
    idArrendador = models.AutoField(primary_key=True, auto_created=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()
    fecha_nac= models.DateField()
    dni= models.IntegerField()
    password = models.CharField(max_length=100)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alojamiento(models.Model):
    idAlojamiento = models.AutoField(primary_key=True, auto_created=True)
    nombre =models.CharField(max_length=100)
    descripcion =models.TextField()
    fecha_publi = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='fotos')
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    disponibilidad = models.BooleanField(default=False)
    ubicacion = models.CharField(max_length=100)
    idArrendador = models.ForeignKey(Arrendador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.fecha_publi}"


class Reserva(models.Model):
    idAReserva = models.AutoField(primary_key=True, auto_created=True)
    idAlojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    idAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha_inicio= models.DateField()
    fecha_final= models.DateField()
    estado= models.BooleanField(default=False)

    def __int__(self):
        return f"{self.idAReserva} {self.idAlumno}"
    

class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True, auto_created=True)
    idAlojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    idAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_publi = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return f"{self.idComentario} {self.idAlumno}"
