# Generated by Django 5.0.6 on 2024-07-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomUsuario', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('fechaPubl', models.DateField()),
                ('categoria', models.IntegerField(choices=[(1, 'Nacional'), (2, 'Internacional'), (3, 'Deportes')])),
                ('imagen', models.ImageField(upload_to='media/')),
                ('contenido', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomUsuario', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('nomCompleto', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('fechaNac', models.DateField()),
                ('contrasena', models.CharField(max_length=10)),
                ('telefono', models.IntegerField()),
                ('genero', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino'), (3, 'Otros')])),
                ('direccion', models.CharField(max_length=60)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.IntegerField(choices=[(1, 'Puente Alto'), (2, 'La Florida'), (3, 'Pirque'), (4, 'Macul'), (5, 'Peñalolen'), (6, 'San Ramón'), (7, 'Cerrillos'), (8, 'Cerro Navia'), (9, 'Conchalí'), (10, 'Estación Central'), (11, 'Huechuraba'), (12, 'Independencia'), (13, 'La Cisterna'), (14, 'La Granja'), (15, 'La Pintana'), (16, 'La Reina'), (17, 'Las Condes'), (18, 'Lo Barnechea'), (19, 'Lo Espejo'), (20, 'Lo Prado'), (21, 'Maipú'), (22, 'Ñuñoa'), (23, 'Pedro Aguirre Cerda'), (23, 'Providencia'), (25, 'Pudahuel'), (26, 'Quilicura'), (27, 'Quinta Normal'), (28, 'Recoleta'), (29, 'Renca'), (30, 'San Joaquín'), (31, 'San Miguel'), (32, 'Santiago'), (33, 'Vitacura'), (34, 'San José de Maipo'), (35, 'San Bernardo'), (36, 'Calera de Tango'), (37, 'Buin'), (38, 'Paine'), (39, 'Colina'), (40, 'Lampa'), (41, 'Til-Til'), (42, 'Alhué'), (43, 'Curacaví'), (44, 'María Pinto'), (45, 'Melipilla'), (46, 'San Pedro')])),
            ],
        ),
    ]
