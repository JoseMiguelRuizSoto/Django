import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import NoticiaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.

def inicio(request):
    noticias = Noticia.objects.all()
    
    usuario = None
    if 'usuario' in request.session:
        usuario = request.session['usuario']
    
    context = {
        'noticias' : noticias,
        'usuario': usuario
    }
    return render(request, 'core/inicio.html', context)

def nacional(request):
    usuario = None
    if 'usuario' in request.session:
        usuario = request.session['usuario']
    
    context = {
        'usuario': usuario
    }

    return render(request, 'core/nacional.html', context)

def internacional(request):
    usuario = None
    if 'usuario' in request.session:
        usuario = request.session['usuario']
    
    context = {
        'usuario': usuario
    }
    return render(request, 'core/internacional.html', context)

def deporte(request):
    usuario = None
    if 'usuario' in request.session:
        usuario = request.session['usuario']
    
    context = {
        'usuario': usuario
    }
    return render(request, 'core/deporte.html', context)

def contactoForm(request):
    if 'usuario' in request.session:
        usuario = request.session['usuario']
    
        context = {
            'usuario': usuario
        }
        return render(request, 'core/contactoForm.html', context)
    
    return HttpResponseRedirect('/accounts/login/')

    

def listarComentario(request):
    if 'usuario' in request.session:
        usuario = request.session['usuario']
        
        comentarios = Comentario.objects.all()

        context = {
            'comentarios' : comentarios,
            'usuario': usuario
        }

        return render(request, 'core/listarComentario.html', context)

    return HttpResponseRedirect('/accounts/login/')


def eliminarComentario(request, pk):
    try:
        comentario = Comentario.objects.get(id=pk)
        comentario.delete()

        mensaje = 'Comentario Eliminado!!!'
        comentarios = Comentario.objects.all()
        context = {
            'comentarios' : comentarios,
            'mensaje' : mensaje
        }

        return render(request, 'core/listarComentario.html', context)
    except:
        mensaje = 'Comentario no existe!!!'
        comentarios = Comentario.objects.all()
        context = {
            'comentarios' : comentarios,
            'mensaje' : mensaje
        }

        return render(request, 'core/listarComentario.html', context)

def nuevoComentario(request):
    comentario = Comentario.objects.create(
        nomUsuario = request.POST["name"],
        correo = request.POST["email"],
        asunto = request.POST["subject"],
        mensaje = request.POST["message"]
    )

    comentario.save
    mensaje = "Te contactaremos a la brevedad!"

    context = {
        'mensaje' : mensaje
    }

    return render(request, 'core/contactoForm.html', context)


def cargaNoticia(request):
    if 'usuario' in request.session:
        usuario = request.session['usuario']
    
        context = {
            'usuario': usuario
        }
        return render(request, 'core/cargaNoticia.html', context)
    
    return HttpResponseRedirect('/accounts/login/')


def listarNoticia(request):
    if 'usuario' in request.session:
        usuario = request.session['usuario']
        noticias = Noticia.objects.all()
        context = {
            'noticias' : noticias,
            'usuario': usuario
        }

        return render(request, 'core/listarNoticia.html', context)

    return HttpResponseRedirect('/accounts/login/')


def editarNoticia(request, pk):

    if 'usuario' in request.session:
        usuario = request.session['usuario']

        try:
            noticia = Noticia.objects.get(id=pk)

            context = {
                'noticia' : noticia,
                'usuario': usuario
            }

            return render(request, 'core/editarNoticia.html', context)
        except:
            mensaje = 'Noticia no existe!!!'
            noticias = Noticia.objects.all()
            context = {
                'noticias' : noticias,
                'mensaje' : mensaje,
                'usuario': usuario
            }

            return render(request, 'core/listarNoticia.html', context)

    return HttpResponseRedirect('/accounts/login/')


