from django.db import models

# Create your models here.

class Comentario(models.Model):
    nomUsuario = models.CharField(max_length= 50)
    correo = models.CharField(max_length= 100)
    asunto = models.CharField(max_length= 50)
    mensaje = models.CharField(max_length= 250)

    def __str__(self):
        return f" {self.nomUsuario} '{self.asunto}'"
    
#-------------- OBJETO NOTICIA --------------------------#
class Noticia(models.Model):
    TIPO_CATEGORIA = (
        (1, 'Nacional'),
        (2, 'Internacional'),
        (3, 'Deportes')
    )
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fechaPubl = models.DateField()
    categoria = models.IntegerField(choices=TIPO_CATEGORIA)
    imagen = models.ImageField(upload_to='media/')
    contenido = models.TextField(max_length=250)

    def __str__(self):
        return f" {self.titulo} {self.autor} {self.categoria}"
    
#----- OBJETO USUARIO --------------------------------#
class Usuario(models.Model):
    TIPO_GENERO = (
        (1, 'Masculino'),
		(2, 'Femenino'),
		(3, 'Otros'),
    )
    TIPO_COMUNA = (
        (1, 'Puente Alto'),
        (2, 'La Florida'),
        (3, 'Pirque'),
        (4, 'Macul'),                  
        (5, 'Peñalolen'),
        (6, 'San Ramón'),
        (7, 'Cerrillos'),
        (8, 'Cerro Navia'),
        (9, 'Conchalí'),
        (10, 'Estación Central'),
        (11, 'Huechuraba'),
        (12, 'Independencia'),
        (13, 'La Cisterna'),                  
        (14, 'La Granja'),                  
        (15, 'La Pintana'),                  
        (16, 'La Reina'),
        (17, 'Las Condes'),                  
        (18, 'Lo Barnechea'),                  
        (19, 'Lo Espejo'),                  
        (20, 'Lo Prado'),                  
        (21, 'Maipú'),                  
        (22, 'Ñuñoa'),                  
        (23, 'Pedro Aguirre Cerda'),                  
        (23, 'Providencia'),                  
        (25, 'Pudahuel'),                  
        (26, 'Quilicura'),                  
        (27, 'Quinta Normal'),                  
        (28, 'Recoleta'),                  
        (29, 'Renca'),                 
        (30, 'San Joaquín'),                  
        (31, 'San Miguel'),                  
        (32, 'Santiago'),                  
        (33, 'Vitacura'),                  
        (34, 'San José de Maipo'),                  
        (35, 'San Bernardo'),                  
        (36, 'Calera de Tango'),                  
        (37, 'Buin'),                  
        (38, 'Paine'),                  
        (39, 'Colina'),                  
        (40, 'Lampa'),                  
        (41, 'Til-Til'),                  
        (42, 'Alhué'),
        (43, 'Curacaví'),                  
        (44, 'María Pinto'),                  
        (45, 'Melipilla'),                  
        (46, 'San Pedro'),                  
                        
        )
    
    nomUsuario = models.CharField(max_length=50)
    correo = models.EmailField(blank=False)
    nomCompleto = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    fechaNac = models.DateField()
    contrasena = models.CharField(max_length=10)
    telefono = models.IntegerField()
    genero = models.IntegerField(choices=TIPO_GENERO)
    direccion = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=50)
    comuna = models.IntegerField(choices=TIPO_COMUNA)

    def __str__(self):
        return self.nomUsuario