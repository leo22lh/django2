from django.urls import path
from app_prueba.views import index, PreguntaView, PreguntaListarView, PreguntaEditView, PreguntaDeleteView, RespuestaCreateView, RespuestaListarView, RespuestaEditarView, RespuestaDeleteView

urlpatterns = [
    path(r'', index, name='index'),
    path(r'pregunta', PreguntaView, name='pregunta'),
    path(r'pregunta/listar', PreguntaListarView, name='pregunta_listar'),
    path(r'pregunta/editar/<id_pregunta>', PreguntaEditView, name='pregunta_editar'),
    path(r'pregunta/eliminar/<id_pregunta>', PreguntaDeleteView, name='pregunta_eliminar'),
    path(r'respuesta/crear', RespuestaCreateView.as_view(), name='pregunta_crear'),
    path(r'respuesta/listar', RespuestaListarView.as_view(), name='respuesta_listar'),
    path(r'respuesta/editar/<pk>', RespuestaEditarView.as_view(), name='respuesta_editar'),
    path(r'respuesta/eliminar/<pk>', RespuestaDeleteView.as_view(), name='respuesta_eliminar'),
]