def actualizaNoticia(request):
    print(request.POST)
    noticia = Noticia.objects.get(id=request.POST['pk'])
    noticia.titulo = request.POST['titulo']
    noticia.autor = request.POST['autor']
    noticia.fechaPubl = request.POST['fecha']
    noticia.categoria = request.POST['categoria']
    noticia.imagen = request.POST['image']
    noticia.contenido = request.POST['contenido']
    noticia.save()
    
    mensaje = 'Noticia actualizada !!!'
    noticias = Noticia.objects.all()
    context = {
        'noticias' : noticias,
        'mensaje' : mensaje
    }

    return render(request, 'core/listarNoticia.html', context)

def agregaNoticia(request):
    print(request.POST)
    noticia = Noticia()
    noticia.titulo = request.POST['titulo']
    noticia.autor = request.POST['autor']
    noticia.fechaPubl = request.POST['fecha']
    noticia.categoria = request.POST['categoria']
    noticia.imagen = request.FILES['image']
    noticia.contenido = request.POST['contenido']
    noticia.save()
    
    mensaje = "Noticia publicada!"
    noticias = Noticia.objects.all()
    context = {
        'noticias' : noticias,
        'mensaje' : mensaje
    }

    return render(request, 'core/listarNoticia.html', context)


def eliminarNoticia(request, pk):
    try:
        noticia = Noticia.objects.get(id=pk)
        noticia.delete()

        mensaje = 'Noticia Eliminada!!!'
        noticias = Noticia.objects.all()
        context = {
            'noticias' : noticias,
            'mensaje' : mensaje
        }

        return render(request, 'core/listarNoticia.html', context)
    except:
        mensaje = 'Noticia no existe!!!'
        noticias = Noticia.objects.all()
        context = {
            'noticias' : noticias,
            'mensaje' : mensaje
        }

        return render(request, 'core/listarNoticia.html', context)


def nuevaNoticia(request):
    if 'usuario' in request.session:
        usuario = request.session['usuario']

        noticia = Noticia.objects.create(
            titulo = request.POST["titulo"],
            autor = request.POST["autor"],
            fecha = request.POST["fecha"],
            categoria = request.POST["categoria"],
            imagen = request.POST["image"],
            contenido = request.POST["contenido"]
        )

        noticia.save
        mensaje = "Noticia publicada!"

        context = {
            'mensaje' : mensaje,
            'usuario': usuario
        }

        return render(request, 'core/cargaNoticia.html', context) 
    
    return HttpResponseRedirect('/accounts/login/')

def registro(request):
    return render(request, 'core/registro.html')

def valida(request):
    user = request.POST["username"]
    password = request.POST["password"]
    print(request.POST)

    try:
        usuario = Usuario.objects.get( nomUsuario = user, contrasena = password)
        mensaje = usuario.nomUsuario
        request.session['usuario'] = usuario.nomUsuario

    except:
        mensaje = ''

    context = {
        'mensaje' : mensaje,
        'usuario': usuario
    }

    return render(request, 'core/inicio.html', context)



def listarUsuario(request):
    if 'usuario' in request.session:
        usuario = request.session['usuario']

        usuarios = Usuario.objects.all()
        context = {
            'usuarios' : usuarios,
            'usuario': usuario
        }

        return render(request, 'core/listarUsuario.html', context)

    return HttpResponseRedirect('/accounts/login/')



def editarUsuario(request, pk):

    if 'usuario' in request.session:
        usuario = request.session['usuario']

        try:
            usuario = Usuario.objects.get(id=pk)
            
            context = {
                'usuario' : usuario
            }

            return render(request, 'core/editarUsuario.html', context)
        except:
            mensaje = 'Usuario no existe!!!'
            usuarios = Usuario.objects.all()
            context = {
                'usuarios' : usuarios,
                'mensaje' : mensaje,
                'usuario': usuario
            }

            return render(request, 'core/listarUsuario.html', context)

    return HttpResponseRedirect('/accounts/login/')


