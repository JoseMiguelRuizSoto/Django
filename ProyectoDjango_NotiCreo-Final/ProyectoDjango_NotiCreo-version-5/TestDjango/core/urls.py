from django.urls import path
from .views import *
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio , name='inicio'),
    path('nacional', nacional, name='nacional'),
    path('internacional', internacional, name='internacional'),
    path('deporte', deporte, name='deporte'),
    path('contactoForm', contactoForm, name='contactoForm'),
    path('listarComentario', listarComentario, name='listarComentario'),
    path('eliminarComentario/<str:pk>', eliminarComentario, name='eliminarComentario'),
    path('nuevoComentario', nuevoComentario, name='nuevoComentario'),
    path('cargaNoticia', cargaNoticia, name='cargaNoticia'),
    path('agregaNoticia', agregaNoticia, name='agregaNoticia'),
    path('listarNoticia', listarNoticia, name='listarNoticia'),
    path("editarNoticia/<str:pk>", editarNoticia, name="editarNoticia"),
    path("actualizaNoticia", actualizaNoticia, name="actualizaNoticia"),
    path('eliminarNoticia/<str:pk>', eliminarNoticia, name='eliminarNoticia'),
    path('nuevaNoticia', nuevoComentario, name='nuevaNoticia'),
    path('registro', registro, name='registro'),
    path('valida', valida, name='valida'),
    path('listarUsuario', listarUsuario, name='listarUsuario'),
    path('editarUsuario/<str:pk>', editarUsuario, name='editarUsuario'),
    path('agregaUsuario', agregaUsuario, name='agregaUsuario'),
    path('eliminarUsuario/<str:pk>', eliminarUsuario, name='eliminarUsuario'),
	path('clima', clima, name='clima'),
	path('obtener_datos_climaticos', obtener_datos_climaticos, name='obtener_datos_climaticos'),
]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)