def actualizaUsuario(request):
    print(request.POST)
    usuario = Usuario.objects.get(id=request.POST['pk'])
    usuario.nomUsuario = request.POST['nomUser']
    usuario.correo = request.POST['email']
    usuario.nomCompleto = request.POST['name']
    usuario.rut = request.POST['rut']
    usuario.fechaNac = request.POST['fecha']
    usuario.contrasena = request.POST['contrasena']
    usuario.telefono = request.POST['telefono']
    usuario.genero = request.POST['genero']
    usuario.direccion = request.POST['direccion']
    usuario.ciudad = request.POST['ciudad']
    usuario.comuna = request.POST['comuna']

    
    usuario.save()
    
    mensaje = 'Usuario actualizada !!!'
    usuarios = Usuario.objects.all()
    context = {
        'usuarios' : usuarios,
        'mensaje' : mensaje
    }

    return render(request, 'core/listarUsuario.html', context)

def agregaUsuario(request):
    print(request.POST)
    usuario = Usuario()
    usuario.nomUsuario = request.POST['nomUser']
    usuario.correo = request.POST['email']
    usuario.nomCompleto = request.POST['name']
    usuario.rut = request.POST['rut']
    usuario.fechaNac = request.POST['fecha']
    usuario.contrasena = request.POST['contrasena']
    usuario.telefono = request.POST['telefono']
    usuario.genero = request.POST['genero']
    usuario.direccion = request.POST['direccion']
    usuario.ciudad = request.POST['ciudad']
    usuario.comuna = request.POST['comuna']

    usuario.save()
    
    mensaje = "Usuario Agregado!"
    usuarios = Usuario.objects.all()
    context = {
        'usuarios' : usuarios,
        'mensaje' : mensaje
    }

    return render(request, 'core/listarUsuario.html', context)


def eliminarUsuario(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()

        mensaje = 'Usuario Eliminada!!!'
        usuarios = Usuario.objects.all()
        context = {
            'usuarios' : usuarios,
            'mensaje' : mensaje
        }

        return render(request, 'core/listarUsuario.html', context)
    except:
        mensaje = 'Usuario no existe!!!'
        usuarios = Usuario.objects.all()
        context = {
            'usuarios' : usuarios,
            'mensaje' : mensaje
        }

        return render(request, 'core/listarUsuario.html', context)


def nuevoUsuario(request):

    if 'usuario' in request.session:
        usr = request.session['usuario']
    
        usuario = Usuario.objects.create(
            nomUsuario = request.POST['nomUser'],
            correo = request.POST['email'],
            nomCompleto = request.POST['name'],
            rut = request.POST['rut'],
            fechaNac = request.POST['fecha'],
            contrasena = request.POST['contrasena'],
            telefono = request.POST['telefono'],
            genero = request.POST['genero'],
            direccion = request.POST['direccion'],
            ciudad = request.POST['ciudad'],
            comuna = request.POST['comuna']
        )

        usuario.save
        mensaje = "Noticia publicada!"

        context = {
            'mensaje' : mensaje,
            'usuario': usr
        }

        return render(request, 'core/registro.html', context) 

    return HttpResponseRedirect('/accounts/login/')

def obtener_datos_climaticos(ciudad):
    api_key = '23589336e142282527e305fefb3d6428'  # Reemplaza con tu clave API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'
    respuesta = requests.get(url)
    datos = respuesta.json()
    if respuesta.status_code == 200:
        return {
            'ciudad': datos['name'],
            'temperatura': datos['main']['temp'],
            'descripcion': datos['weather'][0]['description'],
        }
    else:
        return None

def clima(request):
    ciudad = request.GET.get('ciudad', 'Santiago')  # Ciudad por defecto
    datos_climaticos = obtener_datos_climaticos(ciudad)
    return render(request, 'core/clima.html', {'datos_climaticos': datos_climaticos, 'ciudad': ciudad}) 
